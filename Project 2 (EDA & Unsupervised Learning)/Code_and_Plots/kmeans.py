import numpy as np
import time
from sklearn import datasets
import matplotlib.pyplot as plt

fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()
iris = datasets.load_iris()
X = iris.data

def plot_progress(X, C, np_centroids):
    ax.clear()  # - Clear
    ax.scatter(X[:,0], X[:,1], c=C)
    fig.canvas.draw()
    time.sleep(1)

def kMeans(X, K, maxiters,plot_progress=None):
    J = []
    centroids = X[np.random.choice(np.arange(len(X)), K), :]

    for i in range(maxiters) :
        old_centroids = centroids
        # Cluster Assignment step
        C = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in X])
        J.append(sum([np.dot(X[x_i]-centroids[C[x_i]], X[x_i]-centroids[C[x_i]]) for x_i in range(X.shape[0])]) / X.shape[0])
        # Move centroids step
        centroids = [X[C == k].mean(axis = 0) for k in range(K)]
        if plot_progress != None:
            plot_progress(X, C, np.array(centroids))

        if (np.array(centroids) == np.array(old_centroids)).all() :
            break

    return np.array(centroids) , C, J

K_MEANS = kMeans(X,3,1000,plot_progress=plot_progress)
J = K_MEANS[2]
print(J)

## Computing Squared Error
for i in range(1,len(J) + 1):
    print("After",i,"iterations, the sum of squared error is",J[i-1])

## Check for Convergence
plt.plot(list(range(1,len(J)+1)),J)
plt.show()
