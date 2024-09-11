# double any number hold by parameter

double=lambda x:x*2

result=double(25)
print(result)

# Sort tuple index value (0,1) 
# sorting based on number of expereince index value 1
students = [("Harsh",15), ("Deepti",10), ("Vishal",6)]
students.sort(key=lambda x:x[0])
print (students)

# sorting based on name index value 0
students.sort(key=lambda x:x[1])
print (students)