
for i in range(0,3):
    input_response = input("Names of 3 people you want to invite to a party : " , )
    list = [input_response]

decision = input("Do you want to add another(y/n) : " , )
while decision == 'y': 
    list.append(input("Names of people you want to invite to a party : " , ))
    decision = input("Do you want to add another(y/n) : " , )
    i += 2

print("how many people you have invited to the party :" , i )
