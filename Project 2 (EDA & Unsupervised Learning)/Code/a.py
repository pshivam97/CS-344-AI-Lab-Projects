from matplotlib import pyplot as Plot
from sklearn import datasets
import seaborn as sns
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
sns.pairplot(iris)
Plot.show()
