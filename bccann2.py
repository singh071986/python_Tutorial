class BrestCancerCampaign:
    def __init__(self):
        pass

    def bccampiagain(self):

        import pandas as pd
        df=pd.read_csv('/Users/Yuvaan/Downloads/insurance.csv')
        for col in ["Unnamed: 32", "unnamed: 32", "Unnamed:32"]:
            if col in df.columns:
                df = df.drop(columns=[col])
        #df = df.drop(columns=['id'])
        df = df.dropna()
        y = df["charges"].values
        X = df.drop(columns=["charges"])
        #X = pd.get_dummies(X)
        print(X.columns)

        from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
        from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

        cols = ['smoker', 'sex', 'region']
        encoder = OrdinalEncoder()
        X[cols] = encoder.fit_transform(X[cols]).astype(int)

        print(X.columns)
        print(X.head())


        from sklearn.model_selection import train_test_split
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=0)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=0)

        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        x_train = scaler.fit_transform(X_train)
        x_val = scaler.transform(X_val)
        x_test = scaler.transform(X_test)

        #Using MLP regressor from sklearn
        from sklearn.neural_network import MLPRegressor
        model=MLPRegressor(hidden_layer_sizes=(100,100,100),activation ='relu', solver='adam',max_iter=100,batch_size=20,random_state=0)
        model.fit(x_train, y_train)
        # test metrics
        y_test_pred = model.predict(x_test)
        mse_test = mean_squared_error(y_test, y_test_pred)
        mae_test = mean_absolute_error(y_test, y_test_pred)
        r2_test = r2_score(y_test, y_test_pred) * 100

        # validation metrics
        y_val_pred = model.predict(x_val)
        mse_val = mean_squared_error(y_val, y_val_pred)
        mae_val = mean_absolute_error(y_val, y_val_pred)
        r2_val = r2_score(y_val, y_val_pred) * 100

        print(f"MLPRegressor - Test       MSE: {mse_test:.4f}, MAE: {mae_test:.4f}, R2: {r2_test:.4f}%")
        print(f"MLPRegressor - Validation MSE: {mse_val:.4f}, MAE: {mae_val:.4f}, R2: {r2_val:.4f}%")


        #using tensorflow for regression
        import tensorflow
        from tensorflow import keras
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Dense

        model = Sequential()
        model.add(Dense(100, activation='relu', input_shape=(x_train.shape[1],)))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(100, activation='relu'))
        #model.add(Dense(1, activation='sigmoid'))
        model.add(Dense(1),activation='' )
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        #model.fit(x_train, y_train, epochs=100, batch_size=20, verbose=0, validation_data=(x_val, y_val))

        # fit (example: model already built with final Dense(1) and compiled with loss='mse', metrics=['mae'])
        model.fit(x_train, y_train, epochs=100, batch_size=20, verbose=0, validation_data=(x_val, y_val)) #verbose ==1 for print all epochs

        # compute validation R2 and test R2 after training
        y_val_pred = model.predict(x_val).flatten()
        y_test_pred = model.predict(x_test).flatten()

        mse_tf_val = mean_squared_error(y_val, y_val_pred)
        mae_tf_val = mean_absolute_error(y_val, y_val_pred)
        r2_tf_val = r2_score(y_val, y_val_pred) * 100.0  # percent

        mse_Tf_test = mean_squared_error(y_test, y_test_pred)
        mae_tf_test = mean_absolute_error(y_test, y_test_pred)
        r2_tf_tst = r2_score(y_test, y_test_pred) * 100.0  # percent


        #y_test_pred_tf = model.predict(x_test).flatten()

        # mse_tf = mean_squared_error(y_test, y_test_pred_tf)
        # mae_tf = mean_absolute_error(y_test, y_test_pred_tf)
        # r2_tf = r2_score(y_test, y_test_pred_tf) * 100

        print(f"TensorFlow - Test MSE: {mse_Tf_test:.4f}, MAE: {mae_tf_test:.4f}, R2: {r2_tf_tst:.4f}%")
        print(f"TensorFlow - VaL MSE: {mse_tf_val:.4f}, MAE: {mae_tf_val:.4f}, R2: {r2_tf_val:.4f}%")


bc=BrestCancerCampaign()
print(bc.bccampiagain())


#below code can be used for one column at a time encoding
# from sklearn.preprocessing import LabelEncoder
# encoder = LabelEncoder()
# X['smoker'] = encoder.fit_transform(X['smoker'])
# X['sex'] = encoder.fit_transform(X['sex'])
# X['region'] = encoder.fit_transform(X['region'])
# print(X.head())
#
# encoder = LabelEncoder()
# x_smoker_encoded = encoder.fit_transform(X['smoker'])
# X = X.drop(columns=['smoker'])
# X['smoker'] = x_smoker_encoded
#
# x_sex_encoded = encoder.fit_transform(X['sex'])
# X = X.drop(columns=['sex'])
# X['sex'] = x_sex_encoded
#
# x_region_encoded = encoder.fit_transform(X['region'])
# X = X.drop(columns=['region'])
# X['region'] = x_region_encoded
