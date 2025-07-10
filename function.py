number=int(input("Enter the number to factorize:"))
def factorial(number):
    if number==1:
        return 1
    elif number==0:
        return 1
    elif number>1:    
        return number * factorial(number-1)
    else:
        return"Invalid number😒"
print(factorial(number))