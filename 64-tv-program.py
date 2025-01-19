TV_Programmes = ["Breaking Bad" , "Stranger Things" , "The Crown" , "Friends" , "Planet Earth "]

for i in TV_Programmes :
    print(i)

input_response = input("Do you to enter another show : " , )
position = int(input("Enter the position : " , ))

print(TV_Programmes.insert(position , input_response))
print(TV_Programmes)
