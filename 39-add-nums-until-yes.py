#Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total. 
num1 = int(input("enter the number: " , ))

total = num1 
again = "y"

while again == "y":
    num3 = int(input("enter the another number : " , ))
    total = total + num3
    again = input("Do you want to add another number? (y/n) : " , )
print("the total is : " , total)