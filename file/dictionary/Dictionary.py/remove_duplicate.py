# Write a program in python to remove the duplicate values from the dictionary. For example:
# Original dictionary = {1 : “Aman”, 2: “Suman”, 3: “Aman”}
# New dictionary = {1 : “Aman”, 2: “Suman”}

# dict={1:"aman",2:"suman",3:"aman"}
# dict.pop(3)
# print(dict)

d1={1:"Aman",2:"Suman",3:"Aman"}
a={ }
for k,v in d1.items():
    if v not in a.values():
        a[k]=v
print(a)

