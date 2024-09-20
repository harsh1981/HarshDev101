# Class is a collection of some methods/function or the arrtibutes
# Any function declared in side the class is a method
# Constructor Class defined below Constructor Class=Template of Object

#class FloWer:
#    x = "rose"

#y=FloWer()
#print(y.x)

class Plant:
   def __init__(self,name,color):
       self.name=name
       self.color=color


def __str__(self):
        return f"{self.name},{self.color}"
f1 = Plant("Mango","green")

# modify the value of variable
f1.color=("Yellow")

# delete the value of variable
del f1.name

print(f1.name)
print(f1.color)

print(f1)