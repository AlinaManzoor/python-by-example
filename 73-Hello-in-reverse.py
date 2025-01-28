word = input("Enter the word : " , )
length = len(word)
num = 1

for i in word:
    position = length - num
    letter = word[position]
    print(letter)
    num += 1