# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:49:52 2023

@author: 91630
"""

# !/usr/bin/env python

from flask import Flask, render_template, request
import joblib
import numpy as np

lat = 0
long = 0

account_sid = "AC5ad097d9aade62fcf2d5dcd986ad6803"
auth_token = "daecc70954a586df641c454ba7a82778"

model = joblib.load('mlp.sav')

app = Flask(__name__)


def calculate(form):
    global lat
    global long
    lat = form['lat']
    long = form['lon']
    age_of_driver = form['age']
    vehicle_type = form['vehicle_type']
    age_of_vehicle = form['vehicle_age']
    engine_cc = form['v_capacity']
    day = form['day']
    weather = form['weather_condition']
    light = form['light_condition']
    road_condition = form['road_condition']
    gender = form['gender']
    speed_limit = form['speed_limit']
    arr = np.array([[age_of_driver, vehicle_type, engine_cc, day, weather, road_condition, age_of_vehicle, light,
                     gender, speed_limit]])
    pred = model.predict(arr)
    print(pred[0])
    return render_template("result.html", prediction=pred)


@app.route('/', methods=['GET'])
def homepage():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    road_conditions = ['Dry', 'Wet or Damp', 'Snow', 'Frost or ice', 'Flood over 3cm. deep', 'Oil or diesel', 'Mud']
    weather_conditions = ['Fine no high winds', 'Raining no high winds', 'Snowing no high winds', 'Fine + high '
                                                                                                  'winds',
                          'Raining + high winds', 'Snowing + high winds', 'Fog or mist', 'Other']
    return render_template("index.html", road_conditions=road_conditions, days=days,
                           weather_conditions=weather_conditions)


@app.route('/', methods=['POST'])
def result():
    return calculate(request.form)


@app.route('/statistics', methods=['GET'])
def statistics():
    return render_template("statistics.html")


if __name__ == '__main__':
    app.run()