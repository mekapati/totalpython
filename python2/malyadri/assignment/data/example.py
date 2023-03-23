class Try:

        def __init__(self,name,roll_no):
                self.name=name
                self.roll_no=roll_no
        def printvar(self,):
                print(f"Hello,this is first method, {self.name},{self.roll_no}")
                #return name
        def local_var_without_init(self,test,test2):
                #self.test=test
                #self.test2=test2
                print("This is second Method",test,test2)
class Try2:
        def __init__(self):
                pass

        @staticmethod
        def static_method_example():
                print("Hello !!!.....This is static method")
#obj=Try()
obj1=Try(name='malya', roll_no=420)
obj1.printvar()
obj1.local_var_without_init('hello','world')
obj2=Try2()
obj2.static_method_example()

#print(obj1.name)


class City:
        def __init__(self, city=None):
                self.city = city
        def __repr__(self):
                if self.city:  return self.city
                return ''
c = City('Nellore')
print(c)
c = City()
print(c)
