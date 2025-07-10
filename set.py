#  Set Exercise: 
#    - Write a Python program that creates two sets of numbers, one for odd numbers from 1 
# to 10 and one for even numbers from 1 to 10. 
#    - Use set operations to find the union, intersection, and difference between the two sets. 
#    - Display the results. 
even_number=set(range(0,10,2))
odd_number=set(range(1,10,2))
print("even numbers are {}".format(even_number))
print("odd numbers are {}".format(odd_number))
union_set=even_number|odd_number
print("union  set {}".format(union_set))
intersection_set=even_number&odd_number
print("intersection set {}".format(intersection_set))
difference_set=even_number-odd_number
print("difference of set {}".format(difference_set))