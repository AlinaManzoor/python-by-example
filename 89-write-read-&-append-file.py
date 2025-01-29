file = open("Name.txt" , "a")

name = input("Enter the new name : " , )

file.write(name)

file = open("Name.txt" , "r")
print(file.read())

file.close()