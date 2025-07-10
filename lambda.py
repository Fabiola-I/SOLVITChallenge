# Create Lambda function
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
n= int(input("Enter number to Square: "))
message= input("Enter your massage: ")
add= lambda a,b: a+b
print(add(a,b))
sqrt= lambda n : pow(n,2)
print(sqrt(n))
strin= lambda string: "a" in string
print(strin(message)) 

