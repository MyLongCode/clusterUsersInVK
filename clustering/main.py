import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

cust_df = pd.read_csv('users2.csv')
cust_df.head()

df = cust_df.drop("Имя Фамилия", axis=1)
df = df.drop("Статус", axis=1)
df = df.drop("Пол", axis=1)
df = df.drop("Кол-во подарков", axis=1)
df = df.drop("Дата Рождения", axis=1)

X = df.values[:,1:]
X = np.nan_to_num(X)

clusterNum = 3
k_means = KMeans(init="k-means++", n_clusters=clusterNum, n_init=12)
k_means.fit(X)
labels = k_means.labels_

df['cluster_km'] = labels
df.head(5)
df.groupby('cluster_km').mean()

area = np.pi * (X[:,1])/100
plt.scatter(X[:,0], X[:,1], s=area, c=labels.astype(np.int64), alpha=0.5)
plt.xlabel('Friends', fontsize=18)
plt.ylabel('City', fontsize=18)
print(df)
plt.show()