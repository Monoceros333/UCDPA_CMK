import pandas as pd
import numpy as np

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