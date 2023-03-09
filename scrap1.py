import pandas as pd

import yfinance as yf

from datetime import datetime



amzn = yf.Ticker('amzn')

amzn_df = yf.download('AMZN')
print(amzn_df)


