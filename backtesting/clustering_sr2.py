import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import Counter


ticker = 'AAPL'
df = pd.read_csv(r"C:\Users\yu guang\Desktop\backtesting\ticker_files" + r"\\" + ticker + ".csv")

df['Colour'] = np.where(df['Open'] > df['Close'], 'Green', 'Red')

prev_close = float(df['Close'].iloc[-1])

#resistance
r_high = df['High'].round(decimals=0).tolist()
df1 = df[df['Colour'] == 'Green']
r_close = df1['Close'].round(decimals=0).tolist()
r = r_high + r_close

dict_r = dict(Counter(r))
list_r = []

for key in dict_r:
    if dict_r[key] > 1:
        list_r.append(key)

list_r1 = []
for resistance in list_r:
    if resistance > prev_close:
        list_r1.append(resistance)
# print(list_r1)

#support turned resistance
s_low = df['Low'].round(decimals=1).tolist()
df2 = df[df['Colour'] == 'Red']
s_close = df2['Close'].round(decimals=1).tolist()
s = s_low + s_close

dict_s = dict(Counter(s))
list_s = []

for key in dict_s:
    if dict_s[key] > 1:
        list_s.append(key)

list_s1 = []
for support in list_s:
    if support > prev_close:
        list_s1.append(support)
# print(list_s1)
#plotting
fig = go.Figure(data=[go.Candlestick(
                        x=df['Date'],
                        open=df['Open'],
                        close=df['Close'],
                        high=df['High'],
                        low=df['Low']
)])

fig.update_layout(xaxis_rangeslider_visible=False)

# for resistance in list_r1:
#     fig.add_hline(resistance, line_color="black")
#
# for support in list_s1:
#     fig.add_hline(support, line_color="black")

list_total = list_r1 + list_s1
uniq_list = []

print(list_total)

for item in list_total:
    if item not in uniq_list:
        uniq_list.append(item)
print(uniq_list)

for resistance in uniq_list:
    fig.add_hline(resistance, line_color="black")

fig.show()
