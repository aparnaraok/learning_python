'''*************************************************************************************************************
@summary  : Script to fetch the data
@author   : Aparna Rao Kota
*************************************************************************************************************'''
import logging
import logging.config
import os
import pandas
from pandas import read_csv


logging.config.fileConfig("logging.conf")
# create logger
logger = logging.getLogger("modelLogger")

class FetchData:
    def __init__(self, func_name):
        '''Initializing
        '''
        # logging.info("=" * 50)
        # logging.info("Fetching the Data code ...")
        # logging.info("=" * 50)

        func_dic = {"fetch_data" : self.fetch_data()}  # mapping: string --> variable = function name

        self.active_fn = func_dic[func_name]

    def fetch_data(self):
        '''Returns the training data
        '''
        # logging.info("Fetching the data code..........")
        data_set_path = os.path.join(os.getcwd(), "data_set", "iris.csv")
        # data = read_csv(data_set_path)
        # logging.info("The shape of the data fetched is : : %s", data.shape)

        headernames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', "variety"]
        data = read_csv(data_set_path, names=headernames)
        logging.debug(data.head(50))
        return "fetch data success"

    def run_function(self):
        '''Main Run
        '''
        self.active_fn
