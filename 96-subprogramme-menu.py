def add_name():
    name = input("Enter the name  :" , )
    list_name.append(name)
    return list_name

def del_name():
    select_num = int(input("Select the number of name to  Delete   :" , ))
    del list_name[select_num]
    return list_name

def change_name():
    index = int(input("Enter the index no: that you want to change name : " ,))
    names = input("Enter the name : " ,)
    list_name.insert(index , names)
    return list_name

def view_all():
    print(list_name)
    return list_name

def main():
    again = "Y"
    while again == "y":
        print("1) Add the name...")
        print("2) Delete the name...")
        print("3) Change the name...")
        print("4) View all ...")
        print("5) Quit")

        num = int(input("What do you want to do : " , ))

        if num == 1:
            list_name = add_name()
        elif num ==2 :
            list_name = del_name()
        elif num == 3:
            list_name = change_name()
        elif num == 4:
            view_all()
        elif num == 5:
            again = "n"
        else:
            print("Incorrect")
        data = (list_name , again)
list_name = []
main()


