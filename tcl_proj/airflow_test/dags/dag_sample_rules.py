import os

class TestRules:
    def __init__(self):
        print("Initializing the rules engine ......")
    def test_rules(self, val_list):
        a = "Testing the rules ...."
        flag = None
        flag_list = [] 
        for val in val_list:
            if isinstance(val, int):
               flag = 'int_flag'
            if isinstance(val, float):
               flag = 'float_flag'
            if isinstance(val, str):
               flag = "string"
            flag_list.append(flag)
        return flag_list
