
# coding: utf-8

# In[1]:


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


# In[ ]:


path_py = os.path.dirname(os.path.abspath(__file__))


# In[3]:


# utils = importr('utils')
# utils.install_packages('dplyr')
# utils.install_packages('plyr')
# utils.install_packages('readxl')
# utils.install_packages('geosphere')
# utils.install_packages('gdata')
# utils.install_packages('lubridate')
# utils.install_packages('data.table')
# utils.install_packages('sqldf')
# utils.install_packages('RecordLinkage')
# utils.install_packages('stringr')
# utils.install_packages('randomForest')
# utils.install_packages('reshape2')
# utils.install_packages('RMySQL')
# utils.install_packages('jsonlite')


# In[4]:


app = Flask(__name__)

@app.route('/new/onnet-wireless/api', methods = ['POST'])

def make_predict_onnet_rf():
    #get the json file as an input
    data = request.get_json(force=True)
    input_data = pd.io.json.json_normalize(data,'input_data')
    robjects.r.source("Onnet_RF_with_DB.R")
    r_output_df = robjects.r.run_OnnetRF_feasibility(input_data, path_py)
    py_output_df = pandas2ri.ri2py(r_output_df)
    output_dict = py_output_df.to_dict(orient='records')
    return jsonify(results=output_dict)

if __name__ =='__main__':
    app.run(host='0.0.0.0',port = 9100, debug = True)
