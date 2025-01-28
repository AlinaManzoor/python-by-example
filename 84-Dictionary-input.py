
Info = {}
for i in range(1,5):
    name = input(f"{i}) Enter the name :" ,)
    age = int(input("Enter the age : " ,))
    Shoes= int(input("Enter the shoes size :" , ))
    print ("\n")
    Info[name] = {"Age" : age , "Shoe size" : Shoes}

ask = input("\n Enter the name : " ,)
print("\n",Info[ask]) 