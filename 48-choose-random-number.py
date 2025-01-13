import random

rand = random.randint( 1 , 5)
num = int(input("Pick the number : " , ))

if num == rand:
    print("Well done")

elif num < rand:
    print("too low")
else:
    print("too high")

num2 = int(input("pick another num : " , ))

if num2 == rand:
    print("Correct")
else:
    print("You lose")