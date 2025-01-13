num = int(input("enter the number b/w 10 to 20 : " , ))

while num < 10 or num > 20:
    if num < 10:
        print("too low")
        
    elif num > 20 : 
        print("too high ")
    num = int(input("try again : " , ))
print("thank u")

