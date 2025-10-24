def main():
    import numpy as np
    from sklearn.datasets import load_iris
    dataset = load_iris()
    data=dataset.data #shape: (150,4)
    means = np.mean(data, axis=0)
    variances =np.var(data, axis=0)

    # Calculate means and variances for each attribute (column)

    # Write your code here. Do not change any other parts of the code
    print("max means::",np.max(means))
    print("max vairance :::",np.max(np.var(data, axis=0)))
    print(' sepal length, sepal width, petal length, and petal width mean::',means)
    print(' sepal length, sepal width, petal length, and petal width variances::',variances)
    return means, variances
if __name__=="__main__":
    main()