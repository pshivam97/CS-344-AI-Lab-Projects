import matplotlib.pyplot as Plot
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
Plot.hist(X[:,0],bins=15) # Sepal Length Histogram
Plot.show()

Plot.hist(X[:,1],bins=15) # Sepal Width Histogram
Plot.show()

Plot.hist(X[:,2],bins=15) # Petal Length Histogram
Plot.show()

Plot.hist(X[:,3],bins=15) # Petal Width Histogram
Plot.show()
