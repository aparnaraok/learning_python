import json
import pandas as pd
from pprint import pprint
from prefect import Flow, Parameter
from prefect import task
from prefect.tasks.control_flow import switch
from similarity.jarowinkler import JaroWinkler
from prefect.engine.executors import DaskExecutor

cut_off_fe = 50
cut_off_ge = 100

with open("input_json.json") as f:
    input_data = json.load(f)

#input_data_str = json.dumps(input_data)
#input_data_frame = pd.read_json(json.dumps(input_data['input_data']))
#pprint(input_data_frame)
#pprint(input_data)

#input_data_str = json.dumps(input_data['input_data'][0])
input_data_obj = input_data['input_data'][0]
@task
def debug_json(json_str):
    print('global value :'+ str(cut_off_fe))
    pprint(json_str)

@task
def json_loader(json_str):
    return json.loads(json_str)

@task
def get_llp(input_data):
    '''Returns the Loop loop interface
    '''
    #print(input_data)
    #ret_data = json.loads(input_data)
    ret_data = input_data
    print(type(ret_data))
    llp = ret_data["local_loop_interface"].lower()
    new_llp = llp
    if ("fast" in llp and "ethernet" in llp):
        new_llp = "FE"
    if ("gigabit" in llp and "ethernet" in llp):
       new_llp = "GE"
    ret_data["local_loop_interface"] = new_llp
    if ("FE" in ret_data["local_loop_interface"]) or ("GE" in ret_data["local_loop_interface"]):
       ret_data["valid_llp"] = True
    ret_data["valid_llp"] = False
    #return json.dumps(ret_data)
    return ret_data

@task
def get_calc_match(prospect_name, cust_name):
    '''Gets the record linkage between prospect name and cust name
    '''
    jarowinkler   = JaroWinkler()
    prospect_name = prospect_name.lower()
    cust_name     = cust_name.lower()
    if (prospect_name != "") and not (prospect_name and cust_name) is None:
       record_linkage = jarowinkler.similarity(prospect_name, cust_name)
    print(f"the match  is  {record_linkage}")
    return record_linkage

@task
def convert_bw_to_lle(input_data):
    '''Returns the Local Loop Interface by comparing the BW with FE and GE
    '''
    #arg_dict = kwargs
    
    # local_loop_interface = arg_dict["local_loop_interface"]
    # bw_mbps = arg_dict["bw_mbps"]
    #rl = get_calc_match('something', 'something else')
    #print(input_data)
    #print(rl)
    if (input_data['bw_mbps'] < cut_off_fe and input_data['local_loop_interface'] == "GE"):
       input_data['local_loop_interface'] = "FE"
    if (input_data['bw_mbps'] > cut_off_ge and input_data['local_loop_interface'] == "FE"):
       input_data['local_loop_interface'] = "GE"
    return input_data


@task
def round_bw_to_nearest_2(input_data):
    '''Returns the BW rounding nearest to 2 decimal places
    '''
    # arg_dict = kwargs
    # local_loop_interface = arg_dict["local_loop_interface"]
    # bw_mbps = arg_dict["bw_mbps"]
    
    #raise NameError
    if input_data['bw_mbps'] < 2:
       input_data['bw_mbps'] = 2
    elif ((input_data['bw_mbps'] % 2 == 1) and (input_data['bw_mbps'] <= 100) and (input_data['local_loop_interface'] == "FE")):
       input_data['bw_mbps'] += 1
    elif ((input_data['bw_mbps'] > 100) and (input_data['bw_mbps'] % 50 > 0) and (input_data['local_loop_interface'] == "FE")):
       input_data['bw_mbps'] = round(input_data['bw_mbps'], 2)
    elif ((input_data['bw_mbps'] >= 50) and (input_data['bw_mbps'] % 50 > 0) and (input_data['local_loop_interface'] == "GE")):
       input_data['bw_mbps'] = round(input_data['bw_mbps'], 2)
    return input_data

@task
def convert_metres_to_km(input_data):
    input_data['POP_DIST_KM'] = input_data['POP_DIST_KM']/1000
    return input_data
#
#def get_adjacent_pop_distance(pop_dist_service_mtr, adj_fac):
#    '''Returns the adjacent pop distance by converting m to kms
#    '''
#    # arg_dict = kwargs
#    # pop_dist_service_mtr = arg_dict["pop_dist_service_mtr"]
#    # adj_fac = arg_dict["adj_fac"]
#    
#    pop_dist_km_service = (pop_dist_service_mtr / 1000) * (adj_fac)
#    pop_dist_km_service_mod = round(pop_dist_km_service, 5)
#    
#    if pop_dist_km_service_mod > 501:
#       pop_dist_km_service_mod = 501
#    elif pop_dist_km_service_mod == 0:
#       pop_dist_km_service_mod = 5
#    else:
#       pop_dist_km_service_mod = pop_dist_km_service_mod 
#    return pop_dist_km_service_mod

@task
def load_arc_rate_card(fail):
    if fail:
        raise NameError
    return {'mock':'data'}
@task
def adjust_pop_dist(input_data):
    return input_data
@task
def adjust_bw_arc_and_MACD(input_data):
    return input_data
@task
def get_cust_coords():
    return {'mock':'data'}
@task
def aggregate_connected_cust(connected_custs_match):
    return connected_custs_match

@task
def merge_input_and_rate_card(input_data, rate_card):
    print('merging on BW_mbps_2","POP_DIST_KM_SERVICE_MOD","local_loop_interface ')
    merged_data = input_data
    return merged_data
@task
def merge_input_aggregate(input_data, aggregate):
    print('merging input_json and aggregate cust coords')
    merged_data = input_data
    return merged_data

@task
def get_connected_entitiy(input_data, cust_coords):
    print('matching connected entities')
    merged_data = input_data
    return merged_data

with Flow("cal_match") as f:
   input_data      = Parameter("input_data") 

   step_1                = get_llp(input_data)
   step_2                = convert_bw_to_lle(step_1)
   step_3                = round_bw_to_nearest_2(step_2)
   step_4                = convert_metres_to_km(step_3)
   step_5                = adjust_pop_dist(step_4)
   rate_card             = load_arc_rate_card(fail_on_purpose)
   step_6                = merge_input_and_rate_card(step_5, rate_card)
   step_7                = adjust_bw_arc_and_MACD(step_6)
   cust_coords           = get_cust_coords()
   connected_custs_match = get_connected_entitiy(step_7, cust_coords) 
   aggregate             = aggregate_connected_cust(connected_custs_match)
   aggregate_merged      = merge_input_aggregate(step_7, aggregate)

   debug_json(aggregate_merged)

flow_state = f.run(input_data = input_data_obj)

