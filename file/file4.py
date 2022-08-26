fp="people1-exercise.txt"
count=0
with open(fp,"r") as f:
     for i in f :
        count=count+1
print("number of lines:",count)


