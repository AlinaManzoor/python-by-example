
direction = input("which direction the user wants to count? (up or down) : " , )

if direction == "up":
    top_num = int(input("enter the top number: " ,))
    
    for i in range(1 , top_num+1):
        print(i)
elif direction == "down":
    num = int(input("enter the number below 20: " ,))
    for i in range(20 , num-1 , -1 ):
        print(i)
else:
    print("“I don’t understand")