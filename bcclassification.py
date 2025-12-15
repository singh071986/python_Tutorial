class BrestCancerCampaign:
    def __init__(self):
        pass

    def bccampiagain(self):
        #step 2
        # import pandas as pd
        # df=pd.read_csv('/Users/Yuvaan/Downloads/data_refined.csv')
        import pandas as pd
        df=pd.read_csv('/Users/Yuvaan/Downloads/data.csv')
        for col in ["Unnamed: 32", "unnamed: 32", "Unnamed:32"]:
            if col in df.columns:
                df = df.drop(columns=[col])
        missing_before = df.isna().sum().sum()
        df = df.dropna()
        missing_after = df.isna().sum().sum()

        print(f"Missing values before drop: {missing_before}")
        print(f"Missing values after drop:  {missing_after}")

        #step3
        #Dropping Unnecessary Columns
        # Choose the features you think are relevant to our analysis! There are a lot of features in this dataset but we have to make our model’s training time reasonable for you.
        #     Hint: Notice the fact that some of the data in the Breast Cancer dataset is irrelevant to the research such as the id attribute.
        df=df.drop_duplicates()
        df=df.transpose().drop_duplicates().transpose()
        drop_cols = [c for c in ["id"] if c in df.columns]
        df = df.drop(columns=drop_cols)
        target_col = "diagnosis"
        candidate_features = [
            "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
            "compactness_mean", "concavity_mean", "concave_points_mean", "symmetry_mean",
            "fractal_dimension_mean"]
        kept = [c for c in candidate_features if c in df.columns]
        cols = [target_col] + kept
        df = df[cols].copy()
        print(f"Using {len(kept)} features: {kept}")

        #step 4
        from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
        from sklearn.impute import SimpleImputer
        le = LabelEncoder()
        df[target_col] = le.fit_transform(df[target_col])
        X = df[kept].copy()
        y = df[target_col].copy()
        imputer = SimpleImputer(strategy="median")
        X_imputed = imputer.fit_transform(X)
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X_imputed)
        df_refined = pd.DataFrame(X_scaled, columns=kept)
        df_refined[target_col] = y.values
        print(df_refined.head())

        #xtep2 feature selection
        #     Feature Selection
        # Choosing only the most important features for training your classifier is one of the most important steps of the machine learning process. This can be done in many ways.
        # One of the simplest approaches is choosing the features with the highest correlation to the target data.
        # The label, in this case, is the 'Diagnosed' column.
        # The Diagnosed column has two distinct values:
        # M: Malignant Tumor
        # B: Benign Tumor
        # Calculate the correlation of all the features to their target labels.
        # Choose the most correlated features above a certain limit for training.
        #     Output a list of important feature names. You can use this list to filter your dataset for training.


        #Reduced set fo feature to achive 94%  precision score
        # compute correlations of all numeric columns with the target and sort
        corr_with_target = df_refined.corr()["diagnosis"].drop(labels=["diagnosis"]).sort_values(ascending=False)
        important_features = corr_with_target[corr_with_target > 0.3].index.tolist()
        print(f"Important features based on correlation to diagnosis: {important_features}")
        print(f"Max correlation values:{corr_with_target.idxmax() }: {corr_with_target[corr_with_target.idxmax()]}\n")
        # print feature name and correlation (signed)
        for feature, corr in corr_with_target.items():
            print(f"{feature}: {corr:.4f}")

        from sklearn.model_selection import train_test_split  # import train_test_split to split data into train/test sets
        X_train, X_test, y_train, y_test = train_test_split(df_refined[important_features], y, test_size=0.2, random_state=42)  # split: 80% train, 20% test


        #KNN Classifier
        k_values=[1,3,5,7,9,11,13,15,17,19,21,23,25]
        all_score={}
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import precision_score
        for k in k_values:
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(X_train, y_train)
            y_pred=model.predict(X_test)
            score=model.score(X_test, y_test)
            #print(f"Model score for k={k}: {score}")
            #print(f"Precision score for k={k}: {precision_score(y_test, y_pred, average='weighted')}")
            all_score[k]=score
        print(all_score)
        print(f"Best k value is {max(all_score, key=all_score.get)} ")
        best_k = max(all_score, key=all_score.get)
        print("best k:" , best_k)
        model = KNeighborsClassifier(n_neighbors=best_k)
        model.fit(X_train, y_train)
        y_pred=model.predict(X_test)
        precision = precision_score(y_test, y_pred, average='weighted')
        print(f"KNN model precision score: {precision * 100:.2f}%")
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test, y_pred)
        print(f"KNN data Confusion Matrix score :\n {cm}")

        #Random forest Classifier
        from sklearn.ensemble import RandomForestClassifier  # import the Decision Tree classifier
        model = RandomForestClassifier(criterion='entropy', n_estimators=1000, random_state=42)  # instantiate model with Gini impurity and max depth 4
        model.fit(X_train, y_train)  # train the decision tree on the training set
        y_pred = model.predict(X_test)  # predict labels for the test set
        precision = precision_score(y_test, y_pred, average='weighted')
        print(f"Random access model precision score: {precision * 100:.2f}%")
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test, y_pred)
        print(f"Random access  data Confusion Matrix score :\n {cm}")

        #SVC Classifier
        from sklearn.svm import SVC
        model=SVC( kernel="rbf",gamma="auto",C=1.0, random_state=42 )   #c and degree are hyperparameters
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)
        precision = precision_score(y_test, y_pred, average='weighted')
        print(f"SVC model precision score: {precision * 100:.2f}%")
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test, y_pred)
        print(f"SVC model  Confusion Matrix score :\n {cm}")




        from sklearn.model_selection import train_test_split  # import train_test_split to split data into train/test sets
        X_train, X_test, y_train, y_test = train_test_split(df_refined, y, test_size=0.2, random_state=42)  # split: 80% train, 20% test


        #KNN Classifier
        k_values=[1,3,5,7,9,11,13,15,17,19,21,23,25]
        all_score={}
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import precision_score
        for k in k_values:
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(X_train, y_train)
            y_pred=model.predict(X_test)
            score=model.score(X_test, y_test)
            #print(f"Model score for k={k}: {score}")
            #print(f"Precision score for k={k}: {precision_score(y_test, y_pred, average='weighted')}")
            all_score[k]=score
        print(all_score)
        print(f"Best k value is {max(all_score, key=all_score.get)} ")
        best_k = max(all_score, key=all_score.get)
        print("best k:" , best_k)
        model = KNeighborsClassifier(n_neighbors=best_k)
        model.fit(X_train, y_train)
        y_pred=model.predict(X_test)
        precision = precision_score(y_test, y_pred, average='weighted')
        print(f"KNN model precision score: {precision * 100:.2f}%")
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test, y_pred)
        print(f"KNN data Confusion Matrix score :\n {cm}")

        #Random forest Classifier
        from sklearn.ensemble import RandomForestClassifier  # import the Decision Tree classifier
        model = RandomForestClassifier(criterion='entropy', n_estimators=1000, random_state=42)  # instantiate model with Gini impurity and max depth 4
        model.fit(X_train, y_train)  # train the decision tree on the training set
        y_pred = model.predict(X_test)  # predict labels for the test set
        precision = precision_score(y_test, y_pred, average='weighted')
        print(f"Random access model precision score: {precision * 100:.2f}%")
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test, y_pred)
        print(f"Random access  data Confusion Matrix score :\n {cm}")

        #SVC Classifier
        from sklearn.svm import SVC
        model=SVC( kernel="rbf",gamma="auto",C=1.0, random_state=42 )   #c and degree are hyperparameters
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)
        precision = precision_score(y_test, y_pred, average='weighted')
        print(f"SVC model precision score: {precision * 100:.2f}%")
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test, y_pred)
        print(f"SVC model  Confusion Matrix score :\n {cm}")

        #Find another way to reduce the set of features to achive minimum 94% precision score wihotu corelation method









bc=BrestCancerCampaign()
print(bc.bccampiagain())