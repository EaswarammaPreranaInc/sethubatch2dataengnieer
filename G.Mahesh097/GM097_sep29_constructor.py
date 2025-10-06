# 1) Find  outputs

class Rat:
    def __init__(self, nr1=22, dr1=7):
        self.nr = nr1
        self.dr = dr1
    def __str__(self):
        return f'{self.nr} / {self.dr}'
# end of the class

a = Rat()
b = Rat(9)
c = Rat(5, 8)
d = Rat(dr1=9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  	
y = eval(input('Enter Denominator  :  '))   
f = Rat(x , y)
print('a : ', a)   # 22 / 7
print('b : ', b)   # 9 / 7
print('c : ', c)   # 5 / 8
print('d : ', d)   # 22 / 9
print('e : ', e)   # 2 / 3
print('f : ', f)   # 11 / 15
c.__init__()
print('c : ', c)   # 22 / 7
a.__init__(3.8, 4.6)
print('a : ', a)    # 3.8 / 4.6
g = Rat(nr1=9, 5)   # error as positional argument follows after keyword argument
h = Rat(nr=9, dr=5) # error as unexpected keyword argument

''' 
Output:
Enter numerator  :  11
Enter Denominator  :  15
a :  22 / 7
b :  9 / 7
c :  5 / 8
d :  22 / 9
e :  2 / 3
f :  11 / 15
c :  22 / 7
a :  3.8 / 4.6
'''






# 2) Find  outputs (Home  work)

class Date:
    def __init__(self, dd1, mm1, yy1):
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1
# End of the class

a = Date(15, 8, 1947)
b = Date(yy1=1950, mm1=1, dd1=26)
c = Date(mm1=7, dd1=19, yy1=1985)
print('a : ', a.__dict__)  # {'dd': 15, 'mm': 8, 'yy': 1947}
print('b : ', b.__dict__)  # {'dd': 26, 'mm': 1, 'yy': 1950}
print('c : ', c.__dict__)  # {'dd': 19, 'mm': 7, 'yy': 1985}
d = Date()                     # error as missing 3 args
e = Date(dd=30, mm=4, yy=2022) # error as unexpected keyword arguments
f = Date(dd1=26, mm1=8, 2023)  # error as positional argument follows keyword

''' 
Output:
a :  {'dd': 15, 'mm': 8, 'yy': 1947}
b :  {'dd': 26, 'mm': 1, 'yy': 1950}
c :  {'dd': 19, 'mm': 7, 'yy': 1985}
'''






# 3) Find  outputs (Home  work)

class c1:
    def __init__(self):
        print('c1 class constructor')
        return 25
class c2:
    def __init__(self):
        print('c2 class constructor')
        return None
class c3:
    def __init__(self):
        print('c3 class constructor')

# a = c1()  # error as __init__ cannot return value
b = c2()     # c2 class constructor
print(b)     # <c2 object at <address of object b>>
print(b.__init__())  
c = c3()     # c3 class constructor
print(c.__init__())  

''' 
Output:
c2 class constructor
<c2 object at <address of object b>>
c2 class constructor
None
c3 class constructor
c3 class constructor
None
'''





# 4) Find  outputs (Home  work)

class c1:
    def _init_(self):
        print('Constructor')
        b = c1()  # infinite recursion
a = c1()  # error as it would cause infinite recursion





# 5) Difference between __init__ and init methods

class c1:
    def __init__(self):
        print('Constructor')
        self.x = 10
        self.y = 20
class c2:
    def init(self):
        print('Method')
        self.x = 30
        self.y = 40
a = c1()           # Constructor
print(a.__dict__)  # {'x': 10, 'y': 20}
b = c2()
print(b.__dict__)  # {}
b.init()           # Method
print(b.__dict__)  # {'x': 30, 'y': 40}

''' 
Output:
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}
'''






# 6) Find  outputs (Home  work)

class c1:
    def __init__(self):
        self.a = 10
    def m1(self):
        self.b = 20
class c2:
    def m3(self):
        x.e = 50
def f1():
    x.c = 30

x = c1()
print(x.__dict__)  # {'a': 10}
x.m1()
print(x.__dict__)  # {'a': 10, 'b': 20}
f1()
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30}
x.d = 40
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y.m3()
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z.__dict__)  # {'a': 10}

