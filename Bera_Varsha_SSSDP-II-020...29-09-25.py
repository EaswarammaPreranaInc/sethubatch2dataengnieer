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
print('a  :  ' , a) #   _str_()  method  of  Rat  class  returns  '22 / 7'
print('b  :  ' , b) #   _str_()  method  of  Rat  class  returns  '9 / 7'
print('c  :  ' , c)  #   _str_()  method  of  Rat  class  returns  '5 / 8'
print('d  :  ' , d)   #   _str_()  method  of  Rat  class  returns  '22 / 9'
print('e  :  ' , e)  #   _str_()  method  of  Rat  class  returns  '2 / 3'
print('f  :  ' , f)  #   _str_()  method  of  Rat  class  returns  'x / y'
c . _init_()  #  Constructor  modifies  object  with  nr = 22 , dr = 7
print('c  :  ' , c)   #   _str_()  method  of  Rat  class  returns  '22 / 7'
e . _init_(3.8  , 4.6)  #  Constructor  modifies  object  with  nr = 3.8 , dr = 4.6
print('e  :  ' , e)    #   _str_()  method  of  Rat  class  returns  '3.8 / 4.6'
#g = Rat(nr1 = 9 , 5) # Error :  Positional  argument  5  is  not  permitted after  keyword  argument  nrr1 = 9
#h = Rat(nr = 9 , dr = 5)  # Error :  No  args  nr  and dr  for  constructor

# Find  outputs (Home  work)
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
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
#d = Date()  # Error : Args  are  not  passed  for  dd1 , mm1 and  yy1
#e = Date(dd = 30 , mm = 4 , yy = 2022) # Error :  No  args  dd , mm  and yy for  constructor
#f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error :  Positional  arg  2023  can  not  be  passed  after  keywords  args

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
#a = c1() #  Error :  Object  can  not  be  created  as  constructor  returns  non-None  i.e.  25
b = c2() #  Executes  constructor  of  class  c2  and  ignores   None  (due  to  automcatic  execution  of  constructor)
print(b)  #   __str__()  method  of  object  class   returns  Type  and  address  of  object  'b'
print(b . __init__()) #  Constructor  of  class  c2  prints   a  msg  and  returns  None  to  constructor  call
c = c3() #  Executes  constructor  of  class  c3  and  ignores   None  (due  to  automcatic  execution  of  constructor)
print(c . __init__()) #  Constructor  of  class  c3  prints   a  msg  and  returns  None  to  constructor  call


'''
c2  class  constructor
Type  and  address  of  object  'b'
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None
'''

class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()  #  Executes  constructor  of  same  class  c1  which  leads  to  recursion
# End  of  class
a = c1() #  Executes  constructor  of  class  c1

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
a = c1() #  Constructo  initializes  object  with  x = 10 , y = 20
print(a . __dict__) # {'x' : 10 , 'y' : 20}
b = c2()  #  Empty  object
print(b . __dict__) # { }
b . init()  #  Method  initializes  object  with  x = 30 , y = 40
print(b . __dict__) # {'x' : 30 , 'y' : 40}


'''
Object  'a'  --->  x = 10 , y = 20
Object  'b'  ---> x = 30 , y = 40
'''

# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
# End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
# End  of  function  f1
x = c1() # Constructor  adds  variable 'a'  to object 'x'  with  value  10
print(x . __dict__) # {'a' : 10}
x . m1() #  Method  adds  variable  'b'  to  object 'x'  with  value  20
print(x . __dict__) # {'a' : 10 , 'b' : 20}
f1()  #  Function  adds  variable  'c'  to  object 'x'  with  value  30
print(x . __dict__) # {'a' : 10 , 'b' : 20 , 'c' : 30}
x . d = 40  #  Statement  outside  the  class  adds  variable 'd'   to  object 'x'  with  value  40
print(x . __dict__) # {'a' : 10 , 'b' : 20 , 'c' : 30 , 'd' : 40}
y = c2()  #  Empty  object
y . m3()  #  Method  of  a  different  class  adds  variable 'e'  to  object  'x'  with  value  50
print(x . __dict__) # {'a' : 10 , 'b' : 20 , 'c' : 30 , 'd' : 40 , 'e' : 50}
z = c1()  # Constructor  adds  variable  'a'  to  object  'z'  with  value  10
print(z . __dict__) # {'a' : 10}

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1() #  Constuctor  initializes  object  with  x = 10 , y = 20 , z = 30
b = c1() #  Constuctor  initializes  object  with  x = 10 , y = 20 , z = 30
print(a . __dict__) # {'x' : 10 , 'y' : 20 , 'z' : 30}
print(b . __dict__) # {'x' : 10 , 'y' : 20 , 'z' : 30}
del  a . x  #  Removes  variable  'x'  from  object  'a'
del  b . y  #  Removes  variable  'y'  from  object  'b'
print(a . __dict__) # {'y' : 20 , 'z' : 30}
print(b . __dict__)  # {'x' : 10 , 'z' : 30}
#print(a . x) # Error : No  variable  'x'  in  object  'a'
#print(b . y) #  Error : No  variable  'y'  in  object  'b'

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):   #  Discarded   due  to   another  constructor
		print('1st  constructor')
	def  __init__(self):  #  Discarded   due  to   another  constructor
		print('2nd  constructor')
	def  __init__(self):  #  Recognized
		print('3rd  constructor')
