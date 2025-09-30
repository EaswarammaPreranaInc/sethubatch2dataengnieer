
#Find  outputs

class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()#constructor is executed after object is created i.e nr1=22,dr1=7
b = Rat(9)#nr1=9,dr1=7
c = Rat(5,  8)#nr1=5,dr1=8
d = Rat(dr1 = 9)#nr1=22,dr1=9
e = Rat(dr1 = 3 , nr1 = 2)#nr1=2,dr1=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)#x=11,y=15
print('a  :  ' , a)#__str__()method is executed i.e 22/7
print('b  :  ' , b)#9/7
print('c  :  ' , c)#5/8
print('d  :  ' , d)#22/9
print('e  :  ' , e)#2/3
print('f  :  ' , f)#11/15
c . __init__()#constructor is calling explicitly so modified the object 
print('c  :  ' , c)#22/7
a . __init__(3.8  , 4.6)
print('a  :  ' , a)#3.8/4.6
#g = Rat(nr1 = 9 , 5)#error positional argument follows keyword argument
#h = Rat(nr = 9 , dr = 5)#error because invalid agruments
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
a = Date(15 , 8 , 1947)#Three variables are added to the object 'a' i.e dd=15,mm=8,yy=1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)#Three variables are added to the object 'a' i.e dd=26,mm=1,yy=1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)#Three variables are added to the object 'a' i.e dd=19,mm=7,yy=1985
print('a  :  ' , a . __dict__)#{dd:15,mm:8,yy:1947}
print('b  :  ' , b . __dict__)#{dd:26,mm:1,yy:1950}
print('c  :  ' , c . __dict__)#{dd:19,mm:7,yy:1985}
#d = Date()#error due to there is no arguments 
#e = Date(dd = 30 , mm = 4 , yy = 2022)#error due invalid arguments
#f = Date(dd1 = 26 , mm1 = 8 , 2023)#error positional argument follows keyword argument 




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
#a = c1()#error because constructor is returned ontherthan None so object creation is falied
b = c2()#object is created and constructor is executed i.e c2 class constructor
print(b)#Type and address of the object
print(b . _init_())#c2 class constructor 
                   #None
c = c3()#c3 class constructor
print(c . _init_())#c3 class constructor
                   #None




# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()#recursion error bcz when object is created inthe constructor we will get infinity recursion
# End  of  class
a = c1()#object is created and constructor is executed ie constructor



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
a = c1()#object is created and constructor is executed i.e constructor
print(a . __dict__)#{x:10,y:20}
b = c2()#empty object is created bcz there is no constructor in class c2
print(b . __dict__)#{}
b . init()#method is callling explicitly i.e method
print(b . __dict__)#{x:30,y:40}




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
x = c1()#object is created and constructor is executed 
print(x . __dict__)#{a:10}
x . m1()#calling m1 method
print(x . __dict__)#{a:10,b:20}
f1()#function is calling
print(x . __dict__)#{a:10,b:20,c:30}
x . d = 40
print(x . __dict__)#{a:10,b:20,c:30,d:40}
y = c2()#empty object is created bcz there is no constructor in c2 class
y . m3()#method calling
print(x . __dict__)#{a:10,b:20,c:30,d:40,e=50}
z = c1()#object is created and constructor is executed
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
print(a . __dict__)#{x:10,y:20,z:30}
print(b . __dict__)#{x:10,y:20,z:30}
del  a . x#variable 'x'is deleted from the object'a'
del  b . y#variable 'y' is deleted from the object 'b'
print(a . __dict__)#{y:20,z:30}
print(b . __dict__)#{x:10,z:30}
#print(a . x)#error variable x is not there in object'a'
#print(b . y)#error variable y is not there in object'b'



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()#when multiple constructors are there last one is recognized ie 3rd constructor


#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#Two argument constructor:<space>10<space>20
#b = c1(30)#error one required argument is missing
#c = c1()#error there is aruments 



#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#Two argument constructor:<space>10<space>20
b = c1(30)#Two argument constructor:<space>30<space>200
c = c1()#Two argument constructor:<space>100<space>200



# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() #when  function  and  class  have  same  name last one is recognized i.e construtor
print(a)#__str__()method of object is executed  bcz there is no __str__()method in class f1 and returns type and address



# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()#function
print(a)#None



# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()#error due no argments
b = c1(25)#function:<space>25
print(b)#None




