from array import *

Array = array('i' ,[ 1 ,2 ,3 ,4 , 5])
print(Array)
for i in Array:
    select = int(input("Select one number : " ,))
    if select == Array:
        print (Array.index(select))
    else:
        print("Try Again")
        
