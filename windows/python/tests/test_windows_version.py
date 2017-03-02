from MulticoreTSNE import MulticoreTSNE as TSNE
from sklearn import datasets 

iris = datasets.load_iris()
tsne = TSNE(n_jobs=4)
Y = tsne.fit_transform(iris.data)

