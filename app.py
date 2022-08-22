# -*- coding: utf-8 -*-
"""
Created on Thur Jul 28 2022

@author: DM Charo
"""



from flask import Flask, request, render_template
from sklearn.cluster import KMeans
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

filename = 'freezed_centroids.pkl'
model = pickle.load(open(filename, 'rb'))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        transaction1 = request.form['Monetary_Value']
        transaction2 = request.form['Frequency']
        transaction3 = request.form['Recency']
        result = np.array([[transaction1, transaction2, transaction3]])
        # kmeans=KMeans(n_clusters=3, random_state=0, init='k-means++')
        # kmeans.fit(result)
        # prediction = kmeans.predict(result)
        # prediction = KMeans(n_clusters=3, random_state=0, init='k-means++').fit_predict(result)
        prediction = model.predict(result)
        print(prediction)

        if prediction == 0:
            display = "Transaction belongs to Group 1"
        elif prediction == 1:
            display = "Transaction belongs to Group 2"
       
        else:
            display = "Transaction belongs to Group 3"

    return render_template("submit.html", n=display)


if __name__ == "__main__":
    app.run(debug=True)
