# Ramu(22-10)


#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1() 
x = child()
x . m1()
'''
Overridden  Method
Overriding  Method
'''

# Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
#end of the class
x = parent()
x . m1()
x . m2()
x . m3()
x = child()
x . m1()
x . m2()
x . m3()
'''
m1  method  of  parent  class
m2  method  of  parent class
Error there is no m3  method  in  parent  class
m1  method  of  child  class
m2  method  of  parent class
m3  method  of  child  class
'''


# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()
		print(' + Entertainment')
#end of the class
c = child()
c . marriage()
c . property()
c . study()
'''
Love Marriage
One  Crore
Studies only  + Entertainment
'''


class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30)) #60
print(c . add(10 , 20)) #Error add can take 3 positional arguments but you given 2
print(super(child , c) . add(40,50)) #90


# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
#End  of  the  class
c = child()
print(c . add(10 , 20 , 30)) 
print(c . add(10 , 20))
'''
child  method
60
child  method
33
'''


#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)
c . m1(30 , 40)
'''
child  method  --->  x  :  10   y  :  20
child  method  --->  x  :  30   y  :  40
'''


# Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  _init_(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  _init_(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  _init_(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  _init_(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  _init_(slef):
		print('c1  class  constructor')
# End  of  the  class
#c1() #Error
c2() 
c3()
c4()
#c5() #Error
'''
c2  class  constructor
c3  class  constructor
c4  class  constructor
'''

import math
from abc import *

class shape(ABC):
    def get(self):
        self.a = eval(input("Enter the a value :"))  # How to read value of 'a'

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
        super().get()
        self.b = eval(input("Enter the b value of Triangle :"))
        self.c = eval(input("Enter the c value of Triangle :"))
        print(self.a,self.b,self.c)
        # How to read the 3 sides of triangle

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return (self.a + self.b + self.c)

    def test(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            pass
        else:
            print('Not a triangle')
            exit()


class circle(shape):
    def get(self):
        print('Enter radius of circle: ')
        super().get()

    def area(self):
        return math.pi *self.a ** 2

    def peri(self):
        return 2 * math.pi *self.a

    def test(self):
        if self.a < 0:
            print('Radius can not be -ve')
            exit()


class rectangle(shape):
    def get(self):
        print('Enter length and breadth of rectangle')
        super().get()
        self.b = eval(input("Enter Breadth of Rectangle :"))

    def area(self):
        return self.a * self.b

    def peri(self):
        return 2 * (self.a + self.b)

    def test(self):
        if self.a == self.b:
            print('Not a rectangle')
            exit()


class square(shape):
    def get(self):
        print('Enter any side of square: ', end='\t')
        super().get()

    def area(self):
        return self.a * self.a

    def peri(self):
        return 4 * self.a

    def test(self):
        pass


def menu():
    print('1. Triangle')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Exit')
# End of menu function

t = triangle()
c = circle()
re = rectangle()
sq = square()


def operation(s):
    s.get()  # How to read inputs to object 's'
    s.test()  # to test inputs are valid (or) not
    print('Area  :  ', s.area())
    print('Perimeter  :  ', s.peri())
# End of the function


while True:
    menu()
    ch = eval(input('Enter choice: '))
    match ch:
        case 1:
            operation(t)
        case 2:
            operation(c)
        case 3:
            operation(re)
        case 4:
            operation(sq)
        case 5:
            exit()
    # End of match
# End of while loop

print('Good Bye')


# Find  outputs (Home  work)
from   abc    import    *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m1()
a . m2()
a . m3()
parent() #Error
child()# Error
gc() #Error
'''
m1  method  of  child  class
m2  method  of    gc  class
m3  method  of  ggc  class
'''