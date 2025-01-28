
Info = {}
for i in range(1,5):
    name = input(f"{i}) Enter the name :" ,)
    age = int(input("Enter the age : " ,))
    print ("\n")
    Info[name] = {"Age" : age}

for name in Info:
     print((name) , Info[name] ["Age"]) 