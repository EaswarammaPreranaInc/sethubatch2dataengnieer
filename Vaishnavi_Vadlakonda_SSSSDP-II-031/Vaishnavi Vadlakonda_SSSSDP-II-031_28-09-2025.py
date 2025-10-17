# Find  outputs
class  Rat:
	def __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def __str__(self):
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
g = Rat(nr1 = 9 , 5) # Error, cannot pass positional argument after keyword argument
h = Rat(nr = 9 , dr = 5) # Error because there are no argument names nr and dr in format header
'''
Object  'a'   --->  nr1 = 22 , dr1 = 7

Object  'b'   --->  nr1 = 9 , dr1 = 7


Outputs
Enter numerator  :  2
Enter Denominator  :  3
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   2  /  3
c  :   22  /  7
a  :   3.8  /  4.6
'''









# Find  outputs (Home  work)
class Date:
	def __init__(self , dd1 , mm1  , yy1):
		self . dd = dd1
		self . mm = mm1
		self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)
print('b  :  ' , b . __dict__)
print('c  :  ' , c . __dict__)
d = Date() # Error, it requires arguments
e = Date(dd = 30 , mm = 4 , yy = 2022) # Error, there are no arguments named dd, mm and yy in format header
f = Date(dd1 = 26 , mm1 =  8 , 2023) # Error, cannot pass keyword argument before positional argument
'''
Outputs
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
'''
		 







# Find  outputs (Home  work)
class c1:
	def __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1() # error, constructor cannot return non none
b = c2()
print(b)
print(b . __init__())
c = c3()
print(c.__init__())
'''
Outputs
c2  class  constructor
type and address of c2 class object
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None
'''
	  








# Find  outputs (Home  work)
class c1:
	def __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()
'''
Outputs
infinite recursion, recursion error
'''









#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def _init_(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() # x = 10, y = 20
print(a . _dict_) 
b = c2() # creates empty c2 class object
print(b . _dict_)
b . init()
print(b . _dict_)
'''
Outputs
Constructor
{'x' : 10, 'y' : 20}
{}
Method
{'x' : 30, 'y' : 40}
'''


	






# Find  outputs (Home  work)
class c1:
	def __init__(self):
		self . a = 10
	def m1(self):
		self . b = 20
#End  of  class  c1
class c2:
	def m3(self):
		x . e = 50
# End  of  class  c2
def f1():
	x . c = 30
#  End  of  function  f1
x = c1()
print(x . __dict__)
x . m1()
print(x . __dict__)
f1()
print(x . __dict__)
x . d = 40
print(x . __dict__)
y = c2()
y . m3()
print(x . __dict__)
z = c1()
print(z . __dict__)
'''
Outputs
{'a' : 10}
{'a' : 10, 'b' : 20}
{'a' : 10, 'b' : 20, 'c' : 30}
{'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
{'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40, 'e' : 50}
{'a' : 10}
'''









# Find  outputs  (Home  work)
class c1:
	def __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_)
print(b . _dict_)
del  a . x # deletes variable x of object a
del  b . y # deletes variable y of object b
print(a . _dict_)
print(b . _dict_)
print(a . x) # Error, variable x of object a is already deleted
print(b . y) # Error, variable y of object b is already deleted
'''
Outputs
{'x' : 10, 'y' : 20, 'z' : 30}
{'x' : 10, 'y' : 20, 'z' : 30}
{'y' : 20, 'z' : 30}
{'x' : 10, 'z' : 30}
'''









#  Find  outputs (Home  work)
class c1:
	def __init__(self):
		print('1st  constructor')
	def __init__(self):
		print('2nd  constructor')
	def __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()
'''
Outputs
3rd constructor
'''









#  Find  outputs  (Home  work)
class c1:
	def __init__(self):
		print('No  argument  constructor')
	def __init__(self , x):
		print('single  argument  constructor : ' , x)
	def __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30) # Error, it requires 2 arguments
c = c1() # Error, it requires 2 arguments
'''
Outputs
Two  argument  constructor : 10 20
'''









#  Find  outputs
class c1:
	def __init__(self):
		print('No  argument  constructor')
	def __init__(self , x):
		print('single  argument  constructor : ' , x)
	def __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()
'''
Outputs
Two  argument  constructor :10 20
Two  argument  constructor :30 200
Two  argument  constructor :100 200
'''









# What  happens  when  function  and  class  have  same  name ?
def f1():
	print('Function')
	return  25
class f1:
	def __init__(self):
		print('Constructor')
#end of the  class
a = f1()
print(a)
'''
Outputs
Constructor
Type and address of object a
'''









# Find  outputs (Home  work)
class c1:
	def __init__(self):
		print('Constructor')
def c1():
	print('Function')
#end of the  class
a = c1()
print(a)
'''
Outputs
Function
None
'''









# Find outputs  (Home  work)
class c1:
	def __init__(self):
		print('Constructor')
