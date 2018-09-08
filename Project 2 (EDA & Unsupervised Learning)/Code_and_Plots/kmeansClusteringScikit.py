import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets
from matplotlib import pyplot as Plot
import time
import random

random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target

no_of_clusters = 3

start_time = time.time()
k_means = KMeans(n_clusters=no_of_clusters,max_iter=100,random_state=0).fit(X)
end_time = time.time()

kmeans_centroids = k_means.cluster_centers_
kmeans_labels = k_means.labels_

# PLOTTING THE KMEANS 3D PLOT

Plot.figure(1, figsize=(14,12))
Plot.clf()
color_map = Plot.cm.get_cmap('RdYlBu')
species = ['Setosa','Versicolor','Virginica']
formatter = Plot.FuncFormatter(lambda i, *args: species[i])

fig1 = Plot.figure(1, figsize=(14, 12))
ax = Axes3D(fig1, elev=-165, azim=5)
ax.scatter(X[:, 1], X[:, 2], X[:, 3], c=kmeans_labels, cmap=color_map, edgecolor='k', s=40)
ax.set_title("K-Means Clustering")
ax.set_xlabel("Sepal Width")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Petal Length")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Petal Width")
ax.w_zaxis.set_ticklabels([])
Plot.show()

## Calculating the 3 Centroids of the original Iris Dataset

iris_centroid = [[np.zeros(4),0],[np.zeros(4),0],[np.zeros(4),0]]

for i in range(len(y)) :
    iris_centroid[y[i]][0] = iris_centroid[y[i]][0] + np.array(X[i])
    iris_centroid[y[i]][1] += 1

original_centroids = [(i[0]/i[1]) for i in iris_centroid]

kmeans_to_original = {0:None, 1:None, 2:None}

for i in range(len(kmeans_centroids)) :
    minimum = [None,10000000]
    for j in range(len(original_centroids)) :
        temp = np.linalg.norm(kmeans_centroids[i]-np.array(original_centroids[j]))
        if temp < minimum[1] :
            minimum[1] = temp
            minimum[0] = j
    kmeans_to_original[i] = minimum[0]

error_kmeans = 0
for i in range(len(kmeans_labels)) :
    if y[i] != kmeans_to_original[kmeans_labels[i]] :
        error_kmeans += 1
error_kmeans = error_kmeans*100/len(y)

print("Time to execute K-Means Clustering Algorithm :",end_time - start_time)
print("Error in Marking Correct via K-Means Clustering is",error_kmeans,"%")
