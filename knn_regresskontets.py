def main():

    import pandas as pd
    dataset = pd.read_csv('mushrooms.csv')

    y = dataset.iloc[:, 0].values
    selected_X = dataset.iloc[:, 1:3].values

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    encoded_y = LabelEncoder().fit_transform(y)
    encoded_X = OneHotEncoder().fit_transform(selected_X).toarray()

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(encoded_X, encoded_y, test_size=0.33, random_state=0)

    # Write your code here. Do not change any other parts of the code
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    #uncomment the following line when you write the code for it to run
    print(score)
    return score
main()


# Instructions
#
# Try classifying the Mushrooms dataset using k-nearest neighbor (KNN)!
#
# To complete this mission, your code should perform the following tasks:
#
# 1.    Train a KNeighborsClassifier model using X_train and y_train with the following parameters:
#
# Five neighbors
# 2.    Score your model using X_test and y_test.
#
# Your code should return the model score using the test dataset.
#
# Revisit the Mushrooms dataset here.
