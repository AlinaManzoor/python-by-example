print("1) Create a new file \n 2)Display the file \n 3)Add a new item to the file \n 4)Make a selection 1 ,2 or 3")

file = open("Subject.txt" , "w")
file.write("Math\n")
file.write("English\n")
file.write("Urdu\n")

num = int(input("Enter 1 , 2 or 3 : " ,))
if num < 1 or num >3:
    print("Incorrect")
if num == 1:
    file = open ("Subject.txt" , "w")
    sub = input("Enter the subject :" ,)
    file.write(sub)
    file.close()
if num == 2:
    file = open("Subject.txt" , "r")
    print(file.read())
if num == 3:
    file = open("Subject.txt" , "a")
    sub = input("Enter the subject :" ,)
    file.write(sub)
    file.close()
