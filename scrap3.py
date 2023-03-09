import pandas as pd
import yfinance as yf
from datetime import datetime


security = yf.Ticker("")

securities = ['amzn', 'aapl', 'intc', 'msft','pfe']

#for a few securities declare an empty df
df = pd.DataFrame

for security in securities:
 df[security] = yf.Ticker(security).history(start="1999-12-31",end="2022-12-31")

 print((df))