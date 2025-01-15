subject = ["English" , "Urdu" ,  " Math" , "Science" , "General Knowledge"]
print(subject)

input_response = input("which of these subjects they don’t like: ",)
index = subject.index(input_response)
del subject[index]

print(subject)