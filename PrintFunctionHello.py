# Addition function
def add(x,y):
    value = x+y
    return value
a=add(2,3)    #Calling Add function
print (a)

# String function
def char(name):
    print(f"Hello,{name}")
char("Harsh")    #Calling Char function

#   Default Argument (String) below
def defaArgs(name="World"):
    print(f"Hello,{name}")
#If there is any value in defaArgs then it will print "Hello Deepti" otherwise it will print "Hello World"
defaArgs("Deepti") #Overriding default argument/function 

# Variable Length argument
def print_arg(*args):
    print(args)
print_arg(1,2)

# Variable Length argument with "FOR LOOP"
# if you use *args (normal agument with variable length argument)
def print_arg(*args):
    for arg in args:
        print(arg)
print_arg(1,2,3,4,5,6)


# variable-Length keyword Arguments similar to KeyValue argument but with variable length
# if you use **kwargs (** means dictionary agument (with pair value) then it will become variable length argument)
def print_kwarg(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
print_kwarg(Name="Deepti", Age=30, Gender="Female")

print_kwarg(Router="Cisco", IP="30.30.30.30", Type="Modulor", Software="IOS")


# Recursive function (function that call itself)
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
value = factorial(5)
print (value)