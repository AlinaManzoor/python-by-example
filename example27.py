import math
print(" 1) Square \n 2) Triangle")
num = int(input("enter the 1 or 2 : " ,))

if num == 1:
    len = int(input("enter the length of one side : " , ))
    area1 = len ** 2
    print("Area of square : " ,area1)
elif num ==2:
    base = int(input("enter the base of triangle : " , ))
    height = int(input("enter the hight of triangle : " , ))
    area2 = (base * height)/2
    print("area of triangle : " , area2)
else:
    print("not valid")
