# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:23:13 2020

@author: david
"""

import numpy as np

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

from flask import Flask, jsonify
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#%%

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#%%
#################################################
# Flask Routes
#################################################
#%%
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"api/v1.0/precipitation<br/>"
        f"/app/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"api/v1.0/<start><br/>"
        f"api/v1.0/<startend><br/>"
            )

#%%

def precipitation():
    precipresults=pd.read.sql('SELECT * FROM measurement', engine)

    precipresults_json = precipresults[['date', 'pcrp']].to_json(orient='records')
    
    return precipresults_json

#%%
    
def stations():
    stationresults=pd.read.sql('SELECT * FROM station', engine)
    
    stationresults_json = stationresults[['station']].to_json(orient='records')

    return stationresults_json
#%%
def tobs():
    tobsresults=pd.read.sql("SELECT prcp, date FROM measurement\
                              WHERE date BETWEEN '2016-08-24' and '2017-08-23'", engine)
    
    tobsresults_json = tobsresults[['tobs']].to_json(orient='records')
    
    return tobsresults_json
#%%
def startend():
    maxmin1=pd.read.sql("SELECT MIN(tobs) AS 'minimum temp', \
                        MAX(tobs) AS 'maximum temp', AVG(tobs) AS 'average temp' \
                        FROM measurement WHERE \
                        date BETWEEN '2016-09-13' and '2016-10-13'"), engine
    maxmin1_json = maxmin1[['minimum temp'], 'maximum temp', 'average temp'].to_json(orient='records')
    
    return maxmin1_json

    

    

    




