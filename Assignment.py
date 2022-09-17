import re
import csv
print("*****Welcome to REGISTRATION|LOGIN portal****")


def register(user_input):
        if user_input == "Register":
            print("Welcome to Registration")
            print("NOTE: TO ENTER THE EMAIL ADDRESS","\n"
                  "Email adress should be in this format[ALPHABETS,NUMBERS@_____.____]",'\n'
                  "TO ENTER THE PASSWORD",'\n'
                  "Password must length must be in between[6-16]", "\n"
                  " Password should be having special characters","\n"
                  "Password sholud have the numeric value", "\n"
                  "Password should have uppercase & lowercase letters")
            email = input("Enter the Username/Email adress : ")
            confirm_email=input("Enter your email address to confirm :")
            reg = '[A-Za-z]+[0-9]+@[A-Za-z]+.[A-Z|a-z]{2,}'
            if(re.fullmatch(reg,email)):
                if (confirm_email == email):
                        print("Your Entered Email is correct and matches")
                        password=input("Enter your password : ")
                        confirm_password = input("Enter your password to confirm :")
                        if (re.match(r'[A-Za-z0-9~`!@#$%^&*+=_-]{6,16}', confirm_password)):
                            if (confirm_password == password):
                                        print("Password Entered is right")
                                        print("****Congratulations,You are registered*****")
                                        file = open("user_data.csv", "w", newline="\n")
                                        wo = csv.writer(file)
                                        wo.writerow(["USERNAME", "PASSWORD"])
                                        if True:
                                            data = [confirm_email, confirm_password]
                                            wo.writerow(data)
                                            file.close()

                        else:
                                print("Password entered is not correct/both passwords doesnot match")
                                print("Password must length must be in between[6-16]", "\n"
                                  " Password should be having special characters","\n"
                                  "Password sholud have the numeric value", "\n"
                                  "Password should have uppercase & lowercase letters")
                                print("Sorry!passwords didnot match , Register again")
                                user_input=input("Register|Login :")
                                begin(user_input)

            else:
                print("Invalid Email/Email doesnot matches,Register Again")
                user_input=input("Register|Login :")
                begin(user_input)
        else:
            user_input=input("Register|Login :")
            begin(user_input)

def Login(user_input):
    if user_input=="Login":
        print("Welcome to Login :")
        f1 = open("user_data.csv", "r")
        Email = input("Enter your email to Login : ")
        r = csv.reader(f1)
        flag=True
        for i in r:
            if i[0]==Email:
                password = input("Enter your password to login : ")
                if i[1] == password:
                    print("********Congratulations, you are logged in************* ","\n"
                          "*******************************************************")
                else:
                    print("Username/password doesn't matches,Register to login")
                    ask=input("Do you like to register|forgot password (register/forgot_password) :")
                    if ask == "register":
                        print("Welcome to registration")
                        user_input=input("Register|Login :")
                        register(user_input)
                    else:
                        search_email=input("Enter the email address which you have registered :")
                        if i[0]==search_email:
                              print("your password for the entered email is :",i[1])
                              flag=False
                        else:
                            password=input("Enter the new password :")
                            confirm_password=input("Enter the new password to confirm :")
                            if (re.match(r'[A-Za-z0-9~`!@#$%^&*+=_-]{6,16}', confirm_password)):
                                if (confirm_password == password):
                                    print("Password Entered is right")
                                    print("****Congratulations,You are registered*****")
                                    file = open("user_data.csv", "w", newline="\n")
                                    wo = csv.writer(file)
                                    wo.writerow(["USER NAME","PASSWORD"])
                                    if True:
                                        data=[search_email,confirm_password]
                                        wo.writerow(data)
                                        file.close()

                            else:
                                print("Password entered is not correct/both passwords doesnot match")
                                print("Password must length must be in between[6-16]", "\n"
                                      " Password should be having special characters","\n"
                                      "Password sholud have the numeric value", "\n"
                                      "Password should have uppercase & lowercase letters")
                                print("Sorry!passwords didnot match , Register again")
                                user_input=input("Register|Login")
                                register(user_input)

def begin(welcome):
    user_input=input("Register|Login :")
    if user_input=="Register":
        register(user_input)
    if user_input=="Login":
            Login(user_input)
    else:
        begin(user_input)

welcome=input("Enter whether to register or login (REGISTRATE|lOGIN) : ")
begin(welcome)
