# BATHINI RAJU SSSSDP 103
# 30-09-2025

# Find  outputs
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
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
print('a  :  ' , a) #22/7
print('b  :  ' , b) #9/7
print('c  :  ' , c) #5/8
print('d  :  ' , d) #22/9
print('e  :  ' , e) #2/3
print('f  :  ' , f) #11/15
c . _init_()
print('c  :  ' , c) #22/7
a . _init_(3.8  , 4.6)
print('a  :  ' , a) #3.8/4.6
# g = Rat(nr1 = 9 , 5) #Error
h = Rat(nr = 9 , dr = 5) #Error

'''
Object  'a'   --->  nr = 22 , dr = 7

Object  'b'   --->  nr = 9 , dr = 7
'''
# Find  outputs (Home  work)
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_) #{'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . _dict_) #{'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . _dict_) #{'dd': 19, 'mm': 7, 'yy': 1985}
d = Date() #Error
e = Date(dd = 30 , mm = 4 , yy = 2022) #Error
f = Date(dd1 = 26 , mm1 = 8 , 2023) #Error



# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  _init_(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  _init_(self):
		print('c3  class  constructor')
# End  of  class
# a = c1() #Error
b = c2()
print(b)
print(b . _init_())
c = c3()
print(c . _init_())
'''

c2  class  constructor
Type and Address
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None
'''

# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() #Infinite Recursion


#  Difference  between  init()    and  init()   methods (Home  work)
class c1:
    def  _init_(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()
print(a . _dict_)
b = c2()
print(b . _dict_)
b . init()
print(b . _dict_)

'''
Constructor
{'x':10,'y':20}
{}
Method
{'x':10,'y':20}
'''

# Find  outputs (Home  work)
class   c1:
        def   _init_(self):
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
print(x . _dict_)
x . m1()
print(x . _dict_)
f1()
print(x . _dict_)
x . d = 40
print(x . _dict_)
y = c2()
y . m3()
print(x . _dict_)
z = c1()
print(z . _dict_)

'''
{'a':10}
{'a':10,'b':20}
{'a':10,'b':20,'c':30}
{'a':10,'b':20,'c':30,'d':40}
{'a':10,'b':20,'c':30,'d':40,'e':50}
{'a':10}
'''

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_)
print(b . _dict_)
del  a . x
del  b . y
print(a . _dict_)
print(b . _dict_)
print(a . x) #Error
print(b . y) #Error

'''
{'x':10,'y':20,'z':30}
{'x':10,'y':20,'z':30}
{'y':20,'z':30}
{'x':10,'z':30}
'''
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #3rd  constructor

#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10 20
b = c1(30) #Error
c = c1() #Error


#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10 20
b = c1(30) #Two  argument  constructor : 30 200
c = c1() #Two  argument  constructor : 100 200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
#end of the  class
a = f1()
print(a)
'''
Constructor
Type and address
'''
# Find  outputs (Home  work)
class    c1:
	def   init(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)
'''
Function
None
'''
# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
# a = c1()#Error
b = c1(25) #Function : 25
print(b) #None

#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')
  
#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1() #c1  class  of  prog9b

#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() #c1  class  of  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c11 #How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a=c1()#How  to  create  c1  class  object  of  current  module
b=c11()#How  to  create  c1  class  object  of  prog9a


#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
import prog9a #How  to  import  prog9a
class   c1:
	def  init(self):
		print('c1  class  of  prog9e')
a=c1()#How  to  create  c1  class  object  of  current  module
b=prog9a.c1()#How  to  create  c1  class  object  of  prog9a

# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x=10 #How  to  initialize  public  variable  'x'  to  10
		self.__y=20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)#How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable  'y'
		self.__m2()#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)#How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)#How  to  print  variable  'x'
print(t.Test_y)#How  to  print   variable  'y'
# print(t . __y) #Error
print(t . _dict) #{'x':10,'_Test_y':20}
t.m1()#How  to  call  method  m1()
t.Test_m2()#How  to  call   method  m2()
# t . __m2() #Error
print('End')
'''
Outside
10
20
{'x':10,'Test_y':20}
m1 method
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
	def _init_(self):
		self.x=10 #How  to  initialize  public  variable  'x'  with  10
		self.__x=10 #How  to  initialize  private  variable  'x'  with  20
		self._x_=30#How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)#How  to  print   variable  'x'
print(a._x_)#How  to  print  public  dunder  variable  'x'
print(a.c1_x)#How  to  print   private  variable  'x'
print(a . __x) #Error
a.m1()#How  to  call  public  method  m1()
a._m1_() #How  to  call  public  dunder  method  m1()
a.c1_m1()#How  to  call  private  method  m1()
a . __m1() #Error
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
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
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
Object  is  created  at  address  :  1000
Object  at  address  1000  is  lost
Object  is  created  at  address  :  2000
Object  at  address  2000  is  lost
Object  is  created  at  address  :  3000
Object  is  created  at  address  :  3000
Object  at  address  3000  is  lost
Object  is  created  at  address  :  4000
Object  is  created  at  address  :  5000
Object  at  address  3000  is  lost
Object  at  address  4000  is  lost
Object  at  address  5000  is  lost
'''

# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1() 
a . _del_(25) #destructor : 25

# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . _del_(25)
'''
destructor : 25
destructor : 35
'''
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1()
a = c1()
'''
Infinite REcusrsion
'''
# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  _del_(self):
		print('destructor')
		b = c1()
a = c1()
'''
Infinite Recursion
'''

#  Find  outputs( Home  work)
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()
'''
3rd  destructor
'''

#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')
'''
Object  is  created  at  address  :  1000
Hello
Hi
Object  at  address  1000  is  lost
Bye
Object  is  created  at  address  :  4000
End
Object  at  address  4000  is  lost
'''
# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
'''
Object  is  created  at  address  :  1000
Object  is  created  at  address  :  2000
Object  is  created  at  address  :  3000
Object  at  address  3000  is  lost 
Object  at  address  2000  is  lost 
Object  at  address  1000  is  lost
'''
# Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())
print('Hello')
del   a
'''
destructor
25
Hello
destructor
'''