# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()  # stores object a with values nr1 =22,dr1=7
b = Rat(9)  # stores object b with values nr1 =9,dr1=7
c = Rat(5,  8)  # stores object c with values nr1 =5,dr1=8
d = Rat(dr1 = 9) # stores object d with values nr1 =22,dr1=9
e = Rat(dr1 = 3 , nr1 = 2) # stores object e with values nr1 =2,dr1=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # stores object f with values nr1 =11,dr1=15
print('a  :  ' , a)  #  22/7
print('b  :  ' , b)  #  9/7
print('c  :  ' , c)  #  5/8
print('d  :  ' , d)  #  22/9
print('e  :  ' , e)  #  2/3
print('f  :  ' , f)  #  11/15
c . __init__()  #  # stores object c with values nr1 =22 ,dr1=7
print('c  :  ' , c) #  5/8
a . __init__(3.8  , 4.6)  # stores object a with values nr1 =3.8,dr1=4.6
print('a  :  ' , a)  #  3.8/4.6
g = Rat(nr1 = 9 , 5)  #  Error due to positional argument after keyword argument
h = Rat(nr = 9 , dr = 5)  # Error due to unexpected arguments nr,dr

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
a = Date(15 , 8 , 1947)  # stores object a with values dd1=15,mm1=8,yy1=1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)  # stores object a with values dd1=26,mm1=1,yy1=1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)  # stores object a with values dd1=19,mm1=7,yy1=1985
print('a  :  ' , a . __dict__)  # stores object a with values dd1=15,mm1=8,yy1=1947
print('b  :  ' , b . __dict__)  # stores object a with values dd1=26,mm1=1,yy1=1950
print('c  :  ' , c . __dict__)  # stores object a with values dd1=19,mm1=7,yy1=1985
d = Date()  #  Error due to requered 3 arguments
e = Date(dd = 30 , mm = 4 , yy = 2022)  #  Error due tp there sis no dd , mm,yy arguments
f = Date(dd1 = 26 , mm1 = 8 , 2023)  #  Error duee to positional argument after keyword argument



# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')  #  c1 class constructor
		return  25  #  Error due to __init__ should return None only
class  c2:
	def  __init__(self): 
		print('c2  class  constructor')  #  C2 class constructor
		return  None  
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()
b = c2()
print(b)  #  tYPE AND ADDRESS of object
print(b . __init__())  #  C2 class constructor  and returns none
c = c3()  #  c3 class constructor
print(c . __init__())  #  C3 class constructor



# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')  
		b = c1()  #  Error due to Unlimited Recursion 
# End  of  class
a = c1()


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
a = c1()  #  Constructor , stores x=10,y=20 in object a
print(a . __dict__)  #  {'x': 10, 'y': 20}
b = c2()  
print(b . __dict__)  # {}
b . init()  #  Method
print(b . __dict__)  #  {'x': 30, 'y': 40}


# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x.e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()  #  stores the a=10 at object x
print(x .__dict__)  # {a:10}
x . m1()  #  stores the b=10 at object x
print(x . __dict__)  # {a:10,b:20}
f1() #  stores c=30 in function f1
print(x . __dict__)  #  {a:10,b:20,c:30}
x . d = 40  #  stores the d=10 at object x
print(x . __dict__)  # {a:10,b:20,c:30,d:40}
y = c2()
y . m3() #  stores the e=50 at object x
print(x .__dict__)  # {a:10,b:20,c:30,d:40,e:50}
z = c1()   
print(z . __dict__)  #  {a:10}


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()  #  Stores the values x=10,y=20,z=30 in object a 
b = c1()  #  Stores the values x=10,y=20,z=30 in object b
print(a . __dict__)  #  {x:10,y:20,z:30}
print(b . __dict__)  #  {x:10,y:20,z:30}
del  a . x 
del  b . y
print(a . __dict__)  #  {y:20,z:30}
print(b . __dict__)  #  {x:10,z:30}
print(a . x)  #  Error due to x is not defined in a
print(b . y)  #  Error due to y is not defined in b



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()  #  #rd Constructor


