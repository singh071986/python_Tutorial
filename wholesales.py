class WholesaleOrder:


    def __init__(self):
        pass

    def wholesalesalanalysis(self):
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn.cluster import KMeans
        from sklearn import datasets

        csv_path = "/Users/Yuvaan/Downloads/Wholesale_customers_data.csv"
        df = pd.read_csv(csv_path)

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
        X = df.drop(columns=["Channel","Region"])
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        print(f"Scaled Data:\n {X_scaled[:5]}")

        Inertias = []
        K = range(1,10)
        for k in K:
            kmeanModel = KMeans(n_clusters=k)
            kmeanModel.fit(df[["Fresh", "Milk"]])
            Inertias.append(kmeanModel.inertia_)

            # Create a single figure with 1 row and 2 columns
            fig, axes = plt.subplots(1, 2, figsize=(14, 6))

            # Right subplot: Clustering scatter
            kmeans = KMeans(n_clusters=k, random_state=42)
            clusters = kmeans.fit_predict(X_scaled)
            axes[0].scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.6)
            axes[0].set_xlabel('Fresh')
            axes[0].set_ylabel('Milk')
            axes[0].set_title('Wholesale Customers Clustering for K={}'.format(k))
            # Additional subplot: Cluster centers
            centers = kmeans.cluster_centers_
            axes[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.6)
            axes[1].scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centers')
            axes[1].set_xlabel('Fresh')
            axes[1].set_ylabel('Milk')
            axes[1].set_title('Clusters with Centers')
            axes[1].legend()

            plt.tight_layout()
            plt.show()

            # kmeans = KMeans(n_clusters=k, random_state=42)
            # clusters = kmeans.fit_predict(X_scaled)
            # plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.6)
            # plt.xlabel('Fresh')
            # plt.ylabel('Milk')
            # plt.title('Wholesale Customers Clustering for K={}'.format(k))

            plt.show()


        print(Inertias)

        # Create a single figure with 1 row and 2 columns
        fig, axes = plt.subplots(1, 4, figsize=(14, 6))

        # Left subplot: Elbow method
        axes[0].plot(K, Inertias, 'bx-')
        axes[0].set_xlabel('k')
        axes[0].set_ylabel('Inertia')
        axes[0].set_title('Elbow Method')

        # Right subplot: Clustering scatter
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)
        axes[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.6)
        axes[1].set_xlabel('Fresh')
        axes[1].set_ylabel('Milk')
        axes[1].set_title('FInal Wholesale Customers Clustering with best  K=3')
        # Additional subplot: Cluster centers
        centers = kmeans.cluster_centers_
        axes[2].scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.6)
        axes[2].scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centers')
        axes[2].set_xlabel('Fresh')
        axes[2].set_ylabel('Milk')
        axes[2].set_title('Clusters with Centers')
        axes[2].legend()

        plt.tight_layout()
        plt.show()

        #print(X_scaled.head())

        #optional step: visualise dandogram
        import scipy.cluster.hierarchy as sch
        dendrogram = sch.dendrogram(sch.linkage(X_scaled, method='ward'))
        plt.title("Dendrogram for Wholesale Customers")
        plt.xlabel("Customers")
        plt.ylabel("Euclidean distances")
        plt.show()

        print("Wholesale Sales Analysis Completed")


        from sklearn.cluster import AgglomerativeClustering
        clusters = AgglomerativeClustering(n_clusters=4, linkage='ward').fit_predict(X)




# plt.figure(figsize=(12,8))
# plt.plot(K, Inertias, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Inertias')
# plt.title('The Elbow Method showing the optimal k')
# plt.show()
#
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=3, random_state=42)
# #print(kmeans.inertia_)
# clusters = kmeans.fit_predict(X_scaled)
#
# import seaborn as sns
# plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.6)
# plt.xlabel('Fresh')
# plt.ylabel('Milk')
# plt.title('Wholesale Customers Clustering')
# plt.show()

pd=WholesaleOrder()
pd.wholesalesalanalysis()