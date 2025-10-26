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
print('a  :  ' , a)#22/7
print('b  :  ' , b)#9/7
print('c  :  ' , c) #5/8
print('d  :  ' , d) #9/7
print('e  :  ' , e) #3/2
print('f  :  ' , f) # 11/15
c . __init__()
print('c  :  ' , c) #5/8
a . __init__(3.8  , 4.6) 
print('a  :  ' , a) #3.8/4.6
g = Rat(nr1 = 9 , 5) #error, no key word arg followed by positional arg is not allowed
h = Rat(nr = 9 , dr = 5) #error expected key word args are nr1 and dr1 not nr dr 

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
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__) #{'dd':15, 'mm':8,'yy':1947}
print('b  :  ' , b . __dict__) #{'dd':26, 'mm':1,'yy':1950}
print('c  :  ' , c . __dict__) #{'dd':19, 'mm':7,'yy':1985}
d = Date()
e = Date(dd = 30 , mm = 4 , yy = 2022) #{'dd':30, 'mm':4,'yy':2022}
f = Date(dd1 = 26 , mm1 = 8 , 2023) #key word followed by positional argument is not allowed

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
a = c1() #error, object will not be created since the constructor is returning a value
b = c2() #error, object will not be created since the constructor is returning a value
print(b)
print(b . __init__()) 
c = c3() #c3  class  constructor
print(c . __init__()) #c3  class  constructor None

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() #Constructor Constructor .... infinite recursion

#  Difference  between  init()    and  __init__()   methods (Home  work)
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
a = c1() #Constructor 
print(a . __dict__) #{'x':10,'y':20}
b = c2()#empty
print(b . __dict__) #{}
b . init()
print(b . __dict__)# Method {'x':30,'y':40}

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
print(x . __dict__) #{a:10}
x . m1() 
print(x . __dict__) #{a:10,b:20}
f1() 
print(x . __dict__) #{a:10,b:20,c:30}
x . d = 40
print(x . __dict__) #{a:10,b:20,c:30,d:40}
y = c2()
y . m3() 
print(x . __dict__) #{a:10,b:20,c:30,d:40,e:50}
z = c1()
print(z . __dict__) #{a:10}

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__) #{x:10,y:20,z:30}
print(b . __dict__) #{x:10,y:20,z:30}
del  a . x
del  b . y
print(a . __dict__) #{y:20,z:30}
print(b . __dict__) #{x:10,z:30}
print(a . x) #error there is no instance variable y in a  
print(b . y)#error no y in b 

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #3rd  constructor

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10 20
b = c1(30) #error expecting 1 more positional argument
c = c1()#error expecting 2 positional arguments

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() #Constructor
print(a) #type and address i.e, __main__.f1 address

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1() #Function
print(a)#None

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1() #error expecting 1 positional argument
b = c1(25)
print(b) #Function 25 None

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() #c1 class of prog9b

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
# How  to  import  class  c1  from  prog9a
from prog9a import c1 as c2
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
# How  to  create  c1  class  object  of  current  module
a=c1()
# How  to  create  c1  class  object  of  prog9a
b=c2()

# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10 #How  to  initialize  public  variable  'x'  to  10
		self.__y=20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)#How  to  print   variable  'x'
		print(self.y)#How  to  print  private  variable  'y'
		self.__m2() #How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) #How  to  print  variable  'x'
print(t._Test.__y)#How  to  print   variable  'y'
print(t . __y) #error y is not visible
print(t . __dict__) #{x:10,_Test__y:20}
t.m1() #How  to  call  method  m1() 
# How  to  call   method  m2()
t . __m2()
print('End')

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
a = c1() #Object  is  created  at  address  :1000
a = None  #Object  at  address  1000 is lost
b = c1() #object is created at address: 2000
del    b #object at adress 2000 is lost
c = c1() # object is created at address 3000
c = c1() #object is created at address 4000, object at 3000 is lost
d = c1() #object is created at address 5000, object at 4000 is lost
e = c1()#object is created at address 6000, object at 5000 is lost

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25) #syntactically no error but here even though __del __ is executed
#since it is a explicit call object is not deleted

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25) #destructor: 25

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()
#when this program termonates the object is deleted and new object is created this goes in
# infinite recursion 

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1() #constructor destructor .... inifinite times

#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() 
#when program is terminated 3rd destructor 

#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() #object is created at address 1000
del   a #object at 1000 is lost
print('Hello') #Hello
del   b #error there is no object at b 
print('Hi') #Hi
del   c #there is not object at c
print('Bye') #Bye
d = c1() #object is created at address 2000
print('End')
#object at 2000 is lost

# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()] 
#Object  is  created  at  address  : 1000, Object  is  created  at  address  :2000, Object  is  created  at  address  : 3000
del  list
#object at address 1000 is lost object at address 2000 is lost object at address 3000 is lost

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__()) #destructor 25
print('Hello') #Hello
del   a #destructor 