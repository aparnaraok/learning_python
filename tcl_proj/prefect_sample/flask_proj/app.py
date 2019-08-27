import pandas as pd
import json
import flask
import prefect
from flask import render_template
from .flow_with_pandas_2 import f
# from prefect.engine.executors import DaskExecutor
from pprint import pprint
from .flow_with_pandas_2 import log_stream
#from flow_with_pandas_2 import output_stream

# executor   = DaskExecutor(address="tcp://10.149.124.65:8786")
with open("input_json.json") as fileo:
    input_data = json.load(fileo)
input_data_frame = pd.read_json(json.dumps(input_data['input_data']))
input_data_frame['POP_DIST_KM'] = 48900 

app = flask.Flask(__name__)

@app.route('/<fails>')
def home(fails):
    with open("input_json.json") as fileo:
        input_data_1 = json.load(fileo)
    fail = False
    if fails == 'fail':
        fail = True
    flow_state = f.run(input_data = input_data_frame, fail= fail)
    print("DIR >>>>>>>>>>>>>>>>>>>",dir(flow_state))
    print(" ")
    print("RESULT >>>>>>>>>>>>>>>>>", flow_state.result)
    #return json.dumps(json.loads(output_stream.getvalue()))
    f.visualize(flow_state = flow_state, filename='./static/run')
    if fail == False:
        for i in flow_state.result:
            #pprint(flow_state.result[i].result)
            pprint(i.name)
            #pprint(dir(i))
            # assumes final state has a uniquely named function, will break otherwise
            if i.name == 'merge_input_aggregate':
                pprint(flow_state.result[i].result)
                #return flow_state.result[i].result.to_json(orient = 'records')
                output_json = flow_state.result[i].result.to_json(orient = 'records')
                return render_template('jsonlint.html', output_json = output_json, input_json = json.dumps(input_data_1))

    else:
        return render_template('jsonlint.html', output_json = "{'status':'failed'}", input_json = json.dumps(input_data_1))

@app.route('/distributed')
def distributed():
    flow_state = f.run(input_data = input_data_frame, fail= False, executor=executor)
    #return json.dumps(json.loads(output_stream.getvalue()))
    f.visualize(flow_state = flow_state)
    for i in flow_state.result:
        #pprint(flow_state.result[i].result)
        pprint(i.name)
        #pprint(dir(i))
        # assumes final state has a uniquely named function, will break otherwise
        if i.name == 'merge_input_aggregate':
            pprint(flow_state.result[i].result)
            return flow_state.result[i].result.to_json(orient = 'records')

@app.route('/ui')
def ui():
    return render_template('jsonlint.html')
#f.visualize(flow_state = flow_state, filename = './flowcharts/pandas2')

#print('final dframe that can be returned')
##pprint(dir(f))
##pprint(dir(f.sorted_tasks()[1]))
##pprint(flow_state._result.value)
#pprint('logstream as captured by the stream handler')
##pprint(log_stream.getvalue())
#pprint(output_stream.getvalue())
#pprint(json.loads(output_stream.getvalue()))

