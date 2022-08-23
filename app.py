# # -*- coding: utf-8 -*-
# """
# Created on Thur Jul 28 2022

# @author: DM Charo
# """



# from flask import Flask, request, render_template
# from sklearn.cluster import KMeans
# import pickle
# import numpy as np

# app = Flask(__name__, template_folder='template')

# filename = 'freezed_centroids.pkl'
# loaded_model = pickle.load(open(filename, 'rb'))


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/submit", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         transaction1 = request.form['Monetary_Value']
#         transaction2 = request.form['Frequency']
#         transaction3 = request.form['Recency']
#         result = np.array([[transaction1, transaction2, transaction3]]).reshape(1,3)
#         prediction = loaded_model.predict(result)
#         print(prediction)
#         if prediction == 0:
#             display = "Transaction belongs to Group 1"
#         elif prediction == 1:
#             display = "Transaction belongs to Group 2"
       
#         else:
#             display = "Transaction belongs to Group 3"

#     return render_template("submit.html", n=display)


# if __name__ == "__main__":
#     app.run(debug=True)


import os
import numpy as np
import flask
import pickle
from flask import Flask, redirect, url_for, request, render_template


# creating instance of the class
app = Flask(__name__, template_folder='templates')

# to tell flask what url should trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    
    
# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,3)
    loaded_model = pickle.load(open('freezed_centroids.pkl',"rb")) # load the model
    result = loaded_model.predict(to_predict) # predict the values using loded model
    return result[0]


@app.route('/submit', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.values()
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        print(result)
            
        if float(result) == 0:
            prediction='Transaction belongs to Group 1'
        elif float(result) == 1:
            prediction='Transaction belongs to Group 2'
        elif float(result) == 2:
            prediction='Transaction belongs to Group 3'
            
        return render_template("submit.html", n=prediction)

if __name__ == "__main__":
    app.run(debug=False) #
