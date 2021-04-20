import os
from sklearn import datasets
from joblib import load
import numpy as np
import json
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file
from sklearn import preprocessing

model = load('model.pkl')
UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    import csv
    file = open(filename)
    for row in csv.reader(file):
        stuff = row
        
    data = np.array([stuff])
    data.reshape(-1, 1)

    enc = preprocessing.OrdinalEncoder()
    enc.fit(data)
    data_new = enc.transform(data)
    data_new.shape

    my_prediction = model.predict(data_new)
    my_prediction = int(my_prediction[0])
    if my_prediction == 0:
        reservation = "Your reservation was not canceled"
    else:
        reservation = "Your reservation was canceled"
    return jsonify(reservation)

def arg(hotel, leadtime, weekend, week):
    #hotel: 1-resort hotel, 0-City hotel

    data = np.array([[hotel, leadtime, weekend, week, 2.000e+00, 0.000e+00, 0.000e+00,
 0.000e+00, 1.340e+02, 6.000e+00, 3.000e+00, 0.000e+00, 0.000e+00, 0.000e+00,
 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 1.730e+02, 0.000e+00, 2.000e+00,
 2.488e+03, 0.000e+00, 1.000e+00, 0.000e+00, 7.000e+01, 0.000e+00]])
    data.reshape(-1,1)

    enc = preprocessing.OrdinalEncoder()
    enc.fit(data)
    data_new = enc.transform(data)
    data_new.shape

    my_prediction = model.predict(data_new)
    my_prediction = int(my_prediction[0])
    if my_prediction == 0:
        reservation = "Your reservation was not canceled"
    else:
        reservation = "Your reservation was canceled"
    return jsonify(reservation)
