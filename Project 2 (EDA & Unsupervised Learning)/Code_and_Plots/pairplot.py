import seaborn as sns
from matplotlib import pyplot as Plot
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species", size=4,markers=["o", "x", "+"])
Plot.show()
