global_variable="global"

def add (num1,num2):
    nested_value = "Inside function"
    print(num1+num2)
    print(locals())

print(locals())   #here if you print (locals) outside the def add function then Global will be printed as locals
add (20, 35)