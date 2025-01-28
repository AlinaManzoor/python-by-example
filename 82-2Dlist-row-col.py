
list_2D = [[2,5,8] , [3,7,4] ,[1 ,6, 9] ,[4 ,2,0]]

row = int(input("Which row do you like to display : " , ))
print(list_2D [row])
col = int(input("which column in that row you want displayed  : " , ))
print(list_2D[row][col])

change = input("Do you want to change value y/n : "  ,)
if change == 'y':
    newValue = int(input("enter the new Value : " ,))
    list_2D[row][col] = newValue
    print (list_2D)

