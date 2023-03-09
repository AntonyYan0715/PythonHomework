from pandas_datareader import data
import numpy as np
import pandas as pd

df = data.DataReader("MSFT", "yahoo", 2010, 2011)

df['Daily Return'] = df['Close'].pct_change()
df['Monthly Return'] = df['Close'].resample('M').last().pct_change()
df['MA70'] = df['Close'].rolling(70).mean()
df['MA150'] = df['Close'].rolling(150).mean()
df2 = df['Close'].resample('M').last().pct_change()

df['cond'] = np.where(df['MA70'] > df['MA150'], 1, 0)
df['diff'] = df['cond'].diff()
print(df[df['diff'] == 1])

df['Cash'] = 10000
df['Cash'] = df['Cash'] - (df['diff'] * df['Adj Close']).cumsum()

# print(df2)
# print((1 + df['Daily Return']).cumprod())
