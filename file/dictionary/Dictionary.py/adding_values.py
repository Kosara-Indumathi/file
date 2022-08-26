d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d1:   
    if i in d2:
        d2[i]=d1[i]+d2[i]
d1.update(d2)
print(d1)



