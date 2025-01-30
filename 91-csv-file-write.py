import csv

file = open("Book.csv" , "w")
new_recode1 = "To Kill A Mockingbird \t Harper Lee  \t 1990\n"
file.write(str(new_recode1))

new_recode2 = "A Brief History of Time \t Stephen Hawking \t 1988 \n"
file.write(str(new_recode2))

new_recode3 = "he Great Gatsby \t F. Scott Fitzgerald \t 1922\n "
file.write(str(new_recode3))

new_recode4 = "The Man Who Mistook His Wife for a Hat \t  Oliver Sacks \t 1985\n"
file.write(str(new_recode4))

file.close()