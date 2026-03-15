a# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()   # creating rat class object and constructor called automatically
b = Rat(9)  # creating rat class object and constructor called automatically with nr1=9
c = Rat(5,  8) # creating rat class object and constructor called automatically with nr1=5 , dr1=8
d = Rat(dr1 = 9) # creating rat class object and constructor called automatically with dr1=9
e = Rat(dr1 = 3 , nr1 = 2) # creating rat class object and constructor called automatically with dr1=3 , nr1=2
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # creating rat class object and constructor called automatically with nr1=11 , dr1=15
print('a  :  ' , a) # calling  __str__  method  of  object  a and printing 22/7
print('b  :  ' , b) # calling  __str__  method  of  object  b and printing 9/7
print('c  :  ' , c) # calling  __str__  method  of  object  c and printing 5/8
print('d  :  ' , d) # calling  __str__  method  of  object  d and printing 22/9
print('e  :  ' , e) # calling  __str__  method  of  object  e and printing 2/3
print('f  :  ' , f) # calling  __str__  method  of  object  f and printing 11/15
c . __init__() # explicit call to constructor with default values
print('c  :  ' , c) # calling  __str__  method  of  object  c and printing 22/7
a . __init__(3.8  , 4.6) # explicit call to constructor with nr1=3.8 , dr1=4.6
print('a  :  ' , a) # calling  __str__  method  of  object  a and printing 3.8/4.6
g = Rat(nr1 = 9 , 5) # error as positional argument follows keyword argument
h = Rat(nr = 9 , dr = 5) # error as constructor arguments should be nr1 , dr1

'''
Object  'a'   --->  nr = 22 , dr = 7

Object  'b'   --->  nr = 9 , dr = 7
'''

# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) # creating  object  a  of  class  Date and  constructor is automatically executed
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26) # creating  object  b  of  class  Date and  constructor is automatically executed with named  parameters
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) # creating  object  c  of  class  Date and  constructor is automatically executed with named  parameters
print('a  :  ' , a . __dict__) # prints all instance variables of object a in dictionary format {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . __dict__) # prints all instance variables of object b in dictionary format {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . __dict__) # prints all instance variables of object c in dictionary format {'dd': 19, 'mm': 7, 'yy': 1985}
d = Date()  # error as arguments are missing
e = Date(dd = 30 , mm = 4 , yy = 2022) # error as the arguments are not matching with the constructor
f = Date(dd1 = 26 , mm1 = 8 , 2023) # error as the postional argument follows the keyword argument

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()   #  object creation fails as constructor is not returning None
b = c2()    # creating object of class c2 adn constructor is automatically executed
print(b)    # prints tyoe and address of object b
print(b . __init__())   # calling constructor explicitly with object b
c = c3()   # creating object of class c3 and constructor is automatically executed
print(c . __init__())  # calling constructor explicitly with object c which returns None

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()    # creating object b of class c1 and constructor is automatically executed so it is a recursion and prints constructor n times till memory is full
# End  of  class
a = c1()    # creating object a of class c1 adn constructor is automatically executed

#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):    # it is a constructor
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):    # it is a normal method
        print('Method')
        self . x = 30
        self . y = 40
a = c1()    # c1 class object and constructor is automatically executed
print(a . __dict__) # prints all instance variables of object a and values
b = c2() # creating c2 class object
print(b . __dict__)   # prints empty dictionary because init() method is not called
b . init() # calling init() method
print(b . __dict__)  # prints all instance variables of object b and values

# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()  # creating object x of class c1 and constuctor is executed
print(x . __dict__) # printing all members of object x a:10
x . m1() # calling method m1 of object x
print(x . __dict__) #printing all members a:10,b:20
f1()    # calling f1 function and inside adding variable c to object x
print(x .__dict__) #  printing all members a:10,b:20,c:30
x . d = 40 # adding variable d to object x with value 40
print(x . __dict__) #printing all members a:10,b:20,c:30,d:40
y = c2() # creating object y of class c2
y . m3() # calling method m3 of object y and inside adding variable e to object x
print(x .__dict__) #printing all members a:10,b:20,c:30,d:40,e:50
z = c1() # creating object z of class c1 and constructor is executed
print(z . __dict__) #printing all members of object z a:10

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()  # creating object a of class c1
b = c1() # creating object b of class c1
print(a . __dict__) # prints all instance variables of object a x:10 y:20 z:30
print(b . __dict__) # prints all instance variables of object b x:10 y:20 z:30
del  a . x # deletes instance variable x of object a
del  b . y # deletes instance variable y of object b
print(a . __dict__) # prints all instance variables of object a y:20 z:30
print(b . __dict__) # prints all instance variables of object b x:10 z:30
print(a . x) # error as there is instance variable x of object a is deleted
print(b . y) # error as there is instance variable y of object b is deleted


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()    # creating  object  a  of  class  c1 and last constructor  will  be  called ,prints '3rd  constructor' and remaining are dicarded


#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # creating  object  a  of  class  c1 and last constructor  will  be  called ,prints 'Two  argument  constructor : ' 10 20 and remaining are dicarded
b = c1(30) # error as 2nd argument constructor is not defined
c = c1() # error as no argument constructor is not defined

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() # we have the class created last so it will be called and function is ignored
 creates  object  a  of  class  f1 and contructor is automatically eexecuted