def c1(x):
    print('Function : ' , x)
# End  of  class  c1
a = c1() # Error, it requires one argument
b = c1(25)
print(b)
'''
Outputs
Function : 25
None
'''









#  Find  outputs (Home  work)
from  prog9a  import  c1
class c1:
	def __init__(self):
		print('c1  class  of  prog9b')
a = c1()
'''
Outputs
c1  class  of  prog9b
'''









# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import c1
a = c1()
'''
Outputs
c1  class of prog9a
'''









#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c #How  to  import  class  c1  from  prog9a
class c1:
	def __init__(self):
		print('c1  class  of  prog9d')
a = c1() # How  to  create  c1  class  object  of  current  module
b = c() # How  to  create  c1  class  object  of  prog9a








'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a # How  to  import  prog9a
class c1:
	def __init__(self):
		print('c1  class  of  prog9e')
a = c1() # How  to  create  c1  class  object  of  current  module
b = proga.c1() # How  to  create  c1  class  object  of  prog9a









# Public  and  Private  members  demo  program
class  Test:
	def __init__(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  to  10
		self.__y = 20 #How  to  initialize  private  variable  'y'  to  20
	def m1(self):
		print('m1  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable  'y'
		self.__m2() # How  to  call    private  method   m2()
		print('Back to m1 method')
	def __m2(self):
		print('__m2  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.__y) # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) # How  to  print  variable  'x'
print(t._Test__y) # How  to  print   variable  'y'
print(t . _Test__y)
print(t . __dict__)
t.m1() # How  to  call  method  m1()
t._Test__y # How  to  call   method  m2()
t . _Test__m2()
print('End')
'''
Outputs:
Outside
10
20
Back to m1 method
__m2  method
10
20
End
'''









#  Find  outputs

class c1:
	def __init__(self):
		self.x = 10 # How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30 # How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # How  to  print   variable  'x'
print(a.__x__) # How  to  print  public  dunder  variable  'x'
print(a._c1__x) # How  to  print   private  variable  'x'
print(a . __x) # Error, cannot access private variable without classname
a.m1() #How  to  call  public  method  m1()
a._m1_() # How  to  call  public  dunder  method  m1()
a._c1__m1() # How  to  call  private  method  m1()
a . __m1() # Error , cannot access private method without using _classname as prefix
'''
Outputs
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
class c1:
	def __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def  __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End of the class
a = c1()
a = None
b = c1()
del b
c = c1()
c = c1()
d = c1()
e = c1()
'''
Object  is  created  at  address  : address of object a
Object  at  address  address of object a is  lost
Object  is  created  at  address  :  address of object b
Object  at  address  address of object a is  lost
Object  is  created  at  address  :   address of object c
Object  is  created  at  address  :   address of object c
Object  at  address  address of object c  is  lost
Object  is  created  at  address  :   address of object d
Object  is  created  at  address  :   address of object e
Object  at  address  address of object c  is  lost
Object  at  address  address of object d  is  lost
Object  at  address  address of object e  is  lost
'''









# Identify  Error (Home  work)
class c1:
	def __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)
'''
Outputs
destructor : 25
'''









# Find  outputs (Home  work)
class c1:
	def __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)
'''
Outputs
destructor : 25
destructor : 35
'''









# Find  outputs (Home  work)
class c1:
	def __del__(self):
		print('destructor')
		b = c1()
a = c1()
'''
Outputs
prints destructor infinite times
'''









# Find  outputs (Home  work)
class c1:
	def __init__(self):
		print('constructor')
		del self
	def __del__(self):
		print('destructor')
		b = c1()
a = c1()
'''
constructor 
destructorinfinite times
'''









#  Find  outputs( Home  work)
class  c1:
	def __del__(self):
		print('1st  destructor')
	def __del__(self):
		print('2nd  destructor')
	def __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()
'''
Outputs
3rd  destructor
'''









#Find  outputs (Home  work)
class c1:
	def __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def __del__(self):
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
Outputs
Object  is  created  at  address  : address of c1 class object 
Hello
Hi
Object  at  address {address of c1 class object} is  lost
Bye
Object  is  created  at  address  : address of object d
End
Object  at  address  {address of object d}  is  lost
'''









# Find  outputs(Home  work)
class c1:
	def __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
		def __del__(self):
			print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del list
'''
Outputs
Object  is  created  at  address  : address of 1st object of list
Object  is  created  at  address  : address of 2nd object of list
Object  is  created  at  address  : address of 3rd object of list
Object  at  address  {address of 1st object of list}  is  lost
Object  at  address  {address of 2nd object of list}  is  lost
Object  at  address  {address of 3rd object of list}  is  lost
'''









# Find  outputs  (Home  work)
class c1:
	def __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())
print('Hello')
del a
'''
Outputs
destructor
25
Hello
destructor
'''