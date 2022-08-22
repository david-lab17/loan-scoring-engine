# # -*- coding: utf-8 -*-
# """
# Created on Thur Jul 28 2021

# @author: DM Charo
# """

# from flask import Flask, request, render_template
# import pickle
# import numpy as np

# app = Flask(__name__, template_folder='template')

# filename = 'freezed_centroids1.pkl'
# model = pickle.load(open(filename, 'rb'))


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/submit", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         stock1 = request.form['Monetary_Value']
#         stock2 = request.form['Frequency']
#         stock3 = request.form['Recency']
#         result = np.array([[stock1, stock2, stock3]])
#         prediction = model.predict(result)
#         # prediction = model.predict(result)

#         if prediction == 0:
#             display = "You are in group 1"
#         elif prediction == 1:
#             display = "You are in group 2"
#         elif prediction == 2:
#             display = "You are in group 3"
        
#         else:
#             display = "You are in group 4"

#     return render_template("submit.html", n=display)


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, render_template
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
        prediction = model.predict(result)
        # prediction = model.predict(result)

        if prediction == 0:
            display = "Transaction belongs to Group 1"
        elif prediction == 1:
            display = "Transaction belongs to Group 2"
       
        else:
            display = "Transaction belongs to Group 3"

    return render_template("submit.html", n=display)


if __name__ == "__main__":
    app.run(debug=True)
