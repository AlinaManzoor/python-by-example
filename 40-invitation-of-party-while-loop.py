#Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.
name = input("Tell the name which do you want to invite in party : ",)
print(name , " has now been invited")

count = 0
add = "y"
while add == "y":
    add = input("Do you want to invite somebody else (y/n) :" , )
    count  = count + 1
print("people they have coming to the party : " , count)


