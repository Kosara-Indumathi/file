import json
x='''
  {"name":"indu",
  "age":19,
  "city":"new york"
  }  '''
y=json.loads(x)
print(y)
print(type(y))