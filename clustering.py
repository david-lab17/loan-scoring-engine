# Import modules and packages
import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import KMeans
# Read data
data = pd.read_excel('customer-profile.xlsx')
X = np.array(data)

# System constants
number_of_clusters = 3

# Apply KMEans to the Data
kmeans = KMeans(
	n_clusters=number_of_clusters,
	random_state=1
	)

kfit = kmeans.fit(X)

import pickle
filename ='freezed_centroids.pkl'
pickle.dump(kfit,open(filename,'wb'))

# freeze_centroids = kmeans.cluster_centers_
# print(freeze_centroids)
# print(freeze_centroids.shape)

# # Save centroids as pickle file locally
# with open('freezed_centroids.pkl','wb') as f:
#     pickle.dump(freeze_centroids, f)
#     print('Centroids are being saved to pickle file.')