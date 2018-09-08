from matplotlib import pyplot as Plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
X = iris.data[:, :]  # we only take the first two features.
y = iris.target

Plot.figure(1, figsize=(18, 16))
Plot.clf()
color_map = Plot.cm.get_cmap('RdYlBu')
species = ['Setosa','Versicolor','Virginica']
formatter = Plot.FuncFormatter(lambda i, *args: species[i])

fig = Plot.figure(1, figsize=(18, 16))
ax = Axes3D(fig, elev=-165, azim=5)
ax.scatter(X[:, 1], X[:, 2], X[:, 3], c=y,cmap=color_map, edgecolor='k', s=40)
ax.set_title("3D Model : Iris Dataset")
ax.set_xlabel("Sepal Width")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Petal Length")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Petal Width")
ax.w_zaxis.set_ticklabels([])
Plot.show()
