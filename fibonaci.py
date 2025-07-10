# fibonnaci series
number=int(input("Enter number you want: "))
def fibonaci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    elif number > 1:
        return fibonaci(number-1)+ fibonaci(number-2)
    else:
        return "invalid input😘"
print(fibonaci(number))
    

