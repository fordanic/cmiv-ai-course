from sklearn.datasets import load_digits
from sklearn.cluster import KMeans

# load data
digits = load_digits()

# perform clustering
kmeans = KMeans(n_clusters=10)
clusters = kmeans.fit_predict(digits.data)

# visualize the cluster centers
fig = plt.figure(figsize=(8, 3))
for i in range(10):
    ax = fig.add_subplot(2, 5, 1 + i)
    ax.imshow(kmeans.cluster_centers_[i].reshape((8, 8)),
              cmap=plt.cm.binary)
