import requests
import json
meraki_url="http://saral.navgurukul.org/api/courses"
Data=requests.get(meraki_url)
Data1=Data.json()
with open("merakicourses.json","w")as Meraki_data:
    json.dump(Data1,Meraki_data,indent=4)

saral=0
while saral<len(Data1["availableCourses"]):
    print(saral+1,Data1["availableCourses"][saral]["name"])
    saral=saral+1
meraki_courses=int(input("choose your courses which you want"))
print(Data1["availableCourses"][meraki_courses-1]["name"])

Meraki_id=Data1["availableCourses"][meraki_courses-1]["id"]

saral_data="http://saral.navgurukul.org/api/courses/"+str(Meraki_id)+"/exercises"
data_m=requests.get(saral_data)
data2_m=data_m.json()
with open("saralparents.json","w")as data3:
    json.dump(data2_m,data3,indent=4)

no=0
for child in range(len(data2_m["data"])):
        no+=1
        print("       ",no,".",data2_m["data"][child]["name"])
        serial_no_1=1
        if data2_m["data"][child]["childExercises"] == []:
            print("             ",serial_no_1,".",data2_m["data"][child]["slug"])
            serial_no_1 += 1
        else:

            serial_no=1
            for Question in range(len(data2_m["data"][child]["childExercises"])):
                print("              ",serial_no,".",data2_m["data"][child]["childExercises"][Question]["name"])
                serial_no+=1


Slug= int(input("Enter the number of parents no :"))
print(data2_m["data"][Slug-1]["name"])   
slug_ind=[]
no=0
List=[] 
for child in range(len(data2_m["data"])):
    no+=1
    serial_no_1=1
    if data2_m["data"][child]["childExercises"] == List:
        serial_no_1 += 1

        serial_no=1
        for Question in range(len(data2_m["data"][Slug-1]["childExercises"])):
            if data2_m["data"][child]["childExercises"] == List:
                print("              ",serial_no,".",data2_m["data"][Slug-1]["childExercises"][Question]["name"])
                slug = data2_m["data"][Slug-1]["childExercises"][Question]["slug"]
                parent = data2_m["data"][Slug-1]["childExercises"][Question]['id']
                slug1 = requests.get(" http://saral.navgurukul.org/api/courses/"+parent+"/exercise/getBySlug?slug="+slug)

                slug2 = slug1.json()
                slug_ind.append(slug2["content"])
                serial_no+=1
        break
question_1 = int(input("Enter the question  number: "))
question=question_1-1
print(slug_ind[question])
while question_1 > 0:
    next_question = input("Do you want next or previous: ")
    if question_1==len(slug_ind):
        print("next page")
    if next_question == "p":
        if  question_1 ==1:
            print("no more question")
            break
        elif question_1 > 0:
            question_1=question_1-2
            print(slug_ind[question_1])
    elif next_question == "n":
        if  question_1 < len(slug_ind):
            index = question_1 + 1
            print(slug_ind[index-1])
            question += 1
            question_1 = question_1 + 1
            if question == (len(slug_ind)-1):
                print("no more question here::")
                break