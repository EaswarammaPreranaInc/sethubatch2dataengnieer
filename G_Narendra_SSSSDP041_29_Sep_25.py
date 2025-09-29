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
print('a  :  ' , a)#  22  /  7
print('b  :  ' , b)#  9  /  7
print('c  :  ' , c)#  5  /  8
print('d  :  ' , d)#  22  /  9
print('e  :  ' , e)#  2  /  3
print('f  :  ' , f)#  11  /  15
c . _init_()
print('c  :  ' , c)#  22  /  7
a . _init_(3.8  , 4.6)
print('a  :  ' , a)#  3.8  /  4.6
g = Rat(nr1 = 9 , 5)# error
h = Rat(nr = 9 , dr = 5)# error


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
print('a  :  ' , a . _dict_)# {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . _dict_)# {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . _dict_)# {'dd': 19, 'mm': 7, 'yy': 1985}
d = Date()# error
e = Date(dd = 30 , mm = 4 , yy = 2022)# error
f = Date(dd1 = 26 , mm1 = 8 , 2023)# error


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
a = c1()
b = c2()
print(b)# None
print(b . _init_())# c2 class constructor /n None
c = c3()
print(c . _init_())# c3 class constructor /n None


# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()
#  Difference  between  init()    and  _init_()   methods (Home  work)
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
print(a . _dict_)# {'x': 10, 'y': 20}
b = c2()
print(b . _dict_)# {}
b . init()
print(b . _dict_)# {'x': 30, 'y': 40}


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
print(x . _dict_)# {'a': 10}
x . m1()
print(x . _dict_)# {'a': 10, 'b': 20}
f1()
print(x . _dict_)# {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . _dict_)# {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . _dict_)# {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . _dict_)# {'a': 10}


# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_)# {'x': 10, 'y': 20, 'z': 30}
print(b . _dict_)# {'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . _dict_)# {'y': 20, 'z': 30}
print(b . _dict_)# {'x': 10, 'z': 30}
print(a . x)# error
print(b . y)# error


#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()#  3rd  constructor


#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#  Two  argument  constructor :  10  20
b = c1(30)#  error
c = c1()#  error


#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#  Two  argument  constructor :  10  20
b = c1(30)#  Two  argument  constructor :  30  200
c = c1()#  Two  argument  constructor :  100  200


# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
#end of the  class
a = f1()#  Constructor
print(a)# object  at  some  address


# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()#  Constructor
print(a)# object  at  some  address


# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()#  Constructor
b = c1(25)#  Function :  25
print(b)# None


#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')
		

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()# c1  class  of  prog9b


#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()# c1  class  of  prog9a


#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c11#How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
obj = c1()#How  to  create  c1  class  object  of  current  module
obj_prog9a = c11()#How  to  create  c1  class  object  of  prog9a


'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a as pro#How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a = c1() #How  to  create  c1  class  object  of  current  module
b = pro.c1()#How  to  create  c1  class  object  of  prog9a


# Public and Private members demo program
class Test:
    def __init__(self):
        self.x = 10# How to initialize public variable 'x' to 10
        self.__y = 20# How to initialize private variable 'y' to 20
    def m1(self):
        print('m1 method')
        print(self.x)# How to print variable 'x'
        print(self.__y)# How to print private variable 'y'
        self.__m2()# How to call private method m2()
        print('Back to m1 method')
    def __m2(self):
        print('__m2 method')
        print(self.x)# How to print variable 'x'
        print(self.__y)# How to print private variable 'y'
# End of the class
t = Test()
print('Outside')
print(t.x)# How to print variable 'x'
print(t.__y)# Error (private attribute)
print(t._Test__y)# How to print variable 'y' using name-mangling
print(t.__dict__)# How to print all attributes of object t
t.m1()# How to call method m1()
t._Test__m2()# How to call method m2() (private method, using name-mangling)
t.__m2()# Error
print('End')


# Find outputs
class c1:
    def __init__(self):
        self.x = 10# How to initialize public variable 'x' with 10
        self.__x = 20# How to initialize private variable 'x' with 20
        self.__dunder_x__ = 30# How to initialize public dunder variable 'x' with 30
    def m1(self):
        print('public method')
    def __m1(self):
        print('private method')
    def _m1_(self):
        print('public Dunder method')
# End of the class
a = c1()
print(a.x)# How to print variable 'x'
print(a.__dunder_x__)# How to print public dunder variable 'x'
print(a._c1__x)# How to print private variable 'x' (with name-mangling)
print(a.__x)# Error (private attribute)
a.m1()# How to call public method m1()
a._m1_()# How to call public dunder method m1()
a._c1__m1()# How to call private method m1() (with name-mangling)
a.__m1()# Error (private method)



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
a = c1()# Object  is  created  at  address : ex 1000
a = None# Object  at  address  1000  is  lost
b = c1()# Object  is  created  at  address : ex 2000
del    b# Object  at  address  2000  is  lost
c = c1()# Object  is  created  at  address : ex 3000
c = c1()# Object  is  created  at  address : ex 4000
d = c1()# Object  is  created  at  address : ex 5000
e = c1()# Object  is  created  at  address : ex 6000
# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1()# error
a . _del_(25)# error


# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()# error
a . _del_(25)# destructor :  25


# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1()
a = c1()# destructor


# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  _del_(self):
		print('destructor')
		b = c1()
a = c1()# constructor  destructor  constructor  destructor  constructor  destructor  .....


# Find  outputs( Home  work)
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()# No  output


#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()#
del   a# Object a   is  lost
print('Hello')# Hello
del   b# Object b   is  lost
print('Hi')#  Hi
del   c# Object c   is  lost
print('Bye')# Bye
d = c1()# Object  is  created  at  address  some  address
print('End')# End


 # Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list# all the  three  objects  are  lost


 # Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())# destructor /n 25
print('Hello')# Hello
del   a# destructor