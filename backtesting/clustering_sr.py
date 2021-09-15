import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from kneed import KneeLocator
import plotly.graph_objects as go

ticker = 'TSLA'
df = pd.read_csv(r"C:\Users\yu guang\Desktop\backtesting\ticker_files" + r"\\" + ticker + ".csv")

df['Colour'] = np.where(df['Open'] > df['Close'], 'Green', 'Red')

# print(df)

X1 = np.array(df['High'])
df1 = df[df['Colour'] == 'Green']
X2 = np.array(df1['Close'])
X = np.concatenate((X1, X2))

# print(len(X))
# print(X)

sum_of_squared_distances = []
K = range(1,30)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X.reshape(-1,1))
    sum_of_squared_distances.append(km.inertia_)
kn = KneeLocator(K, sum_of_squared_distances, S=1.0, curve="convex", direction="decreasing")

# print(kn.knee)

kmeans = KMeans(n_clusters= kn.knee).fit(X.reshape(-1,1))
c = kmeans.predict(X.reshape(-1,1))
cent_resistances = np.array(kmeans.cluster_centers_)

resistances = []

for i in range(kn.knee):
    resistances.append(-np.inf)

for i in range(len(X)):
    cluster = c[i]
    if X[i] > resistances[cluster]:
        resistances[cluster] = X[i]
# print(resistances)

###############################

X1 = np.array(df['Low'])
df1 = df[df['Colour'] == 'Red']
X2 = np.array(df1['Close'])
X = np.concatenate((X1, X2))

sum_of_squared_distances = []
K = range(1,30)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X.reshape(-1,1))
    sum_of_squared_distances.append(km.inertia_)
kn = KneeLocator(K, sum_of_squared_distances, S=1.0, curve="convex", direction="decreasing")

# print(kn.knee)

kmeans = KMeans(n_clusters= kn.knee).fit(X.reshape(-1,1))
c = kmeans.predict(X.reshape(-1,1))
cent_supports = np.array(kmeans.cluster_centers_)

supports = []

for i in range(kn.knee):
    supports.append(np.inf)

for i in range(len(X)):
    cluster = c[i]
    if X[i] < supports[cluster]:
        supports[cluster] = X[i]
# print(supports)


#plotting
fig = go.Figure(data=[go.Candlestick(
                        x=df['Date'],
                        open=df['Open'],
                        close=df['Close'],
                        high=df['High'],
                        low=df['Low']
)])
fig.update_layout(xaxis_rangeslider_visible=False)

for resistance in resistances:
    fig.add_hline(resistance, line_color="red")
for cent_resistance in cent_resistances:
    fig.add_hline(cent_resistance[0], line_dash="dash", line_color="red")
for support in supports:
    fig.add_hline(support, line_color="green")
for cent_support in cent_supports:
    fig.add_hline(cent_support[0], line_dash="dash", line_color="green")

fig.show()