''' Output:
{'a': 10}
{'a': 10, 'b': 20}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
{'a': 10}
'''





# 7) Find  outputs (Home  work)

class c1:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30
a = c1()
b = c1()
print(a.__dict__)  # {'x': 10, 'y': 20, 'z': 30}
print(b.__dict__)  # {'x': 10, 'y': 20, 'z': 30}
del a.x
del b.y
print(a.__dict__)  # {'y': 20, 'z': 30}
print(b.__dict__)  # {'x': 10, 'z': 30}
print(a.x)  # error as a doesn't have variable x
print(b.y)  # error as b doesn't have variable y

''' Output:
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}
'''





# 8) Find  outputs (Home  work)

class c1:
    def __init__(self):
        print('1st constructor')
    def __init__(self):
        print('2nd constructor')
    def __init__(self):
        print('3rd constructor')
a = c1()  # 3rd constructor

''' Output:
3rd constructor
'''





# 9) Find  outputs  (Home  work)

class c1:
    def __init__(self):
        print('No argument constructor')
    def __init__(self, x):
        print('Single argument constructor:', x)
    def __init__(self, x, y):
        print('Two argument constructor:', x, y)
a = c1(10, 20)   # Two argument constructor: 10 20
b = c1(30)     # error as one argument is missing
c = c1()       # error as two arguments are missing

''' Output:
Two argument constructor: 10 20
'''





# 10) Find  outputs  (Home  work)

class c1:
    def __init__(self, x=100, y=200):
        print('Two argument constructor:', x, y)
a = c1(10, 20)  # Two argument constructor: 10 20
b = c1(30)      # Two argument constructor: 30 200
c = c1()        # Two argument constructor: 100 200

''' Output:
Two argument constructor: 10 20
Two argument constructor: 30 200
Two argument constructor: 100 200
'''





# 11) Function and class same name
# ================================
def f1():
    print('Function')
    return 25
class f1:
    def __init__(self):
        print('Constructor')
a = f1()   # Constructor
print(a)   # <__main__.f1 object at ...>

''' Output:
Constructor
<__main__.f1 object at 0x...>
'''





# 12) Find  outputs  (Home  work)

class c1:
    def __init__(self):
        print('Constructor')
def c1():
    print('Function')
a = c1()   # Function
print(a)   # None

''' Output:
Function
None
'''





# 13) Find  outputs  (Home  work)

class c1:
    def _init_(self):
        print('Constructor')
def c1(x):
    print('Function :', x)
# a = c1()   # error as c1 function expects one arument
b = c1(25)  # Function: 25
print(b)    # None

''' Output:
Function : 25
None
'''





# Save  the  program  in  prog9a.py  file

class c1:
    def __init__(self):
        print('c1 class of prog9a')





# 14) Find  outputs (Home  work)

from  prog9a  import  c1
class   c1:
	def __init__(self):
		print('c1  class  of  prog9b')
a = c1()                       
''' Output:
c1 class of prog9b
'''






# 15) Find  outputs (Home  work)
class   c1:
	def __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()                    

''' Output:
c1 class of prog9a
'''




# How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
# from prog9a import c1 as c11#How  to  import  class  c1  from  prog9a

class   c1:
	def __init__(self):
		print('c1  class  of  prog9d')
a = c1()                # How  to  create  c1  class  object  of  current  module
b = c11()               # How  to  create  c1  class  object  of  prog9a





# 16) Public  and  Private  members  demo  program

class  Test:
	def __init__(self):
		self.x = 10         # How to initialize public variable 'x' to 10
		self.__y = 20       # How to initialize private variable 'y' to 20
	def  m1(self):
		print('m1  method')
		print(self.x)          # How to print variable 'x'
		print(self.__y)        # How  to  print  private variable 'y'
		self.__m2()            # How  to  call  private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)           # How to print variable 'x'
		print(self.__y)         # How to print private variable 'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)                      # How  to  print  variable  'x'
