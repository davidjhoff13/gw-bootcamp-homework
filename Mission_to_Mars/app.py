# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:53:18 2020

@author: david
"""

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:5000/mars_app"
mongo = PyMongo(app)




@app.route("/")
def index():
    marsdata = list(mongo.db.marsdata.find())
    print(len(marsdata))
    return render_template("index.html", marsdata=marsdata)


@app.route("/scrape")
def scraper():
    marsdata = mongo.db.marsdata
    mars_data = scrape_mars.scrape_everything()
    
         
    marsdata.update({}, marsdata, upsert=True)
    
    print(len(mars_data))
            
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

