from abc import ABC, abstractmethod 

class polygon(ABC): 

    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(polygon):
    def _init_(self):
        pass
    def no_of_sides(self):
        print('I have 3 sides')

class Rectangle(polygon):
    def _init_(self):
        pass
    def no_of_sides(self):
        print('I have 4 sides')

obj1 = Triangle()
obj2 = Rectangle()
obj1.no_of_sides()
obj2.no_of_sides()