#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #  Two  argument  constructor : 10 20
b = c1(30) #  error due to 2 arguments required
c = c1()  #  Error due to 2 arguments required


#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)  #  Two  argument  constructor : 10 20
b = c1(30)  #  Two  argument  constructor : 30 200
c = c1()  #  Two  argument  constructor : 100 200



# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1()  #  Constructor
print(a)  #  Tyep and address of class



# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()  #  Function
print(a)  #  None




# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()  #  Error due to no arguemnts
b = c1(25)  #  Function 25
print(b)  #  None



#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')
  
  
#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()  #  c1 class of prog9b



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()  #  c1  class  of  prog9a




#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c2  #   How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1()  #  How  to  create  c1  class  object  of  current  module
b=c2()  #  How  to  create  c1  class  object  of  prog9a



'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a   #  How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1()  #  How  to  create  c1  class  object  of  current  module
b=prog9a.c1()  #  How  to  create  c1  class  object  of  prog9a



# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10  #  How  to  initialize  public  variable  'x'  to  10
		self.__y=20  #  How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)  #  How  to  print   variable  'x'
		print(self.__y)  #  How  to  print  private  variable  'y'
		self.__m2()  #  How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)  #  How  to  print   variable  'x'
		print(self.__y)  #  How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)  #  How  to  print  variable  'x'
print(t._Test__y)  # How  to  print   variable  'y'
#print(t . __y)  #  error due to we cant access pvt variable directly
print(t . __dict__)  #  {'x': 10, '_Test__y': 20}
t.m1()  #  How  to  call  method  m1()
t._Test__m2()  #  How  to  call   method  m2()
#t . __m2()  #  error due to we cant access directly pvt method
print('End')



#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10  #  How  to  initialize  public  variable  'x'  with  10
		self.__x=20  #  How  to  initialize  private  variable  'x'  with  20
		self.__x__=20  #  How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)  #  How  to  print   variable  'x'
print(a.__x__)  #  How  to  print  public  dunder  variable  'x'
print(a._c1__x)  #  How  to  print   private  variable  'x'
print(a . __x)  #  error due to we cant access Pvt variable directly 
a.m1()  #  How  to  call  public  method  m1()
a.__m1__()  #  How  to  call  public  dunder  method  m1()
a._c1__m1()  #  How  to  call  private  method  m1()
a . __m1()  #  error due to we cant access Pvt method directly



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
a = c1()  # Object a is created and constructor is executed
a = None #  Destructor is executed
b = c1()  # Object b is created and constructor is executed
del    b  #  Object b is deleted before destructor is executed
c = c1()  # Object c is created and constructor is executed
c = c1()  # Object c is created and constructor is executed and destructor is executed to previos c object
d = c1()  # Object d is created and constructor is executed
e = c1()  # Object e is created and constructor is executed

#  Before program terminates the destructor is executed to c,d,e objects




# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)  #  destructor 25
#  Before program terminates destructor is executed in destructor call we not givened variable x



# Find  outputs (Home  work)S
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)  #  destructor 25
# Destructor 35


# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')  #  Destructor
			b = c1()  #  Error due to maximum Recursion
a = c1()



# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')  #Constructor
		del  self  #  Object deleted after destructor is executed
	def  __del__(self):
		print('destructor')  #  Destructor
		b = c1()  #  Error max recursion error
a = c1()



#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')  #  3rd destructor
# End  of  the  class
a = c1()



#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()  #  Constrcutor is executed 3 times
del   a  #  object a deleted after destructor execution
print('Hello')  #   Hello
del   b  #  object b deleted after destructor execution
print('Hi')  #  Hi
del   c  #  object c deleted after destructor execution
print('Bye')  #  Bye
d = c1()  #  Construstructor is executed
print('End')  #  End
#  Destructor is executed for d object





# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]  #  constructor is executed 3 times
del  list  # Destructor is executed 3 times



# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()  #  Object a is created
print(a . __del__())  #  Destructor is executd
print('Hello')  # Hello
del   a  #  Object a is deleted after destructor execution

