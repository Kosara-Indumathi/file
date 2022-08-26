def word(user):
    count={}
    for i in user:
        count[i]=user.count(i)
    return count
user=input("enter the string")
print(word(user))

    










