word = input("Type in a word in upper case : " ,)
try_again = False

while try_again == False:

        if word.isupper():
           print("Thank u")
           try_again = True  
        else:
            print("Try Again")
            word = input("Enter the word in upper case : " ,)
