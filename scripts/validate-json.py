import json
import jsonschema
import sys

def validate(file,schema):
    with open(file) as f:
        data=json.load(f)

    with open(schema) as s:
        sch=json.load(s)

    jsonschema.validate(data,sch)

validate(sys.argv[1],sys.argv[2])