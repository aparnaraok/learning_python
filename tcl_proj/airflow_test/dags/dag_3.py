from __future__ import print_function
import os
import requests
import time
from builtins import range
from pprint import pprint

import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag1 = DAG(
    dag_id='example_dag_3',
    default_args=args,
    schedule_interval=None,
)


# [START howto_operator_python]
def print_context(ds, **kwargs):
    # pprint(kwargs)
    # print(ds)
    a = "https://api.github.com/users"
    print(a)
    resp = requests.get(a)
    print(resp.text)
    return 'Whatever you return gets printed in the logs'

def get_cwd(**kwargs):
    return os.getcwd()

run_this = PythonOperator(
    task_id='print_the_resp3_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag1,
)
# [END howto_operator_python]


# [START howto_operator_python_kwargs]
def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
   # print(os.getcwd())
    time.sleep(random_base)


# Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively

task = PythonOperator(
       task_id="Task",
       python_callable=get_cwd, 
       dag=dag1,
    )

run_this >> task
