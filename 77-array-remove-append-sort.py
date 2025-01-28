from array import *

list1 = array ('i' , [])
list1
for i in range (0 ,5):
    num = int(input("enter the number : " , ))
    list1.append(num)
    
num = sorted(list1)
print(num)
select = int(input(" select one of the numbers from list1 :" , ))
list1.remove(select)
print(list1)



