# Identify  error
class c1:
	def  m1(self):
	pass
class c2:
    pass
class c3:
   # Error, there should one pass statement inside the class.

class c1:
    pass
# End of the class
a = c1()
print(id(a))  # prints memory address of object
print(type(a))  # <class '__main__.c1'>
print(a.__dict__)  # {}
print(a)  # <__main__.c1 object at memory_address>
del a  # deletes object a
print(a)  # Error: NameError, 'a' is deleted

def m1():
    print('Function')
class c1:
    def m1(self):                 # discarded
        print('1st  method')
    def m1(self):                 # discarded
        print('2nd  method')
    def m1(self):                 # recognized
        print('3rd  method')
# End of class c1
a = c1()
a.m1()   # 3rd  method
m1()     # Function

class c1:
    def m1(self):                      # discarded
        print('No argument method')
    def m1(self, x):                   # discarded
        print('Single argument method :', x)
    def m1(self, x, y):                # recognized
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)   # Two argument method : 10 20
a.m1(30)       # Error: missing 1 required positional argument 'y'
a.m1()         # Error: missing 2 required positional arguments 'x' and 'y'

class c1:
    def m1(self):                            # discarded
        print('No argument method')
    def m1(self, x):                         # discarded
        print('Single argument method :', x)
    def m1(self, x=1, y=2):                  # recognized
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)   # Two argument method : 10 20
a.m1(30)       # Two argument method : 30 2
a.m1()         # Two argument method : 1 2

class c1:
    def m1(self):     # discarded
        print('Method of first c1 class')
class c1:
    def m1(self):     # discarded
        print('Method of second c1 class')
class c1:
    def m1(self):     # recognized
        print('Method of third c1 class')
a = c1()
a.m1()    # Method of third c1 class

class c1:
    def m1(self):     # discarded
        print('Method of first c1 class')
class c1:
    def m1(self):     # discarded
        print('Method of second c1 class')
class c1:             # recognized
    pass
a = c1()
a.m1()    # Error: 'c1' object has no attribute 'm1'

class c1:
    pass
# End of class
a = c1()
print(a.__dict__)      # {}
a.x = 10
print(a.__dict__)      # {'x': 10}
a.y = 20
print(a.__dict__)      # {'x': 10, 'y': 20}
a.x = 30
print(a.__dict__)      # {'x': 30, 'y': 20}
a.y = 40
print(a.__dict__)      # {'x': 30, 'y': 40}
del a.x
print(a.__dict__)      # {'y': 40}
del a.y
print(a.__dict__)      # {}
del a
print(a.__dict__)      # Error: NameError, 'a' is deleted

q) Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))
2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2
3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
Ans) import math
import sys
class triangle:
    def get(self):
        self.x = int(input("Enter the first side : "))
        self.y = int(input("Enter the second side : "))
        self.z = int(input("Enter the third side : "))  # How to read three sides into object self
    def test(self):
        if (self.x + self.y) > self.z and (self.y + self.z) > self.x and (self.x + self.z) > self.y:  # sum of every 2 sides >= 3rd side
            pass  # Do nothing
        else:
            print('Not a triangle')
            sys.exit()  # How to stop execution
    def area(self):
        s = (self.x + self.y + self.z) / 2
        return math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))  # area of triangle
    def peri(self):
        return self.x + self.y + self.z  # perimeter of triangle
# End of the class
a = triangle()  # How to create triangle class object
a.get()  # How to read inputs into object
a.test()  # How to test whether inputs are valid
print('Area : ', a.area())           
print('Perimeter : ', a.peri())
