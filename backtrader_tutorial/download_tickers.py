import pandas_datareader.data as web
import datetime as dt

end = dt.datetime(2021, 5, 11)
start = dt.datetime(2021, 1, 1)
df = web.DataReader('AAPL', 'yahoo', start, end)
df.to_csv(r'C:\Users\yu guang\Desktop\backtrader_tutorial\ticker_files\AAPL.csv')

# print(df)