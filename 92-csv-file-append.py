import csv

file = open("Book.csv" , "a")
title = input("Enter the title : ", )
author = input("Enter the author : ", )
year = input("Enter the year : ", )

new_recode = title ,"" , author , ""  , year, "\n"
file.write(str(new_recode))
file.close()

file = open("Book.csv" , "r")
for row in file:
    print(row)
file.close()