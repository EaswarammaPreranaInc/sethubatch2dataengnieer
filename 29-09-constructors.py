class Rat:
    def __init__(self, nr1=22, dr1=7):
        self.nr = nr1
        self.dr = dr1
    def __str__(self):
        return f'{self.nr} / {self.dr}'
a = Rat()        
b = Rat(9)      
c = Rat(5, 8)   
d = Rat(dr1=9)   
e = Rat(dr1=3, nr1=2) 
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x, y)    
print('a  :  ', a)  # 22 / 7
print('b  :  ', b)  # 9 / 7
print('c  :  ', c)  # 5 / 8
print('d  :  ', d)  # 22 / 9
print('e  :  ', e)  # 2 / 3
print('f  :  ', f)  # 11 / 15
c.__init__()       # reset to default nr=22, dr=7
print('c  :  ', c)  # 22 / 7
a.__init__(3.8, 4.6)  # update a
print('a  :  ', a)    # 3.8 / 4.6
 g = Rat(nr1=9, 5)  # Error: positional after keyword
 h = Rat(nr=9, dr=5) # Error: unexpected keyword arguments

class Date:
    def __init__(self, dd1, mm1, yy1):
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1
a = Date(15, 8, 1947)
b = Date(yy1=1950, mm1=1, dd1=26)
c = Date(mm1=7, dd1=19, yy1=1985)
print('a  :  ', a.__dict__)  # {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ', b.__dict__)  # {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ', c.__dict__)  # {'dd': 19, 'mm': 7, 'yy': 1985}
 d = Date() # Error: missing 3 required positional arguments
 e = Date(dd=30, mm=4, yy=2022)  # Error: unexpected keyword arguments
 f = Date(dd1=26, mm1=8, 2023)   # Error: positional argument after keyword argument

class c1:
    def __init__(self):
        print('c1  class constructor')  # c1  class constructor
        return 25   # Error: constructor con only returns None
class c2:
    def __init__(self):
        print('c2  class  constructor')  #  c2  class  constructor
        return None  # Valid but ignored
class c3:
    def __init__(self):
        print('c3  class  constructor')  #  c3  class  constructor
a = c1()          
b = c2()          
print(b)      #  <__main__.c2 object at 0x...>
print(b.__init__()) # c2  class  constructor
                              # None
c = c3()          
print(c.__init__()) # c3  class  constructor
                              #  None

class c1:
    def __init__(self):
        print('Constructor')
        b = c1()  # Creates a new object of c1 inside constructor → calls __init__ again
                  # This repeats indefinitely
a = c1()  # infinite recursion

class c1:
    def __init__(self):
        print('Constructor') # Constructor
        self.x = 10  # sets x=10
        self.y = 20  # sets y=20
class c2:
    def init(self):
        print('Method') # Method
        self.x = 30  # sets x=30
        self.y = 40  # sets y=40
a = c1()                   
print(a.__dict__)   # {'x': 10, 'y': 20}
b = c2()                   
print(b.__dict__)   # {}
b.init()                   
print(b.__dict__)   # {'x': 30, 'y': 40}

class c1:
    def __init__(self):
        self.a = 10
    def m1(self):
        self.b = 20
class c2:
    def m3(self):
        x.e = 50  # accesses the existing object x of c1
def f1():
    x.c = 30     # adds attribute 'c' to object x
x = c1()          # adds a=10
print(x.__dict__)  # {'a': 10}
x.m1()            # adds b=20
print(x.__dict__)  # {'a': 10, 'b': 20}
f1()              # adds c=30
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30}
x.d = 40          # adds d=40
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y.m3()            # adds e=50 to x
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()          # creates new object a=10
print(z.__dict__)  # {'a': 10}

