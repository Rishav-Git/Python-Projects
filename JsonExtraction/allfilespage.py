import xlsxwriter
import json
import requests
import os
import collections
from operator import itemgetter

path= input("Enter the path:")
jiles=[]
files = os.listdir(path)
for i in range(len(files)):
    jiles.append(os.path.join(path,files[i]))


def getJSON(filePathAndName):
    with open(filePathAndName,'r') as fp:
        return json.load(fp)
allparam=[]
j=1
for i in jiles:
    myObj=getJSON(i)
    ## Getting tobacco

    tobacco = myObj.get("tobaccoUse","")

    res1= tobacco.get("resources","")

    length=len(res1)

    if length !=0:
        for i in range(length):
            tob=res1[i]
            pg = int(tob["pageNumber"])
            d = { "page" : pg, "value" : tob["status"]}
            allparam.append(d)


    ## Getting alcohol
        
    alch = myObj.get("alcoholUse","")
    if alch !="":
        res = alch.get("resources","")
        length=len(res)
        if length !=0:
            for i in range(length):
                al=res[i]
                pg = int(al.get("pageNumber",""))
                ss = str(al["status"])+"->"+str(al["lineText"]) 
                
                d={"page":pg,"value":ss}
                allparam.append(d)


    ## Getting the blood pressure

    BP = myObj.get("bloodPressure","")

    res3 = BP.get("resources","")
    length=len(res3)

    if length!=0:
        for i in range(length):
            b=res3[i]
            ss = "SBP/DBP -> "+ str(b.get("valueString",""))
            pg = int(b.get("pageNumber",""))
            d={"page":pg,"value":ss}
            allparam.append(d)
            ss1 = "PP -> "+ str(b.get("pulsePressure",""))
            
            d1={"page":pg,"value":ss1}
            allparam.append(d1)




    ## Getting cholesterol


    chol= myObj.get("cholesterol","")

    res = chol.get("resources","")

    length = len(res)
    da={}
    if length !=0:
        for i in range(length):
            cho=res[i]
            ss = cho.get("comment") +"->"+cho.get("valueString")
            pg=int(cho.get("pageNumber",""))
            d= {"page" : pg, "value" : ss}
            allparam.append(d)

    ## Getting build


    build=myObj.get("build","")
    res2 = build.get("resources","")
    length=len(res2)
    if length!=0:
        for i in range(length):
            bui = res2[i]
            pg = int(bui.get("pageNumber",""))
            com = bui.get("component","")
            for j in range(len(com)):
                co= com[j]
                c=co.get("valueQuantity","")
                a=c.get("value","")
                b=c.get("unit","")
                if a != None:
                    code = co.get("code","")
                    t=code.get("text")
                    ss = str(t)+"->"+str(a)+"("+str(b)+")"
                    d1 = {"page" : pg, "value" : ss}
                    allparam.append(d1)


    ## sorting the list

           
    length = len(allparam)
    allparam.sort(key=itemgetter("page"))

    # Creating the excel file
    path1=r"C:\Users\736288\Downloads\Excelfiles"
    a=str(j)+".xlsx"
    s12=os.path.join(path1,a)
    workbook = xlsxwriter.Workbook(s12)
    worksheet = workbook.add_worksheet("Data")

    row=0
    col=0
    worksheet.write(row, col, "PageNumber")
    worksheet.write(row, col+1, "Reference")

    row+=1
    col=0

    for i in range(length):
        row+=1
        col=0
        rishav = allparam[i]
        worksheet.write(row,col,rishav["page"])
        worksheet.write(row,col+1,rishav["value"])




    ## Final Steps
    workbook.close()
    j+=1
