import pandas as pd
import json
from flow_with_pandas_2 import f
from pprint import pprint
from flow_with_pandas_2 import log_stream
from flow_with_pandas_2 import output_stream

with open("input_json.json") as fileo:
    input_data = json.load(fileo)
input_data_frame = pd.read_json(json.dumps(input_data['input_data']))


flow_state = f.run(input_data = input_data_frame)

#f.visualize(flow_state = flow_state, filename = './flowcharts/pandas2')

print('final dframe that can be returned')
#pprint(dir(f))
#pprint(dir(f.sorted_tasks()[1]))
#pprint(flow_state._result.value)
pprint('logstream as captured by the stream handler')
#pprint(log_stream.getvalue())
pprint(output_stream.getvalue())
pprint(json.loads(output_stream.getvalue()))

