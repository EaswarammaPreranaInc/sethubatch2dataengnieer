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
print('a  :  ' , a)
print('b  :  ' , b)
print('c  :  ' , c)
print('d  :  ' , d)
print('e  :  ' , e)
print('f  :  ' , f)
c . __init__()
print('c  :  ' , c)
a . __init__(3.8  , 4.6)
print('a  :  ' , a)
g = Rat(nr1 = 9 , 5)                           Error
h = Rat(nr = 9 , dr = 5)                       Error
Outputs:
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   11  /  15
c  :   22  /  7
a  :   3.8  /  4.6

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
print('a  :  ' , a . __dict__)                                         a :{'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . __dict__)                                         b :{'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . __dict__)                                         c :{'dd': 19, 'mm': 7, 'yy': 1985}
d = Date()                                                             Error
e = Date(dd = 30 , mm = 4 , yy = 2022)
f = Date(dd1 = 26 , mm1 = 8 , 2023)                                    Error

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
a = c1()                                                                Error
print(b)                                                                c1 class constructor
print(b . __init__())                                                   None
c = c3()                                                                Error 
print(c . __init__())

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()                                                           printing Constructor in infinite times 

#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')                                            Constructor
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')                                                 Method
        self . x = 30
        self . y = 40
a = c1()
print(a . __dict__)                                                    {'x':10,'y':20}
b = c2()
print(b . __dict__)                                                    {}
b . init()
print(b . __dict__)                                                    {'x':30,'y':40}

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
print(x . __dict__)                                                        {'a':10}
x . m1()
print(x . __dict__)                                                       {'a':10,'b':20}
f1()
print(x . __dict__)                                                       {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . __dict__)                                                       {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . __dict__)                                                       {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . __dict__)                                                       {'a': 10}

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)                                        {'x':10,'y':20,'z':30}
print(b . __dict__)                                        {'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . __dict__)                                        {'y': 20, 'z': 30}
print(b . __dict__)                                        {'x': 10, 'z': 30}
print(a . x)                                               Error 
print(b . y)                                               Error

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()                                                3rd constructor

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)                                           Two  argument  constructor :  10 20
b = c1(30)                                                Error due to one argument missing
c = c1()                                                  Error due to two argument missing

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')                                       Constructor
#end of the  class
a = f1()
print(a)                                                       type and address

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')                               Function
#end of the  class
a = c1()
print(a)                                          None

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()                                         Error
b = c1(25)
print(b)                                         Function: 25   None

#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')
Outputs:
c1  class  of  prog9a
Enter roll number: 101
Enter name of student: Jagannath
Enter m or f: m
Enter marks of 3 subjects :
Subject 1 : 75
Subject 2 : 64
Subject 3 : 82

Roll Number :  101
Student Name :  Jagannath
Gender :  m
Total Marks :  221
Average :  73.66666666666667
Grade :  Distinction
Roll: 101, Name: Jagannath, Gender: m, Total: 221, Average: 73.67, Grade: Distinction

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')                                                                          c1  class  of  prog9b
a = c1()

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()                                                                                                     c1  class  of  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a                                                                    from prog9a import c1 as c1_prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
How  to  create  c1  class  object  of  current  module                                                     a = c1()
How  to  create  c1  class  object  of  prog9a                                                              b = c1_prog9a()

''' 
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a                                                                                  import prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module                                                   a = c1()
How  to  create  c1  class  object  of  prog9a                                                            b = prog9a.c1()

# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		How  to  initialize  public  variable  'x'  to  10                                                           self.x = 10
		How  to  initialize  private  variable  'y'  to  20                                                          self.__y = 20
	def  m1(self):
		print('m1  method')
		How  to  print   variable  'x'                                                                               print("x =", self.x)
		How  to  print  private  variable  'y'                                                                       print("y =", self.__y)
		How  to  call    private  method   m2()                                                                      self.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x'                                                                              print("x =", self.x)
		How  to  print  private  variable   'y'                                                                     print("y =", self.__y)
# End  of  the  class
t = Test()
print('Outside')
How  to  print  variable  'x'                                                                                  print("x =", t.x)
How  to  print   variable  'y'                                                                                 print("y =", t._Test__y)
print(t . __y)                                                                                                 Error
print(t . __dict__)                                                                                            
How  to  call  method  m1()                                                                                    t.m1()
How  to  call   method  m2()                                                                                   t._Test__m2()
t . __m2()                                                                                                     Error
print('End')

#  Find  outputs
class  c1:
	def __init__(self):
		How  to  initialize  public  variable  'x'  with  10                                           self.x=10
		How  to  initialize  private  variable  'x'  with  20                                          self.__x=20
		How  to  initialize  public  dunder  variable  'x'  with  30                                   self.__x__=30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
How  to  print   variable  'x'                                                                   print(a.x)
How  to  print  public  dunder  variable  'x'                                                    print(a.__X__)
How  to  print   private  variable  'x'                                                          print(a._c1__x)
print(a . __x)                                                                                   Error
How  to  call  public  method  m1()                                                              a.m1()
How  to  call  public  dunder  method  m1()                                                      a.__m1__()
How  to  call  private  method  m1()                                                             a._c1__m1()
a . __m1()                                                                                       Error

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
a = c1()                                                                            Object  is  created  at  address  :  id(a)
a = None                                                                            Object  at  address id(a)  is  lost
b = c1()                                                                            Object  is  created  at  address  :  id(b)
del    b                                                                            Object  at  address  id(b) is  lost
c = c1()                                                                            Object  is  created  at  address  :   id(c)
c = c1()                                                                            Object  is  created  at  address  :   id(c)  Object  at  address  id(c)  is  lost
d = c1()                                                                            Object  is  created  at  address  :   id(d)
e = c1()                                                                            Object  is  created  at  address  :   id(e)

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)                                                   destructor :  25
a = c1()
a . __del__(25)

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)                                                                Error due to no arguments in destructor

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()                                                                      infinite destructor will print

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
Outputs:
constructor 
destructor will go on infinite print

#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()                                                                  destructor  3rd destructor

#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))                    Object  is  created  at  address  :   id(a)
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a                                                                         3rd destructor
print('Hello')                                                                  Hello
del   b
print('Hi')                                                                     Hi
del   c                                                                         Object  at  address  id(c)  is  lost 
print('Bye')                                                                    Bye
d = c1()                                                                        Object  is  created  at  address  :   id(d)    Object  at  address id(d)  is  lost
print('End')                                                                    End

# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
Outputs:
Object  is  created  at  address  :   id(c1)
Object  is  created  at  address  :   id(c1)
Object  is  created  at  address  :   id(c1)
Object  at  address  id(c1)  is  lost 
Object  at  address  id(c1)  is  lost 
Object  at  address  id(c1)  is  lost 

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')                                      destructor
		return  25
a = c1()
print(a . __del__())                                        25
print('Hello')                                              Hello
del   a                                                     destructor
