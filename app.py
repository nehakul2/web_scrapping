#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:39:05 2018

@author: nkulkar
"""

from flask import Flask, render_template, jsonify, redirect
import pymongo
from pymongo import MongoClient
import mission_to_mars

app = Flask(__name__)

#mongo = PyMongo(app)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# Define database and collection
# Note: Database names CANNOT be with underscores. "nasa_news" <-- DID not work earlier.
db = client.nasaNews
collection = db.missionToMars

@app.route('/')
def index():
    mission = mongo.db.missionToMars.find_one()
    print(mission)
    return render_template('index.html', mission=mission)



@app.route('/scrape')
def scrape():
    mission = mongo.db.missionToMars
    data = mission_mars.scrape()
    #print("this is data in scrape", data)
    mission.update({}, data, upsert=True)
    return redirect("http://localhost:5010/", code=302)


if __name__ == "__main__":
    app.run(debug=True , port=5010)
    
