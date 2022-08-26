# n=int(input("enter the number"))
# d={i:i*5 for i in range(1,n+1)}
# print(d)


n=int(input("enter the number"))
a={}
for x in range(n):
    a[x+1]=(x+1)*5
# for x in range(1,n+1):
#     a[x]=x*5
print(a)




