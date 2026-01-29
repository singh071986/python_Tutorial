# Unsupervised Machine Learning: Clustering Analysis

Summary
- This report summarizes four resources on clustering algorithms, practical use cases, and recommended evaluation and methodology for clustering projects.

Sources
- 10 use-cases for K-means: https://dzone.com/articles/10-interesting-use-cases-for-the-k-means-algorithm
- Hierarchical Clustering Applications: https://codinginfinite.com/hierarchical-clustering-applications-advantages-and-disadvantages/
- Clustering in Data Mining: https://www.scaler.com/topics/data-mining-tutorial/what-is-clustering-in-data-mining/
- Clustering for Social Media: https://medium.com/@data-overload/social-network-analysis-cb324aa45bd4

Key takeaways
- Clustering groups unlabeled data based on similarity; common goals include discovery of structure, customer segmentation, anomaly detection, and preprocessing for supervised tasks.
- K-means: efficient for large, spherical clusters; sensitive to initialization and k choice; fast and easy to scale.
- Hierarchical clustering: produces dendrograms for multi-level structure; useful when cluster count is unknown; can be computationally expensive for large datasets.
- Social media clustering: often focuses on community detection, influence analysis, topic grouping and edge-based clustering — graph clustering algorithms and network metrics are important.

10 practical K-means use cases (condensed)
1. Customer segmentation (marketing personalization)
2. Image compression and color quantization
3. Market basket analysis / product grouping
4. Anomaly detection (after modeling normal clusters)
5. Document clustering for topic discovery
6. Sensor data grouping (IoT)
7. Retail store layout and grouping similar stores
8. Biological data (gene expression clustering)
9. Recommendation systems (user grouping)
10. Geo-spatial clustering (locations and hotspots)

Hierarchical clustering: applications, pros & cons
- Applications: phylogenetics, document taxonomy, anomaly detection with multilevel insights, exploratory data analysis when the number of clusters is unknown.
- Advantages: no need to pre-specify k, visual dendrograms, works with arbitrary distance metrics.
- Disadvantages: O(n^2) memory/time for naive implementations, sensitive to noise and linkage choice (single/complete/average).

Clustering in data mining (practical notes)
- Use-case selection: choose clustering when labels unavailable and objective is pattern discovery.
- Preprocessing: scale/normalize features, handle categorical variables (one-hot or dedicated distance), remove or treat outliers.
- Algorithm choice: K-means for large numeric datasets; Gaussian Mixture Models for soft assignments; DBSCAN for arbitrary shapes and noise; hierarchical for nested structures.
- Choosing k: elbow method, silhouette score, gap statistic, domain knowledge.

Clustering for social media (short)
- Goals: detect communities, identify influencers, topic and sentiment groups, spam/bot detection.
- Graph algorithms: Louvain, Girvan-Newman, label propagation, spectral clustering on adjacency or Laplacian matrices.
- Feature engineering: text embeddings (TF-IDF, word2vec, BERT), interaction graphs, temporal activity features.

Recommended methodology (concise)
1. Define objectives and success criteria.
2. Collect and clean data; engineer features relevant to similarity.
3. Choose algorithm(s) based on scale and shape: K-means, DBSCAN, GMM, hierarchical, or graph methods.
4. Run with multiple initializations and parameter sweeps (e.g., k, eps, min_samples).
5. Evaluate using internal metrics: silhouette, Davies–Bouldin, Calinski–Harabasz. Use stability and domain validation where possible.
6. Visualize clusters (PCA/TSNE/UMAP for high-dim) and inspect representative samples per cluster.
7. Iterate and document choices.

Evaluation metrics (brief)
- Silhouette score: cohesion vs separation.
- Davies–Bouldin: lower is better (compactness vs separation).
- Calinski–Harabasz: higher indicates well-separated clusters.
- For graph/community detection: modularity, conductance.
- Use domain-specific validation (business metrics, labeled holdout if available).

Practical tips
- Standardize numeric features before K-means.
- Use robust clustering (DBSCAN) for noisy datasets with varying densities.
- For text/social data, prefer embeddings + cosine similarity or spectral methods on affinity matrices.
- For large data, use mini-batch K-means or approximate nearest neighbors for speed.

Conclusion
- Choose clustering algorithm based on data type, scale, noise characteristics, and the need for interpretability.
- Combine quantitative metrics with qualitative inspections to validate clusters.
- The linked articles provide practical examples and deeper explanations for each algorithm and use case.

Original report file (local)
- file:///Users/Yuvaan/IdeaProjects/Anncnn/Clustering_Report.md

