# Any argument value reference inside the function will change outside the function 

def add_to_list(number,x):
    number.append(x)

mylist=[1,2,3,4]
add_to_list(mylist,5)
print(mylist)



# Any argument is passed by value then value will not change outside the function 

def square(x):
    x = x**2
    return x
re = 5
square(re)
print(re)