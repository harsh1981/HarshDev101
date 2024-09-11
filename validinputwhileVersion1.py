valid_input=False

while not valid_input:
    user_input = input("Please Enter a Number:")
    if user_input.isdigit():
        print("You entered:", user_input)
        valid_input=True
    else:
        print("Invalid input, Please try again")
