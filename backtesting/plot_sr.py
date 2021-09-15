import plotly.graph_objects as go
import pandas as pd

ticker = 'TSLA'
df = pd.read_csv(r"C:\Users\yu guang\Desktop\backtesting\ticker_files" + r"\\" + ticker + ".csv")

# print(df.head())

fig = go.Figure(data=[go.Candlestick(
                        x=df['Date'],
                        open=df['Open'],
                        close=df['Close'],
                        high=df['High'],
                        low=df['Low']
)])



fig.update_layout(xaxis_rangeslider_visible=False)
levels = [600, 700]
for level in levels:
    fig.add_hline(level)

#export candlestick to offline plot
fig.show()

#https://stackoverflow.com/questions/64949228/plot-horizontal-lines-in-plotly