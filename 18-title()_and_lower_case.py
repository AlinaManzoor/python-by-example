name = input("enter the name  : " , )

if len(name) <= 5:
    surname = input("enter surname : " , )
    print(name.title(), surname.title())

else:
    print(name.lower())