# End  of  the  class
a = c1() #  Executes  3rd constructor  of  class  c1

# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):  #  Discarded   due  to  another  constructor
		print('No  argument  constructor')
	def  __init__(self , x):  #  Discarded   due  to  another  constructor
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):  #  Recognized  :  Last  constructor
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :<space>10<space>20
#b = c1(30) # Error : Argument  is  not  passed  for  'y'
#c = c1() # Error : Arguments  are  not  passed  for  'x'  and  'y'

#  Find  outputs
class   c1:
	def  __init__(self):  #  Discarded   due  to  another  constructor
		print('No  argument  constructor')
	def  __init__(self , x):  #  Discarded   due  to  another  constructor
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):  #  Recognized  :  Last  constructor
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :<space>10<space>20
b = c1(30) # Two  argument  constructor :<space>30<space>200
c = c1() # Two  argument  constructor :<space>100<space>200

# What  happens  when  function  and  class  have  same  name ?
def   f1():   #  Discarded :  A  class  is  defined  with  same  name
	print('Function')
	return  25
class   f1: #   Recognized
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() #  Executes  constructor  of  class  f1
print(a) #  _str_()  method  of  object  class  returns  type  and  address  of  object  'a'

# Find  outputs (Home  work)
class    c1:  # Discarded :  A  function is  defined  with  same  name  later
	def   __init__(self):
		print('Constructor')
def  c1():  #  Recognized
	print('Function')
#end of the  class
a = c1() #  Executes  function  c1()  which  returns  None  by  default  i.e.  a = None
print(a) # None

'''
Function
None
'''

# Find outputs  (Home  work)
class  c1:  #  Discarded :  A  function  is  defined  with  same  name  later
        def  __init__(self):
                print('Constructor')
def  c1(x):  #  Recognized
	print('Function : ' , x)
# End  of  class  c1
#a = c1() # Error : Argument  is  not  passed  for  'x'  of  function  c1()
b = c1(25) #  Executes  function  c1(25)  which  returns  None  by  default  i.e.  b = None
print(b) # None


'''
Function :  25
None
'''

# Find  outputs (Home  work)
from  prog9a  import  c1  #  Ignores  class  c1  becoz  another  class  c1  is  defined  with  same  name  later
class   c1:  #  Recognized
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() #  Executes  constructor  of  class  c1  of  prog9b

# Find  outputs (Home  work)
class   c1:  #  Discarded : Another  class  with  same  name  is  imported  from  prog9a   later
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1  #  Recognized
a = c1() #  Executes  constructor  of  class  c1  imported  from  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from  prog9a  import  c1  as  c2  #  Imports  class  c1  of  prog9a  with  another  name  c2
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a = c1() #  Executes  constructor  of  class  c1  of  current  module
b = c2() #  Executes  constructor  of  class  c1  imported  from  prrog9a

'''
c1  class  of  prog9d
c1  class  of  prog9a
'''

# How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
import prog9a  #  Imports  prog9a  module
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a = prog9a . c1() #  Executes  constructor  of  class  c1   of  prog9a  module
b = c1()  #  Executes  constructor  of  class  c1   of  current  module


'''
c1  class  of  prog9a
c1  class  of  prog9e
'''

# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self . x = 10 #  Adds  public  variable  'x'  to  object  self  with  value  10
		self . __y = 20 # Adds  private  variable  'y'  to  object  self  with  value  20
	def  m1(self):
		print('m1  method')
		print(self . x) #  10
		print(self . __y) # 20
		self . __m2() #  Executes  private  method  of  same  class
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self . x) # 10
		print(self . __y) # 20
