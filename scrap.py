import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

aapl_df = yf.download('AAPL')


print(aapl_df)








