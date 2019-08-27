
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


# In[2]:


path_py = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/api', methods = ['POST'])

def make_predict_onnet_wireline():
    #get the json file as an input
    data = request.get_json(force=True)
    input_data = pd.io.json.json_normalize(data,'input_data')
    # here write your rcode
    robjects.r.source("scripts/onnet_wireline_score_api.R")
    r_output_df = robjects.r.score(input_data, path_py)
    py_output_df = pandas2ri.ri2py(r_output_df)
    output_dict = py_output_df.to_dict(orient='records')
    return jsonify(results=output_dict)


# In[ ]:


if __name__ =='__main__':
    app.run(port = 6000, debug = True)

