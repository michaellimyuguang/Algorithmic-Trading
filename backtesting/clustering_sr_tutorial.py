import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt

ticker = 'TSLA'
df = pd.read_csv(r"C:\Users\yu guang\Desktop\backtesting\ticker_files" + r"\\" + ticker + ".csv")

df['Colour'] = np.where(df['Open'] > df['Close'], 'Green', 'Red')

# print(df)

X = np.array(df['Close'])
sum_of_squared_distances = []
K = range(1,30)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X.reshape(-1,1))
    sum_of_squared_distances.append(km.inertia_)
kn = KneeLocator(K, sum_of_squared_distances, S=1.0, curve="convex", direction="decreasing")
# kn.plot_knee()
# plt.show()

kmeans = KMeans(n_clusters= kn.knee).fit(X.reshape(-1,1))
c = kmeans.predict(X.reshape(-1,1))
minmax = []
for i in range(kn.knee):
    minmax.append([-np.inf,np.inf])
print(c)
print(minmax)
for i in range(len(X)):
    cluster = c[i]
    if X[i] > minmax[cluster][0]:
        minmax[cluster][0] = X[i] #find the resistance
    if X[i] < minmax[cluster][1]:
        minmax[cluster][1] = X[i] #find the support
print(minmax)

for i in range(len(X)):
    colors = ['b','g','r','c','m','y','k','w']
    c = kmeans.predict(X[i].reshape(-1,1))[0]
    color = colors[c]
    plt.scatter(i,X[i],c = color,s = 1)
for i in range(len(minmax)):
    plt.hlines(minmax[i][0],xmin = 0,xmax = len(X),colors = 'g') #resistance
    plt.hlines(minmax[i][1],xmin = 0,xmax = len(X),colors = 'r') #support

plt.show()
