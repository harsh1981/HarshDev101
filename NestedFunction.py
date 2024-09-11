# Defining the Inner function

def Outer_function():
    def Inner_function():
        print("This is a test Inner function")
    Inner_function()

Outer_function()




# Returning the inner function

def Outer_function():
    def Inner_function():
        print("This is a Innerrrrrrrrrr function")
    return Inner_function()
Outer_function()