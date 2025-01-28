from array import *

nums = array ('f' ,[20.22 , 40.44, 60.66 , 80.88 , 100.11])
print(nums)
input_response = int(input("enter the num : " ,))

while input_response <=2 or input_response >=5:
    print("Try again")
    input_response = int(input("enter the num : " ,))
for i in nums:
    x = i/input_response
    print(round(2,x))
