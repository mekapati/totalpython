class Vehicle:  
    def display(self):  
        print("I am from the Vehicle Class")


class Car(Vehicle):  
   
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  
obj1.display()  