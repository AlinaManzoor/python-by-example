compnum = 50
num = int(input("enter the value  :" , ))
count = 0
while num != compnum:
    if num < compnum:
        print("too low")
    else:
        print("too high")
    num = int(input("Another guess: " , ))
    count += 1
print("Well done, you took" , count, " attempts")
