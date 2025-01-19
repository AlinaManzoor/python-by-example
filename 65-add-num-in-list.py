num = []

for i in range(1 , 4):
    input_num = int(input(f"enter the number {i} in list : "  ,))
    num.append(input_num)

print(num)
input_suggest = input("Do you still want the last number they entered saved (y/n) : " , )
if input_suggest == "n":
   num.remove(input_num)
   print(num)
else:
    print("Thank you")
