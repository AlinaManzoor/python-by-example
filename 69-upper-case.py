word = input("Type in a word in upper case : " ,)
tryagain = False

while tryagain == False:

        if word.isupper():
           print("Thank u")
           tryagain = True  
        else:
            print("Try Again")
            word = input("Enter the word in upper case : " ,)
