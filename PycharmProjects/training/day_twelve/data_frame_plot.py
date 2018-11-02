import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=['A', 'B', 'C', 'D'], index=np.arange(0, 100, 10))
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'], index=np.arange(0, 100, 10))
df.plot()

plt.show()

#cumsum
#0
#0+10 (0+0.5)
#0+10 (0+0.5+1)
