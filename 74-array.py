from array import *

num = array("i" , [])
for i in range (0, 5):
    nums = int(input("Enter the integers : " , ))
    num.append(nums)

num = sorted(num)
print(num)
num.reverse()
print(num)

