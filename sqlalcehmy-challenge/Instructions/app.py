
"""
Created on Sat Jun  6 17:23:13 2020

@author: david
"""


from sqlalchemy import create_engine
import pandas as pd

from flask import Flask
#################################################




#%%

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

conn=engine.connect()


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
        f"api/v1.0/stations<br/>"
        f"api/v1.0/tobs<br/>"
        f"api/v1.0/start<br/>"
        f"api/v1.0/vacation<br/>"
        f"api/v1.0/startend<br/>"
            )

#%%
@app.route("/api/v1.0/precipitation")

def precipitation():
    precipresults=pd.read_sql('SELECT * FROM measurement', engine)

    precipresults_json = precipresults[['date', 'prcp']].to_json(orient='records')
    
    return precipresults_json

#%%
@app.route('/api/v1.0/stations')
    
def stations():
    stationresults=pd.read_sql('SELECT * FROM station', engine)
    
    stationresults_json = stationresults[['station']].to_json(orient='records')

    return stationresults_json
#%%
@app.route('/api/v1.0/tobs')
def tobs():
    tobsresults=pd.read_sql("SELECT tobs, date FROM measurement\
                              WHERE date BETWEEN '2016-08-24' and '2017-08-23'", engine)
    
    tobsresults_json = tobsresults[['tobs']].to_json(orient='records')
    
    return tobsresults_json
#%%
    
@app.route('/api/v1.0/start')

def start():
    maxmin1=pd.read_sql("SELECT MIN(tobs) AS 'minimum temp', \
                        MAX(tobs) AS 'maximum temp', AVG(tobs) AS 'average temp' \
                        FROM measurement WHERE \
                        date BETWEEN '2016-09-13' and '2016-10-13'", engine)
    
    maxmin1_json = maxmin1[['minimum temp', 'maximum temp', 'average temp']].to_json(orient='records')
    
    return maxmin1_json

#%%
    
@app.route('/api/v1.0/vacation')

def vacation():
    maxmin2= pd.read_sql("SELECT date, MIN(tobs) AS 'minimum temp', MAX(tobs) AS 'maximum temp', AVG(tobs) AS 'average temp' \
                        FROM measurement WHERE date BETWEEN '2016-09-13' and '2017-08-23' GROUP BY date", engine) 
    maxmin2_json = maxmin2[['date', 'minimum temp', 'maximum temp', 'average temp']].to_json(orient='records')
    return maxmin2_json
    
#%%
    
@app.route('/api/v1.0/startend') 
    
def started():
    maxmin3=pd.read_sql("SELECT date, MIN(tobs) AS 'minimum temp', MAX(tobs) AS 'maximum temp', AVG(tobs) AS 'average temp' \
                        FROM measurement WHERE date BETWEEN '2016-09-13' and '2016-10-13' GROUP BY date", engine)
                        
    maxmin3_json = maxmin3[['date', 'minimum temp', 'maximum temp', 'average temp']].to_json(orient='records')
    
    return maxmin3_json

#%%
    
if __name__== '__main__':
    app.run(debug=True)

    

    




