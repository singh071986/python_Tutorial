Fashion MNIST classifier

This folder contains scripts to train and evaluate a CNN on the Fashion-MNIST dataset.

Quick start:

1. Install dependencies:

   pip install -r fashion_mnist/requirements.txt

2. Run a smoke test (1 epoch):

   python fashion_mnist/train.py --epochs 1 --model improved --use-augmentation --save-dir fashion_mnist/models

3. Full training example:

   python fashion_mnist/train.py --epochs 40 --batch-size 128 --model improved --use-augmentation --save-dir fashion_mnist/models

4. Evaluate a saved model:

   python fashion_mnist/evaluate.py --model-path fashion_mnist/models/fashion_mnist_best.h5 --out-dir fashion_mnist/reports

Files:
- train.py: training entry point
- models.py: model definitions
- evaluate.py: evaluation and plots
- requirements.txt: minimal dependencies

Goal: achieve >90% test accuracy using the improved model with augmentation and regularization.

