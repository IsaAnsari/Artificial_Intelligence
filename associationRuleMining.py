from sklearn.datasets import make_blobs

X, Y = make_blobs(n_samples=500, centers=2,random_state=0, cluster_std=0.40)

import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring');
plt.show()

import numpy as np

xfit = np.linspace(-1, 3.5)
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring')

for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none', color='#AAAAAA', alpha=0.4)
    
plt.xlim(-1, 3.5);
plt.show()
print(X,Y)
