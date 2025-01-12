
total = 0 

for i in range( 0 , 5):
    num = int(input("enter the numbers : " , ))
    decision = input("Do you want that number included? (y/n): " , )
    if decision == "y":
        total = total + num
print(total) 
    