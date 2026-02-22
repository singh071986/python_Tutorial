"""Train script for Fashion MNIST models.
Usage examples:
  python fashion_mnist/train.py --model improved --epochs 1
"""
import os
import argparse
import json

import numpy as np
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from fashion_mnist.models import build_baseline, build_improved


def prepare_data():
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0

    # reshape to (N, 28, 28, 1)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    # create a small validation split from training data
    val_size = 5000
    x_val = x_train[-val_size:]
    y_val = y_train[-val_size:]
    x_train = x_train[:-val_size]
    y_train = y_train[:-val_size]

    return x_train, y_train, x_val, y_val, x_test, y_test


def get_datagen():
    return ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
    )


def main(args):
    x_train, y_train, x_val, y_val, x_test, y_test = prepare_data()

    input_shape = x_train.shape[1:]
    num_classes = 10

    if args.model == 'baseline':
        model = build_baseline(input_shape=input_shape, num_classes=num_classes, lr=args.lr)
    else:
        model = build_improved(input_shape=input_shape, num_classes=num_classes, lr=args.lr)

    os.makedirs(args.save_dir, exist_ok=True)
    checkpoint_path = os.path.join(args.save_dir, 'fashion_mnist_best.h5')

    callbacks = [
        ModelCheckpoint(checkpoint_path, save_best_only=True, monitor='val_accuracy', mode='max'),
        EarlyStopping(monitor='val_loss', patience=6, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6),
    ]

    if args.use_augmentation:
        datagen = get_datagen()
        datagen.fit(x_train)
        history = model.fit(datagen.flow(x_train, y_train, batch_size=args.batch_size),
                            epochs=args.epochs,
                            validation_data=(x_val, y_val),
                            steps_per_epoch=len(x_train) // args.batch_size,
                            callbacks=callbacks)
    else:
        history = model.fit(x_train, y_train, batch_size=args.batch_size, epochs=args.epochs,
                            validation_data=(x_val, y_val), callbacks=callbacks)

    # save history
    history_path = os.path.join(args.save_dir, 'history.json')
    with open(history_path, 'w') as f:
        json.dump({k: [float(x) for x in v] for k, v in history.history.items()}, f)

    # final evaluation on test set
    loss, acc = model.evaluate(x_test, y_test, verbose=2)
    print(f"Test loss: {loss:.4f}, Test accuracy: {acc:.4f}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', choices=['baseline', 'improved'], default='improved')
    parser.add_argument('--epochs', type=int, default=20)
    parser.add_argument('--batch-size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--save-dir', type=str, default='models')
    parser.add_argument('--use-augmentation', action='store_true')
    args = parser.parse_args()
    main(args)

