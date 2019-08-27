import matplotlib.pyplot as plt
import numpy as np

#X = np.arange(n)
n = 12
X = np.arange(n)

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
#plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, +Y1, facecolor='pink', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    plt.ylim(-1.25, +1.25)

plt.show()

#ha-->horizontal axis