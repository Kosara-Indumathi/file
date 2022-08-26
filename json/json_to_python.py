import json
d={
   "name":"indu",
   "course":"bsc",
   "class":"2nd year"
}
f=open("abc.json","w")
json.dump(d,f)
with open("abc.json","r") as f:
    a=json.load(f)
print(a)
a=open("abc.json","r")
b=json.load(a)
print(b)










