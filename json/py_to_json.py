# import json
# dict={
#     "name":"indu",
#     "class":"2nd year",
#     "course":"bsc"
#   }   
# with open("myfile.json","w") as file:
#     json.dump(dict,file)







import json
def function(list):
    a={}
    for i in range(len(list)-1):
       b={list[i]:list[i+1]}
       a.update(b)
    print(a)
    b=json.dumps(a)
    print(b)
    print(type(b))
function([0,1,2,3,4,5])



