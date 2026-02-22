"""Colorize Movies - CelebA-based Image Colorization using VGG16 encoder

This script contains helper functions and a runnable CLI to:
- Load images (e.g., CelebA) from a directory
- Convert images from RGB -> LAB and prepare L (input) and AB (target)
- Build a model using VGG16 (transfer learning) as encoder and a small decoder
  that predicts the AB channels from the L channel.
- Train and evaluate the model (80/20 split)
- Visualize results (original, grayscale input, predicted colorization)
- Colorize a video using moviepy by processing frames

Notes:
- Training colorization models is computationally heavy. Use a GPU and enough
  data for reasonable results. This implementation is intended as a clear,
  working baseline you can extend and tune.

Usage examples (from repo root):
python colorize_movies.py --data-dir /path/to/celeba/img_align_celeba --epochs 10 --batch-size 32 --output-dir outputs/colorize
python colorize_movies.py --colorize-video /path/to/charlie.mp4 --model-path outputs/colorize/model.keras --video-out colored_charlie.mp4

"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable, Tuple

import numpy as np
from skimage import color, io, transform
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# set a global seed helper
def set_seed(seed: int = 42) -> None:
    import random
    import tensorflow as tf

    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def load_images_from_dir(
    data_dir: str | Path,
    max_images: int | None = None,
    target_size: Tuple[int, int] = (224, 224),
) -> np.ndarray:
    """Load images from a directory into an array of shape (N, H, W, 3) in RGB.

    Args:
        data_dir: directory with images (jpg/png). Will recurse one level.
        max_images: optional max number of images to load for quick experiments.
        target_size: size to resize images (H, W)

    Returns:
        images: float32 array with values in [0,1]
    """
    data_dir = Path(data_dir)
    exts = ("*.jpg", "*.jpeg", "*.png")
    paths = []
    for ext in exts:
        paths.extend(list(data_dir.glob(ext)))
        paths.extend(list((data_dir / "img_align_celeba").glob(ext)))
    paths = sorted(paths)
    if max_images:
        paths = paths[:max_images]

    imgs = []
    for p in paths:
        try:
            im = io.imread(str(p))
            # some images may be grayscale, skip them
            if im.ndim == 2:
                continue
            # convert to float in [0,1]
            im = transform.resize(im, target_size, anti_aliasing=True, preserve_range=True)
            # if image has alpha channel, drop it
            if im.shape[-1] == 4:
                im = im[..., :3]
            im = np.asarray(im, dtype=np.float32) / 255.0
            imgs.append(im)
        except Exception:
            continue
    if not imgs:
        raise ValueError(f"No images found in {data_dir} (tried {len(paths)} paths)")

    return np.stack(imgs, axis=0)


def rgb_to_lab_batch(imgs: np.ndarray) -> np.ndarray:
    """Convert batch of RGB images (float in [0,1]) to LAB color space.

    Returns LAB images where L in [0, 100], A and B in approximately [-128,127].
    """
    labs = []
    for im in imgs:
        lab = color.rgb2lab(im)
        labs.append(lab)
    return np.stack(labs, axis=0)


def prepare_data_from_rgb(
    imgs_rgb: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """Prepare inputs and targets for training.

    Input: L channel normalized to [0,1] with shape (N, H, W, 1)
    Target: AB channels normalized to [-1,1] with shape (N, H, W, 2)
    """
    labs = rgb_to_lab_batch(imgs_rgb)
    # L channel: 0..100 -> normalize to 0..1
    L = labs[..., 0:1] / 100.0
    # AB channels: roughly -128..127 -> scale to -1..1
    AB = labs[..., 1:3] / 128.0
    return L.astype(np.float32), AB.astype(np.float32)


def build_colorization_model(input_shape: Tuple[int, int, int] = (224, 224, 1)):
    """Build a model that uses VGG16 as encoder (transfer learning) and a decoder
    to predict AB channels.

    The VGG16 expects 3 channels, so we tile the single L channel to 3 channels
    before feeding it to VGG16. We use pretrained imagenet weights and freeze the
    initial layers.
    """
    import tensorflow as tf
    from tensorflow.keras import layers, models

    H, W, C = input_shape
    # Input is L channel
    inp = layers.Input(shape=(H, W, 1), name="L_input")
    # replicate to 3 channels so VGG can process it
    x = layers.Concatenate()([inp, inp, inp])

    # use VGG16 without top
    vgg = tf.keras.applications.VGG16(weights="imagenet", include_top=False, input_shape=(H, W, 3))
    vgg.trainable = False  # freeze for transfer learning baseline
    vgg_out = vgg(x)

    # Fusion / Bottleneck: small convs
    x = layers.Conv2D(512, 3, padding="same", activation="relu")(vgg_out)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(256, 3, padding="same", activation="relu")(x)

    # Decoder: upsample progressively to original size
    x = layers.UpSampling2D(2)(x)
    x = layers.Conv2D(128, 3, padding="same", activation="relu")(x)
    x = layers.UpSampling2D(2)(x)
    x = layers.Conv2D(64, 3, padding="same", activation="relu")(x)
    x = layers.UpSampling2D(2)(x)
    x = layers.Conv2D(32, 3, padding="same", activation="relu")(x)
    # output AB channels
    x = layers.Conv2D(2, 3, padding="same", activation="tanh", name="AB_output")(x)
    # tanh gives outputs in [-1,1], which matches our AB normalization

    model = models.Model(inputs=inp, outputs=x)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4), loss="mse", metrics=["mse"])
    return model


def lab_to_rgb_batch(L: np.ndarray, AB: np.ndarray) -> np.ndarray:
    """Combine L and AB batches and convert back to RGB in [0,1].

    L is expected in 0..1, AB in -1..1
    """
    outs = []
    for l, ab in zip(L, AB):
        lab = np.concatenate([l * 100.0, ab * 128.0], axis=-1)
        rgb = color.lab2rgb(lab)
        # clip to [0,1]
        rgb = np.clip(rgb, 0.0, 1.0)
        outs.append(rgb)
    return np.stack(outs, axis=0)


def plot_results(
    orig_rgb: np.ndarray, L_in: np.ndarray, pred_ab: np.ndarray, n: int = 5, out_dir: Path | None = None
):
    """Plot n results (original, grayscale, predicted colorized) side-by-side."""
    out_dir = Path(out_dir) if out_dir is not None else None
    N = min(n, orig_rgb.shape[0])
    fig, axes = plt.subplots(N, 3, figsize=(12, 4 * N))
    if N == 1:
        axes = np.expand_dims(axes, 0)
    for i in range(N):
        axes[i, 0].imshow(orig_rgb[i])
        axes[i, 0].set_title("Original")
        axes[i, 0].axis("off")

        gray = np.squeeze(L_in[i], axis=-1)
        axes[i, 1].imshow(gray, cmap="gray")
        axes[i, 1].set_title("Grayscale (L input)")
        axes[i, 1].axis("off")

        colorized = lab_to_rgb_batch(L_in[i:i+1], pred_ab[i:i+1])[0]
        axes[i, 2].imshow(colorized)
        axes[i, 2].set_title("Predicted Colorized")
        axes[i, 2].axis("off")

        if out_dir:
            # save each colorized image
            out_path = Path(out_dir) / f"colorized_{i}.png"
            io.imsave(str(out_path), (colorized * 255).astype(np.uint8))
    plt.tight_layout()
    if out_dir:
        fig_path = Path(out_dir) / "results_plot.png"
        fig.savefig(fig_path, dpi=200)
    plt.show()


def colorize_video_frames(
    model, video_path: str | Path, out_path: str | Path, frame_size: Tuple[int, int] = (224, 224), sample_rate: int = 1
):
    """Colorize a video using the provided model.

    Args:
        model: trained Keras model that accepts (H,W,1) L inputs and returns (H,W,2) AB outputs.
        video_path: input video path
        out_path: output video path
        frame_size: size to resize frames for model
        sample_rate: process every sample_rate-th frame (1 means all frames)
    """
    from moviepy.editor import VideoFileClip

    clip = VideoFileClip(str(video_path))
    H, W = frame_size

    def process_frame(frame):
        # frame: HxWx3 RGB in 0..255 as numpy array
        # resize
        im = transform.resize(frame, (H, W), preserve_range=True, anti_aliasing=True)
        im = np.asarray(im / 255.0, dtype=np.float32)
        lab = color.rgb2lab(im)
        L = lab[..., 0:1] / 100.0
        L_input = np.expand_dims(L, axis=0)
        pred_ab = model.predict(L_input, verbose=0)[0]
        rgb = lab_to_rgb_batch(L, pred_ab[np.newaxis, ...])[0]
        # resize back to original frame size
        rgb_orig = transform.resize(rgb, (frame.shape[0], frame.shape[1]), preserve_range=True, anti_aliasing=True)
        return (rgb_orig * 255).astype(np.uint8)

    # apply process_frame to each frame and write video
    new_clip = clip.fl_image(process_frame)
    new_clip.write_videofile(str(out_path), audio=False)


def build_arg_parser():
    p = argparse.ArgumentParser()
    p.add_argument("--data-dir", default=None, help="Path to CelebA image directory (or any face images) where images are stored.")
    p.add_argument("--max-images", type=int, default=2000, help="Max images to load for quick experiments (None for all).")
    p.add_argument("--epochs", type=int, default=10)
    p.add_argument("--batch-size", type=int, default=32)
    p.add_argument("--output-dir", default="outputs/colorize")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--model-path", default=None, help="Path to save/load model.keras (HDF5 or Keras format).")
    p.add_argument("--train", action="store_true", help="Train model")
    p.add_argument("--colorize-video", default=None, help="Path to video to colorize")
    p.add_argument("--video-out", default="colored_output.mp4", help="Path for output colored video")
    p.add_argument("--no-gui", action="store_true", help="Don't show matplotlib plots (useful on headless servers)")
    return p


def main():
    args = build_arg_parser().parse_args()
    set_seed(args.seed)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.data_dir is None and args.colorize_video is None:
        print("Provide --data-dir to train or --colorize-video to colorize a movie.")
        return

    # build or load model
    model = build_colorization_model((224, 224, 1))
    if args.model_path and Path(args.model_path).exists():
        print(f"Loading model from {args.model_path}")
        import tensorflow as tf

        model = tf.keras.models.load_model(args.model_path)

    if args.train:
        imgs = load_images_from_dir(args.data_dir, max_images=args.max_images, target_size=(224, 224))
        L, AB = prepare_data_from_rgb(imgs)
        X_train, X_test, y_train, y_test, imgs_train, imgs_test = None, None, None, None, None, None
        # train/test split
        X_train, X_test, y_train, y_test = train_test_split(L, AB, test_size=0.2, random_state=args.seed)

        print("Training shapes:", X_train.shape, y_train.shape)
        # fit
        callbacks = []
        try:
            import tensorflow as tf
            callbacks = [tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)]
        except Exception:
            pass

        history = model.fit(
            X_train,
            y_train,
            validation_split=0.1,
            epochs=args.epochs,
            batch_size=args.batch_size,
            callbacks=callbacks,
        )

        # save model
        model_path = Path(args.model_path) if args.model_path else out_dir / "model.keras"
        model.save(model_path)
        print(f"Saved model to {model_path}")

        # evaluate
        loss, mse = model.evaluate(X_test, y_test, verbose=1)
        print(f"Test MSE: {mse:.6f}")

        # predict a few and plot
        preds = model.predict(X_test[:10], verbose=0)
        if not args.no_gui:
            plot_results(imgs[:10], X_test[:10], preds, n=5, out_dir=out_dir)

    if args.colorize_video:
        if not Path(args.model_path or out_dir / "model.keras").exists():
            print("Model path not found. Train a model first or provide --model-path to an existing trained model.")
            return
        # load model if not already
        import tensorflow as tf

        if args.model_path:
            model = tf.keras.models.load_model(args.model_path)
        else:
            model = tf.keras.models.load_model(str(out_dir / "model.keras"))

        print("Colorizing video (may be slow). This processes every frame at 224x224 resolution then resizes back.")
        colorize_video_frames(model, args.colorize_video, args.video_out, frame_size=(224, 224))


if __name__ == "__main__":
    main()

