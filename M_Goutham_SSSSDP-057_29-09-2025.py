# Find  outputs
class  Rat: #Here class Rat is created
	def   __init__(self , nr1 = 22, dr1 = 7): #This is constructor with default values nr1 = 22, dr1 = 7
		self . nr = nr1 #Here nr is added to the object self with value nr1
		self . dr = dr1 #Here dr is added to the object self with value dr1
	def   __str__(self): #This is __str__ method
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #Here Rat class obj is created and constructor is Executed
b = Rat(9) #Here another Rat class object is created and constructor is executed 
c = Rat(5,  8) #Here another Rat class object is created and constructor is executed and default values are replaced with this values
d = Rat(dr1 = 9) #Here another Rat class object is created and constructor is executed with dr1 value is modified to 9
e = Rat(dr1 = 3 , nr1 = 2) #Here also rat class object is created and constructor is executed and also initializes the object with dr1 value 3 and nr1 value 2
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) #Here another rat class object is created and constructor is executed and also initializes the user input x and y
print('a  :  ' , a) #Here it prints a : 22 / 7
print('b  :  ' , b) #Here it prints b : 9 / 7 #default argument is replaced by positional argument 
print('c  :  ' , c) #Here it prints c : 5 / 8 #default arguments are replaced by positional arguments
print('d  :  ' , d) #Here it prints d : 22 / 9 
print('e  :  ' , e) #Here it prints e : 2 / 3
print('f  :  ' , f) #Here it prints f : user input for numerator / user input for denominator
c . __init__()  #Here we are explicitly calling the constructor with respect to obj c i.e modifies the default values with 5 and 8
print('c  :  ' , c) #Prints the c : 5 / 8
a . __init__(3.8  , 4.6) #Explicit call of constructor 
print('a  :  ' , a) #prints a : 3.8 / 4.6
#g = Rat(nr1 = 9 , 5) #Error #When argument 1 is keyword argument then next argument should also be keyword argument only
h = Rat(nr = 9 , dr = 5) #Error #arguments are not valid not nr it is nr1 and not dr it is dr1




# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1): #Here constructor with 3 arguments 
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) #Here obj for Date class is created and constructor is executed and also values for instance variables have initialized with positional arguments
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26) #Here obj for Date class is created and constructor is executed and also values for instance variables have initialized with keyword arguments
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) #Here obj for Date class is created and constructor is executed and also values for instance variables have initialized with keyword arguments
print('a  :  ' , a . __dict__) #Here we are printing the instance variables of obj a with values in the form of key-values pairs
print('b  :  ' , b . __dict__) #Here we are printing the instance variables of obj b with values in the form of key-values pairs
print('c  :  ' , c . __dict__) #Here we are printing the instance variables of obj c with values in the form of key-values pairs
d = Date() #Error #obj is created but here constructor is excepting 3 arguments
e = Date(dd = 30 , mm = 4 , yy = 2022) #Here we are printing the instance variables of obj e with values in the form of key-values pairs
#f = Date(dd1 = 26 , mm1 = 8 , 2023) #Error #After keyword arguments we cannot use positional arguments
'''outputs:
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
'''



# Find  outputs (Home  work)
class  c1:
	def  __init__(self): #Here we have defined the constructor and it is returning 25
		print('c1  class constructor')
		#return 25
class  c2:
	def  __init__(self): #Here we have defined the constructor and it is returning None
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self): #Here we have defined the constructor
		print('c3  class  constructor')
# End  of  class
a = c1() #Error #Here we have created the obj for c1 class and constructor is exeecuted but raises error constructor cannot return int obj 
b = c2() #Here we have created the obj for c2 class and constructor is executed and returns None
print(b)
print(b . __init__()) #Here we are printing the constructor explicitly with respect to obj b
c = c3() #Here we are creating the c3 class obj and constructor is executed 
print(c . __init__()) #Here we are calling the constructor explicitly with respect to obj c
'''outputs:
c1 class constructor
c2 class constructor
Type and address
c2 class constructor 
None
c3 class constructor
c3 class constructor
'''




# Find  outputs (Home  work)
class  c1:
	def  __init__(self): #Here constructor is defined
		print('Constructor')
		b = c1() #Leads to recursion 
# End  of  class
a = c1() #Here obj is created for c1 class and constructor is executed 
'''
constructor
recursion as inside constructor one more object is created which leads to recursion 
'''



