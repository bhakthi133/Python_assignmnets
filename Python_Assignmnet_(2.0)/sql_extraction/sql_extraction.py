import sys
import re
import json

if len(sys.argv) < 2:
    print("Please provide a SQL filename")
    sys.exit(1)

sql_file = sys.argv[1]

with open(sql_file, "r") as file:
    sql_content = file.read()

pattern = r"CREATE PROCEDURE\s+(\w+)"

matches = re.findall(pattern, sql_content, re.IGNORECASE)

print(matches)
li=[]
for i in matches:
    li.append({"procedure_name":i})


pattern = r"CREATE PROCEDURE\s+(\w+)\s*\((.*?)\)"

matches = re.findall(pattern, sql_content, re.IGNORECASE | re.DOTALL)

for name, parameters in matches:
    print("Procedure:", name)
    print("Parameters:", parameters)
    print("-------------------")


param_pattern = r"\b(IN|OUT|INOUT)\s+(\w+)"

for name, parameters in matches:
    print("Procedure:", name)

    param_matches = re.findall(param_pattern, parameters, re.IGNORECASE)

    for mode, param_name in param_matches:
        print("Mode:", mode)
        print("Name:", param_name)

    print("-------------------")

param_pattern = r"\b(IN|OUT|INOUT)\s+(\w+)\s+(\w+)"

for name, parameters in matches:
    print("Procedure:", name)

    param_matches = re.findall(param_pattern, parameters, re.IGNORECASE)
    i=0
    param_list = []

    for mode, param_name, data_type in param_matches:
        param_dict = {}

        param_dict["mode"] = mode
        param_dict["name"] = param_name
        param_dict["type"] = data_type

        param_list.append(param_dict)

        li[i]["parameters"] = param_list
        i=i+1
    print("-------------------")

body_pat=r"BEGIN(.*?)END\s*//"

body=re.findall(body_pat,sql_content,re.IGNORECASE | re.DOTALL)
i=0
for bod in body:
    li[i]["body"]=bod.strip()
    i=i+1
    print(bod.strip())
    print("----------------")

print(li)
with open("sample_stored_procedure.json", "w") as file:
    json.dump(li, file, indent=4)

print("JSON file created successfully!")

