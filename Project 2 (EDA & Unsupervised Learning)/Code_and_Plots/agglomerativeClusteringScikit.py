import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
from matplotlib import pyplot as Plot
import time

np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target

no_of_clusters = 3

start_time = time.time()
agglomerative_clustering = AgglomerativeClustering(n_clusters=no_of_clusters, linkage='average').fit(X)
end_time = time.time()

final_labels = agglomerative_clustering.labels_

# PLOTTING THE KMEANS 3D PLOT

Plot.figure(1, figsize=(14, 12))
Plot.clf()
color_map = Plot.cm.get_cmap('RdYlBu')
species = ['Setosa','Versicolor','Virginica']
formatter = Plot.FuncFormatter(lambda i, *args: species[i])

fig2 = Plot.figure(1, figsize=(14, 12))
ax = Axes3D(fig2, elev=-165, azim=5)
ax.scatter(X[:, 1], X[:, 2], X[:, 3], c=final_labels, cmap=color_map, edgecolor='k', s=40)
ax.set_title("Agglomerative Clustering")
ax.set_xlabel("Sepal Width")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Petal Length")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Petal Width")
ax.w_zaxis.set_ticklabels([])
Plot.show()

ag_centroid = [[np.zeros(4),0],[np.zeros(4),0],[np.zeros(4),0]]

for i in range(len(final_labels)) :
    ag_centroid[final_labels[i]][0] = ag_centroid[final_labels[i]][0] + np.array(X[i])
    ag_centroid[final_labels[i]][1] += 1

iris_centroid = [[np.zeros(4),0],[np.zeros(4),0],[np.zeros(4),0]]

for i in range(len(y)) :
    iris_centroid[y[i]][0] = iris_centroid[y[i]][0] + np.array(X[i])
    iris_centroid[y[i]][1] += 1

original_centroids = [(i[0]/i[1]) for i in iris_centroid]
agglomerative_centroids = [(i[0]/i[1]) for i in ag_centroid]
ag_to_original = {0:None, 1:None, 2:None}

for i in range(len(agglomerative_centroids)) :
    minimum = [None,10000000]
    for j in range(len(original_centroids)) :
        temp = np.linalg.norm(agglomerative_centroids[i]-np.array(original_centroids[j]))
        if temp < minimum[1] :
            minimum[1] = temp
            minimum[0] = j
    ag_to_original[i] = minimum[0]

error_agg = 0
for i in range(len(final_labels)) :
    if y[i] != ag_to_original[final_labels[i]] :
        error_agg += 1
error_agg = error_agg*100/len(y)

print("Time to execute Agglomerative Clustering Algorithm :",end_time - start_time)
print("Error in Marking Correct via Agglomerative Clustering is",error_agg,"%")
