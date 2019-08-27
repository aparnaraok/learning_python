#!/usr/bin/env python3
import csv
import os
import json
import logging
import logging.config

logging.config.fileConfig("logging.conf")

# create logger
logger = logging.getLogger("modelLogger")


class ParseJson:

    def __init__(self):
        '''Initializing
        '''
        logging.info("=" * 50)
        logging.info("Initializing the JSON Parser...")
        logging.info("=" * 50)


    def load_json_content(self):
        '''Returns the JSON content
        '''
        pwd = os.getcwd()
        json_file = os.path.join(pwd, "new_config.json")
        with open(json_file) as f:
            json_content = json.load(f)
        return json_content

# parser = ParseJson()
# json_content = parser.load_json_content()