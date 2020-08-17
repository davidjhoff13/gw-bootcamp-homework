# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 01:46:16 2020

@author: david
"""
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#establish engine

engine = create_engine("sqlite:///db/coronavirus.sqlite") #will update as necessary

@app.route("/")

def home():
    return render_template(index.html)

@app.route('cases_plot')
def cases_plot_data():
    conn = engine.connect()
    query = '''
       # [include sql query to pull date and new national cases]

        '''
    case_results_df = pd.read_sql(query, con=conn)
    case_results_json = results_df.to_json(orient='records')

    conn.close()
    return case_results


if __name__ == '__main__':
    app.run(debug=True)