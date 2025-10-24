from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Load the digits dataset
dataset = load_digits()

# Show dataset size
print("Dataset shape:", dataset.data.shape)

# Show a sample image
plt.imshow(dataset.images[400], cmap='gray')
plt.title(f"Label: {dataset.target[500]}")
plt.show()

# Show the output label
print("Label for image 400:", dataset.target[500])
