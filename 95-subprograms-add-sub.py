import random

def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1 , " + " , num2 , " = " )
    user_answer= int(input( "Your answer : "  ))
    actual_answer = num1 + num2
    answer = (user_answer , actual_answer)
    return answer
    

def minus():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    print(num1 , " - " , num2 , " = " )
    user_answer= int(input( "Your answer : "  ))
    actual_answer = num1 - num2
    answer = (user_answer , actual_answer)
    return answer

def compare(user_answer , actual_answer): 
    if user_answer == actual_answer:
         print("Correct")
    else:
       print("Incorrect the correct answer is : " , actual_answer)

def main():
    print("1) Addition \n 2) Subtraction")
    num = int(input("Enter the 1 or 2 : " , ))

    if num == 1:
        user_answer,actual_answer = addition()
        compare(user_answer , actual_answer)

    elif num == 2:
        user_answer,actual_answer = minus()
        compare(user_answer , actual_answer)
    else:
         print("Incorrect selection")
main()