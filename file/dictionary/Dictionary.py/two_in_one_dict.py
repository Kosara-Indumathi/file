a={"a":1,"b":2}
b={"amla":"jhana","tree":"mango"}
for i in (a, b):
    a.update(b)
print(a)