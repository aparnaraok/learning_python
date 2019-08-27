'''*************************************************************************************************************
@summary  : Script to train the model
@author   : Aparna Rao Kota
***************************************************************************************************************'''
import os
import logging
import logging.config


logging.config.fileConfig("logging.conf")
# create logger
logger = logging.getLogger("modelLogger")
# import rpy2.robjects as robjects
# from rpy2.robjects.packages import importr


path_py = os.path.dirname(os.path.abspath(__file__))

class TrainModel:
    def __init__(self, func_name):
        '''Initializing
        '''
        func_dic = {"train_model": self.train_model()}  # mapping: string --> variable = function name

        self.active_fn = func_dic[func_name]


    def train_model(self):
        '''Trains the model
        '''
        # r_model_code_path = os.path.join(path_py, "train_model.R")
        # robjects.r.source(r_model_code_path)
        # r_output = robjects.r.sample_func(path_py)
        # print(r_output)
        # return r_output
        logging.info("Training the model begins.....")
        return "model train success"


    def run_function(self):
        '''Main Run
        '''
        self.active_fn