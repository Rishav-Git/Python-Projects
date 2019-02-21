import xlsxwriter
import json
import requests
import os

def getJSON(filePathAndName):
    with open(filePathAndName,'r') as fp:
        return json.load(fp)
##    return requests.get(filePathAndName).json()

m=input("Enter the URL:\n")

myObj = getJSON(m)
s12 = "ExcelOfJson.xlsx"
workbook = xlsxwriter.Workbook(s12)
worksheet = workbook.add_worksheet("Basic_Information")

row =0
col=0





#getting basic information


basicinfo = myObj.get("patientDemographics","")







#Getting the name of the patient


name= basicinfo.get("name","")

name1= name[0]

name2 = name1.get("given","")


worksheet.write(row, col, "First Name:")
worksheet.write(row, col+1, name2[0])
row+=1
col=0
worksheet.write(row, col, "Middle Name:")
worksheet.write(row, col+1, name2[1])
row+=1
col=0

worksheet.write(row, col, "Last Name:")
worksheet.write(row, col+1, name1["family"])

row+=1
col=0

#Getting date of birth


worksheet.write(row, col, "Date Of Birth")
worksheet.write(row, col+1, basicinfo["birthDate"])


row+=1
col=0

#getting the gender


worksheet.write(row, col, "Gender")
worksheet.write(row, col+1, basicinfo["gender"])


row+=1
col=0

#getting location

address = basicinfo.get("address","")

address1=address[0]
worksheet.write(row, col, "City:")
worksheet.write(row, col+1, address1["city"])

row+=1
col=0

worksheet.write(row, col, "State")
worksheet.write(row, col+1, address1["state"])
row+=1
col=0



#getting date range





worksheet.write(row, col, "Date Range:")
row+=1

daterange=myObj.get("dateRange","")

worksheet.write(row, col, "Effective Date High:")
worksheet.write(row, col+1, daterange["effectiveDateHigh"])
row=row+1
col=0
worksheet.write(row, col, "Effective Date Low:")
worksheet.write(row, col+1, daterange["effectiveDateLow"])

row+=1
col=0



#getting tobacco status


row=0
col=0
worksheet1 = workbook.add_worksheet("Parameters")

tobacco = myObj.get("tobaccoUse","")

worksheet1.write(row, col, "Tobacco Status")
worksheet1.write(row, col+1, tobacco["tobaccoStatus"])

row=6
col=0


res1 = tobacco.get("resources","")

l=len(res1)

if l!=0:
    worksheet1.write(row, col, "Page Number")
    worksheet1.write(row, col+1, "Tobacco Status")

    for i in range(l):
        row+=1
        col=0
        tob=res1[i]
        worksheet1.write(row,col, tob["pageNumber"])
        worksheet1.write(row, col+1, tob["valueString"])



# getting the build

row=0
col=4




build=myObj.get("build","")

res2 = build.get("resources","")

l=len(res2)

if l !=0 :

    worksheet1.write(row, col,"Build Average")
    row+=2
    worksheet1.write(row,col, "Height Average")

    a=build["heightGraphic"]
    i=a%12
    f=a//12
    s= str(f)+"' "+str(i)+'"'
    worksheet1.write(row, col, s)

    worksheet1.write(row, col, "Height Average")
    worksheet1.write(row, col+1, s)

    row+=1
    col=4


    worksheet1.write(row, col, "Weight in graph:")
    worksheet1.write(row, col+1, build["weightGraphic"])

    row+=1
    col=4


    worksheet1.write(row, col, "BMI in graph:")
    worksheet1.write(row, col+1, build["bmiGraphic"])


    row+=2
    col=4

    worksheet1.write(row, col, "Page Number")
    worksheet1.write(row, col+1, "Weight" )
    worksheet1.write(row, col+2, "Height")
    worksheet1.write(row, col+3, "BMI")







    for i in range(l):
        row+=1
        col=4
        bui= res2[i]
        worksheet1.write(row,col, bui["pageNumber"])
        com = bui.get("component","")
        for j in range(2,-1,-1):
            co=com[j]
            c=co.get("valueQuantity","")
            a=c.get("value")
            b=c.get("unit")
            ss = str(a) +"("+str(b) +")"
            worksheet1.write(row, col+1, ss)
            col=col+1



# Getting blood pressure


row = 0
col= 9





BP = myObj.get("bloodPressure","")

res3 = BP.get("resources","")
l=len(res3)

if l!=0:

    pulseArray = []
    worksheet1.write(row, col, "Blood Pressure")
    row+=2
    s1 = BP["systolicGraphic"]
    s2 = BP["diastolicGraphic"]
    s = str(s1)+"/"+str(s2)

    worksheet1.write(row, col, "Systolic/Diastolic")
    worksheet1.write(row, col+1, s)
    row+=1
    col=9


     # pulse pressure
    worksheet1.write(row, col, "Pulse Pressure")
    r=row
    c=col

    row+=3
    col=9


    worksheet1.write(row, col, "Page Number:")
    worksheet1.write(row, col+1, "SBP/DBP:")
    worksheet1.write(row, col+2, "PP:")

    sum1=0


    for i in range(l):
        row+=1
        col=9
        bpul = res3[i]
        worksheet1.write(row, col, bpul["pageNumber"])
        worksheet1.write(row, col+1, bpul["valueString"])
        worksheet1.write(row,col+2, bpul["pulsePressure"])
        pulseArray.append(bpul["pulsePressure"])
        

    for i in range(len(pulseArray)):
        sum1=sum1+(pulseArray[i])
        
    avg = round(sum1/len(pulseArray))

    worksheet1.write(r,c+1,avg)






workbook.close()
print("Opening Excel file......")

os.startfile(s12)