# End  of  the  class
t = Test() #  Constuctor  initializes  object  with  x = 10 , __y = 20
print('Outside') # Outside
print(t . x) #  10
print(t . Test_y) # 20
#print(t . __y) # Error :  private variable  __y   can  not  accessed  outside  the  class  as  it  is  not  visible
print(t . _dict) # {'x' : 10 , '_Test_y' : 20}
t . m1() #  Executes  method  m1()  of  Test  class
t . Test_m2() # Executes  private  method  m2()  of  Test  class  indirectly
#t . __m2() # Error :  private method  __m2()  can not  be  called  outside   the  class  as  it  is  not  visible
print('End') # End


'''
Outside
10
20
{'x':10,'Test_y':20}
m1 method
10
20
__m2 method
10
20
Back to m1 method
__m2 method
10
20
End
'''

# Find  outputs
class  c1:
	def __init__(self):
		self . x = 10  #  Adds  public  variable  'x'  to  object  self  with  value  10
		self . __x = 20 #  Adds  private   variable  'x'  to  object  self  with  value  20
		self . _x_ = 30  #  Adds  public  dunder  variable  'x'  to  object  self  with  value  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()  #  Constructor  initializes  object   with  x = 10 , _x = 20 , __x_ = 30
print(a . x) #  10
print(a . _x_) #  30
print(a . c1_x) #  20  i.e. Accessing  private  variable  indirectly
#print(a . __x) # Error :  private variable  is  not  visible  outside  the  class
a . m1() #  Executes  public  method  m1()  of  class  c1
a . __m1__() #   Executes  public  dunder  method  m1()  of  class  c1
a . c1_m1() #  Executes  private  method  m1()  indirectly
#a . __m1() # Error : private  method is  not  visible  outside  the  class and  hence  can  not  be  called


'''
10
30
20
public method
public Dunder method
private method
'''

'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() #  Executes  constructor wrt  first  object
a = None #  Executes  destructor  wrt  first  object  as  it  does  not  have  reference  (Ref  'a'  is  modified  to  object  None)
b = c1() #  Executes  constructor wrt  2nd  object
del    b #  Executes  destructor  wrt  2nd  object  as  it  does  not  have  reference  (Ref  'b'  is  deleted)
c = c1()  #  Executes  constructor wrt  3rd  object
c = c1() #  Executes  constructor wrt  4th  object  and  destructor  wrt  3rd  object  as  it  does  not  have  reference  (Ref  'c'  is  modified  to  4th  object)
d = c1() #  Executes  constructor wrt  5th  object
e = c1() #  Executes  constructor wrt  6th   object
# Executes  destructor  thrice  wrt  4th , 5th  and  6th  objects  as  their  references  are  lost  after  program  terminates

class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1() #  Creates  an  empty  c1  class  object
a . __del__(25)  #  Executes  destructor  and  25  is  passed  to  the  destructor
# Executes  destructor  before  object  is  lost  but  throws  error  as  arg  is  not  passed  to  the  destructor

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()  #   Creates  an  empty  c1  class  object
a . __del__(25)  #  Executes  destructor  and  25  is  passed  to  the  destructor
#  Executes  destructor  with  default  value  35  before  object  'a'  is  lost

'''
destructor :  25
destructor :  35
'''

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		b = c1()  #  #  Creates  an  empty  c1  class  object
    #  Executes  same  destructor  before  object  'b'  is  lost  which  leads  to  recursion  (infinite  recursion)
a = c1()  #  Creates  an  empty  c1  class  object
# Executes  destructor before  object  'a'  is  lost


'''
destructor
destructor
destructor
destructor
destructor
and so  on
'''

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self  #   Executes   destructor  before  object  is  deleted
	def  __del__(self):
		print('destructor')
		b = c1()  # Executes  constructor
a = c1() # Executes  constructor


'''
constructor
destructor
constructor
destructor
constructor
destructor
and  so  on

Finally  what  is  the  morale ?  --->  Do  not  create  object  in  constructor  and  destructor.
'''

class   c1:
	def  __del__(self):  # Discarded  due   to  another  destructor  in the  class
		print('1st  destructor')
	def  __del__(self):    # Discarded  due  to  another  destructor  in the  class
		print('2nd  destructor')
	def  __del__(self): #  Recognized  :as  it  is  the  last  destructor
		print('3rd  destructor')
# End  of  the  class
a = c1()
#  Executes  3rd destructor  before   object  'a'  is  lost

# Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()  #  Executes  constructor  only  once  as  only  one  object  is  created  with  3  references
del   a #  Object  is  not  lost  as  there  are  two  more  references  to  the  object  and  destructor  is  not  executed
print('Hello')
del   b  # Object  is  not  lost  as  there  is  one   more  reference  to  the  object  and  destructor  is  not  executed
print('Hi')
del   c #  Executes  destructor before  object  is  lost
print('Bye')
d = c1()  #  Executes  constructor
print('End')
 # Executes  destructor before  object  'd'  is  lost


# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]  #  Executes  constructor  thrice  as  3  objects  are  created
del  list  #   Executes  destructor  thrice  before  the  3  objects  are  lost  in  reverse order

'''
Object  is  created  at  address  :  Address of 1st c1 class  object  (may  be  1000)
Object  is  created  at  address  :  Address of 2nd c1 class  object   (may  be  2000)
Object  is  created  at  address  :  Address of 3rd c1 class  object   (may  be  3000)
Object  at  address  3000  is  lost
Object  at  address  2000  is  lost
Object  at  address  1000  is  lost
'''

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()  #  Creates  an  empty  c1  class  object
print(a . __del__()) #  Executes  destructor  which  returns  25  i.e.  print(25)
print('Hello')
del   a  #  Executes  destructor  before  object  'a'  is  deleted  and  25  gets  ignored


'''
destructor
25
Hello
destructor
'''

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() #  Executes  constructor  and  ignores  None
print(t . __init__())  #  Executes constructor  ands  prints  None
print(sys . getrefcount(t))  #  Number  of  references  to  object  't'  i.e. 1 + 1   = 2
print(t . __del__())  #  Executes  destructor  and  prints  25
print(sys . getrefcount(t))   #  Number  of  references  to  object  't'  i.e. 1 + 1   = 2
print('Bye')
# Destructor  is  executed  before  object  't'  is  lost

'''
Constructor : address of  object  't'
Constructor : address of  object  't'
None
2
Destructor : address of  object  't'
25
2
Bye
Destructor : address of  object  't'
'''

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()  #  Executes  constructor
	print(a)  #  _str_()  method  of   object  class  returns  type  and  address  of object  'a'
	print('Function  end')
	return   a  #  Object  'a'  is  returned  to  function  call   f1()
# Object  'a'  is   not  lost  becoz  it  has  ref  'b'
print('Program  Begin')
b = f1() #   b = a  --->  Ref  'b'  points to  object  'a'  which  is  returned  by  f1()  function
print(b)   #  _str_()  method  of   object  class  returns  type  and  address  of object  'a'
print('Program  End')
# Executes  destructor  before  object  'b'  is  lost

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()  #  Executes  constructor
        print('Function  end')
        return   a  #  Object  'a'  is   returned  to  function  call  f1()
#  Executes  destructor  before  object  'a'  is  lost
print('Program  Begin')
f1()
print('Program  End')

'''
Program Begin
Function Begin
Object  is    created
Function End
Object is Lost
Program End
'''

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()  #  Executes  constructor
        print('Function  end')
# Executes  destructor  before  object  'a'  is  lost
print('Program  Begin')
b = f1()   #  Function  returns  None  by  default  i.e.  b = None
print(b)   #  None
print('Program  End')

'''
Program Begin
Function Begin
Object is created
Function End
Object  is  lost
None
Program End
'''

# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):  #  self  is   object  x . a   and  'k'  is  object  'x'
		print('c1  class  object  is  created')
		self . b = k  #   x . a . b = x   --->  Adds  variable  'b'  to  object  x . a which  points  to  c2 class  object
		print('End  of  c1  class constructor')
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):  #  self  is   object  'x'
		print('c2  class  object  is  created')
		self . a = c1(self)   #   x . a = c1(x)  --->  Adds  variable  'a'  to  object  'x'  which  points  to  c1 class  object  and  executes  constructor  of  class  c1
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()  #  Executes  constructor  of class  c2
print('program end')
#  Executes  destructor  of  classes  c2  and   c1  before  objects  are  lost

'''
Program Begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
Program End
c2  class  object  is  lost
c1  class  object  is  lost
'''

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):  #  self  is  the  object  to  be  lost
		print('Destructor')
		global  b  #  Treats  ref  'b'  as  global  to  destructor
		b = self  #  Ref  'b'  points  to  the  object  which  is   to  be  lost
   # Object  'a'  is  not  lost  becoz  there is  global  ref 'b'  to  the object
a = c1()  #   Creates  an  empty  c1  class  object
del  a   #  Executes  destructor  before  object  'a'  is  lost
print('Hello')
# Destructor  is  not  executed  before  object  'b'  is  lost   becoz  it  is already executed


'''
Destructor
Hello
'''


