import json
x={
   4: 5, 
   6: 7, 
   1: 3, 
   2: 4
  }
y=json.dumps(x)
print(y)
z=json.loads(y)
x=(dict(sorted(z.items())))
x.sort(reverse=True)
print(x)





