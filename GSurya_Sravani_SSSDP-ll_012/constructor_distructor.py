# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()#nr1=22,dr1=7
b = Rat(9)#nr=9,dr1=7
c = Rat(5,  8)#nr=5,dr=8
d = Rat(dr1 = 9)#nr1=22,dr1=9
e = Rat(dr1 = 3 , nr1 = 2)#nr1=2,dr1=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)#error
print('a  :  ' , a)#nr1=22,dr1=7
print('b  :  ' , b)#nr=9,dr1=7
print('c  :  ' , c)#nr=5,dr=8
print('d  :  ' , d)#nr1=22,dr1=9
print('e  :  ' , e)#nr1=2,dr1=3
print('f  :  ' , f)#error
c . __init__()
print('c  :  ' , c)#5 8
a . __init__(3.8  , 4.6)#3.8,4.6
print('a  :  ' , a)#
g = Rat(nr1 = 9 , 5)#nr1=9,dr1=7
h = Rat(nr = 9 , dr = 5)#error

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
print('a  :  ' , a . __dict__)#{dd1:15 , mm1 :8 , yy1:1947
print('b  :  ' , b . __dict__)#{yy1 : 1950 , mm1 : 1 , dd1 : 26}
print('c  :  ' , c . __dict__)#{dd1:19 , mm1:7  , yy1:1985}
d = Date()#constructor is initialized
e = Date(dd = 30 , mm = 4 , yy = 2022)#error
f = Date(dd1 = 26 , mm1 = 8 , 2023)#error


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
a = c1()#'c1  class constructor'  then error object creation failed
b = c2()#'c2  class  constructor'then error object creation failed
print(b)#
print(b . __init__())#c2  class  constructor'
c = c3()
print(c . __init__())#'c3  class  constructor'




# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()#'Constructor' then error




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
a = c1()
print(a . __dict__)#Constructor' {x:10,y:20}
b = c2()
print(b . __dict__)#'Method'   {x:10,y:20}
b . init()
print(b . __dict__)#'Method'   {x:10,y:20}




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
print(x . __dict__)#{a:10}
x . m1()
print(x . __dict__)#{a:10,b:20}
f1()
print(x . __dict__)#error
x . d = 40
print(x . __dict__)#{a:10,b:20,d:40}
y = c2()
y . m3()
print(x . __dict__)#{a:10,b:20,d:40}
z = c1()
print(z . __dict__)#{a:10}




# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)#{x :10, y:20 z : 30}
print(b . __dict__)#{x :10, y:20 z : 30}
del  a . x
del  b . y
print(a . __dict__){y:20 z : 30}
print(b . __dict__){x :10 z : 30}
print(a . x)#error
print(b . y)#error


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()#'3rd  constructor'


#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#'Two  argument  constructor : ' , 10 , 20
b = c1(30)#error
c = c1()#error


#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#'Two  argument  constructor : ' , 10 , 20
b = c1(30)#error
c = c1()#error



# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1()
print(a)#constructor


# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)#function



# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()#error
b = c1(25)#'Function : ' , 25
print(b)


#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')



#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()#
'c1  class  of  prog9b'
none



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()#c1  class  of  prog9a



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()#c1  class  of  prog9a



#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1()How  to  create  c1  class  object  of  current  module
import prog9a
a=prog9a.c1()#How  to  create  c1  class  object  of  prog9a





# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self,x,y):
		self.x=10 #How  to  initialize  public  variable  'x'  to  10
		self.__y=20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable  'y'
		How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test(x,y)
print('Outside')
print(t.x) #How  to  print  variable  'x'
print(t.y) #How  to  print   variable  'y'
print(t . __y)#20
print(t . __dict__)#{x:10}
t.m1() #How  to  call  method  m1()
How  to  call   method  m2()
t . __m2()#__m2  method
10
20
print('End')



#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10  #How  to  initialize  public  variable  'x'  with  10
		self.__x=20  #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30  #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a.__x__)How  to  print  public  dunder  variable  'x'
print(a.__x) #How  to  print   private  variable  'x'
print(a . __x)#20
a.__m1()  #How  to  call  public  method  m1()
print(a)How  to  call  public  dunder  method  m1()
How  to  call  private  method  m1()
a . __m1()#private method




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
a = c1()#Object  is  created  at  address  :  ' , 1000
a = None#Object  at  address  {1000}  is  lost
b = c1()#Object  is  created  at  address  :  ' , 2000
Object  at  address  {2000}  is  lost
del    b
c = c1()#Object  is  created  at  address  :  ' , 3000
c = c1()#Object  is  created  at  address  :  ' , 3000
Object  at  address  {3000}  is  lost

d = c1()#Object  is  created  at  address  :  ' , 4000
e = c1()#Object  is  created  at  address  :  ' , 5000



# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()#error
a . __del__(25)#'destructor : ' ,  25




# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()#'destructor'
error



# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()#'constructor'
'destructor
error



#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()#'1st  destructor'



#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()#Object  is  created  at  address  :  ' , id(self)
Object  at  address  {id(self)}  is  lost 
del   a#error
print('Hello')#hello
del   b
print('Hi')#hi
del   c
print('Bye')
d = c1()#error
print('End')




# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]#'Object  is  created  at  address  :  ' , id(self
Object  at  address  {id(self)}  is  lost 
del  list#error





# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())#destructor
25
print('Hello')#hello
del   a#destructor'
25
object not lost

