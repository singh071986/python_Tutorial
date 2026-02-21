class BrestCancerCampaign:
    def __init__(self):
        pass

    def bccampiagain(self):

        import pandas as pd
        df=pd.read_csv('/Users/Yuvaan/Downloads/data.csv')

        for col in ["Unnamed: 32", "unnamed: 32", "Unnamed:32"]:
            if col in df.columns:
                df = df.drop(columns=[col])
        df = df.drop(columns=['id'])
        df = df.dropna()
        # df_encoded = pd.get_dummies(df, drop_first=True)

        y = df["diagnosis"].values
        X = df.drop(columns=["diagnosis"])

        X = pd.get_dummies(X)

        from sklearn.preprocessing import LabelEncoder
        encoder = LabelEncoder()
        y = encoder.fit_transform(y)

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)


        import tensorflow
        from tensorflow import keras
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Dense

        model = Sequential()
        model.add(Dense(100, activation='relu', input_shape=(x_train.shape[1],)))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=100, batch_size=20, verbose=0)
        y_pred_prob = model.predict(x_test)
        y_pred = (y_pred_prob.flatten() > 0.5).astype(int)
        from sklearn.metrics import accuracy_score, confusion_matrix
        print('Accuracy score: ' + str(accuracy_score(y_test, y_pred) * 100))
        confusion_matrix = confusion_matrix(y_test, y_pred)
        print('Confusion Matrix:\n' + str(confusion_matrix))
        from sklearn.metrics import r2_score
        print('R2 squared score: ' + str(r2_score(y_test,y_pred)*100))
        return confusion_matrix

bc=BrestCancerCampaign()
print(bc.bccampiagain())


# df_insurence=pd.read_csv('/Users/Yuvaan/Desktop/insurance.csv')
# for col in ["Unnamed: 32", "unnamed: 32", "Unnamed:32"]:
#     if col in df_insurence.columns:
#         df_insurence = df_insurence.drop(columns=[col])
# y_insurence = df_insurence["charges"]
# X_insurence = df_insurence.drop(columns=["charges"])
