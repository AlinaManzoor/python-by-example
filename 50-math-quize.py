import random

def randomInt():
    return random.randint(1, 100)

score = 0
# Initialization, condition, increment
for i in range(1,6):
    num1 = randomInt()
    num2 = randomInt()
    userInput = int(input(f"{i}) Addition of  {num1} + {num2}   : "))
    ans = num1 + num2
    if userInput == ans:
        score += 1 
print("the final score : " , score)