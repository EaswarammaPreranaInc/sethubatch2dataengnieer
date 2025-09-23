
1. Identify Error

class c1:
    def m1(self):
        pass
class c2:
        pass
class c3:

####Error: class c3: has no body.
In Python, a class must have at least pass inside.




2. Object & Attributes

class c1:
    pass
a = c1()
print(id(a))       # memory address (unique each run)
print(type(a))     # <class '__main__.c1'>
print(a.__dict__)  # {} → empty dictionary (no attributes yet)
print(a)           # <__main__.c1 object at 0x...>
del a
print(a)           # Error → NameError: name 'a' is not defined



3. Multiple Methods with Same Name


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
a.m1()   # "3rd method" (latest definition overrides earlier ones)
m1()     # "Function"



4. Method Overloading Attempt

class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method:', x)
    def m1(self, x, y):
        print('Two argument method:', x, y)
a = c1()
a.m1(10, 20)   #  "Two argument method: 10 20"
a.m1(30)       #  TypeError: missing 1 required positional argument 'y'
a.m1()         #  TypeError: missing 2 required positional arguments

## Python does not support true method overloading. Only the last definition remains.

5. Using Default Arguments

class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method:', x)
    def m1(self, x=1, y=2):
        print('Two argument method:', x, y)
a = c1()
a.m1(10, 20)   # Two argument method: 10 20
a.m1(30)       # Two argument method: 30 2
a.m1()         # Two argument method: 1 2


6. Multiple Classes with Same Name

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
a.m1()   # "Method of third c1 class"



7. Last Class is Empty

class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    pass
a = c1()
a.m1()   #  AttributeError: 'c1' object has no attribute 'm1'



 8. Object Attribute Dictionary


class c1:
    pass
a = c1()
print(a.__dict__)   # {}
a.x = 10
print(a.__dict__)   # {'x': 10}
a.y = 20
print(a.__dict__)   # {'x': 10, 'y': 20}
a.x = 30
print(a.__dict__)   # {'x': 30, 'y': 20}
a.y = 40
print(a.__dict__)   # {'x': 30, 'y': 40}
del a.x
print(a.__dict__)   # {'y': 40}
del a.y
print(a.__dict__)   # {}
del a
print(a.__dict__)   #  NameError: name 'a' is not defined


9. Triangle Program


import math

class Triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            return True
        else:
            print("Not a triangle")
            exit()

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# === Main Program ===
t = Triangle()
t.get()
if t.test():
    print("Area:", t.area())
    print("Perimeter:", t.peri())




