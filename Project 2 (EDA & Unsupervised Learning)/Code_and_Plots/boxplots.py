import seaborn as sns
from matplotlib import pyplot as Plot
sns.set(style="whitegrid")
iris = sns.load_dataset("iris")
sns.boxplot(x='species',y='sepal_length',data=iris)
Plot.show()

sns.boxplot(x='species',y='sepal_width',data=iris)
Plot.show()

ns.boxplot(x='species',y='petal_length',data=iris)
Plot.show()

sns.boxplot(x='species',y='petal_width',data=iris)
Plot.show()
