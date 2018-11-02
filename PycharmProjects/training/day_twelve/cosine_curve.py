#Run file in console

import numpy as np
import matplotlib.pyplot as plt


t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',  xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16,  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))