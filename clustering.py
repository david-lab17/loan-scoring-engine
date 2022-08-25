# Import modules and packages
import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import KMeans
# Read data
data = pd.read_excel('Customer-profile-data.xlsx')
X = np.array(data)

# System constants
number_of_clusters = 4


k_means = KMeans(n_clusters=4,random_state=0,init='k-means++')
k_means.fit(X)
y_kmeans = k_means.fit_predict(X)
labels = k_means.labels_

data['cluster']=y_kmeans
data['cluster'].dtypes
data['cluster']=data['cluster'].astype(object)
print(data['cluster'].unique())

freeze_centroids1 = k_means.cluster_centers_
filename = 'freezed_centroids1.pkl'
pickle.dump(k_means, open(filename, 'wb'))