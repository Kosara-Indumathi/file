fp=open("file-question3.txt","w")
lines=["Kotak\n","HDFC\n","RBL\n","SBI\n", "Bank of Baroda"]
fp.writelines(lines)
fp.close()
# i=0
# while i<len(lines):
#     print(lines[i])
#     i=i+1

my=open("file-question3.txt","r")
print(my.read())
my.close()

