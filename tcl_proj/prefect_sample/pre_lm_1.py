import json
from pprint import pprint
from prefect import Flow, Parameter
from prefect import task
from prefect.tasks.control_flow import switch
from similarity.jarowinkler import JaroWinkler

cut_off_fe = 50
cut_off_ge = 100

with open("input_json.json") as f:
    input_data = json.load(f)
input_data_str = json.dumps(input_data)
#pprint(input_data)

@task
def debug_json(json_str):
    pprint(json.loads(json_str))

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
def convert_bw_to_lle(local_loop_interface, bw_mbps):
    '''Returns the Local Loop Interface by comparing the BW with FE and GE
    '''
    #arg_dict = kwargs
    
    # local_loop_interface = arg_dict["local_loop_interface"]
    # bw_mbps = arg_dict["bw_mbps"]
    #rl = get_calc_match('something', 'something else')
    print(input_data)
    #print(rl)
    if (bw_mbps < cut_off_fe and local_loop_interface == "GE"):
       local_loop_interface = "FE"
    if (bw_mbps > cut_off_ge and local_loop_interface == "FE"):
       local_loop_interface = "GE"
    return local_loop_interface


#def round_bw_to_nearest_2(local_loop_interface, bw_mbps):
#    '''Returns the BW rounding nearest to 2 decimal places
#    '''
#    # arg_dict = kwargs
#    # local_loop_interface = arg_dict["local_loop_interface"]
#    # bw_mbps = arg_dict["bw_mbps"]
#    
#    if bw_mbps < 2:
#       bw_mbps = 2
#    elif ((bw_mbps % 2 == 1) and (bw_mbps <= 100) and (local_loop_interface == "FE")):
#       bw_mbps += 1
#    elif ((bw_mbps > 100) and (bw_mbps % 50 > 0) and (local_loop_interface == "FE")):
#       bw_mbps = round(bw_mbps, 2)
#    elif ((bw_mbps >= 50) and (bw_mbps % 50 > 0) and (local_loop_interface == "GE")):
#       bw_mbps = round(bw_mbps, 2)
#    return bw_mbps
#
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
def get_llp(input_data):
    '''Returns the Loop loop interface
    '''
    print(input_data)
    ret_data = json.loads(input_data)
    print(type(ret_data))
    llp = ret_data['input_data'][0]["local_loop_interface"].lower()
    new_llp = llp
    if ("fast" in llp and "ethernet" in llp):
        new_llp = "FE"
    if ("gigabit" in llp and "ethernet" in llp):
       new_llp = "GE"
    ret_data["local_loop_interface"] = new_llp
    if ("FE" in ret_data["input_data"][0]["local_loop_interface"]) or ("GE" in ret_data["input_data"][0]["local_loop_interface"]):
       ret_data["input_data"][0]["valid_llp"] = True
    ret_data["input_data"][0]["valid_llp"] = False
    return json.dumps(ret_data)


with Flow("cal_match") as f:
   prospect_name, customer_name = Parameter("pros_name"), Parameter("cust_name")
   match = get_calc_match(prospect_name,customer_name)
    
# with Flow("bw") as f1:
   local_loop_interface, bw_mbps = Parameter("local_loop_interface"), Parameter("bw_mbps")
   match_2 = convert_bw_to_lle(local_loop_interface, bw_mbps)
   
   input_data = Parameter("input_data") 
   #print(input_data)
   match_3 = get_llp(input_data)
   debug_json(match_3)
flow_state = f.run(pros_name = "SOMETHING", cust_name = "SOMETHING_ELSE", local_loop_interface = "GE", bw_mbps = 110, input_data = input_data_str)
# flow_state_2 = f1.run(local_loop_interface = "GE", bw_mbps = 110)




#f.visualize(flow_state = flow_state, filename = 'leven5')
# f1.visualize(flow_state = flow_state_2, filename = "leven3")

