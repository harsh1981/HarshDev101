import random

first_name = "Harsh"
surname = "Kumar"

print(globals())

def print_variable():
    random_number = random.randint(0,9)
    print(first_name)
    print(surname)
    print(random_number)
    print(locals())

print_variable()