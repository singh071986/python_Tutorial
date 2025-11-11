class ChocolateDataAnalysis:
    def __init__(self):
        pass
    def chocolate_analysis(self):
        import pandas as pd
        df=pd.read_csv('/Users/Yuvaan/Downloads/flavors_of_cacao.csv')
        #print(df.head())
        #df.info()
        #print(df.isnull().sum())
        #print(df_cleaned.isnull().head())
        print(f"total count before cleaning ::{df.shape}")
        print(f"total rows/tuple before cleaning: {df.shape[0]}")
        print(f"total columns/attributes before cleaning: {df.shape[1]}")
        print("Total missing values before cleaning :", df.isnull().sum().sum())
        df_cleaned=df.dropna()
        print(f"\ntotal count after cleaning ::{df_cleaned.shape}")

        print(f"total columns/attributes after cleaning: {df_cleaned.shape[1]}") #
        print("Total missing values after cleaning :", df_cleaned.isnull().sum().sum())
        #print(f"Rows with missing values:{df.isnull().any(axis=1).sum()}")
        #step3
        print(f"total rows/tuple after cleaning: {df_cleaned.shape[0]}") #
        print(f"Unique company names count : {df_cleaned['Company'].nunique()}")
        print(f"Number of reviews in 2013: {df_cleaned[df_cleaned['Review_Date']==2013].shape[0]}")
        print(f"Number of Bean_Type null values in df: {df['Bean_Type'].isnull().sum()}")

        #step4
        #Visualize the rating column with a histogram!
        import matplotlib.pyplot as plt
        rating=df_cleaned['Rating']
        plt.hist(rating,color='purple', bins=10,alpha=0.6 ,label='Rating Distribution ')
        plt.xlabel("Ratings")
        plt.ylabel("Count")
        plt.legend()
        plt.title("Chocolate Ratings Distribution")
        plt.show()
        count_of_cocoa_in_chocolate=df_cleaned['Cocoa_Percent'].str.rstrip('%').astype(float)

        #Step5
        plt.scatter(count_of_cocoa_in_chocolate, rating,color='brown',alpha=0.1 ,label='Cocoa Percent as number vs Rating')
        plt.xlabel("Cocoa Percent as number")
        plt.ylabel("Ratings")
        plt.legend()
        plt.title("Cocoa Percent vs Chocolate Ratings")
        plt.show()

        #step6
        min_rating, max_rating=rating.min(), rating.max() # or df['Rating'].min(), df['Rating'].max()
        print(f"Minimum Rating: {min_rating}")
        print(f"Maximum Rating: {max_rating}")
        df['Normalizedrating']=(rating - min_rating) / (max_rating - min_rating) # or (df['Rating'] - min_rating) / (max_rating - min_rating)
        print(f"Dataframe with Normalized Rating:\n {df[['Rating', 'Normalizedrating']].head()}")

        #step7
        #List the companies ordered by their average score (averaged over each company’s reviews).
        company_avg_rating=df_cleaned.groupby('Company')['Rating'].mean().sort_values(ascending=False)
        print(f"Companies ordered by their average score:\n {company_avg_rating}")
        #step8
        #Suppose we are interested in the company’s names and locations for some collective analysis. Encode the two categorical columns with the encoder you think is best for the job!
        from sklearn.preprocessing import LabelEncoder
        encoder=LabelEncoder()
        df_cleaned['Company_Encoded']=encoder.fit_transform(df_cleaned['Company'])
        df_cleaned['Location_Encoded']=encoder.fit_transform(df_cleaned['Company_location'])
        print(f"Dataframe with Encoded Company and Company_location:\n {df_cleaned[['Company', 'Company_Encoded', 'Company_location', 'Location_Encoded']].head()}")
ca=ChocolateDataAnalysis()
ca.chocolate_analysis()