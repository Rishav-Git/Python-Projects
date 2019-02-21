import os
import json


path= input("Enter:")
jiles=[]
files = os.listdir(path)
for i in range(len(files)):
    jiles.append(os.path.join(path,files[i]))
    

def getJSON(filePathAndName):
    with open(filePathAndName,'r', encoding="utf8") as fp:
        return json.load(fp)

for i in jiles:
    myObj=getJSON(i)
    q=json.dumps(myObj,indent=2)
    os.remove(i)
    file = open(i,"w")
    file.write(q)
    file.close()


print("Done")
