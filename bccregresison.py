from scipy.stats import gamma


class BrestCancerCampaignRegression:
    def __init__(self):
        pass

    def bccampiagain(self):
        #step 1
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import OneHotEncoder, StandardScaler
        from sklearn.pipeline import Pipeline
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.svm import SVR
        from sklearn.metrics import r2_score

        df=pd.read_csv('/Users/Yuvaan/Downloads/insurance.csv')

        #step2 drop. missing value and colum and data cleanup
        for col in ["Unnamed: 32", "unnamed: 32", "Unnamed:32"]:
            if col in df.columns:
                df = df.drop(columns=[col])
        missing_before = df.isna().sum().sum()
        df = df.dropna()
        missing_after = df.isna().sum().sum()

        print(f"Missing values before drop: {missing_before}")
        print(f"Missing values after drop:  {missing_after}")

        #drop duplicates and unnecessary columns
        df=df.drop_duplicates()
        df=df.transpose().drop_duplicates().transpose()
        #drop_cols = [c for c in ["id"] if c in df.columns]
        #df = df.drop(columns=drop_cols)

        #step3 feature selection and prepreocessing prepration
        target_col = "charges"
        X = df.drop(columns=[target_col])
        y = df[target_col].astype(float)
        numeric_features = list(X.select_dtypes(include=["int64", "float64"]).columns)
        categorical_features = list(X.select_dtypes(include=["object", "bool", "category"]).columns)
        transformers_prep = []
        if numeric_features:
            transformers_prep.append(("num", StandardScaler(), numeric_features))
        if categorical_features:
            transformers_prep.append(("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features))
        preprocessor = ColumnTransformer(transformers=transformers_prep)


        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
        print(f"Train size: {len(X_train)}")
        print(f"Validation size: {len(X_val)}")
        print(f"Test size: {len(X_test)}")

        X_train_full = pd.concat([X_train, X_val])
        y_train_full = pd.concat([y_train, y_val])
        svr_pipeline = Pipeline(steps=[("preprocess", preprocessor), ("model", SVR(kernel="rbf", gamma='auto', C=20.0, epsilon=0.1))])
        svr_pipeline.fit(X_train_full, y_train_full)
        y_test_pred_svr = svr_pipeline.predict(X_test)
        svr_r2_test = r2_score(y_test, y_test_pred_svr)

        from sklearn.tree import DecisionTreeRegressor
        dct_pipeline = Pipeline(steps=[("preprocess", preprocessor), ("model", DecisionTreeRegressor(random_state=0,criterion='absolute_error'))]) #
        dct_pipeline.fit(X_train_full, y_train_full)
        y_test_pred_dct = dct_pipeline.predict(X_test)
        tree_r2_test = r2_score(y_test, y_test_pred_dct)


        from sklearn.ensemble import RandomForestRegressor  # import the Decision Tree classifier
        rf_pipeline = Pipeline(steps=[("preprocess", preprocessor), ("model", RandomForestRegressor(n_estimators=100, random_state=42))]) #
        rf_pipeline.fit(X_train_full, y_train_full)
        y_test_pred_rf = rf_pipeline.predict(X_test)
        rf_r2_test = r2_score(y_test, y_test_pred_rf)




        print("\n============== FINAL TEST RESULTS ==============")
        #print(f"Decision Tree Regressor (criterion={best_criterion}): R^2 on test set = {tree_r2_test:.4f}")
        print(f"Decision Tree Regressor (criterion=mae): R^2 on test set = {tree_r2_test:.4f}")
        print(f"SVR Regressor (RBF kernel):                   R^2 on test set = {svr_r2_test:.4f}")
        print(f"Random forest:                   R^2 on test set = {rf_r2_test:.4f}")

        #Prepare Visualization
        # You are required to deliver a number of visualization for your dataset, including:
        #     Pair plots for the features.
        #     A correlation matrix heat map.
        # Box plots for the features.
        #     Hint:
        # Feel free to add any other visualizations you would like!
        import matplotlib.pyplot as plt
        import seaborn as sns
        import numpy as np
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Features", y=1.02)
        plt.show()
        plt.figure(figsize=(10, 8))
        corr = df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Matrix Heatmap")
        plt.tight_layout()
        plt.show()
        df_long = df.melt(id_vars=[target_col], value_vars=X.columns, var_name="feature", value_name="value")
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df_long, x="feature", y="value")
        plt.title("Box Plots for Features")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        return "Done"



bc=BrestCancerCampaignRegression()
print(bc.bccampiagain())