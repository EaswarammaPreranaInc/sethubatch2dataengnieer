
# Identify error (Home work)
class c1:
    def m1(self):
        pass
class c2:
    pass
class c3:  # error

# Find outputs (Home work)
class c1:
    pass
# End of the class
a = c1()
print(id(a))         # corresponding output
print(type(a))       # <class 'main.c1'>
print(a.dict)    # {}
print(a)             # <main.c1 object at ...>
del a
# print(a)           # error

# Find outputs (Home work)
def m1():
    print('Function')
class c1:
    def m1(self):
        print('1st method')
    def m1(self):
        print('2nd method')
    def m1(self):
        print('3rd method')
# End of class c1
a = c1()
a.m1()               # 3rd method
m1()                 # Function

# Find outputs (Home work)
class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x, y):
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)         # Two argument method : 10 20
# a.m1(30)           # error
# a.m1()             # error

# Find outputs (Home work)
class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x=1, y=2):
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)         # Two argument method : 10 20
a.m1(30)             # Two argument method : 30 2
a.m1()               # Two argument method : 1 2

# Find outputs (Home work)
class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    def m1(self):
        print('Method of third c1 class')
a = c1()
a.m1()               # Method of third c1 class

# Find outputs (Home work)
class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    pass
a = c1()
# a.m1()             # error

# Find outputs (Home work)
class c1:
    pass
# End of class
a = c1()
print(a.dict)    # {}
a.x = 10
print(a.dict)    # {'x': 10}
a.y = 20
print(a.dict)    # {'x': 10, 'y': 20}
a.x = 30
print(a.dict)    # {'x': 30, 'y': 20}
a.y = 40
print(a.dict)    # {'x': 30, 'y': 40}
del a.x
print(a.dict)    # {'y': 40}
del a.y
print(a.dict)    # {}
del a
# print(a.dict)   # error

# Triangle class program (Home work)
import math
class triangle:
    def get(self):
        self.a = float(input('Enter side a: '))
        self.b = float(input('Enter side b: '))
        self.c = float(input('Enter side c: '))
    def test(self):
        if (self.a + self.b >= self.c) and (self.b + self.c >= self.a) and (self.c + self.a >= self.b):
            pass
        else:
            print('Not a triangle')
            exit()  # stop execution
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
# End of the class

t = triangle()       # create object
t.get()              # read inputs
t.test()             # validate triangle
print('Area :', t.area())       # corresponding output
print('Perimeter :', t.peri())  # corresponding output
