num = 10

while num >0 :
    print(" “There are ", num , "green bottles hanging on the wall")
    print(num , "green bottles hanging on the wall. ")
    print("And if 1 green bottle should accidentally fall")
    num = num-1

    ans  = int(input("“how many green bottles will be hanging on the wall?” : "))

    if ans == num:
        print("“There will be " , num1, " green bottles hanging on the wall”")

    else :
        while ans != num:
            ans = int(input("“No, try again” : " , ))
print("“how many green bottles will be hanging on the wall?”")
