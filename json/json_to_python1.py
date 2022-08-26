import json
x="""
{"key1":"value1",
"key2":"value2"
}"""
y=json.loads(x)
print(y["key2"])