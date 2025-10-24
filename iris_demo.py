from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def main():
    # Load the iris dataset
    datasets = load_iris()
    # Extract the data tuple and target at index 7
    data_tuple = datasets.data[7]
    target_label = datasets.target[7]
    # Extract sepal width (element at index 1)
    sepal_width = data_tuple[1]
    print("Sepal width at index 7:", sepal_width)
    print("Target label at index 7:", target_label)

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("Model score:", score)

    return sepal_width, target_label, score  # Return as a tuple

if __name__ == "__main__":
    main()
