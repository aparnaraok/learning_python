import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()

plt.savefig('plot.png')
plt.show()