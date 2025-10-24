"""
Logistic Regression Example in Python using Scikit-learn

This script demonstrates how to:
1. Load data from a CSV file using pandas
2. Normalize features using StandardScaler
3. Split data into training and test sets
4. Train a logistic regression model
5. Make predictions
6. Evaluate accuracy
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Step 1: Load data
# Replace 'data.csv' with your actual CSV file name
# The CSV should have features in columns and the target variable in the last column

def main():

    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    # Write your code here. Do not change any other parts of the code
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial', max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)

    from sklearn.metrics import precision_score
    print('precision score: '+ str(precision_score(y_test, y_pred, average='weighted')))

    return score
main()


# Instructions
#
# Let's try classifying the Iris dataset using logistic regression!
#
# To complete this mission, your code should perform the following tasks:
#
# 1. Train a LogisticRegression model using X_train and y_train with the following parameters:
#    - random_state=0 (for consistent output)
#    - L-BFGS solver
#    - multi_class='multinomial' (because the data is not binary)
#    - max_iter = 1000
# 2. Score your model using X_test and y_test.
#
# Your code should return the model score using the test dataset.
#
# Revisit the iris dataset here.
