
list_2D = [[2,5,8] , [3,7,4] ,[1 ,6, 9] ,[4 ,2,0]]
row = int(input("Which row do you like to display : " , ))
print(list_2D [row])

newValue = int(input("Enter the value : " ,))
list_2D[row].append(newValue)
print(list_2D)