#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()#current program constructor is executed i.e c1 class of prog9b



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()#class c1 constructor is executed of prog9a ie c1 class of prog9a



#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import  c1 as c2#How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1()#How  to  create  c1  class  object  of  current  module
a=c2()#How  to  create  c1  class  object  of  prog9a

#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
import prog9a#How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1()#How  to  create  c1  class  object  of  current  module
a=prog9a.c1()#How  to  create  c1  class  object  of  prog9a



# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10#How  to  initialize  public  variable  'x'  to  10
		self.__y=20#How  to  initialize  private  variable  'y'  to  20
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
print('Outside')#outside
print(t.x)#How  to  print  variable  'x'
print(t._Test__y)#How  to  print   variable  'y'
#print(t . __y)#error bcz not visible
print(t . __dict__)#{x:10,y:20}
t.m1()#How  to  call  method  m1()
t._Test__m2()#How  to  call   method  m2()
#t . __m2()#error not visible
print('End')#end
'''
o/p:
Outside
10
20
{'x': 10, '_Test__y': 20}
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
		self.x=10#How  to  initialize  public  variable  'x'  with  10
		self.__x=20#How  to  initialize  private  variable  'x'  with  20
		self.__x__=30#How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.__x__)#How  to  print  public  dunder  variable  'x'
print(a._c1__x)#How  to  print   private  variable  'x'
#print(a . __x)#error bcz not visible
a.m1()#How  to  call  public  method  m1()
a.__m1__()#How  to  call  public  dunder  method  m1()
a._c1__m1()#How  to  call  private  method  m1()
#a . __m1()#error not visible
'''
o/p:
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
a = c1()#object is created and constructor is executed i.e object is created at address:object 1 address
a = None#object 'a' is created another object i.e none so first object is lost before that destructor is executed i.e object at address object 1 address is lost
b = c1()#object s created at address:2nd object address
del    b#object is deleted before that destructor is executed i.e object at address 2nd object address is lost
c = c1()#object is created at address: 2nd object address
c = c1()#object is created at address:3rd address and Object  at  address 2nd object address  is  lost
d = c1()#Object  is  created  at  address  : 4th object  address
e = c1()#Object  is  created  at  address  : 5th object address

'''
o/p:
Object  is  created  at  address  :   2726501445856
Object  at  address  2726501445856  is  lost
Object  is  created  at  address  :   2726504778960
Object  at  address  2726504778960  is  lost
Object  is  created  at  address  :   2726504778960
Object  is  created  at  address  :   2726501916768
Object  at  address  2726504778960  is  lost
Object  is  created  at  address  :   2726501915856
Object  is  created  at  address  :   2726501640976
Object  at  address  2726501916768  is  lost
Object  at  address  2726501915856  is  lost
Object  at  address  2726501640976  is  lost
'''
# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)#error destructor cannot have arguments it must accept only self argument,so 25 is not allowed


# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')#infinite destructor i.e recursion error
			b = c1()#
a = c1()


# Find  outputs (Home  work)
class   c1:
	def  __init__(self):#self is a
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()# infinite destructor
a = c1()# infinte constructor

'''
o/p:
constructor
destructor
constructor
destructor
constructor
destructor
...
RecursionError
'''


#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()#when multiple destructor are there in class last one is recongnized i.e 3rd destructor


#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()#Object  is  created  at  address  :  address of objects
del   a#Object 'a' deleted)
print('Hello')#hello
del   b#object 'b' is deleted
print('Hi')#hi
del   c#Object 'c' address is lost)
print('Bye')#bye
d = c1()#Object  is  created  at  address  : object 'd' address)
print('End')#end
            #Object  at  address  'd'  is  lost


'''
o/p
Object  is  created  at  address  :   1753564738096
Hello
Hi
Object  at  address  1753564738096  is  lost
Bye
Object  is  created  at  address  :   1753567808400
End
Object  at  address  1753567808400  is  lost
'''


# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]#Object  is  created  at  address  :  some address1
                            #Object  is  created  at  address  :  some address2
							#Object  is  created  at  address  :  some address 3 
del  list#Object  at  address  some address1  is  lost
         #Object  at  address  some address2  is  lost
         #Object  at  address  some address3  is  lost



# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())#destructor
                    #25
print('Hello')#hello
del   a#destructor
#object at some address is lost

