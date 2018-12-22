import json

with open("sample_file.json", 'r') as jsonFile:
    compounds = json.load(jsonFile)

print (compounds[0]["name"])
print (compounds[0]["formula"])