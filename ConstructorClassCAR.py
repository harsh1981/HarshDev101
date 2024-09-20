# Class is a collection of some methods/function or the arrtibutes
# Any function declared in side the class is a method
# Constructor Class defined below Constructor Class=Template of Object
class car:
    def __init__(anything,name,brand):
        anything.name=name
        anything.brand=brand

    def MyFunction(self):
        print("This is a " + self.name + " " + self.brand)
        print("This is a " + self.brand)

#Below is Child Class (vehicle) that inherited the attribute from parent class
class vehicle(car):
        pass 

class newvehicle(car):
        def __init__(ilil, name, brand):
            car.__init__(ilil,name,brand)

        def NewFunction(newvehicle):
            print("This is a " + ilil.name + " " + ilil.brand)
            print("This is a " + ilil.brand)

MyCar = car("Toyota","Camry")
MyCar.MyFunction()

MyVehicle = vehicle("BMW", "X6")
MyVehicle.MyFunction()