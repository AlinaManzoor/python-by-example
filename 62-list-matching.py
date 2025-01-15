list = [543 , 987, 645 , 129]

for i in list:
    print(i)

input_response = int(input("Enter the 3-digit number: " , ))

if input_response in list :
    print(list.index(input_response))
else:
    print("“That is not in the list”. ")