#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self): #It is a constructor 
        print('Constructor')
        self . x = 10 #Here variable x is added to obj with value 10
        self . y = 20 #Here variable y is added to obj with value 20
class c2:
    def  init(self): #It is a regular method as there are no '__' before init and after init so treated as regular method
        print('Method')
        self . x = 30 #Here variable x is added to obj with value 30
        self . y = 40 #Here variable y is added to obj with value 40
a = c1() #Here obj is created and constructor is executed
print(a . __dict__) #Prints the instance variables of obj in the form of key-value pairs
b = c2() #Here obj is created 
print(b . __dict__) #Here empty dict is printed i.e {}
b . init() #Here init method is called 
print(b . __dict__) #Here instance variables of obj b is printed in the form of key-value pairs
'''outputs:
Constructor
{'x' : 10, 'y' : 20}
{}
Method
{'x' : 30, 'y' : 40}'''






# Find  outputs (Home  work)
class   c1:
        def   __init__(self): #Here constructor is defined
                self . a = 10 #Here variable a is added to obj with value 10
        def   m1(self): #Here it is method m2 is defined
                self . b = 20 #Here variable b is added to obj with value 20
#End  of  class  c1
class   c2: #Here c2 class is created
        def  m3(self): #Here m3 method is defined
                x . e = 50 #Variable e is added to obj x with value 50
# End  of  class  c2
def   f1(): #Here regular function is defined 
        x . c = 30 #Error
#  End  of  function  f1
x = c1() #Here obj is created for c1 class and constructor is executed 
print(x . __dict__) #Prints {'a': 10}
x . m1() #Here m1 method of c1 class is called
print(x . __dict__) #prints {'a': 10, 'b': 20}
f1() #Here f1 function is called
print(x . __dict__) #prints {'a': 10, 'b': 20, 'c':50}
x . d = 40 #Here variable d is added to obj x with value 40
print(x . __dict__) #{'a': 10, 'b': 20, 'c':50, 'd': 40}
y = c2() #Here c2 class obj is created
y . m3() #Here m3 method of c2 class is called
print(x . __dict__) #prints {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1() #Here another object is created for c1 class and constructor is executed
print(z . __dict__) #Prints {'a': 10}






# Find  outputs  (Home  work)
class   c1: #Here c1 class is created
	def   __init__(self): #Here constuctor is defined
		self . x = 10 #Here variable x is added to obj with value 10
		self . y = 20 #Here variable y is added to obj with value 20
		self . z = 30 #Here variable z is added to obj with value 30
#end  of  the  class
a = c1() #Here c1 class object is created and constructor is executed and also initializes the obj
b = c1() #Here c1 class object is created and constructor is executed and also initializes the obj
print(a . __dict__) #prints {'x': 10, 'y': 20, 'z': 30}
print(b . __dict__) #prints {'x': 10, 'y': 20, 'z': 30}
del  a . x #Here variable x is deleted from the obj a 
del  b . y #Here variable y is deleted from the obj b
print(a . __dict__) #Prints {'y': 20, 'z': 30}
print(b . __dict__) #Prints {'x': 10, 'z': 30}
print(a . x) #Error #x is already deleted
print(b . y) #Error #y is already deleted


#  Find  outputs (Home  work)
class   c1:  #Here c1 class is created
	def  __init__(self): #Here constructor is defined but discarded
		print('1st  constructor') 
	def  __init__(self): #Here another constructor is defined but discarded
		print('2nd  constructor')
	def  __init__(self): #Here another constructor is defined but it is recognized
		print('3rd  constructor')
# End  of  the  class
a = c1() #Here c1 class obj is created and 3rd constructor is executed
'''output:
3rd constructor'''



#  Find  outputs  (Home  work)
class   c1: #Here c1 class is created
	def  __init__(self): #Here constructor is defined but discarded
		print('No  argument  constructor')
	def  __init__(self , x): #Here constructor is defined with 1 argument but discarded 
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y): #Here constructor is defined with 2 argument is recognized
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Here c1 class object is created and 2 argument constructor is executed
b = c1(30) #Error #as 2 argument constructor will execute so gives error
c = c1() #Error #as 2 argument constructor will execute so gives error
'''outputs:
Two argument constructor : 10 20
'''


