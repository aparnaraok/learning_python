# -*- coding: utf-8 -*-
import json

mycompounds = [{"name :" : "Fructose", "formula" : "C6H12O6", "id" : 12345, "similarTo" : ["Hexose", "Glucose"]}]

with open("sample_file.json", "w") as jsonFile:
    json.dump(mycompounds, jsonFile) #here dump will overwrite