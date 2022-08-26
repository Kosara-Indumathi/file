import json
filename='your_file.json'
entry={'car1':33}
with open(filename,"r") as file:
    data=json.load(file)
data.append(entry)
with open(filename,"w") as file :
    json.dump(data,file)