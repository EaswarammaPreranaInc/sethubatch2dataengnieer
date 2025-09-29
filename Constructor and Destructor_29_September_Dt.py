# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()
b = Rat(9)
c = Rat(5,  8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a) # a : 22/7
print('b  :  ' , b) # b : 9/7
print('c  :  ' , c) # c : 5/8
print('d  :  ' , d) # d : 22/9
print('e  :  ' , e) # e : 2/3
print('f  :  ' , f) # 11/15
c . __init__() 
print('c  :  ' , c) # c : 22/7
a . __init__(3.8  , 4.6)
print('a  :  ' , a) # a : 3.8/4.6
g = Rat(nr1 = 9 , 5) # error as KA is followed by PA
h = Rat(nr = 9 , dr = 5) # Error as there are no arguments nr and dr

'''
Object  'a'   --->  nr = 22 , dr = 7

Object  'b'   --->  nr = 9 , dr = 7
'''


# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) # date class object is created and constructor is executed
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26) # date class object is created and constructor is executed
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) # date class object is created and constructor is executed
print('a  :  ' , a . __dict__) # {'dd' : 19 , 'mm' : 8 , 'mm' : 1947}
print('b  :  ' , b . __dict__) # {'dd' : 26 , 'mm' : 1 , 'mm' : 1950}
print('c  :  ' , c . __dict__) # {'dd' : 19 , 'mm' : 7 , 'mm' : 1985} 
d = Date() # error as object is not created
e = Date(dd = 30 , mm = 4 , yy = 2022) # error as there are no arguments dd , mm , yy
f = Date(dd1 = 26 , mm1 = 8 , 2023) # error as ka is followed by pa



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
a = c1() # Error as object is not created as return type is integer
b = c2() 
print(b) # c2 class constructor <next line> type and address of the object
print(b . __init__()) # c2 class constructor <next line> none
c = c3() # c3 class constructor
print(c . __init__()) # c3 class constructor <next line> none


# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() # constructor infinite times


#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() # Constructor
print(a . _dict_) # {'x' : 10 , 'y' : 20}
b = c2() 
print(b . __dict__) # {}
b . init() # Method
print(b . __dict__) # {'x' : 30 , 'y' : 40} 


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
x = c1()
print(x . __dict__) # {'a' : 10}
x . m1()
print(x .__dict__) # {'a' : 10 , 'b' : 20}
f1()
print(x . __dict__) # {'a' : 10 , 'b' : 20 , 'c' : 30} 
x . d = 40
print(x . __dict__) # {'a' : 10 , 'b' : 20 , 'c' : 30 , 'd' : 40}
y = c2()
y . m3()
print(x . __dict__) # {'a' : 10 , 'b' : 20 , 'c' : 30 , 'd' : 40 , 'e' : 50} 
z = c1()
print(z . __dict__) # {'a' : 10}




# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__) # {'x' : 10 , 'y': 20 , 'z' : 30}
print(b . __dict__) # {'x' : 10 , 'y': 20 , 'z' : 30}
del  a . x
del  b . y
print(a . __dict__) # {'y': 20 , 'z' : 30}
print(b . __dict__) # {'x' : 10 , 'z' : 30}
print(a . x) # Error as variable x is deleted
print(b . y) # Error as variable y is deleted


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() # 3rd constructor



#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two argument constructor : 10 <space> 20
b = c1(30) # Error as 1 arg is missing
c = c1() # error as there are nno arguments


#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two argument constructor : 10 <space> 20
b = c1(30) # error as there is only 1 argument
c = c1() # error as there are no arguments




# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() # Constructor
print(a) # Type and address of the constructor object



# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1() # Function
print(a) # None



# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1() # Error as there is no argument passed for functiom
b = c1(25) # Function : 25
print(b) # None


#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # c2 class of prog 9b


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a import c1
a = c1() # c1 class of prog 9a


#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c11 # How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a = c1() # How  to  create  c1  class  object  of  current  module
b = c11() # How  to  create  c1  class  object  of  prog9a



'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a # How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a = c1() # How  to  create  c1  class  object  of  current  module
b = prog9a.c1() # How  to  create  c1  class  object  of  prog9a



# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self . x = 10 # How  to  initialize  public  variable  'x'  to  10
		self . y = 20 # How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.y) # How  to  print  private  variable  'y'
		self._Test__m2() # How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.y) # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) # How  to  print  variable  'x'
print(t.y) # How  to  print   variable  'y'
print(t . __y) # Error as private variable cannot be called outside
print(t . __dict__) # {'x' : 10 , 'y' : 20}
t . m1() # How  to  call  method  m1() 
t . m2() # How  to  call   method  m2()
t . __m2() # Eroor as private method cannot be called outside
print('End')

'''
Outside
10
20
{'x': 10, 'y': 20}
m1  method
10
20
__m2  method
10
20
Back to m1 method
__m2  method
10
20
End

'''




#  Find  outputs
class  c1:
	def __init__(self):
		self . x = 10 # How  to  initialize  public  variable  'x'  with  10
		self . __x = 20 # How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30 # How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # How  to  print   variable  'x'
print(a.__x__) # How  to  print  public  dunder  variable  'x'
print(a._c1__x) #  How  to  print   private  variable  'x'
print(a . __x) # Error as there is no variable __x in the current program
a . m1() # How  to  call  public  method  m1()
a . __m1__() # How  to  call  public  dunder  method  m1()
a._c1__m1() # How  to  call  private  method  m1()
a . __m1() # Error as there is no method in class c1

'''
10
30
20
public method
public Dunder method
private method

'''




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
a = c1() 
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()

'''
Object is created at address : 1000
Object at address 1000 is lost
Object is created at address : 2000
Object at address 2000 is lost
Object is created at address : 3000
Object is created at address : 3000
first c1 Object at address 3000 is lost
Object is created at address : 4000
Object is created at address : 5000
second c1 Object at address 3000 is lost
Object at address 3000 is lost : 4000
Object at address 4000 is lost : 4000

''' 



# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25) # Error as destructor does not have the arguments


# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25) 

'''
Destructor : 25
destructor : 35
'''



# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1() # Infinite destructor




# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()

'''
constructor 
destructor infinite times
'''


#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() # 3rd destructor


#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del a
print('Hello')
del b
print('Hi')
del c
print('Bye')
d = c1()
print('End')

'''
Object is created at address : address of the object a
Object is created at address : address of the object b
Object is created at address : address of the object c
Object at address address of a is lost
Hello
Object at address address of b is lost
Hi
Object at address address of c is lost
Bye
Object is created at addresss : address of object d
End
Object at address address of d is lost

''' 


# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list

'''
Object  is  created  at  address  : first c1 class object
Object  is  created  at  address  : second c1 class object
Object  is  created  at  address  : third c1 class object
Object  at  address  first c1 class object is  lost
Object  at  address  second c1 class object is  lost
Object  at  address  third c1 class object is  lost
'''



# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a

'''
destructor
25
Hello
destructor
'''
