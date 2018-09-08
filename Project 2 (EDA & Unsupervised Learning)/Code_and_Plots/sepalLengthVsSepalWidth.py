from matplotlib import pyplot as Plot
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data # numpy.ndarray [Sepal Length, Sepal Width, Petal Length, Petal Width]
y = iris.target # numpy.ndarray [0->Setosa,1->Versicolour,2->Virginica]

x_min, x_max = X[:, 0].min() - .3, X[:, 0].max() + .3
y_min, y_max = X[:, 1].min() - .3, X[:, 1].max() + .3

Plot.figure(1, figsize=(8, 6))
Plot.clf()
color_map = Plot.cm.get_cmap('RdYlBu')
species = ['Setosa','Versicolor','Virginica']
formatter = Plot.FuncFormatter(lambda i, *args: species[i])

# Plot the training points
scatter_plot = Plot.scatter(X[:, 0], X[:, 1], c = y, cmap = color_map, edgecolor='k')
Plot.colorbar(ticks=[0,1,2], format=formatter)
Plot.xlabel('Sepal Length')
Plot.ylabel('Sepal Width')
Plot.xlim(x_min, x_max)
Plot.ylim(y_min, y_max)
#Plot.xticks(())
#Plot.yticks(())
Plot.tight_layout()
Plot.show()
