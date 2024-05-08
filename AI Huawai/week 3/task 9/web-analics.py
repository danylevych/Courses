import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate synthetic data
X, y = make_blobs(n_samples=2000, centers=2, n_features=2, random_state=30)

# Initialize KMeans with the desired number of clusters
kmeans = KMeans(n_clusters=5)

# Fit KMeans to the data
kmeans.fit(X)

# Get the cluster centroids and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualize the data and cluster centroids
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(X[:, 0], X[:, 1], alpha=0.5)
ax2.scatter(X[:, 0], X[:, 1], c=labels, alpha=0.5)

plt.show()
