import requests
import json

# def request(requ):

def request():
    api=requests.get("http://saral.navgurukul.org/api/courses")
    req=(api.json())
    with open("courses.json","w") as f:
        file=json.dump(req,f,indent=4)
    with open("courses.json","r") as f1:
        r=json.load(f1)
        print((r))
    store=(req["availableCourses"])
    i=1
    name=[]
    id=[]
    for i in range(len(store)):
        print(i,store[i]["name"], end="--")
        print(store[i]["id"])
        name.append(store[i]["name"])
        id.append(store[i]["id"])
    print(" ")
    user=int(input("enter the course serial number.... "))
    user1=id[user]
    user2=name[user-1]
    print(user2,end=" ")
    print(user1)
    # first_api()


    # user=int(input("enter the course serial number.... "))
    # user1=id[user]
    api2=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
    b=(api2.json())
    # print(b)
    with open("second_api.json","w") as file1:
        json.dump(b,file1,indent=4)
    api3=requests.get("http://saral.navgurukul.org/api/courses/"+user1+"/exercises")
    print(api3)
    data2=api3.json()
    slug=[]
    count=1
    for sec in data2["data"]:
        print(count,sec["name"])
        slug.append(sec["slug"])
        count2 = 1
        for child in sec["childExercises"]:
            print("      ",count2,child["name"])
            slug.append(child["slug"])
            count2 += 1
        count+=1
    print(".........................")
    print("you want slug? or up")
    print(".........................")
    want=input("1.up\n2.slug")
    print(".........................")
    if want == "slug":
        print('WELCOME TO SLUG CONTENT')

        var2=int(input("Enter number for showing content of slug :- "))
        var3=requests.get("https://saral.navgurukul.org/api/courses/"+user1+"/exercise/getBySlug?slug="+str(slug[var2-1]))
        data3=var3.json()
        print(data3["content"])
        while True:
            x=var2
            print("....................")
            options=input("enter your option\n1.up\n2.next\n3.privious\n4.exit\n.................. ")
            if options=="2":
                x+=1
                req=requests.get("https://saral.navgurukul.org/api/courses/"+user1+"/exercise/getBySlug?slug="+str(slug[x-1]))
                r1=req.json()
                print("content",r1["content"])
                print(x)
                break
            elif options=="3":
                x-=1
                req=requests.get("https://saral.navgurukul.org/api/courses/"+user1+"/exercise/getBySlug?slug="+str(slug[x-1]))
                r1=req.json()
                print("content",r1["content"])
                print(x)
                break
            elif options=="1":
                c=1
                for dic1 in data2["data"]:
                    print(c,dic1["name"])
                    c+=1
                    for i in dic1["childExercises"]:
                        print("    ",c,i["name"])
                        c+=1
                        break
            elif options=="4":
                [print("Exit the page")]
            else:
                break
    else:
            api=requests.get("http://saral.navgurukul.org/api/courses")
    req=(api.json())
    with open("courses.json","w") as f:
        file=json.dump(req,f,indent=4)
    with open("courses.json","r") as f1:
        r=json.load(f1)
        print((r))
    store=(req["availableCourses"])
    i=1
    name=[]
    id=[]
    for i in range(len(store)):
        print(i,store[i]["name"], end="--")
        print(store[i]["id"])
        name.append(store[i]["name"])
        id.append(store[i]["id"])
    print(" ")
    user=int(input("enter the course serial number.... "))       
request()













