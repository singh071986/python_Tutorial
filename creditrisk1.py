# python
from prompt_toolkit.shortcuts import clear


def main():
    import pandas as pd
    from sklearn.datasets import fetch_openml

    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import precision_score

    data = fetch_openml(data_id=31, as_frame=True)
    df = data.frame
    if df.isna().sum().sum() > 0:
        df = df.dropna(inplace=True)  # assign result back to df to drop missing values
    df = df.drop_duplicates() # drop duplicate rows
    df = df.transpose().drop_duplicates().transpose() # drop duplicate columns
    #Feature Selection
    #Choose the features you think are relevant to our analysis! There are A LOT of features in this dataset, but we have to make our model's training time reasonable.
    #You MUST include at least four (4) numeric features and at least three (3) nominal features. You can choose more if you prefer.
    # identify target (last column) and encode it to discrete labels first
    target_col = df.columns[-1] # or "class"
    numeric_features = ["duration", "credit_amount", "age", "installment_commitment"]
    categorical_features = ["checking_status", "credit_history", "purpose", "savings_status"]
    # keep only features that actually exist in the dataframe
    y=df[target_col]
    x=df[numeric_features+ categorical_features]
    print(y)
    print(x)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.20, random_state=0)
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
    preprocessor = ColumnTransformer([("num", StandardScaler(),numeric_features),("cat",OneHotEncoder(handle_unknown="ignore"),categorical_features)])
    X_train=preprocessor.fit_transform(X_train)
    X_test=preprocessor.transform(X_test)
    k_values=[1,3,5,7,9,11,13,15,17,19,21,23,25]
    all_score={}
    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred=model.predict(X_test)
        score=model.score(X_test, y_test)
        #print(f"Model score for k={k}: {score}")
        print(f"Precision score for k={k}: {precision_score(y_test, y_pred, average='weighted')}")
        all_score[k]=score
    print(all_score)
    print(f"Best k value is {max(all_score, key=all_score.get)} ")


    #step 6
    #     Training Classifiers
    # Use the KNN-classifier model to train your data.
    # Choose the best k for the KNN algorithm by trying different values and validating performance on the validation set.
    # Note:
    # choosing the best k is an example of hyper-parameter tuning.
    # Classification Metrics
    # Print the accuracy score of your final classifier.
    # print the confusion matrix.
    best_k = max(all_score, key=all_score.get)
    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(X_train, y_train)
    y_pred=model.predict(X_test)
    score=model.score(X_test, y_test)
    print(f"Final Model score for best k={best_k}: {score}")
    from sklearn.metrics import confusion_matrix
    cm=confusion_matrix(y_test, y_pred)
    print(f"Confusion Matrix:\n {cm}")

    #step 6 using SVC classifier
    from sklearn.svm import SVC
    model=SVC( kernel="rbf",gamma="auto",C=1.0, random_state=42 )   #c and degree are hyperparameters
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    score=model.score(X_test, y_test)
    print('SVC model score: '+ str(score))
    print('SVC precision score: '+ str(precision_score(y_test, y_pred, average='weighted')))




main()


