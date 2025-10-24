def main():
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    X, y = load_iris(return_X_y=True)

    # Write your code here. Do not change any other parts of the code
    import numpy as np
    scaler= StandardScaler()
    scaled_X=scaler.fit_transform(X)
    #uncomment the two lines after assigning the values to "scaled_X" in order to complete this mission
    print(np.mean(scaled_X))
    print(scaled_X)
    return scaled_X


if __name__=="__main__":
    main()



# Instructions:
#
# Time to practice scaling features! You will now return to the Iris dataset!
#
# Your code should perform the following tasks to complete this mission in the editor provided:
#
# Load the Iris dataset from scikit-learn as a data vector X and a label vector y; and
# Scale the data vector X with a standard scaler (normalize X).
# Your code should return the scaled data vector scaled_X.
#
# SELF-CHECK: notice the result of calling mean(axis=0) and var(axis=0) (or var(axis=0)) for scaled_X!
#
# Revisit the Iris dataset here.