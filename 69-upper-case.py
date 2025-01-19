word = input("Type in a word in upper case : " ,)
for letter in word : 
    if word != letter.isupper():
        print("Try again")
        word = input("Type in a word in upper case : " ,)
    else:
        (word)
