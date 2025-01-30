import random

def choose_num():
    high_num = int(input("Pick the high number: " ,))
    low_num = int(input("Pick the low number: " ,))
    comp_num = random.randrange(low_num, high_num)
    return comp_num

def instruction():
    print("“I am thinking of a number…......”")
    guess = int(input("Guess the number I am thinking of :  " ,))
    return guess

def compare(comp_num , guess):
    condition = False
    while condition == False:
        if comp_num == guess:
            print("“Correct, you win”")
            condition = True
        elif guess > comp_num:
            guess = int(input("Too High try again" ,))
        else:
            guess = int(input("Too Low try again" ,))
            
def main():
    comp_num = choose_num()
    guess = instruction()
    compare(comp_num , guess)
main()
            

