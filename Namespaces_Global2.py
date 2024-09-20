print(globals())

global_variable = "global"

def print_global():
    global_variable = "nested global"
    nested_variable = "nested value"

print_global()   #it's a printing function but just a name

print(globals())        # Printing global variable after the change of value as "Nested" 
