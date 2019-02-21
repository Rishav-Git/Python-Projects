import os
import json


path= input("Enter:")

    

def getJSON(filePathAndName):
    with open(filePathAndName,'r', encoding="utf8") as fp:
        return json.load(fp)

myObj=getJSON(path)
q=json.dumps(myObj,indent=2)
os.remove(path)
file = open(path,"w")
file.write(q)
file.close()


print("Done")
