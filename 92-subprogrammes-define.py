# function

def num_function():

    num = int(input("Enter the number : "  ,))
    return num

def count_num(num):
    for i in range(0 , num):
        print(i)
        i += 1
    

def main():
    num = num_function()
    count_num(num)
    
main()
