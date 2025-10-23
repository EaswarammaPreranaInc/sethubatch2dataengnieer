#  Find  outputs  (Home  work)
class parent:
    def m1(self):
        print('Overridden  Method')     

class child(parent):
    def m1(self):
        print('Overriding  Method')     

# end of the class
x = parent()
x.m1()#  Overridden  Method
x = child()
x.m1()#Overriding  Method


# Find  outputs   (Home  work)
class parent:
    def m1(self):
        print('m1  method  of  parent  class')    
    def m2(self):
        print('m2  method  of  parent class')     

class child(parent):
    def m1(self):
        print('m1  method  of  child  class')      
    def m3(self):
        print('m3  method  of  child  class')      

# end of the class
x = parent()
x.m1()#  m1  method  of  parent  class
x.m2()#m2  method  of  parent  class                                     
x.m3()#  Error

x = child()
x.m1()#  m1  method  of  child  class
x.m2()#  m2  method  of  parent class
x.m3()# m3  method  of  child  class


# Find  outputs  (Home  work)
class parent:
    def marriage(self):
        print('Arranged Marriage')#  Arranged Marriage

    def property(self):
        print('One  Crore')                         

    def study(self):
        print('Studies only', end='\t')             

class child(parent):
    def marriage(self):
        print('Love Marriage')                     

    def study(self):
        super().study()# Calls parent’s study()
        print(' + Entertainment')                

# end of the class
c = child()
c.marriage()
c.property()
c.study()
'''
output:
Love Marriage
One  Crore
Studies only	 + Entertainment
'''


# Find  outputs  (Home  work)
class parent:
    def add(self, x, y):
        return x + y                                

class child(parent):
    def add(self, x, y, z):
        return x + y + z                            

# End of the class
c = child()
print(c.add(10, 20, 30))#  60
print(c.add(10, 20))#  Error 
print(super(child, c).add(40, 50))#  90


# Find  outputs  (Home  work)
class parent:
    def add(self, x, y):
        print('parent  method')# parent  method
        return x + y

class child(parent):
    def add(self, x, y, z = 3):# Default z = 3
        print('child  method')#child  method
        return x + y + z

# End of the class
c = child()
print(c.add(10, 20, 30))#child  method                   
print(c.add(10, 20))#child  method                      
                    
# Find  outputs  (Home  work)
class parent:
    def m1(self, a, b, /):
        print(f'parent  method  --->   a  :  {a}  \t  b  :  {b}')     

class child(parent):
    def m1(self, x, y):
        print(f'child  method  --->  x  :  {x}  \t  y  :  {y}')    

# End of the class
c = child()
c.m1(x = 10, y = 20)#  child  method  --->  x  :  10  	y  :  20
c.m1(30, 40)# child  method  --->  x  :  30  	y  :  40



# Find  outputs (Home  work)
from abc import *

class c1(ABC):
    @abstractmethod
    def m1(self):
        pass
    def __init__(self):
        print('c1  class  constructor')

class c2(ABC):
    def m1(self):
        pass
    def __init__(self):
        print('c2  class  constructor')

class c3:
    @abstractmethod
    def m1(self):
        pass
    def __init__(self):
        print('c3  class  constructor')

class c4(c1):
    def m1(self):
        pass
    def __init__(self):
        print('c4  class  constructor')

class c5(c1):
    def __init__(self):
        print('c1  class  constructor')  
# End of the class

c1()# Error 
c2()#  c2  class  constructor
c3()#  c3  class  constructor
c4()# c4  class  constructor
c5()#  Error 

'''
Write a program to determine area and perimeter of triangle, circle, rectangle and square
'''
import math
from abc import *
class shape(ABC):
    def get(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def peri(self):
        pass

    @abstractmethod
    def test(self):
        pass
class triangle(shape):
    def get(self):
        print('Enter 3 sides of triangle')
        self.a = float(input('Enter side a : '))
        self.b = float(input('Enter side b : '))
        self.c = float(input('Enter side c : '))

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c

    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass
        else:
            print('Not a triangle')
            exit()

class circle(shape):
    def get(self):
        print('Enter radius of circle : ', end='\t')
        self.a = float(input())

    def area(self):
        return 3.14159 * self.a ** 2

    def peri(self):
        return 2 * 3.14159 * self.a

    def test(self):
        if self.a < 0:
            print('Radius can not be -ve')
            exit()

class rectangle(shape):
    def get(self):
        print('Enter length and breadth of rectangle')
        self.a = float(input('Enter length : '))
        self.b = float(input('Enter breadth : '))

    def area(self):
        return self.a * self.b

    def peri(self):
        return 2 * (self.a + self.b)

    def test(self):
        if self.a == self.b:
            print('Not a rectangle (both sides equal)')
            exit()

class square(shape):
    def get(self):
        print('Enter any side of square : ', end='\t')
        self.a = float(input())

    def area(self):
        return self.a ** 2

    def peri(self):
        return 4 * self.a

    def test(self):
        pass
def menu():
    print('\n1. Triangle')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Exit')
# End of menu function
def operation(s):
    s.get()          # read inputs
    s.test()         # validate
    print('Area       :', s.area())
    print('Perimeter  :', s.peri())
# End of the function
while True:
    menu()
    ch = eval(input('Enter choice : '))
    match ch:
        case 1:
            operation(triangle())
        case 2:
            operation(circle())
        case 3:
            operation(rectangle())
        case 4:
            operation(square())
        case 5:
            print('Good Bye')
            break
        case _:
            print('Invalid choice')
# End of while loop
'''
output:
Triangle
Enter 3 sides of triangle
Enter side a : 3
Enter side b : 4
Enter side c : 5
Area       : 6.0
Perimeter  : 12.0

circle
Enter radius of circle : 	7
Area       : 153.93804
Perimeter  : 43.98226

rectangle
Enter length and breadth of rectangle
Enter length : 8
Enter breadth : 5
Area       : 40.0
Perimeter  : 26.0

square
Enter any side of square : 	6
Area       : 36.0
Perimeter  : 24.0

'''
# Find  outputs   (Home  work)
from abc import *
class parent(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass

class child(parent):
    def m1(self):
        print('m1  method  of  child  class')

class gc(child):
    def m2(self):
        print('m2  method  of    gc  class')

class ggc(gc):
    def m3(self):
        print('m3  method  of  ggc  class')

# End  of the class
a = ggc()
a.m1()#  m1  method  of  child  class
a.m2()#  m2  method  of    gc  class
a.m3()#  m3  method  of  ggc  class
parent()#  Error 
child()# Error 
gc()# Error