#  Find  outputs
class   c1:
	def  __init__(self): #Here constructor is defined with 0 arguments but discarded
		print('No  argument  constructor')
	def  __init__(self , x): #Here constructor is defined with 1 arguments but discarded
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200): #Here constructor is defined with 2 arguments it is recognized
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Here c1 class object is created and constructor is executed
b = c1(30) #Here c1 class object is created and constructor is executed with positional argument 30 and default arguments 
c = c1() #Here c1 class object is created and constructor is executed with two default arguments 
'''outputs:
Two  argument  constructor : 10 20
Two  argument  constructor : 30 200
Two  argument  constructor : 100 200
'''



# What  happens  when  function  and  class  have  same  name ?
def   f1(): #Here regular function is defined 
	print('Function')
	return  25 #function returns 25
class   f1: #f1 class is created 
	def  __init__(self): #Here constructor is defined
		print('Constructor')
#end of the  class
a = f1() #f1 class object is created and constructor is executed
print(a) #Prints Type and address
'''
outputs:
Constructor
Type and address'''



# Find  outputs (Home  work)
class    c1: #Here c1 class is created 
	def   __init__(self): #Here constructor is defined
		print('Constructor')
def  c1(): #Here regular c1 function is defined
	print('Function')
#end of the  class
a = c1() #Here ref a points to result of c1() function
print(a) #Function
'''
outputs:
Function
None'''




# Find outputs  (Home  work)
class    c1: #Here c1 class is created
        def  __init__(self): #Here constructor is defined
                print('Constructor')
def    c1(x): #Here regular function is defined with argument x
        print('Function : ' , x)
# End  of  class  c1
#a = c1() #Error #as c1 function expects 1 argument but no argument is given
b = c1(25) #Ref b points to result of c1 function
print(b) #Prints Function : 25
		 #None



#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')




#  Find  outputs (Home  work)
from  prog9a  import  c1 #Here we are importing the c1 class from prog9a 
class   c1: #Here c1 class is created
	def  __init__(self): #Here constructor is defind
		print('c1  class  of  prog9b')
a = c1() #Here c1 class object is created and constructor is executed
'''output:
c1  class  of  prog9b''' #After importing we have defined again created the c1 class so current program class c1 is used if it is not there then imported class

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()



#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
import prog9a #How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self): #Here constructor is defined
		print('c1  class  of  prog9d')
a = c1() #How  to  create  c1  class  object  of  current  module
b = prog9a.c1() #How  to  create  c1  class  object  of  prog9a
'''outputs:
c1  class  of  prog9d
c1  class  of  prog9a'''

								#or
				
#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c #How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self): #Here constructor is defined
		print('c1  class  of  prog9d')
a = c1() #How  to  create  c1  class  object  of  current  module
b = c() #How  to  create  c1  class  object  of  prog9a
'''outputs:
c1  class  of  prog9d
c1  class  of  prog9a'''




'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a #How  to  import  prog9a
class   c1: 
	def  __init__(self):
		print('c1  class  of  prog9e')
a = c1() #How  to  create  c1  class  object  of  current  module
b = prog9a.c1() #How  to  create  c1  class  object  of  prog9a




# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  to  10
		self.__y = 20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable  'y'
		self.__m2() #How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) #How  to  print  variable  'x'
print(t._Test__y) #How  to  print   variable  'y'
#print(t . __y) #Error #we cannot use private variable outside the class
print(t . __dict__) 
t.m1() #How  to  call  method  m1()
t._Test__m2() #How  to  call   method  m2()
#t . __m2()  #Error #we have to call the priavte method using class name 
print('End')
'''outputs:
Outside
10
20
{'x':10,'_Test__y':20}
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
End'''




#  Find  outputs
class  c1:
	def __init__(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a.__x__) #How  to  print  public  dunder  variable  'x'
print(a._c1__x) #How  to  print   private  variable  'x'
#print(a . __x) #Error #We cannot use private variable outside the class if at all we want to use we have use with class name
a.m1()        #How  to  call  public  method  m1()
a.__m1__()        #How  to  call  public  dunder  method  m1()
a._c1__m1()        #How  to  call  private  method  m1()
#a . __m1() #Error #We have to call the private method outside class with obj._classname__methodname() 
'''outputs:
10
30
20
public method
public dunder method
private method
'''


