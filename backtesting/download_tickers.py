import pandas_datareader.data as web
import datetime as dt

ticker = 'NIO'

# end = dt.datetime(2021, 5, 15)
# start = dt.datetime(2018, 1, 1)
end = dt.datetime.today()
start = dt.datetime.today() - dt.timedelta(days=365) #average trading days = 253 a year
df = web.DataReader(ticker, 'yahoo', start, end)
df.to_csv(r'C:\Users\yu guang\Desktop\backtesting\ticker_files' + r"\\" + ticker + '.csv')

print(df)