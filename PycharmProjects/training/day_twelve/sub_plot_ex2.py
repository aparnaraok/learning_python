import matplotlib.pyplot as plt
import numpy as np
fix, axes = plt.subplots(2,2,sharex=False, sharey=False)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='b', alpha=0.5 )
plt.subplots_adjust(wspace=0, hspace=0) #Everything inside a plus
#even if y is false...oly 2 cols show up y ticks

plt.show()

#sharex = True---->x axis ticks shown only for bottom 2 graphs
#sharex = False---->x axis ticks shown for all graphs