'''
Tricky  program
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1: #class c1 is created
	def   __init__(self): #Constructor is defined
		print('Object  is  created  at  address  :  ' , id(self)) 
	def   __del__(self): #Destructor is defined 
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() #Here object is created and constructor is executed
a = None #Ref a points to None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()
'''outputs:
Object is created at address : 1000
Object at address 1000 is lost
Object is created at address : 2000
Object at address 2000 is lost
Object is created at address : 3000
Object is created at address : 3000
object at address 3000 is lost
Object is created at address : 4000
Object is created at address : 5000
object at address 3000 is lost
object at address 4000 is lost
object at address 5000 is lost
'''

'''
Objects  :   a      b      c      d      e

addresses: 1000   2000   3000    4000   5000

'''



# Identify  Error (Home  work)
class   c1: #Here c1 class is defined
	def  __del__(self , x): #Here distructor is defined with 1 argument but destructor cannot take arguments but here given
		print('destructor : ' ,  x)
a = c1() #Here object is created 
a . __del__(25) #Here we are calling the distructor explicitly #destructor : 25 but not recommended
'''outputs:
destructor : 25
throws Error in destructor execution'''




# Find  outputs (Home  work)
class   c1: #Here c1 class is defined
	def  __del__(self , x = 35): #Here again destructor is defined with 1 default argument
		print('destructor : ' , x) 
a = c1() #Here object is created
a . __del__(25) #Here destructor is called explicitly 
'''outputs:
destructor : 25
destructor : 35'''



# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1() #Recursion 
a = c1() #Object is created and soon before object lost destructor is executed and in the destructor again object is created after destructor again destructor is executed infinite loop


# Find  outputs (Home  work)
class   c1: #Here class c1 is created
	def  __init__(self): #Here constructor is defined
		print('constructor')
		del  self #Here object is deleted and destructor is executed
	def  __del__(self): #Here destructor is defined
		print('destructor')
		b = c1() #Here obj is created and constructor is executed
a = c1() #Here object is created and constructor is executed
#Here in loop constructor and destructor are executing 
'''outputs:
Constructor
destructor
soo on'''


#  Find  outputs( Home  work)
class   c1: #Here c1 class is created
	def  __del__(self): #Here destructor is defined #But discarded
		print('1st  destructor')
	def  __del__(self): #Here another destructor is defined #But discarded
		print('2nd  destructor')
	def  __del__(self): #Here another destructor is defined #But discarded
		print('3rd  destructor')
# End  of  the  class
a = c1() #Here obj is created and soon after program terminates obj is deleted and before object deletion 3rd constructor is executed
'''output:
3rd destructor'''


#Find  outputs (Home  work)
class   c1: #Here c1 class is created
	def   __init__(self): #Here constructor is defined
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self): #Here destructor is defined
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() #Here c a b are pointing to the c1 class object and constructor is executed
del   a # # ref a is deleted 
print('Hello')
del   b #Ref b is deleted
print('Hi')
del   c #Ref c is deleted and destructor is executed
print('Bye')
d = c1() #Here again c1 class object is created and constructor is executed
print('End')
'''output:
Object is created at address : 1000
Hello
Hi
Object at address 1000 is lost
Bye
Object is created at address : 1000
End
Object at address 1000 is lost
'''


# Find  outputs(Home  work)
class  c1: #Class c1 is created
        def     __init__(self): #Here constructor is defined
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self): #Here destructor is defined
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()] #Here ref list is pointing to 3 c1 class objects and constructor is executed 3 times
del  list #Here list is deleted and constructor is executed 3 times
'''outputs:
Object  is  created  at  address  :   1000
Object  is  created  at  address  :   2000
Object  is  created  at  address  :   3000
Object  at  address  1000  is  lost 
Object  at  address  2000  is  lost 
Object  at  address  3000  is  lost '''


# Find  outputs  (Home  work)
class   c1: #Here class c1 is created
	def  __del__(self): #Here destructor is defined
		print('destructor')
		return  25 #destructor is returning a value but ignored if its automatically called but for explicit calls 25 is returned
a = c1() #Here c1 class object is created
print(a . __del__()) #Here we are calling the constructor explicitly so output: destructor 
																				# 25
print('Hello') 
del   a #Here obj is deleted and constructor is executed
'''outputs:
destructor
25
Hello
destructor
25 is ignored'''