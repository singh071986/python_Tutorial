class ProductDemandForecast:

    def __init__(self):
        pass

    def prodctdemand_analysis(self):
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import OneHotEncoder, StandardScaler
        from sklearn.pipeline import Pipeline
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.svm import SVR
        from sklearn.metrics import r2_score
        import numpy as np

        csv_path = "/Users/Yuvaan/Downloads/Historical_Product_Demand.csv"
        df = pd.read_csv(csv_path)
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.year
            df["Month"] = df["Date"].dt.month
            df["Day"] = df["Date"].dt.day
            df.drop(columns=["Date"], inplace=True)
        target_col = "Order_Demand"
        df[target_col] = pd.to_numeric(df[target_col], errors="coerce")

        df = df.dropna()
        X = df.drop(columns=[target_col])
        y = df[target_col].astype(float)

        numeric_features = list(X.select_dtypes(include=["int64", "float64"]).columns)
        categorical_features = list(X.select_dtypes(include=["object", "bool", "category"]).columns)
        transformers = []
        if numeric_features:
            transformers.append(("num", StandardScaler(), numeric_features))
        if categorical_features:
            transformers.append(("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features))
        preprocessor = ColumnTransformer(transformers=transformers)

        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
        print(f"Train size: {len(X_train)}")
        print(f"Validation size: {len(X_val)}")
        print(f"Test size: {len(X_test)}")

        X_train_full = pd.concat([X_train, X_val])
        y_train_full = pd.concat([y_train, y_val])
        svr_pipeline = Pipeline(steps=[("preprocess", preprocessor), ("model", SVR(kernel="rbf", C=10.0, epsilon=0.1, max_iter=100))])
        svr_pipeline.fit(X_train_full, y_train_full)
        y_test_pred_svr = svr_pipeline.predict(X_test)
        svr_r2_test = r2_score(y_test, y_test_pred_svr)

        from sklearn.tree import DecisionTreeRegressor
        dct_pipeline = Pipeline(steps=[("preprocess", preprocessor), ("model", DecisionTreeRegressor(random_state=0,criterion='absolute_error'))]) #
        dct_pipeline.fit(X_train_full, y_train_full)
        y_test_pred_dct = dct_pipeline.predict(X_test)
        tree_r2_test = r2_score(y_test, y_test_pred_dct)



        print("\n============== FINAL TEST RESULTS ==============")
        #print(f"Decision Tree Regressor (criterion={best_criterion}): R^2 on test set = {tree_r2_test:.4f}")
        print(f"Decision Tree Regressor (criterion=mae): R^2 on test set = {tree_r2_test:.4f}")
        print(f"SVR Regressor (RBF kernel):                   R^2 on test set = {svr_r2_test:.4f}")

pd=ProductDemandForecast()
pd.prodctdemand_analysis()