class c1:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30
a = c1()           # x=10, y=20, z=30
b = c1()           # x=10, y=20, z=30
print(a.__dict__)  # {'x': 10, 'y': 20, 'z': 30}
print(b.__dict__)  # {'x': 10, 'y': 20, 'z': 30}
del a.x            # remove attribute x from a
del b.y            # remove attribute y from b
print(a.__dict__)  # {'y': 20, 'z': 30}
print(b.__dict__)  # {'x': 10, 'z': 30}
print(a.x)         # Error: AttributeError: 'c1' object has no attribute 'x'
print(b.y)         # Error: AttributeError: 'c1' object has no attribute 'y'

class c1:
    def __init__(self):
        print('1st  constructor') # discarded
    def __init__(self):
        print('2nd  constructor')  # discarded
    def __init__(self):
        print('3rd  constructor')   # recognized  
a = c1()   #  3rd  constructor

class c1:
    def __init__(self):
        print('No  argument  constructor') # discarded
    def __init__(self, x):
        print('single  argument  constructor :', x) # discarded
    def __init__(self, x, y):
        print('Two  argument  constructor :', x, y) # recognized
a = c1(10, 20)  # Two  argument  constructor : 10 20
b = c1(30)    # Error missing 1 required positional argument 'y'
c = c1()      # Error missing 2 required positional arguments 'x' and 'y' 

class c1:
    def __init__(self, x=100, y=200):
        print('Two  argument  constructor :', x, y)
a = c1(10, 20)  # Two  argument  constructor : 10 20
b = c1(30)       #  Two  argument  constructor : 30 200 (default y)
c = c1()           #  Two  argument  constructor : 100 200 100 (default x,y)

def f1():
    print('Function')
    return 25
class f1:
    def __init__(self):
        print('Constructor') # Constructor
a = f1()       # f1 now refers to the class, not the function 
print(a)       # <__main__.f1 object at 0x79……..>

class c1:
    def __init__(self):
        print('Constructor')
def c1():
    print('Function') # Function
a = c1()      # c1 now refers to the function 
print(a)      # no return statement so prints None

class c1:
    def __init__(self):
        print('Constructor')
def c1(x):
    print('Function :', x)

a = c1()   # Error: missing 1 required positional argument 'x'
b = c1(25)
print(b) #  Function : 25
#  None

from prog9a import c1
class c1:
    def __init__(self):
        print('c1 class of prog9b')  # c1 class of prog9b
a = c1()   # does not import c1

class c1:
    def __init__(self):
        print('c1 class of prog9c') # import overrides previous class definition
from prog9a import c1   
a = c1()   # c1 class of prog9a

from prog9a import c1 as c11
class c1:                            # local class c1
    def __init__(self):
        print('c1 class of prog9d')
a = c1()     # How  to  create  c1  class  object  of  current  module
b = c11()   # How  to  create  c1  class  object  of  prog9a

import prog9a  # How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a = c1()  # How  to  create  c1  class  object  of  current  module
b = prog9a.c1() #How  to  create  c1  class  object  of  prog9a

class  Test:
	def  _init_(self):
		self . x = 10 # How  to  initialize  public  variable  'x'  to  10
		self.__y = 20 # How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method') # m1 method
		print(self.x)  # How  to  print   variable  'x'
		print(self.__y)  # How  to  print  private  variable  'y'
		self.m2()  # How  to  call    private  method   m2()
		print('Back to m1 method')  # Back to m1 method
	def  __m2(self):
		print('__m2  method')  # __m2  method 
		print(self.x)  # How  to  print   variable  'x'
		print(self.__y)  # How  to  print  private  variable   'y' 
# End  of  the  class
t = Test()
print('Outside')  # Outside
print(t.x)  # How  to  print  variable  'x'
print(t.__y)  # How  to  print   variable  'y'
print(t ._Test__y) # Error private variable __y cannot be accessed directly 
print(t . __dict__) # {'x':10,’__y’:20} 
t.m1()             # How  to  call  method  m1()
t._Test__m2()  # How  to  call   method  m2()
# t.__m2()         # Error private method __m2 cannot be accessed directly
print('End')       # End

