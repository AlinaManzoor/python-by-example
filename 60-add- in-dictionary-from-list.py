# index number is not available in dictionary

food_dictionary = {}

for i in range (1,6):
    food = input(f"Enter the fruit {i} : " , )
    food_dictionary[i] = food

print(food_dictionary)
dislike = input("enter the dislike fruit number from list : ",) 
del food_dictionary[dislike]
print(food_dictionary)




