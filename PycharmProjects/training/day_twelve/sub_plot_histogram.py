import matplotlib.pyplot as plt
import numpy as np

#creates a 2by3 matrix with (1,3,5) as values.
#k - black
#b - blue

#bins means no of histograms...

fig = plt.figure(figsize=(8, 6))
fig.add_subplot(231).hist(np.random.randn(100), bins=5, color='k', alpha=0.3)
fig.add_subplot(233).scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
#x and y must be of same size...(30)
fig.add_subplot(235).plot(np.arange(10))#325 s transpose of 235
fig.add_subplot(236).plot(np.sin(np.linspace(-np.pi, np.pi, 256)))#325 s transpose of 235



plt.show()

