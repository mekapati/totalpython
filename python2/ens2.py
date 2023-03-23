class Student:
    __name = None
    __rollnumber = None

    def setName(self,name):
      self.__name=name

    def getName(self):
        return (self.__name)

    def setRollNumber(self,rollNumber):
        self.__rollNumber=rollNumber

    def getRollNumber(self):
        return (self.__rollNumber)

example = Student()
example.setName("Tom")        
print("Name:", example.getName())    
example.setRollNumber(456)
print("Roll Number:", example.getRollNumber())