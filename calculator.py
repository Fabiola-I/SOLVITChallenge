# # calculator 
# num1= int(input("Enter first number:"))
# num2= int(input("Enter second number:"))
# operator= input("Enter the operator")
# def calculation():
    
#     if operator=="+":
#         return num1+num2
#     elif operator=="*":
#         return num1*num2
#     elif operator=="-":
#         return num1-num2
#     elif operator=="/":
#         if num2==0:
#             return "indeterminate form😂!"
#         else:
#             return num1/num2
#     else:
#         return " invalid Operator"
    
# print(calculation())
n=[ x for x in range(1,20) if x % 2==0]
squares= list(map(lambda x:x**2,n))
print(n)
print(squares)
    
    