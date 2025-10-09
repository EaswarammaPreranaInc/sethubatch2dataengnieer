# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):  #   Constructor  with  default  values  22  and  7
		self . nr = nr1  #  Adds  variable  nr  to  object  self  with  value  nr1
		self . dr = dr1  #  Adds  variable  dr  to  object  self  with  value  nr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()  #  Constructor  initializes  object  with  nr = 22 , dr = 7
b = Rat(9)  #  Constructor  initializes  object  with  nr = 9 , dr = 7
c = Rat(5,  8) #  Constructor  initializes  object  with  nr = 5 , dr = 8
d = Rat(dr1 = 9) #  Constructor  initializes  object  with  nr = 22 , dr = 9
e = Rat(dr1 = 3 , nr1 = 2) #  Constructor  initializes  object  with  nr = 2 , dr = 3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) #  Constructor  initializes  object  with  nr = user  input  'x'  , dr =  user  input  'y'
print('a  :  ' , a) #   __str__()  method  of  Rat  class  returns  '22 / 7'
print('b  :  ' , b) #   __str__()  method  of  Rat  class  returns  '9 / 7'
print('c  :  ' , c)  #   __str__()  method  of  Rat  class  returns  '5 / 8'
print('d  :  ' , d)   #   __str__()  method  of  Rat  class  returns  '22 / 9'
print('e  :  ' , e)  #   __str__()  method  of  Rat  class  returns  '2 / 3'
print('f  :  ' , f)  #   __str__()  method  of  Rat  class  returns  'x / y'
c . __init__()  #  Constructor  modifies  object  with  nr = 22 , dr = 7
print('c  :  ' , c)   #   __str__()  method  of  Rat  class  returns  '22 / 7'
e . __init__(3.8  , 4.6)  #  Constructor  modifies  object  with  nr = 3.8 , dr = 4.6
print('e  :  ' , e)    #   __str__()  method  of  Rat  class  returns  '3.8 / 4.6'
g = Rat(nr1 = 9 , 5) # Error :  Positional  argument  5  is  not  permitted after  keyword  argument  nrr1 = 9
h = Rat(nr = 9 , dr = 5)  # Error :  No  args  nr  and dr  for  constructor

'''Object  'a'   --->  nr = 3.8 , dr = 4.6
Object  'b'   --->  nr = 9 , dr = 7
Object  'c'   --->  nr = 22 , dr = 7
Object  'd'   --->  nr = 22 , dr = 9
Object  'e'   --->  nr = 2 , dr = 3
Object  'f'   --->  nr = 11 , dr = 15
'''

'''
1) What is  the  advantage  with  default  arguments  for  constructor ?  ---> Object  can  be  created  with  0 , 1  (or)  2  arguments Eg: Rat()  , Rat(5)  and  Rat(5 , 8)  are  valid due  to  default  arguments
2) What  is  the  issue  without  default  arguements  ?  --->  Object  has  to  be  created  with  two  arguments  only Eg:  Rat(5 , 8)
3) In  other  words,  Rat()  and  Rat(5)  throw  error  without  default  arguments
4) Can  parameter  and  instance  variable  have  same  name ?  --->  Yes  but  not  recommended
5) How  are  they  distinguished  when  they  have  same  name ?  ---> Instance  variables  are  denoted  by  self . nr , self . dr and  parameters  are  denoted  by  nr , drEg:  def   __init__(self , nr = 22 , dr = 7): self . nr = nr self . dr = nr
'''
# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) # Constructor  initializes  object  with  dd = 15, mm = 8 , yy = 1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)  # Constructor  initializes  object  with  dd = 26 , mm = 1 , yy = 1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) # Constructor  initializes  object  with  dd = 19 , mm = 7 , yy = 1985
print('a  :  ' , a . __dict__) # a : {'dd' : 15 , 'mm' : 8 , 'yy' : 1947}
print('b  :  ' , b . __dict__) # b : {'dd' : 26 , 'mm' : 1 , 'yy' : 1950}
print('c  :  ' , c . __dict__) # c : {'dd' : 19 , 'mm' : 7 , 'yy' : 1985}
d = Date()  # Error : Args  are  not  passed  for  dd1 , mm1 and  yy1
e = Date(dd = 30 , mm = 4 , yy = 2022) # Error :  No  args  dd , mm  and yy for  constructor
f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error :  Positional  arg  2023  can  not  be  passed  after  keywords  args

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
		print('c3  class  constructor') # c3  class  constructor