print(t._Test__y)               # How  to  print   variable  'y'
print(t . __y)                  # error as private variable cannot be accessed directly outside class
print(t .__dict__)              # {'x': 10}
t.m1()                          # How  to  call  method  m1()
t._Test__m2()                   # How  to  call   method  m2()
t . __m2()                      # error as m2 can't be accessed directly outside class
print('End')

''' Output:
Outside
10
20
{'x': 10, '_Test__y': 20}
m1 method
10
20
__m2 method
10
20
Back to m1 method
__m2 method
10
20
'''





# 17) Find  outputs

class  c1:
	def __init__(self):
		self.x = 10         #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20       #How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30     #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)          #How  to  print   variable  'x'
print(a.__x__)      #How  to  print  public  dunder  variable  'x'
print(a._c1__x)     #How  to  print   private  variable  'x'
print(a . __x)      #Throws error as private variab;e can't be accessed directly outside class
a.m1()              #How  to  call  public  method  m1()
a.__m1__()          #How  to  call  public  dunder  method  m1()
a._c1__m1()         #How  to  call  private  method  m1()
a . __m1()          #Throws error as private method can't be accessed directly outside class

''' Output:
10
30
20
public method
public Dunder method
private method
'''





''' 18) Tricky  program
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class c1:
    def __init__(self):
        print('Object is created at address:', id(self))
    def __del__(self):
        print(f'Object at address {id(self)} is lost')

a = c1()
a = None
b = c1()
del b
c = c1()
c = c1()
d = c1()
e = c1()

''' Output (addresses assumed):
Object is created at address : 1000
Object at address 1000 is lost
Object is created at address : 2000
Object at address 2000 is lost
Object is created at address : 3000
Object is created at address : 4000
Object at address 3000 is lost
Object is created at address : 5000
Object is created at address : 6000
Object at address 4000 is lost
Object at address 5000 is lost
Object at address 6000 is lost
'''






# 19) Identify  Error (Home  work)

class c1:
    def __del__(self, x):
        print('destructor:', x)
a = c1()
a.__del__(25)  # destructor : 25, then Throws error as PVM tries to call dunder del implicitly but del expects one argument






# 20) Find  outputs (Home  work)

class c1:
    def __del__(self, x=35):
        print('destructor:', x)
a = c1()
a.__del__(25) 

''' Output:
destructor : 25
destructor : 35
'''





# 21) Find  outputs (Home  work)

class c1:
    def __init__(self):
        print('constructor')
        del self
    def __del__(self):
        print('destructor')
        b = c1()
a = c1()  # infinite recursion






# 22) Find  outputs (Home  work)

class c1:
    def __del__(self):
        print('1st destructor')
    def __del__(self):
        print('2nd destructor')
    def __del__(self):
        print('3rd destructor')
a = c1()

''' Output:
3rd destructor
'''





# 23) Find  outputs (Home  work)

class c1:
    def __init__(self):
        print('Object created at address:', id(self))
    def __del__(self):
        print(f'Object at address {id(self)} is lost')

c = b = a = c1()
del a
print('Hello')
del b
print('Hi')
del c
print('Bye')
d = c1()
print('End')

''' Output (addresses assume 1000, 2000):
Object created at address : 1000
Hello
Hi
Object at address 1000 is lost
Bye
Object created at address : 2000
End
Object at address 2000 is lost
'''





# 24) Find  outputs  (Home  work)

class c1:
    def __init__(self):
        print('Object is created at address:', id(self))
    def __del__(self):
        print(f'Object at address {id(self)} is lost')

list = [c1(), c1(), c1()]
del list

''' Output:
Object is created at address : 1000
Object is created at address : 2000
Object is created at address : 3000
Object at address 1000 is lost
Object at address 2000 is lost
Object at address 3000 is lost
'''







# 25)Find  outputs  (Home  work)

class c1:
    def __del__(self):
        print('destructor')
        return 25
a = c1()
print(a.__del__())  
print('Hello')
del a               

''' Output:
destructor
25
Hello
destructor
'''
