#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')  #  Overridden Method
class  child(parent):
	def  m1(self):
		print('Overriding  Method')  #  Overriding Method
#end of the class
x = parent()
x . m1()
x = child()
x . m1()



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
#x . m3()  #  Error due to no m3 method in parent class
x = child()
x . m1()
x . m2()
x . m3()

'''
m1  method  of  parent  class
m2  method  of  parent class
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
Studies only	 + Entertainment
'''



# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30))  #  60
#print(c . add(10 , 20))  #  Error
print(super(child , c) . add(40,50))  #  90



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
print(c . add(10 , 20 , 30))  #  60
print(c . add(10 , 20))  #  33


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
hild  method  --->  x  :  10  	  y  :  20
child  method  --->  x  :  30  	  y  :  40
'''


# Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(slef):
		print('c1  class  constructor')
# End  of  the  class
c1()  #  Error
c2()  #  c2 class constructor
c3()  #  c3 class constructor
c4()  #  c4 class constructor
c5()  #  Error



'''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  ---> sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  ---> a * b  where  'a'  is  length and  'b'  is  breadth
     What  is  the  perimter  of  rectangle ?  --->2 * (a + b)

5) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square  ?  ---> 4 * a
'''
import math
from abc import *

class shape(ABC):
    def get(self):
        self.a = float(input("Enter a value: "))   # Read value of 'a'

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
        self.a = float(input("Enter a value (a): "))
        self.b = float(input("Enter b value: "))
        self.c = float(input("Enter c value: "))  # Read the 3 sides of triangle

    def area(self):
        self.s = (self.a + self.b + self.c) / 2
        return "Area of triangle: ", math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))

    def peri(self):
        return "Perimeter of triangle: ", self.a + self.b + self.c

    def test(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            pass
        else:
            print('Not a triangle')
            exit()  # Stop execution


class circle(shape):
    def get(self):
        print('Enter radius of circle: ', end='\t')
        super().get()  # Read radius

    def area(self):
        return "Area of circle: ", (22 / 7) * self.a * self.a

    def peri(self):
        return "Circumference of circle: ", 2 * (22 / 7) * self.a

    def test(self):
        if self.a < 0:
            print('Radius cannot be negative')
            exit()  # Stop execution
class rectangle(shape):
    def get(self):
        print('Enter length and breadth of rectangle')
        self.l = float(input("Enter length: "))
        self.b = float(input("Enter breadth: "))  # Read length and breadth

    def area(self):
        return "Area of rectangle: ", self.l * self.b

    def peri(self):
        return "Perimeter of rectangle: ", 2 * (self.l + self.b)

    def test(self):
        if self.l == self.b:  # length and breadth same
            print('Not a rectangle')
            exit()  # Stop execution
class square(shape):
    def get(self):
        print('Enter any side of square: ', end='\t')
        super().get()  # Read the side

    def area(self):
        return "Area of square: ", self.a * self.a

    def peri(self):
        return "Perimeter of square: ", 4 * self.a

    def test(self):
        if self.a < 0:
            print("Side cannot be negative")
            exit()
def menu():
    print('\n1. Triangle')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Exit')
# End of menu function

def operation(s):
    s.get()     # Read inputs to object 's'
    s.test()    # Test inputs are valid or not
    print(*s.area())
    print(*s.peri())
# End of the function
while True:
    menu()
    ch = eval(input('Enter choice: '))
    match ch:
        case 1:
            operation(triangle())  # Call operation() function
        case 2:
            operation(circle())    # Call operation() function
        case 3:
            operation(rectangle()) # Call operation() function
        case 4:
            operation(square())    # Call operation() function
        case 5:
            exit()                 # Stop execution
# End of while loop
print("Good Bye")
