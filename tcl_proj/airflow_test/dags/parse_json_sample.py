from __future__ import print_function
import os
import requests
import json
from pprint import pprint

import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from dag_sample_rules import TestRules
 
args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='example_json_rule_dag',
    default_args=args,
    schedule_interval=None,
)


# [START howto_operator_python]
def print_json_context(*args, **kwargs):
    print("Entering into the Print JSON context.....")
    print("Current working dir >>>>", os.getcwd())
    print(os.listdir())
    with open('input.json', 'r') as f:
        resp = json.load(f)
    val_list = (list(resp.values()))
    tr = TestRules().test_rules(val_list)
    print("Test rules is >>>>>", tr)
    resp.update({'tr': tr})
    with open('output.json', 'w') as f:
        json.dump(resp, f)
     # print(resp)
    return resp
 
    # return 'Whatever you return gets printed in the logs'

def parse_json_context(*args, **kwargs):
    print("Entering into the Print JSON context.....")
    with open('input.json', 'r') as f:
        resp = json.load(f)
    return resp

def apply_rules(**Kwargs):
    print("Inside my test 2 function with resp print ...")
    resp = print_json_context()
    print("Resp >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", resp)
    val_list = (list(resp.values()))
    tr = TestRules().test_rules(val_list)
    resp.update({'tr': tr})
    return resp 

def dump_output_json(**Kwargs):
    resp = apply_rules()
    with open('output.json', 'w') as f:
        json.dump(resp, f)

task_1 = PythonOperator(
    task_id='parse_input_json',
    provide_context=True,
    python_callable=parse_json_context,
    dag=dag,
)

task_2 = PythonOperator(
     task_id='rules_check',
     python_callable=apply_rules,
     op_kwargs={'random_print': 'abc'},
     dag=dag,
)

task_3 = PythonOperator(
       task_id='dump_output_json',
       provide_context=True,
       python_callable=dump_output_json,
       dag=dag,
)
task_1 >> task_2 >> task_3