class c1:
    def __init__(self):
        self.x = 10         # How  to  initialize  public  variable  'x'  with  10
        self.__x = 20     # How  to  initialize  private  variable  'x'  with  20
        self._x = 30       # How  to  initialize  public  dunder  variable  'x'  with  30
    def m1(self):
        print('public method')  # public method
    def __m1(self):
        print('private method') # private method
    def _m1_(self):
        print('public Dunder method')  # public dunder-like method
# End of the class
a = c1()
print(a.x)           # How to print variable 'x'
print(a._x)          # How to print public dunder variable '_x'
print(a._c1__x)      # How to print private variable '__x'
print(a.__x)       # Error private variable __x cannot be accessed directly
a.m1()               # How to call public method m1()
a._m1_()             # How to call public dunder method _m1_()
a._c1__m1()          # How to call private method __m1()
# a.__m1()           # Error private method __m1 cannot be accessed directly

# Tricky program
# Find outputs
# Assume addresses: a=1000, b=2000, c=3000, d=4000, e=5000

class c1:
    def __init__(self):
        print('Object is created at address :', id(self))
    def __del__(self):
        print(f'Object at address {id(self)} is lost')
# End of the class
a = c1()       # Object is created at address : 1000
a = None       # Object at address 1000 is lost
b = c1()       # Object is created at address : 2000
del b          # Object at address 2000 is lost
c = c1()       # Object is created at address : 3000
c = c1()       # Object at address 3000 is lost
               # Object is created at address : 3000 (new object)
d = c1()       # Object is created at address : 4000
e = c1()       # Object is created at address : 5000

class c1:
    def __del__(self , x):   # Error: destructor __del__ cannot take extra arguments except self
        print('destructor : ' ,  x)
a = c1()
a.__del__(25)  # Error destructor should not be called explicitly and it accepts only self

class   c1:
def  _del_(self , x = 35):
		print('destructor : ' , x)  # destructor : 25
a = c1()
a . _del_(25)

class c1:
    def __del__(self):
        print('destructor')
        b = c1()   # Error: creating new object inside destructor causes recursion and memory issues
a = c1()   # Object created, destructor not called yet

class c1:
    def __init__(self):
        print('constructor') 
        # del self    # Error: cannot delete self inside constructor
    def __del__(self):
        print('destructor')
        # b = c1()    # Error: creating new object inside destructor causes recursion
a = c1()   # constructor destructor ………………………

class   c1:
	def  _del_(self):
		print('1st  destructor')  # discarded
	def  _del_(self):
		print('2nd  destructor')  # discarded
	def  _del_(self):
		print('3rd  destructor')  # recognized
# End  of  the  class
a = c1()  # 3rd  destructor

class c1:
    def __init__(self):
        print('Object is created at address :', id(self))
    def __del__(self):
        print(f'Object at address {id(self)} is lost')
# end of the class
c = b = a = c1()     # Object is created at address : <address>
del a                # No destructor yet, object still referenced by b and c
print('Hello')       # Hello
del b                # No destructor yet, object still referenced by c
print('Hi')          # Hi
del c                # Object at address <address> is lost → destructor called
print('Bye')         # Bye
d = c1()             # Object is created at address : <new_address>
print('End')         # End

class c1:
    def __init__(self):
        print('Object is created at address :', id(self))
    def __del__(self):
        print(f'Object at address {id(self)} is lost')
# End of the class
list = [c1(), c1(), c1()]   # Object is created at address : <addr1>
                             # Object is created at address : <addr2>
                             # Object is created at address : <addr3>
del list                     # Object at address <addr1> is lost
                             # Object at address <addr2> is lost
                             # Object at address <addr3> is lost

class c1:
    def __del__(self):
        print('destructor')
         return 25   # Error __del__ cannot return a value
a = c1()
a.__del__()  # Error __del__ should not be called manually
print('Hello')  # Hello
del a           # destructor called automatically → prints 'destructor'
