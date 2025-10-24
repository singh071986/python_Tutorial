def main():

    import pandas as pd
    from sklearn.preprocessing import LabelEncoder,OneHotEncoder
    dataset = pd.read_csv('mushrooms.csv')

    y = dataset.iloc[:, 0].values
    selected_X = dataset.iloc[:, 1:3].values

    # Encode y (class attribute) using LabelEncoder
    label_encoder=LabelEncoder()
    encoded_y=label_encoder.fit_transform(y)

    # Encode selected_X using OneHotEncoder
    pne_hot_encoder=OneHotEncoder(sparse=False)
    #pne_hot_encoder=OneHotEncoder().toarray()
    encoded_X=pne_hot_encoder.fit_transform(selected_X)

    # Write your code here. Uncomment the following when you are done.
    print(encoded_X[0,:])
    return encoded_y, encoded_X

if __name__=="__main__":
    main()