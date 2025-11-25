def main():

    #step 2
    import pandas as pd
    df = pd.read_csv('/Users/Yuvaan/Downloads/KaggleV2-May-2016.csv')
    print(f"Dataframe shape: {df.shape}")
    print(f"Number of missing values:\n {df.isnull().sum().sum()}")       # detect missing values
    df_cleaned = df.dropna()  # drop missing values
    print(f"Dataframe shape after dropping missing values: {df_cleaned.shape}")
    df_cleaned.drop_duplicates() # drop duplicate rows
    print(f"Dataframe shape after dropping duplicate values: {df_cleaned.shape}")
    # df_cleaned.transpose().drop_duplicates().transpose() # drop duplicate columns
    # print(f"Dataframe shape after dropping duplicate column values: {df_cleaned.shape}")


   #step 3
    # Feature Extraction
    # Extract the following features:
    # Gender
    # Age
    # Scholarship
    # Hipertension
    # Diabetes
    # Alcoholism
    # Handcap
    # SMS_received
    # Note: you may see incorrect spelling. It is related to the dataset, for example:
    #     Hipertension=Hypertension
    # Handcap=Handicap
    selected_columns = ['Gender', 'Age', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received']
    df_features = df_cleaned[selected_columns]
    print(f"Extracted features dataframe shape: {df_features.shape}")
    print(f"First 5 rows of extracted features:\n {df_features.head()}")

    #step 4
    #     Preprocessing
    # Perform any needed pre-processing of the chosen features including:
    # Scaling
    # Encoding
    # Dealing with Nan values
    # Hint: use only the preprocessing steps you believe are useful.
    from sklearn.preprocessing import StandardScaler, LabelEncoder,OneHotEncoder
    print(df_features.dtypes)

    encoder = LabelEncoder()
    for col in df_features.select_dtypes(include=['object']).columns:
        df_features[col] = encoder.fit_transform(df_features[col])
    print(f"First 5 rows after encoding:\n {df_features.head()}")

    scaler = StandardScaler()
    df_features_scaled = scaler.fit_transform(df_features)
    print(f"First 5 rows after scaling:\n {df_features_scaled[:5]}")


    #Dealing with Nan values
    print(df_features.dtypes)
    #step 5
    #     Splitting the Data
    # Split your data as follows:
    # 80% training set
    # 10% validation set
    # 10% test set
    from sklearn.model_selection import train_test_split
    y=df["No-show"].map({'No':0,'Yes':1})
    x=df_features_scaled
    X_train, X_temp, y_train, y_temp = train_test_split(df_features_scaled, y, stratify=y, test_size=0.20, random_state=0)
    X_val, X_test = train_test_split(X_temp, test_size=0.50, random_state=0)
    y_val, y_test = train_test_split(y_temp, test_size=0.50, random_state=0)
    print(f"Training set shape: {X_train.shape}")
    print(f"Validation set shape: {X_val.shape}")
    print(f"Test set shape: {X_test.shape}")

    kernels = ["linear", "rbf", "poly", "sigmoid"]
    #kernels = ["rbf"]
    for k in kernels:
        from sklearn.svm import SVC
        model=SVC( kernel=k,gamma="auto",C=5, random_state=0, max_iter=100 )   #c and degree are hyperparameters
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)
        score=model.score(X_test, y_test)
        print(f'SVC model score with {k} kernel: '+ str(score))

    #step6
    from sklearn.tree import DecisionTreeClassifier  # import the Decision Tree classifier
    model = DecisionTreeClassifier(criterion='entropy', random_state=42)  # instantiate model with Gini impurity and max depth 4
    model.fit(X_train, y_train)  # train the decision tree on the training set
    y_pred = model.predict(X_test)  # predict labels for the test set
    score=model.score(X_test, y_test)
    print(f'decion tree   model score \n: '+ str(score))

    #step7
    from sklearn.ensemble import RandomForestClassifier  # import the Decision Tree classifier
    model = RandomForestClassifier(criterion='gini', n_estimators=100, random_state=42)  # instantiate model with Gini impurity and max depth 4
    model.fit(X_train, y_train)  # train the decision tree on the training set
    y_pred = model.predict(X_test)  # predict labels for the test set
    score=model.score(X_test, y_test)
    print(f'randon estate tree   model score \n: '+ str(score))

main()

# Convert 'ScheduledDay' and 'AppointmentDay' to datetime
    # df_cleaned['ScheduledDay'] = pd.to_datetime(df_cleaned['ScheduledDay'], errors='coerce')
    # df_cleaned['AppointmentDay'] = pd.to_datetime(df_cleaned['AppointmentDay'], errors='coerce')