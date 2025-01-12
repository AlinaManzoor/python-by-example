
people = int(input ("how many people the do you wants to invite to a party? " , ))

if people < 10:
    for i in range(0 , people):
        name = input("Enter the name : " , )
        print(name  , "has been invited")
else:
    print("Too many people")