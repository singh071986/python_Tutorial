import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
class AvocadoAnalysis:
    def __init__(self):
        pass

    def analyze_avocados(self):
        df = pd.read_csv('/Users/Yuvaan/Downloads/avocado.csv')
        print(f"Initial DataFrame shape: {df.shape}")
        print(f"Missing values in each column before cleaning:\n{df.isnull().sum()}")

        df_cleaned = df.dropna()
        print(f"\nDataFrame shape after dropping missing values: {df_cleaned.shape}")
        print(f"Missing values in each column after cleaning:\n{df_cleaned.isnull().sum()}")


        # Encode categorical columns
        encoder = LabelEncoder()
        y= df_cleaned['type']
        y_cleaned= encoder.fit_transform(y)


        # Extract Features
        # Exclude the region and date from the considered features
        selected_columns = ['AveragePrice', 'Total Volume', '4046', '4225', '4770', 'Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags']

        X = df_cleaned[selected_columns]
        # Encode categorical columns



        # Perform Preprocessing
        # Perform any needed pre-processing on the chosen features including:
        # Scaling.
        # Encoding.
        # Dealing with Nan values.
        from sklearn.model_selection import train_test_split
        X_train, X_temp, y_train, y_temp = train_test_split(X, y_cleaned, test_size=0.2, random_state=42)

        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        x_train_scaled = scaler.fit_transform(X_train)
        X_temp_scaled = scaler.transform(X_temp)

        X_val, X_test, y_val, y_test = train_test_split(X_temp_scaled, y_temp, test_size=0.5, random_state=42)

        k_values=[1,3,5,7,9,11,13,15,17,19,21,23,25]
        all_score={}
        from sklearn.neighbors import KNeighborsRegressor
        from sklearn.metrics import precision_score
        for k in k_values:
            model = KNeighborsRegressor(n_neighbors=k)
            model.fit(x_train_scaled, y_train)
            y_val_pred=model.predict(X_val)
            score=model.score(X_val, y_val)
            all_score[k]=score
        print(all_score)
        best_k = max(all_score, key=all_score.get)
        print("best k:" , best_k)

        model=KNeighborsRegressor(n_neighbors=best_k)
        model.fit(x_train_scaled,y_train)
        score=model.score(X_test, y_test)

        print(score)
        #Print the R-squared score of your final KNN regressor.
        print(f"KNN Regressor score: {score * 100:.2f}%")
        from sklearn.metrics import r2_score
        y_test_pred=model.predict(X_test)
        r2 = r2_score(y_test, y_test_pred)
        print(f"KNN Regressor R2 score: {r2 * 100:.2f}%")


        # Visualize the average price distribution
        plt.hist(df_cleaned['AveragePrice'], color='green', bins=20, alpha=0.7, label='Average Price Distribution')
        plt.xlabel("Average Price")
        plt.ylabel("Count")
        plt.legend()
        plt.title("Avocado Average Price Distribution")
        plt.show()

av=AvocadoAnalysis()
av.analyze_avocados()