
password = input("Enter the password : " , )
password2 = input("Enter it again : " , )

if password == password2:
    print("Thank u")

elif password.lower() == password2.lower():
    print(" “They must be in the same case”  ")
else:
    print("Incorrect")
