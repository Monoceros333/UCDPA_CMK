import pandas as pd
import numpy as np

equity = pd.read_csv(r'C:\users\kearnecl\Desktop\data for github (2)\equity_data.csv')
print(equity)

equity1 = equity[['date','indu','sp500','ccmp','ftse100','iseq_as','sxxp','sxxe','aapl','amzn','intc','msft','pfe']]
print(equity1)

missing_values_count = equity1.isnull().sum()
print(missing_values_count[0:13])

cleaned_equity2 =equity1.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_equity2)


droprows=cleaned_equity2.dropna()

print(cleaned_equity2.shape,droprows.shape)


