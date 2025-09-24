class c1:
    def m1(self):
        pass
class c2:
    pass
class c3:# error due to indentation and no pass statement

# Find outputs (Home work)
class c1:
    pass

a = c1()
print(id(a))# prints id of object a
print(type(a))# <class '__main__.c1'>
print(a.__dict__)# {}
print(a)# <__main__.c1 object>
del a
print(a)# error a is deleted

def m1():
    print('Function')
class c1:
    def m1(self):
        print('1st method')
    def m1(self):
        print('2nd method')
    def m1(self):
        print('3rd method')


a = c1()
a.m1()# 3rd method
m1()# Function


class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x, y):
        print('Two argument method :', x, y)

a = c1()
a.m1(10, 20)# Two argument method : 10 20
a.m1(30)# error
a.m1()# error 


class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x=1, y=2):
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)# Two argument method : 10 20
a.m1(30)# Two argument method : 30 2
a.m1()# Two argument method : 1 2


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
a.m1()# Method of third c1 class

'
class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    pass
a = c1()
a.m1()# error c1 has no method m1


class c1:
    pass
# End of class
a = c1()
print(a.__dict__)# {}
a.x = 10
print(a.__dict__)# {'x': 10}
a.y = 20
print(a.__dict__)# {'x': 10, 'y': 20}
a.x = 30
print(a.__dict__)# {'x': 30, 'y': 20}
a.y = 40
print(a.__dict__)# {'x': 30, 'y': 40}
del a.x
print(a.__dict__)# {'y': 40}
del a.y
print(a.__dict__)# {}
del a
print(a.__dict__)# error a is deleted



import math

class triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            pass
        else:
            print('Not a triangle')
            exit()  

    def area(self):
        s = (self.a + self.b + self.c) / 2  
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c

# How to create triangle class object
t = triangle()
# How to read inputs into object
t.get()
# How to test whether inputs are valid
t.test()
print('Area :',  t.area())
print('Perimeter :', t.peri())
