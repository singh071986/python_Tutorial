"""Evaluate a saved Fashion-MNIST model and produce reports/plots."""
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import fashion_mnist


def prepare_data():
    (_, _), (x_test, y_test) = fashion_mnist.load_data()
    x_test = x_test.astype('float32') / 255.0
    x_test = np.expand_dims(x_test, -1)
    return x_test, y_test


def plot_confusion_matrix(y_true, y_pred, labels, out_path):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_sample_predictions(x_test, y_true, y_pred, out_path, class_names):
    plt.figure(figsize=(12, 8))
    for i in range(20):
        plt.subplot(4, 5, i+1)
        plt.imshow(x_test[i].squeeze(), cmap='gray')
        plt.title(f"T:{class_names[y_true[i]]}\nP:{class_names[y_pred[i]]}")
        plt.axis('off')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main(args):
    x_test, y_test = prepare_data()
    model = load_model(args.model_path)
    preds = model.predict(x_test, batch_size=256)
    y_pred = preds.argmax(axis=1)

    labels = [
        'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
    ]

    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir, exist_ok=True)

    # metrics
    report = classification_report(y_test, y_pred, target_names=labels, digits=4)
    print(report)
    with open(os.path.join(args.out_dir, 'classification_report.txt'), 'w') as f:
        f.write(report)

    plot_confusion_matrix(y_test, y_pred, labels, os.path.join(args.out_dir, 'confusion_matrix.png'))
    plot_sample_predictions(x_test, y_test, y_pred, os.path.join(args.out_dir, 'sample_predictions.png'), labels)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-path', type=str, required=True)
    parser.add_argument('--out-dir', type=str, default='reports')
    args = parser.parse_args()
    main(args)

