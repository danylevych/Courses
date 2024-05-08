import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate random number of true centers and features
num_centers = random.randint(1, 30)
num_features = random.randint(2, 10)

# Generate synthetic data
X, _ = make_blobs(n_samples=2000, centers=num_centers, n_features=num_features, random_state=2)

# Calculate inertia for different values of k
inertia = []
for k in range(1, 31):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(range(1, 31), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()