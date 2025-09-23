# 1. Error Identification

## Block 1

class c1:
    def m1(self):
        pass
class c2:
    pass
class c3:
'''
output: The class 'c3' is incomplete. it lacks a body (at least 'pass' is required for an empty class).
'''




# 2. Find Outputs

## Block 2

class c1:
    pass
# End of the class
a = c1()
print(id(a))       # Output: some unique integer (memory address)
print(type(a))     # Output: <class '__main__.c1'>
print(a._dict_)    # Error: AttributeError; should be 'a.__dict__'
print(a)           # Output: <__main__.c1 object at ...>
del a
print(a)           # Error: NameError; 'a' is deleted
'''
Errors:  
   - `a._dict_` is incorrect (should be `a.__dict__`).
   - `print(a)` after `del a` causes NameError.
'''




## Block 3

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
a.m1()         # Output: '3rd method'
m1()           # Output: 'Function'
'''
-Only the last declared method (`m1`) is used due to overriding, so '3rd method' is printed when `a.m1()` is called.
'''





## Block 4

class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x, y):
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)   # Output: 'Two argument method : 10 20'
a.m1(30)       # Error: missing one argument, TypeError
a.m1()         # Error: missing two arguments, TypeError
'''
- Only the last defined method is available. Calls without required arguments cause errors.
'''





## Block 5

class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x = 1, y = 2):
        print('Two argument method :', x, y)
# End of class c1
a = c1()
a.m1(10, 20)   # Output: 'Two argument method : 10 20'
a.m1(30)       # Output: 'Two argument method : 30 2'
a.m1()         # Output: 'Two argument method : 1 2'
'''
- Default arguments are used for missing inputs; all calls will work.
'''





## Block 6

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
a.m1()         # Output: 'Method of third c1 class'
'''
- Each redefinition of c1 overwrites the previous one.
'''






## Block 7

class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    pass
a = c1()
a.m1()         # Error: AttributeError, since final c1 has no m1
'''
- The last c1 definition has no methods, so an error occurs when calling m1.
'''






## Block 8

class c1:
    pass
# End of class
a = c1()
print(a.__dict__)   # Output: {}
a.x = 10
print(a.__dict__)   # Output: {'x': 10}
a.y = 20
print(a.__dict__)   # Output: {'x': 10, 'y': 20}
a.x = 30
print(a.__dict__)   # Output: {'x': 30, 'y': 20}
a.y = 40
print(a.__dict__)   # Output: {'x': 30, 'y': 40}
del a.x
print(a.__dict__)   # Output: {'y': 40}
del a.y
print(a.__dict__)   # Output: {}
del a
print(a.__dict__)   # Error: NameError, 'a' is deleted




# 3. Triangle Program


import math
class Triangle:
    def get(self):
        self.a = float(input('Enter side a: '))
        self.b = float(input('Enter side b: '))
        self.c = float(input('Enter side c: '))
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass
        else:
            print('Not a triangle')
            exit()  # Stops execution (alternatively, use 'return' if not exiting)
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Area formula
    def peri(self):
        return self.a + self.b + self.c  # Perimeter formula

# End of class

t = Triangle()      # Create triangle class object
t.get()            # Read inputs into object
t.test()           # Test for valid triangle
print('Area :', t.area())           # Outputs area
print('Perimeter :', t.peri())      # Outputs perimeter
'''
# Sample output sides (example for inputs 3, 4, 5)
# Area : 6.0
# Perimeter : 12.0
'''
