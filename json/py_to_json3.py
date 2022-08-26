# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# Expected Output:
# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }

import json
a={"id" : 1, "name" : "value2", "age" : 29}
b=json.dumps(a,sort_keys=True,indent=2)
print(b)