# End  of  class
a = c1() # Error
b = c2() # Error
print(b) # Error
print(b . __init__()) # Error
c = c3()
print(c . __init__()) # c3  class  constructor and None

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor') # Infinity loop
		b = c1() 
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
a = c1()
print(a . __dict__)
b = c2()
print(b . __dict__)
b . init()
print(b . __dict__)
'''Output:
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}'''

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
'''Output:
{'a': 10}
{'a': 10, 'b': 20}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
{'a': 10}'''

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)
print(b . __dict__)
del  a . x
del  b . y
print(a . __dict__)
print(b . __dict__)
print(a . x) # Error
print(b . y) # Error
'''Output:
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}'''

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() # Executes 3rd constructor

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Error
b = c1(30) # error
c = c1() # Nothing is printed

#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Error
b = c1(30) # Error
c = c1() # Nothing is printed

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor') # Constructor
#end of the  class
a = f1()
print(a) # type and address of object of a

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1() # Function is printed
print(a) # None is returned

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1() # Error argument is missing
b = c1(25) # Function :  25
print(b) # None is returned


#Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # c1  class  of  prog9b

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() # c1  class  of  prog9c

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c2 # How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1() # How  to  create  c1  class  object  of  current  module
b=c2() # How  to  create  c1  class  object  of  prog9a
#Output: c1  class  of  prog9d

#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
import prog9a # How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a = prog9a.c1() #How  to  create  c1  class  object  of  current  module
b= c1() # How  to  create  c1  class  object  of  prog9a
'''Output:
c1  class  of  prog9a
c1  class  of  prog9e'''

# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10 # How  to  initialize  public  variable  'x'  to  10
		self.__y=10 # How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.__y) # How  to  print  private  variable  'y'
		self.__m2# How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)# How  to  print   variable  'x'
		print(self.__y) # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) # How  to  print  variable  'x'
print(t._Test__y) #How  to  print   variable  'y'
print(t . __y) # Error
print(t . __dict__)
t.m1() # How  to  call  method  m1()
t._Test__m2() # How  to  call   method  m2()
t . __m2() # Error
print('End')
'''Output:
Outside
10
10
{'x': 10, '_Test__y': 10}
m1  method
10
10
Back to m1 method
__m2  method
10
10
End'''

#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10 #How  to  initialize  public  variable  'x'  with  10
		self.__x=20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)#How  to  print   variable  'x'
print(a.__x__) #How  to  print  public  dunder  variable  'x'
print(a._c1__x)#How  to  print   private  variable  'x'
print(a . __x) # Error
a.m1() # How  to  call  public  method  m1()
a.__m1__() # How  to  call  public  dunder  method  m1()
a._c1__m1() # How  to  call  private  method  m1()
a . __m1() # Error
'''Output:
10
30
20
public method
public Dunder method
private method'''

#Tricky  program
#Find  outputs
#Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1()
a = None
b = c1()
del b
c = c1()
c = c1()
d = c1()
e = c1()
'''Output:
Object  is  created  at  address  :   100
Object  at  address  100  is  lost
Object  is  created  at  address  :   200
Object  at  address  200  is  lost
Object  is  created  at  address  :   200
Object  is  created  at  address  :   300
Object  at  address  200  is  lost
Object  is  created  at  address  :   400
Object  is  created  at  address  :   500
Object  at  address  300  is  lost
Object  at  address  400  is  lost
Object  at  address  500  is  lost'''

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x) # destructor :  25
a = c1()
a . __del__(25) # Executes destructor and 25 is passed to the destructor
#Executes destructor before object is lost but throws error as arg is not passed to the destructor 

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)
'''Output:
destructor :  25
destructor :  35'''

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') # infinity recursion
			b = c1()
a = c1()

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor') 
		del  self # Executes destructor before object is deleted
	def  __del__(self):
		print('destructor')
		b = c1() # Executes constructor 
a = c1() # Executes constructor

#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() # 3rd  destructor

#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
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

'''Output:
Object  is  created  at  address  :   100
Hello
Hi
Object  at  address  100  is  lost  
Bye
Object  is  created  at  address  :   200
End
Object  at  address  200  is  lost'''

# Find  outputs(Home  work)
class  c1:
        def __init__(self):
            print('Object  is  created  at  address  :  ' , id(self))
        def __del__(self):
            print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
'''Output:
Object  is  created  at  address  :   100
Object  is  created  at  address  :   200
Object  is  created  at  address  :   300
Object  at  address  2840015113744  is  lost
Object  at  address  2840015113424  is  lost
Object  at  address  2840012484496  is  lost'''

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del a
'''Output:
destructor
25
Hello
destructor'''