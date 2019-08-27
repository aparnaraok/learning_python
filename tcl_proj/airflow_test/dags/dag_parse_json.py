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
    dag_id='example_json_dag',
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


run_this = PythonOperator(
    task_id='parse_json_check_rules',
    provide_context=True,
    python_callable=print_json_context,
    dag=dag,
)

def my_test_function(**kwargs):
    """This is a function that will run within the DAG execution"""
    print(os.getcwd())

def my_test_2_function(**Kwargs):
    print("Inside my test 2 function with resp print ...")
    resp = print_json_context()
    print("Resp >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", resp)
    return "Success" 


task = PythonOperator(
     task_id='json_print',
     python_callable=my_test_function,
     op_kwargs={'random_print': 'abc'},
     dag=dag,
)

task_3 = PythonOperator(
       task_id='final_print',
       provide_context=True,
       python_callable=my_test_2_function,
       dag=dag,
)
run_this >> task >> task_3
