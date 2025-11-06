import pandas as pd

#class ChocolateDataAnalysis:

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