
# coding: utf-8


import os 
import numpy as np 
import pandas as pd
import requests,json
import io
import rpy2.robjects as robjects
from flask import Flask, abort, jsonify, request
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
pandas2ri.activate()

path_py = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)

@app.route('/new/pricing/api', methods = ['POST'])

def make_predict_ill_pricing():
    #get the json file as an input
    data = request.get_json(force=True)
    input_data = pd.io.json.json_normalize(data,'input_data')
    # here write your rcode
    robjects.r.source("ILL_Price_Generation.R")
    r_output_df = robjects.r.run_ILL_pricing(input_data, path_py)

    py_output_df = pandas2ri.ri2py(r_output_df)
    output_dict = py_output_df.to_dict(orient='records')
    return jsonify(results=output_dict)

if __name__ =='__main__':
    app.run(host = '0.0.0.0', port = 2100, debug = True)
