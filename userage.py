#person 
#   - Write a Python program that prompts the user to enter their age. 
#    - Convert the user input to an integer using casting. 
#    - Calculate the user's birth year based on the current year (you can use the `datetime` 
# module for the current year). 
#    - Display the user's birth year.
import datetime 
age= int(input("Enter your age"))
current_date= datetime.datetime.now()
birth_year= current_date.year - age
print("Your birth year is: ", birth_year)
