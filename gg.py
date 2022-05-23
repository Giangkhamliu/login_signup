import json
import os
list,dic_out,user_details=[],{},{}
start=int(input("Enter 1 or 2. '1' for signup '2' for login:-"))
if start==1:
    username=input("Enter the Username:-").capitalize()
    print("Password should contain Upper,Small Letter, Special Character and number")
    password1=input("Enter your password :-")
    special="!@#$%^&*():,;"
    u,l,n,s=0,0,0,0
    for varify in password1:
        if (varify.isupper()):
            u+=1
        if (varify.islower()):
            l+=1
        if (varify.isnumeric()):
            n+=1
        if varify in special:
            s+=1
    if len(password1)>=6:
        if (u and l and s and n)>=1 and u+l+s+n==len(password1):
            password2=input("Enter to confirm your  password:-")
            if password1==password2:
                if (os.path.isfile("userdetails.json")):
                    file1=open("userdetails.json","r")
                    out_file=json.load(file1)
                    for i in out_file["User"]:
                        if i["Username"]==username :
                            print("This user already exist")
                            break
                    else:
                        d1,d2={},{}
                        d1["Username"]=username
                        d1["Password"] = password1
                        d2["Description"]=input("Introduce yourself: ")    
                        d2["Date of Birth"]=input("Enter your Date of Birth: " )
                        d2["Gender"]=input("Enter your Sex: ")  
                        d2["Hobbies"]=input("Enter your Hobbies: ")  
                        d2["Contact"]=input("Enter your Contact:-")
                        d2["Gmail"]=input("Enter your Gmail:-")
                        d1["Profile"]=d2
                        x=out_file["User"]
                        x.append(d1)
                        file2=open("userdetails.json","w+")
                        json.dump(out_file, file2,indent=4)
                        file2.close()
                        print("sign_up succesfully")
                else:
                    dic,list,d,d1={},[],{},{}
                    dic["Username"]=username
                    dic["Password"]=password1
                    d["Description"]=input("Introduce yourself: ")
                    d["Date of Birth"]=input("Enter your Date of Birth: ")
                    d["Gender"]=input("Enter your sex: ")
                    d["Hobbies"]=input("enter your Hobbies:  ")
                    d["Contact"]=input("Enter your Contact:-")
                    d["Gmail"]=input("Enter your Gmail:-")
                    dic["Profile"]=d
                    list.append(dic)
                    d1["User"]=list
                    f2=open("userdetails.json","w+")
                    json.dump(d1,f2 ,indent=4)
                    f2.close()
                    print("Signup Successful") 
            else:
                    print("Password1 and password2 should match")
        else:
            print("password must contain upper,lower,special and number") 
    else:
       print("password should be more than 5")
elif start==2:
    user_name=input("Enter your username:-").capitalize()
    log_in_password=input("Enter your Log in Password:-")
    with open("userdetails.json","r") as log_in:
        log_in_info=json.load(log_in)
        for output_data in log_in_info["User"]:
            if output_data["Username"] == user_name and output_data["Password"]==log_in_password:
                print(user_name,"You Logged In Succesfully")
                print("................")
                print("PERSONAL RECORD")
                print("................")
                print("Username",":",output_data["Username"])
                print("Gender",":",output_data["Profile"]["Gender"])
                print("Bio",":",output_data["Profile"]["Description"])
                print("Date of Birth",":",output_data["Profile"]["Date of Birth"])
                print("Hobbies",":",output_data["Profile"]["Hobbies"])
                print("Contact",":",output_data["Profile"]["Contact"])
                print("Email",":",output_data["Profile"]["Gmail"])
                break
            else:
                  print("Password or user name is not same")

