'''*************************************************************************************************************
@summary  : Modelling Framework Script
@author   : Aparna Rao Kota
*************************************************************************************************************'''
import json
import logging
import logging.config
import log_formatter
import os
import subprocess
import time
from param_parser import ParseJson
from db_connector import DbConnector
from data_code import fetch_data_code
from data_code.fetch_data_code import FetchData
from data_code import transform_data_code
from data_code.transform_data_code import TransformData
from model_code import train_model
from model_code.train_model import TrainModel
from model_code import random_forest_model
from model_code.random_forest_model import RandomForestModel
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr


logging.config.fileConfig("logging.conf")
# create logger
logger = logging.getLogger("modelLogger")

class Modelling:
    def __init__(self):
        '''Initializing
        '''
        msg = "Initializing the Modelling Framework....."
        log_formatter.get_log_formatter(msg)

        self.json_data = ParseJson().load_json_content()


    def ret_fetch_data(self):
        '''Returns the fetch data functionality
        '''
        msg = "Fetching the data code....."
        log_formatter.get_log_formatter(msg)

        cls_dir_list = dir(fetch_data_code)
        fn_dir_list = dir(fetch_data_code.FetchData)

        data_properties = self.json_data["parameters"]["data_properties"]

        for key in data_properties:
            if key == "data_fetch":
                df_code_props = data_properties[key]["code_properties"]
                enable_mode = df_code_props["enabled"]
                lang = df_code_props["language"]
                file_path = df_code_props["filepath"]
                file_name = df_code_props["filename"]
                class_name = df_code_props["classname"]
                method_name = df_code_props["methodname"]
                module_name = os.path.join(file_path, file_name)

                if enable_mode:
                    if class_name in cls_dir_list:
                        if method_name in fn_dir_list:
                            try:
                                g = FetchData(method_name)
                                g.run_function()
                            except KeyError:
                                logging.error(
                                    "Please make sure whether the method name : : %s : : in the config JSON matches with the method name in the module : : %s",
                                    method_name, module_name)
                        else:
                            logging.error(
                                "Please make sure whether the method name : : %s : : in the config JSON matches with the method name in the module : : %s", method_name, module_name)
                    else:
                        logging.error(
                            "Please make sure whether the class name : : %s : :  in the config JSON matches with the classname in the module : : %s" , class_name, module_name)
                else:
                    logging.error("Please make sure whether the data fetch mode is enabled in config JSON")

    def ret_transform_data(self):
        '''Returns the transform data functionality
        '''
        msg = "Transforming the data....."
        log_formatter.get_log_formatter(msg)

        cls_dir_list = dir(transform_data_code)
        fn_dir_list = dir(transform_data_code.TransformData)

        data_properties = self.json_data["parameters"]["data_properties"]

        for key in data_properties:
            if key == "data_transform":
                dt_code_props = data_properties[key]["code_properties"]
                enable_mode = dt_code_props["enabled"]
                lang = dt_code_props["language"]
                file_path = dt_code_props["filepath"]
                file_name = dt_code_props["filename"]
                class_name = dt_code_props["classname"]
                method_name = dt_code_props["methodname"]
                module_name = os.path.join(file_path, file_name)

                if enable_mode:
                    if class_name in cls_dir_list:
                        if method_name in fn_dir_list:
                            try:
                                g = TransformData(method_name)
                                g.run_function()
                            except KeyError:
                                logging.error(
                                    "Please make sure whether the method name : : %s : : in the config JSON matches with the method name in the module : : %s",
                                    method_name, module_name)
                        else:
                            logging.error(
                                "Please make sure whether the method name : : %s : : in the config JSON matches with the method name in the module : : %s", method_name, module_name)
                    else:
                        logging.error(
                            "Please make sure whether the class name : : %s : :  in the config JSON matches with the classname in the module : : %s" , class_name, module_name)
                else:
                    logging.error("Please make sure whether the data transform mode is enabled in config JSON")


    def ret_train_model(self):
        '''Returns the model train data
        '''
        msg = "Training the model....."
        log_formatter.get_log_formatter(msg)

        cls_dir_list = dir(train_model)
        fn_dir_list = dir(train_model.TrainModel)

        model_properties = self.json_data["parameters"]["model_properties"]

        for key in model_properties:
            if key == "model_train":
                mt_code_props = model_properties[key]["code_properties"]
                enable_mode = mt_code_props["enabled"]
                lang = mt_code_props["language"]
                file_path = mt_code_props["filepath"]
                file_name = mt_code_props["filename"]
                class_name = mt_code_props["classname"]
                method_name = mt_code_props["methodname"]

                # module_name = os.path.join(file_path, file_name)
                # file_name = file_name + "." + lang
                # module_name = os.path.join(file_path, "train_model.py")
                path_py = os.path.join(os.getcwd(), "model_code")
                module_name = os.path.join(path_py, "train_model.py")

                if enable_mode:
                    # with open("new_file.py", "w") as f:
                    #     data = """print("hello world")"""
                    #     f.write(data)
                    # subprocess.call(["python", os.getcwd()+ "/" + "new_file.py"])
                    if file_name.endswith(".py"):
                        logging.info("Model File Language : : Python")
                        if class_name in cls_dir_list:
                            if method_name in fn_dir_list:
                                try:
                                    g = TrainModel(method_name)
                                    g.run_function()
                                except KeyError:
                                    logging.error(
                                        "Please make sure whether the method name : : %s : : in the config JSON matches with the method name in the module : : %s",
                                        method_name, module_name)
                            else:
                                logging.error(
                                    "Please make sure whether the method name : : %s : : in the config JSON matches with the method name in the module : : %s",
                                    method_name, module_name)
                        else:
                            logging.error(
                                "Please make sure whether the class name : : %s : :  in the config JSON matches with the classname in the module : : %s",
                                class_name, module_name)
                    elif file_name.endswith(".R"):
                        logging.info("Model File Language : : R")
                        path_py = os.path.join(os.getcwd(), "model_code")
                        r_model_code_path = os.path.join(path_py, file_name)

                        # r_model_code_path = os.path.join(path_py, "train_model.R")
                        if os.path.exists(r_model_code_path):
                            robjects.r.source(r_model_code_path)
                            r_output = robjects.r.sample_func(path_py)
                            # print(r_output)
                        else:
                            logging.error("Please make sure whether the file : : %s exists in the path : : %s", file_name, file_path)

                else:
                    logging.error("Please make sure whether the train model is enabled in config JSON")

    def get_rf_model(self):
        '''Runs the Random forest model
        '''

        msg = "Performing the Random Forest Algorithm to the model....."
        log_formatter.get_log_formatter(msg)

        rf = RandomForestModel()
        confusion_matrix, classification_rep = rf.perform_random_forest()

        msg = "Confusion Matrix"
        log_formatter.get_log_formatter(msg)
        print(confusion_matrix)
        # logging.debug(confusion_matrix)

        msg1 = "Classification Report"
        log_formatter.get_log_formatter(msg1)
        # logging.debug(classification_rep)
        print(classification_rep)

    def run_model_framework(self):
        '''Entry point of the framework
        '''
        json_data = self.json_data
        time.sleep(1)
        DbConnector().get_db_creds(json_data)
        time.sleep(1)
        self.ret_fetch_data()
        time.sleep(1)
        self.ret_transform_data()
        time.sleep(1)
        self.ret_train_model()
        time.sleep(1)
        self.get_rf_model()


m = Modelling()
m.run_model_framework()
