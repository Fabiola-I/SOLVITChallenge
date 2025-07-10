# String Manipulation Exercise: 
#    - Write a Python program that asks the user to enter their full name. 
#    - Convert the input string to lowercase using the `lower()` method. 
#    - Split the lowercase string into a list of words using the `split()` method. 
#    - Count the number of words in the list. 
#    - Display the number of words and the list of words. 
full_name=input("Enter your full name")
lowername= full_name.lower()
split_name= lowername.split()
number_of_word=len(split_name)
print(lowername)
print(split_name)
print(number_of_word)


