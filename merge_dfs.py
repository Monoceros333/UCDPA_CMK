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

other_data =pd.read_csv(r'C:\Users\kearnecl\Desktop\data for github (2)\other_data.csv')
print(other_data)
other_data1 = other_data[['date','LUATTRUU','BCEK1T', 'ecb_refi','FEDL01','ukbrbase','brent_oil','gold']]
print(other_data1)

missing_values_count = other_data1.isnull().sum()
print(missing_values_count)

cleaned_odata2 =other_data1.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_odata2)
droprows=cleaned_odata2.dropna()
print(cleaned_odata2.shape,droprows.shape)

equity =cleaned_equity2
other = cleaned_odata2

df1 = equity
df2 = other

df3=df1.join(df2,lsuffix='_left', rsuffix='_right', how='outer')
print(df3)








