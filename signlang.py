"""Sign Language MNIST - Mini Project (CNN classifier).

Implements the full mini-project pipeline:
- Load Sign Language MNIST CSVs (train/test)
- Reshape + normalize
- Train/test split (80/20) if only a single CSV is provided
- Build a CNN
- Evaluate accuracy + classification report + confusion matrix
- Optional: predict on 5 external images you provide (local file paths)

Dataset (Kaggle):
- sign_mnist_train.csv
- sign_mnist_test.csv
Each CSV has columns: label, pixel1..pixel784 (28x28 grayscale)

Usage examples:

1) Using provided train/test CSVs:
    python sign_language_mnist_project.py \
      --train-csv /path/to/sign_mnist_train.csv \
      --test-csv  /path/to/sign_mnist_test.csv

2) If you only have one CSV (auto 80/20 split):
    python sign_language_mnist_project.py --train-csv /path/to/sign_mnist_train.csv

3) Predict your own images:
    python sign_language_mnist_project.py \
      --train-csv ... --test-csv ... \
      --predict-images img1.png img2.jpg img3.png img4.jpg img5.png

Notes on labels:
- Dataset uses 24 letters (A-Z excluding J and Z because they require motion).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Protocol, runtime_checkable

import numpy as np


@runtime_checkable
class KerasLikeModel(Protocol):
    def summary(self) -> None:
        ...

    def fit(self, *args, **kwargs):
        ...

    def evaluate(self, *args, **kwargs):
        ...

    def predict(self, *args, **kwargs):
        ...

    def save(self, *args, **kwargs) -> None:
        ...


def set_seed(seed: int) -> None:
    import os

    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    try:
        import tensorflow as tf

        tf.random.set_seed(seed)
    except Exception:
        pass


def label_to_letter(label: int) -> str:
    """Map 0-23 label to letter, skipping J and Z."""
    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
    ]
    return letters[int(label)]


def load_sign_mnist_csv(csv_path: str | Path) -> tuple[np.ndarray, np.ndarray]:
    """Load a Sign Language MNIST CSV into (X, y).

    Returns:
        X: float32 array of shape (n, 28, 28, 1) normalized to [0,1]
        y: int array of shape (n,)
    """
    import pandas as pd

    df = pd.read_csv(csv_path)
    if "label" not in df.columns:
        raise ValueError("CSV must have a 'label' column.")

    y = df["label"].to_numpy(dtype=np.int64)
    X = df.drop(columns=["label"]).to_numpy(dtype=np.float32)

    # reshape to images
    X = X.reshape((-1, 28, 28, 1))
    # normalize [0,255] -> [0,1]
    X /= 255.0
    return X, y


def build_model(num_classes: int) -> KerasLikeModel:
    import tensorflow as tf
    from typing import cast

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(28, 28, 1)),
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(num_classes, activation="softmax"),
        ]
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return cast(KerasLikeModel, cast(object, model))


def evaluate_and_report(
        model,
        X_test: np.ndarray,
        y_test: np.ndarray,
        out_dir: Path,
) -> None:
    from sklearn.metrics import classification_report, confusion_matrix

    out_dir.mkdir(parents=True, exist_ok=True)

    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    metrics = {"loss": float(loss), "accuracy": float(acc)}
    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))

    y_prob = model.predict(X_test, verbose=0)
    y_pred = np.argmax(y_prob, axis=1)

    labels = list(range(len(set(y_test.tolist()))))
    target_names = [label_to_letter(i) for i in range(24)]

    report_txt = classification_report(y_test, y_pred, target_names=target_names, zero_division=0)
    (out_dir / "classification_report.txt").write_text(report_txt)

    report_dict = classification_report(
        y_test, y_pred, target_names=target_names, output_dict=True, zero_division=0
    )
    (out_dir / "classification_report.json").write_text(json.dumps(report_dict, indent=2))

    cm = confusion_matrix(y_test, y_pred)
    np.save(out_dir / "confusion_matrix.npy", cm)

    # plot cm (optional)
    try:
        import matplotlib.pyplot as plt
        import importlib

        sns = importlib.import_module("seaborn")
        plt.figure(figsize=(12, 10))
        sns.heatmap(cm, cmap="Blues", cbar=True)
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.tight_layout()
        plt.savefig(out_dir / "confusion_matrix.png", dpi=200)
        plt.close()
    except Exception:
        pass


def load_external_image(path: Path) -> np.ndarray:
    """Load an external image and convert to (28,28,1) normalized float32."""
    from PIL import Image

    img = Image.open(path).convert("L")
    img = img.resize((28, 28))
    arr = np.asarray(img, dtype=np.float32) / 255.0
    return arr.reshape((1, 28, 28, 1))


def predict_external_images(model, image_paths: Iterable[str | Path]) -> list[dict]:
    results: list[dict] = []
    for p in image_paths:
        path = Path(p).expanduser().resolve()
        x = load_external_image(path)
        prob = model.predict(x, verbose=0)[0]
        pred = int(np.argmax(prob))
        results.append(
            {
                "path": str(path),
                "pred_label": pred,
                "pred_letter": label_to_letter(pred),
                "confidence": float(prob[pred]),
            }
        )
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("--train-csv", required=True, help="Path to sign_mnist_train.csv (or a single CSV).")
    p.add_argument("--test-csv", default=None, help="Optional path to sign_mnist_test.csv")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--epochs", type=int, default=10)
    p.add_argument("--batch-size", type=int, default=128)
    p.add_argument("--out-dir", default="reports/sign_language_mnist")
    p.add_argument("--predict-images", nargs="*", default=None, help="Optional list of image paths to predict")
    return p


def main() -> None:
    args = build_arg_parser().parse_args()
    set_seed(args.seed)

    X_train_full, y_train_full = load_sign_mnist_csv(args.train_csv)

    if args.test_csv:
        X_test, y_test = load_sign_mnist_csv(args.test_csv)
        X_train, y_train = X_train_full, y_train_full
    else:
        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(
            X_train_full,
            y_train_full,
            test_size=0.2,
            random_state=args.seed,
            stratify=y_train_full,
        )

    num_classes = 24
    model = build_model(num_classes=num_classes)
    model.summary()

    callbacks = []
    try:
        import tensorflow as tf

        callbacks = [
            tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", patience=3, restore_best_weights=True)
        ]
    except Exception:
        pass

    model.fit(
        X_train,
        y_train,
        validation_split=0.1,
        epochs=args.epochs,
        batch_size=args.batch_size,
        verbose=1,
        callbacks=callbacks,
    )

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    model.save(out_dir / "sign_language_cnn.keras")

    evaluate_and_report(model, X_test, y_test, out_dir=out_dir)

    if args.predict_images:
        preds = predict_external_images(model, args.predict_images)
        (out_dir / "external_predictions.json").write_text(json.dumps(preds, indent=2))
        for row in preds:
            print(row)


if __name__ == "__main__":
    main()
