import json,os
main_dict,list,dic1,user_info={},[],{},{}
def sign_up():
    global username,password1
    username=input("Enter your Username:-")
    print("Password should be more than 5 letters and contain upper,lower,number and special character")
    password1=input("Enter your password:-")
    special="!@#$%^&*():.,;?"
    u,l,n,s=0,0,0,0
    for pas in password1:
        if pas.isupper():
            u+=1
        if pas.islower():
            l+=1
        if pas.isnumeric():
            n+=1
        if pas in special:
            s+=1
    if len(password1)>=6:
        if (u and l and n and s)>=1 and u+l+n+s==len(password1):
            password2=input("Enter to confirm your password:-")
            if password1==password2:
                if (os.path.isfile("log_signup.json")):
                    file1=open("log_signup.json","r")
                    out_file=json.load(file1)
                    for i in out_file["User"]:
                        if i["Username"]==username :
                            print("This user already exist")
                            break
                    else:
                        info()
                        x=out_file["User"]
                        x.append(dic1)
                        file2=open("log_signup.json","w+")
                        json.dump(out_file, file2,indent=4)
                        file2.close()
                else:
                    info()
                    list.append(dic1)
                    main_dict["User"]=list
                    f2=open("log_signup.json","w+")
                    json.dump(main_dict,f2 ,indent=4)
                    f2.close()
            else:
                print("Both password should match")
        else:
            print("Password must contain all characters and cases(upper,lower,number,special")
    else:
        print("Password must be more the five characters")
def log_in():
    user_name=input("Enter the username:-")
    user_password=input("Enter the Password:-")
    with open("log_signup.json","r") as log_in:
        login_info=json.load(log_in)
        for  out_data in login_info["User"]:
            if out_data["Username"]==user_name and out_data["Password"]==user_password:
                print(user_name.capitalize(),"You've login successfully:")
                print("-----------------")
                print("PERSONAL RECORD")
                print("-----------------")
                print("Username",":",out_data["Username"])
                print("Gender",":",out_data["Profile"]["Gender"])
                print("Bio",":",out_data["Profile"]["Description"])
                print("Date of Birth",":",out_data["Profile"]["Date Of Birth"])
                print("Hobbies",":",out_data["Profile"]["Hobbies"])
                print("Contact",":",out_data["Profile"]["Contact"])
                print("Email",":",out_data["Profile"]["Gmail"])
                break
            else:
                print("Password or Username is not same")
def info():
    print("sign_up succesfully")
    dic1["Username"]=username
    dic1["Password"]=password1
    user_info["Description"]=input("Enter your Description:-")
    user_info["Date Of Birth"]=input("Enter your Date Of Birth:-")
    user_info["Hobbies"]=input("Enter your Hobbies:-")
    user_info["Gender"]=input("Enter your Gender:-")
    user_info["Contact"]=input("Enter your Contact:-")
    user_info["Gmail"]=input("Enter your Gmail:-")
    dic1["Profile"]=user_info
def main():
    global choice
    print("Enter '1' or '2'")
    choice=int(input("'1' for sign_up '2' for log_in :-"))
    if choice==1:
        sign_up()
    elif choice==2:
        log_in()
    else:
        print("Invalid choice")
        print("Check the choice before you Enter")
main()
