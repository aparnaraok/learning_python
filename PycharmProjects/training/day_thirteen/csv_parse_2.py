import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

min_index = pd.read_csv("NIFTY-I.csv", header=None)
min_index.columns = ['date', 'time', 'open', 'high', 'low', 'close', 'volume', 'OI']
min_index['period'] = min_index['date'].map(str) + \
    min_index['time']
min_index = min_index.drop(axis = 1, columns=['date', 'time'])
min_index['period'] = pd.to_datetime(min_index['period'], format="%Y%m%d%H:%M")
min_index = min_index.set_index('period')
print(min_index.head())
min_index.plot()
plt.show()


#                         open     high    ...     volume        OI
# period                                   ...
# 2017-01-02 09:15:00  8215.05  8215.05    ...     143627  17107050
# 2017-01-02 09:16:00  8198.20  8201.00    ...      84075  17148525
# 2017-01-02 09:17:00  8197.55  8197.90    ...      70200  17148525
# 2017-01-02 09:18:00  8182.95  8190.95    ...      71700  17148525
# 2017-01-02 09:19:00  8190.95  8191.85    ...      54600  17201625
#
# [5 rows x 6 columns]
