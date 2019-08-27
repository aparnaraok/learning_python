from __future__ import print_function
import os
import requests
import json
from pprint import pprint

import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from Levenshtein import *
# import MySQLdb

# Connect to MySQL Database
# db = MySQLdb.connect(host="INP44XDDB2552", user="optimus_user", passwd="Tata123", db="optimus_abstract")
#cur = db.cursor()
#print("CURSOR >>>>>", cur)

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='lm_cost_dag',
    default_args=args,
    schedule_interval=None,
)

cut_off_fe = 50
cut_off_ge = 100

def get_calc_match(*args, **kwargs):
    '''Gets the record linkage between prospect name and cust name
    '''
    arg_dict = kwargs

    prospect_name = arg_dict["prospect_name"].lower()
    cust_name = arg_dict["cust_name"].lower()
    if (prospect_name != "") and not (prospect_name and cust_name) is None:
       record_linkage = distance(prospect_name, cust_name)
    return record_linkage


def convert_bw_to_lle(*args, **kwargs):
    '''Returns the Local Loop Interface by comparing the BW with FE and GE
    '''
    arg_dict = kwargs
    
    local_loop_interface = arg_dict["local_loop_interface"]
    bw_mbps = arg_dict["bw_mbps"]
    if (bw_mbps < cut_off_fe and local_loop_interface == "GE"):
       local_loop_interface = "FE"
    if (bw_mbps > cut_off_ge and local_loop_interface == "FE"):
       local_loop_interface = "GE"
    return local_loop_interface


def round_bw_to_nearest_2(*args, **kwargs):
    '''Returns the BW rounding nearest to 2 decimal places
    '''
    arg_dict = kwargs
    local_loop_interface = arg_dict["local_loop_interface"]
    bw_mbps = arg_dict["bw_mbps"]
    
    if bw_mbps < 2:
       bw_mbps = 2
    elif ((bw_mbps % 2 == 1) and (bw_mbps <= 100) and (local_loop_interface == "FE")):
       bw_mbps += 1
    elif ((bw_mbps > 100) and (bw_mbps % 50 > 0) and (local_loop_interface == "FE")):
       bw_mbps = round(bw_mbps, 2)
    elif ((bw_mbps >= 50) and (bw_mbps % 50 > 0) and (local_loop_interface == "GE")):
       bw_mbps = round(bw_mbps, 2)
    return bw_mbps


def get_adjacent_pop_distance(*args, **kwargs):
    '''Returns the adjacent pop distance by converting m to kms
    '''
    arg_dict = kwargs
    pop_dist_service_mtr = arg_dict["pop_dist_service_mtr"]
    adj_fac = arg_dict["adj_fac"]
    
    pop_dist_km_service = (pop_dist_service_mtr / 1000) * (adj_fac)
    pop_dist_km_service_mod = round(pop_dist_km_service, 5)
    
    if pop_dist_km_service_mod > 501:
       pop_dist_km_service_mod = 501
    elif pop_dist_km_service_mod == 0:
       pop_dist_km_service_mod = 5
    else:
       pop_dist_km_service_mod = pop_dist_km_service_mod 
    return pop_dist_km_service_mod


def no_return(*args, **kwargs):
    '''Returns None
    '''
    pass    
     
task_1 = PythonOperator(
    task_id = "get_rcd_linkage",
    op_kwargs = {"prospect_name" : "something", "cust_name" : "something_else"},
    python_callable = get_calc_match,
    dag = dag,
)


task_2 = PythonOperator(
     task_id = "get_local_loop_interface",
     python_callable = convert_bw_to_lle,
     op_kwargs = {"local_loop_interface": "GE", "bw_mbps" : 10},
     dag = dag,
)

task_2_a = PythonOperator(
     task_id = "clean_local_loop_interface_for_lm_cost",
     python_callable = no_return,
     dag = dag,
)

task_3 = PythonOperator(
    task_id = "round_bw_to_nearest_2",
    python_callable = round_bw_to_nearest_2,
    op_kwargs = {"local_loop_interface" : "GE", "bw_mbps" : 80.1879900},
    dag = dag,
)

task_4 = PythonOperator(
    task_id = "converting_m_to_km_and_adjust",
    python_callable = get_adjacent_pop_distance,
    op_kwargs = {"pop_dist_service_mtr" : 0, "adj_fac" : 1.25},
    dag = dag,
)

task_5 = PythonOperator(
    task_id = "merging_rc_with_input_file",
    python_callable = no_return,
    dag = dag,
)

task_1 >> task_2 >> task_2_a >> task_3 >> task_4 >> task_5
