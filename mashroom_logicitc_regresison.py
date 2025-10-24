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
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr', max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)

    from sklearn.metrics import precision_score



    #uncomment the following two lines when you write the code for them to run
    print('precision score: '+ str(precision_score(y_test, y_pred)))
    return score
main()


# Instructions
#
# Let’s try classifying the Mushrooms dataset using logistic regression!
#
# To complete this mission, your code should perform the following tasks:
#
# 1.  Train a LogisticRegression model using X_train and y_train with the following parameters:
#
# random_state=0 (for consistent output)
# L-BFGS solver
# multi_class='ovr' (because the data is not binary)
# max_iter = 1000
# 2. Score your model using X_test and y_test.
#
# Using the test dataset, your code should return the model score.
#
# Revisit the Mushrooms dataset here.