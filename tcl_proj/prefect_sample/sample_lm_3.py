
from pprint import pprint
from prefect import Flow, Parameter
from prefect import task
from prefect.tasks.control_flow import switch
from similarity.jarowinkler import JaroWinkler

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

with Flow("cal_match") as f:
    prospect_name, cust_name = Parameter("pros_name"), Parameter("cust_name")
    match = get_calc_match(prospect_name, cust_name)


flow_state = f.run(prospect_name = "something", cust_name = "something_else")
f.visualize(flow_state = flow_state, filename = 'leven2')

