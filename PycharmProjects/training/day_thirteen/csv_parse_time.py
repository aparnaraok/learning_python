import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st_price = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
st_imp = st_price[['AAPL', 'MSFT']]
print(st_imp)

#st_imp[['AAPL', 'MSFT']].plot()
#plt.show()

st_imp.loc['16-02-2003' : '20-06-2003'].plot()
plt.show()
