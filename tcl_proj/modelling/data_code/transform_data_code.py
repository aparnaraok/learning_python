'''*************************************************************************************************************
@summary  : Script to transform the data
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


class TransformData:
    def __init__(self, func_name):
        '''Initializing
        '''
        # logging.info("=" * 50)
        # logging.info("Transforming the Data code ...")
        # logging.info("=" * 50)

        func_dic = {"transform_data": self.transform_data()}  # mapping: string --> variable = function name

        self.active_fn = func_dic[func_name]

    def transform_data(self):
        '''Returns the transformed data
        '''
        logging.info("Inside the data transform function..........")
        data_set_path = os.path.join(os.getcwd(), "data_set", "iris.csv")
        data = read_csv(data_set_path)
        logging.info("The shape of the data fetched is : : %s", data.shape)
        return "data transform success"

    def run_function(self):
        '''Main run
        '''
        self.active_fn