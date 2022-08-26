import requests
import json
def request():
    a = requests.get("http://saral.navgurukul.org/api/courses")
    b=a.json()
    # print(b)
    print("Slug No : Courses -----> ID")
    with open("txt.json","w") as f:
        json.dump(b,f,indent=4)
    with open("txt.json","r") as f:
        data = json.load(f)
        # print(data)
    id= [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i+1," : ",data['availableCourses'][i]['name']," -----> ",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1 
    # print(id)
    
    
    user=int(input("enter the serial number:"))-1
    x=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    y=x.json()
    with open("indu.json","w") as k:
        json.dump(y,k,indent=4)
    with open("indu.json","r") as k:
        c=json.load(k)
    # print(c)
    
    
    slug=[]
    j=0
    while j<len(y['data']):
        print(j+1,":",y['data'][j]['name'])
        slug.append(c['data'][j]['slug'])
        j=j+1
    # print(slug)
    
    d=int(input("enter the slug number:"))-1
    z=requests.get("http://saral.navgurukul.org/api/courses/"+str(d)+"/exercise/getBySlug?slug="+slug[d])
    m=z.json()
    with open("likki.json","w") as g:
        json.dump(m,g,indent=4)
    with open("likki.json","r") as g:
        n=json.load(g)
    # print(n)
    print(m['name'])
    print(m['slug'])
    print("CONTENT",m['content'])
    # user1=input("enter the user1:")
    for x in range (len(slug)):
        user1=input("enter the user1:")
        if user1=="back":
            x=0
        if x<len(slug):
            print(slug[i])
            print(b['content'])
    else:
        print("exit") 
request()





