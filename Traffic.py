# traffic light control
# Current_status=input("Enter the color of ON LED")
# Current_statuslow= Current_status.lower()
# if Current_statuslow=='red':
#     print("Stop your are not allowed moving the color is:",Current_statuslow)
# elif Current_statuslow=='yellow':
#     print("Waiting for the clearance the color is:",Current_statuslow)
# elif Current_statuslow== 'green':
#     print("Dear pedistrian you are free to navigate the color is:", Current_statuslow)
# else:
#     print("The LED color not exixt in our system") 
print("Welcome to our Traffic light system")
choices=["1.Red","2.yellow","3.green","None!"]
for choice in choices:
    print(choice)
user_input= input("Enter the color of ON LED: ")
choose=user_input.lower()
match choose:
    case 1:
        print("Wait there is danger: ")
    case 2:
        print("we are clearing:")
    case 3:
        print("you are free to go: ")
    case 4:
        print("Not included in our system!")
                

    

  
