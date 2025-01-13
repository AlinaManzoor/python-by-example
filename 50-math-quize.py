import random

score = 0
i = 1 
while i <=5:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    ques = num1 + num2 
    ans = int(input(f"{i}) Addition of  {num1} + {num2}   : "))
    i += 1
    if ans == ques:
        score += 1 
print("the final score : " , score)