print(a) # prints  type and address  of  object  a

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')   # prints function
#end of the  class
a = c1()    # we have the function created last so it will be called and class is ignored
print(a)  # prints None because function c1 does not return anything


# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()     # we have the function created last so it will be called but it is expecting 1 argument so error
b = c1(25) # calling function c1 with argument 25 and none is returned to function call
print(b) # printing value returned by function call which is None

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # as c1 class of current prgm is latest created its object will be created and constructor of c1 class of current prgm will be executed


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() # as c1 is lastly imported from prog9a its c1 class object is created and constructor is called


#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c2  #How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a=c1()  #How  to  create  c1  class  object  of  current  module
b=c2()  #How  to  create  c1  class  object  of  prog9a

'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a   #How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1()  ##How  to  create  c1  class  object  of  current  module
b=prog9a.c1()  ##How  to  create  c1  class  object  of  prog9a

# Public  and  Private  members  demo  program
class Test:
    def __init__(self):
        self.x = 10        # How  to  initialize  public  variable  'x'  to  10
        self.__y = 20      # How  to  initialize  private  variable  'y'  to  20

    def m1(self):
        print('m1  method')
        print(self.x)            # How  to  print   variable  'x'
        print(self.__y)          # How  to  print  private  variable  'y'
        self.__m2()              # How  to  call    private  method   m2()
        print('Back to m1 method')

    def __m2(self):
        print('__m2  method')
        print(self.x)            # How  to  print   variable  'x'
        print(self.__y)          # How  to  print  private  variable   'y'
# End  of  the  class

t = Test()
print('Outside')
print(t.x)                # How  to  print  variable  'x'
# print(t.__y)            # Error (private), cannot access directly
print(t._Test__y)         # How  to  print  private  variable  'y'
print(t.__dict__)         # How  to  print all data members of object

t.m1()                    # How  to  call  method  m1()
# t.__m2()                # Error (private), cannot call directly
t._Test__m2()             # How  to  call   method  m2()
print('End')


#  Find  outputs
class c1:
    def __init__(self):
        self.x = 10        # How  to  initialize  public  variable  'x'  with  10
        self._x = 20       # How  to  initialize  private  variable  'x'  with  20
        self.__x = 30      # How  to  initialize  public  dunder  variable  'x'  with  30
    
    def m1(self):
        print('public method')

    def __m1(self):
        print('private method')

    def _m1_(self):
        print('public Dunder method')
# End of the class

a = c1()

print(a.x)           # How  to  print   variable  'x'
print(a._c1__x)      # How  to  print  public  dunder  variable  'x'
print(a._x)          # How  to  print   private  variable  'x'

a.m1()               # How  to  call  public  method  m1()
a._m1_()             # How  to  call  public  dunder  method  m1()
a._c1__m1()          # How  to  call  private  method  m1()


'''
Tricky  program
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1()    # creating  c1 class object a and calling  __init__ method
a = None   #  now reference a points to none object so object  at  address 1000  
            #  is  lost so as the ref is deleted the object is deleted before deletion destructor is exectued 
b = c1()    # creating  c1 class object b and calling  __init__ method
del    b   #  now reference b is deleted so object  at  address 2000  is  lost so as the ref is deleted the object is deleted before deletion destructor is exectued
c = c1()   # creating  c1 class object c and calling  __init__ method
c = c1() # now c1 points to new object so object  at  address 3000  is  lost so as the ref is deleted the object is deleted before deletion destructor is exectued
d = c1()  # creating  c1 class object d and calling  __init__ method
e = c1() # creating  c1 class object e and calling  __init__ method

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()    # Create  object  of  c1  class 
a . __del__(25)   #  error as destructor  takes  only  self  argument

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()    # c1 class  object  is  created
a . __del__(25)     # explicit  call  to  destructor with 25 as x
# before the prgm termination , destructor  is  called  implicitly with x as 35

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()   #  object  creation  before  the  termination  destructor  will  be  called and it is infinite recurssion
a = c1()    #  object  creation before the termination destructor  will  be  called


# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')    # constructor  is  called  when  object  is  created
		del  self  #  destructor  is  called  when  object  is  deleted
	def  __del__(self):
		print('destructor')  # destructor  is  called  when  object  is  deleted
		b = c1()    # c1 class  object  is  created  and  constructor  is  called   so infinit recursion
a = c1()    # c1 class  object  is  created  and  constructor  is  called

#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() #  object  creation and before prgm termination the last create destructor will be called and rest are ignored

#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()    # three references  to  the  same  object of c1 class so constructor  will  be  called  only  once
del   a     # one  reference  a is  deleted 
print('Hello') # prints Hello
del   b   # one  reference  b  is  deleted
print('Hi') # prints Hi
del   c  # last  reference  c  is  deleted  so  destructor  will  be  called
print('Bye') # prints Bye =
d = c1() # new  object  is  created  so  constructor  will  be  called
print('End') # prints End and program  ends so destructor  will  be  called

# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()] #  Create  three  objects and for the 1st object creation constructor is called three  times
del  list   #  Delete  the  list  reference variable  which  holds  three  object references so destructor is called three times

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1() # c1 class  object  is  created
print(a . __del__())  # explicit call  to  destructor but does not delete  the  object
print('Hello') #  print  statement
del   a #  implicit call  to  destructor and  object  is  deleted
