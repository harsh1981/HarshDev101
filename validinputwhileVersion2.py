
while True:
    user_input = input('Please Enter a number or Type quit to exit:')
    if user_input == "quit":
        break
    elif user_input.isdigit():
        print("You entered:", user_input)    
    else:
        print("Invalid input, Please try again")
        break
