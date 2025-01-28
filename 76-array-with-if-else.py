from array import *

list = array('i' , [])

for i in range (0 , 5):
    num = int(input("enter the value b/w 10 to 20: " , ))
    if num >= 10 and num <= 20:
        list.append(num)
    else:
        print(" “Outside the range”")

for x in list:
    print(x)
