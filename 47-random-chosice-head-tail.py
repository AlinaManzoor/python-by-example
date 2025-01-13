import random

choose = input("Head or Tails : " , )
random_choice = random.choice(["head" , "tails"])

if choose == random_choice:
    print("You win")
else:
    print("Bad luck")
    choose = input ("if the computer selected heads or tails (y/n) :" , )
    if choose == "y":
        choose = random.choice(["head" , "tails"])
        print(choose)