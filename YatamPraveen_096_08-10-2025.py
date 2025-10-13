# Find outputs (Home work)
class outer:
	def init (self):
		print('Outer class object is created')
def ml(self):
print('Outer class method')
class inner:
def init (self):
print('Inner class object is created')
def ml (self):
print('Inner class method')
#end of the class
o outer() # Executes outer class constuctor
m1() # Executes method of outer class as outer class object '0'# Find  outputs  (Home  work)

class   outer:
	def  __init__(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
o = outer()                 # How  to  call  m1()  method  of  outer  class
o.m1()      
i = outer.inner()           # How  to  call  m1()  method  of  inner  class
i.m1()
o = outer()                 # How  to  call  m1()  method  of  inner  class  in  another  way
i = o.inner()
i.m1()          
outer.inner().m1()          # How  to  call  m1()  method  of  inner  class  in  one  more  way
i=inner()                   # Error as inner is not defined







# Find  outputs  (Home  work)

class   emp:
	def __init__(self):
		# How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		self.d = self.date()			# How  to  create  date  class  object
	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print("Emp No:", self.empno)
		print("Emp Name:", self.ename)
		print("Salary:", self.sal)
		self.d.disp()				# How  to  call  disp()  method  of  date  class
	class   date:
		def __init__(self):
			# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			# How  to  print  dd , mm , yy  of  object  self
			print("Date of Joining: {}/{}/{}".format(self.dd, self.mm, self.yy))
# End  of  the  class
# How  to  call  disp()  method  of  emp  class
e = emp()
e.disp()







# Find outputs (Home  work)

class  outer:
	def __init__(self):
		self.x = 25			# How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1 = self.inner1()		# How  to  create  inner1  class  object
		self.i2 = self.inner2()		# How  to  create  inner2  class  object
	def  disp(self):
		print(self.x)
	class inner1:
		def disp(self):
			print('1st  inner  class  method')
	class inner2:
		def disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer()
o.disp()				# How  to  call   disp()  method  of outer  class
o.i1.disp()				# How  to  call   disp()  method  of inner1  class
o.i2.disp()				# How  to  call   disp()  method  of inner2  class








# Find  outputs  (Home  work)

class c1:
	def __init__(self):
		print('outer  class  c1  constructor')
	class c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
# How  to  create  c1  class  object
o1 = c1()      # creates object of outer class c1
# How  to  create  inner  c2  class  object
i1 = c1.c2()   # creates object of inner class c2 inside class c1
# How  to  create  outer  c2  class  object
o2 = c2()      # creates object of outer (separate) class c2







# Find  outputs  (Home  work)

class c2:
	def __init__(self):
		print('outer  class  constructor')

	class c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
o = c2()			# How  to  create  outer  c2  class  object
i = c2.c2()			# How  to  create  inner  c2  class  object
o1 = c2()			# How  to  create  inner  c2  class  object  in  another  way
i1 = o1.c2()







# Find  outputs (Home  work)
class c1:
    x = 10                     # static variable (class variable)
    def __init__(self):
        self.y = 20            # instance variable
a = c1()
b = c1()
a.x += 1        # creates instance variable x = 11 for object 'a'
b.y += 1        # increases b.y → 21
print(a.x)      # 11
print(a.y)      # 20
print(b.x)      # 10
print(b.y)      # 21
print(c1.x)     # 10
print(a.__dict__)  # {'y': 20, 'x': 11}
print(b.__dict__)  # {'y': 21}
print(c1.__dict__) # {Environmental Variables and static variable}








# Find  outputs (Home  work)

class c1:
	x = 10
	def m1(self):
		self.x = 20     # creates instance variable x for object 'a'.
a = c1()
a.m1()
print(c1.x)   # 10
print(a.x)    # 20







# Find  outputs (Home  work)

class c1:
    x = 10
    def __init__(self):
        self.y = 20
    @classmethod
    def m1(cls):
        cls.x = 30
        cls.y = 40      # adds a class variable 'y'
# End of the class
a = c1()
b = c1()
c1.m1()
print(a.x)      # 30  
print(a.y)      # 20  
print(b.x)      # 30  
print(b.y)      # 20 
print(c1.x , c1.y)  # 30 40  
print(cls.x , cls.y)  # Error as cls is not defined 
print(self.x , self.y)  # Error as self is not defined 






#  Find  outputs

class c1:
	@staticmethod
	def m1(self):
		print(self)
#  End  of  the   class
c1.m1(25)        # 25
a = c1()
a.m1(35)         # 35







#  Find  outputs

class c1:
	def m1(self):
		print(self)
#  End  of  the   class
c1.m1(25)                           # Error as we cannot call instance method on class without instance
a = c1()
a.m1()                              # prints the instance reference
a.m1(35)                            # Error as m1() takes 1 positional argument but 2 were given


#  Find  outputs

class c1:
	@staticmethod
	def m1(self):
		print('static  method')
		print(self)
	
	def m1(self):
		print('static / instance  method')
		print(self)
#  End  of the   class
c1.m1(25)  # Error m1() takes 1 positional argument but 2 were given
a = c1()
a.m1()     # static / instance  method







# How  to  access  static  variable  in  different  ways

class c1:
    x = 25  # static variable
    def __init__(self):
        # How  to  print  static  variable  'x'
        print(c1.x)  # access via class inside instance
        # How  to  print  static  variable  'x'  in  another  way
        print(self.x)  # access via instance inside instance
    def m1(self):
        # How  to  print  static  variable  'x'
        print(c1.x)  # access via class inside instance method
        # How  to  print  static  variable  'x'  in  another  way
        print(self.x)  # access via instance inside instance method
    @classmethod
    def m2(cls):
        # How  to  print  static  variable  'x'
        print(cls.x)  # access via class inside classmethod
        # How  to  print  static  variable  'x'  in another way
        print(c1.x)  # access via class inside classmethod
    @staticmethod
    def m3():
        # How  to  print  static  variable  'x'
        print(c1.x)  # access via class inside staticmethod
# End  of  the  class
# How  to  print  static  variable  'x'
print(c1.x)        # 25  (access via class)
obj = c1()         # __init__ prints x via class and self
# How  to  print  static  variable  'x'  in  another  way
print(obj.x)       # 25  (access via instance)
# How  to  call  method  m1()
obj.m1()           # prints x via class and via self
# How  to  call  method  m2()
c1.m2()            # prints x via cls and via class
# How  to  call  method  m3()
c1.m3()            # prints x via class







# How  to  add  static  variable  to  the  class  at  different  locations  of  the program

class c1:
    a = 10			# How  to  add  static  variable  'a'  with  value  10
    def __init__(self):
        c1.b = 20		# How  to  add  static  variable  'b'  with  value  20
        self.c = 30		# How  to  add  instance  variable  'c'  with  value  30
        # cls.k = 25 → use class name
        c1.k = 25
    def m1(self):
        c1.d = 40		# How  to  add  static  variable  'd'  with  value  40
        self.e = 50		# How  to  add  instance  variable  'e'  with  value  50
    @classmethod
    def m2(cls):
        cls.f = 60		# How  to  add  static  variable  'f'  with  value  60
        c1.g = 70		# How  to  add  static  variable  'g'  with  value  70  in  another  way
    @staticmethod
    def m3():
        c1.h = 80		# How  to  add  static  variable  'h'  with  value  80
#End  of  the  class

print('Begin')
print(c1.__dict__)     #{'__module__', 'a': 10, ...}
print()
x = c1()
print('Constructor')
print(c1.__dict__)     #{'__module__', 'a':10, 'b':20, 'k':25, '__init__', ...}
print()
x.m1()			# How  to  call  m1()  method
print('Instance  method  m1')
print(c1.__dict__)     #{'__module__', 'a':10, 'b':20, 'k':25, 'd':40, ...}
print()
c1.m2()			# How  to  call  m2()  method
print('class  method   m2')
print(c1.__dict__)     #{'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, ...}
print()
# How  to  call  m3()  method
c1.m3()
print('static   method   m3')
print(c1.__dict__)     #{'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, ...}
print()
c1.i = 90		# How  to  add  static  variable  'i'  with  value  90
x.j = 100		# How  to  add  instance  variable  'j'  with  value  100







# Find  outputs  (Home  work)

class c1:
    a, b, c = range(1, 4)
# How  to  print  variable  'b'
print(c1.b)   # 2
# How  to  print  variable  'c'
print(c1.c)   # 3








# Find outputs (Home work)

class Test:
    @classmethod
    def get1(cls):
        cls.x = int(input('Enter any number    :  '))  # input 10

    def get2(self):
        self.y = int(input('Enter any number  :  '))     # inputs 20 / 40 / 60
        self.z = int(input('Enter any number  :  '))     # inputs 30 / 50 / 70

    def compute(self):
        Test.x += 1        # increments class variable x
        self.y += 1        # increments instance y
        self.z += 1        # increments instance z
        self.x = Test.x + 1  # creates instance variable x

    def disp(self):
        print(Test.x, self.y, self.z, self.x, sep='\t')
# End of the class
Test.get1()       # Enter 10
a = Test()
b = Test()
c = Test()
a.get2()          # Enter 20, 30
b.get2()          # Enter 40, 50
c.get2()          # Enter 60, 70
a.compute()
b.compute()
c.compute()
a.disp()          # 13    21    31    14
b.disp()          # 13    41    51    14
c.disp()          # 13    61    71    14







'''
Write a program to add two Vector objects

1) What are the names of objects ?  ---> x , y   and  z

2) What are the names of lists held by each object ?  --->  x.a , y.a , z.a

3) How to access elements of 1st list ?  ---> x.a[i]
   How to access elements of 2nd list ?  ---> y.a[i]

4) How to access static variable 'n' ?  ---> vector.n
'''

class vector:
    # Static variable n to store number of elements
    n = 0
    @staticmethod
    def get1():
        # How to read number of elements into variable 'n'
        vector.n = int(input("Enter number of elements: "))
    def get2(self):
        # How to read the list into the object
        self.a = []
        print(f"Enter {vector.n} elements for the vector:")
        for i in range(vector.n):
            self.a.append(int(input()))
    def add(self, x, y):
        # How add the lists held by objects 'x' and 'y' and store the results in list held by owner object
        self.a = []
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])

# How to call get1() method
vector.get1()   # reads vector.n
# How to read the list into 1st object
x = vector()
x.get2()        # reads x.a
# How to read the list into 2nd object 'y'
y = vector()
y.get2()        # reads y.a
# How to add the lists held by objects 'x' and 'y' and store the results in list of 3rd object 'z'
z = vector()
z.add(x, y)
# How to print the list of 3rd object
print("Sum of two vectors:")
print(z.a)     # prints list of sums








'''
Write a program to print only static variables but not environment variables of classname.__dict__
Hint: Use startswith() and endswith() methods
'''

class c1:
    x = 1
    y = 2
    z = 3
# End of the class
static_vars = {}
for key, value in c1.__dict__.items():
    if not (key.startswith('__') and key.endswith('__')):
        static_vars[key] = value
print("static variables of class c1 :", static_vars)








# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)

k = 80  # What is variable 'k' ---> global variable
class c1:
    x = 10  # What is variable 'x' ---> class variable
    def m1(self):
        self.y = 20   # What is variable 'y' ---> instance variable
        z = 30        # What is variable 'z' ---> local variable
        c1.m = 40     # What is variable 'm' ---> class variable
        print("Inside m1():")
        print("z (local variable) =", z)
        print("self.y (instance variable) =", self.y)
        print("c1.m (class variable) =", c1.m)
# Adding class variable outside class
c1.l = 90  # What is variable 'l' ---> class variable
def f1():
    a = c1()
    a.p = 50       # What is variable 'p' ---> instance variable
    c1.q = 60      # What is variable 'q' ---> class variable
    s = 70         # What is variable 's' ---> local variable
    print("Inside f1():")
    print("a.p (instance variable) =", a.p)
    print("c1.q (class variable) =", c1.q)
    print("s (local variable) =", s)
    return a  # return object a to use outside

# Creating objects
b = c1()
b.n = 100  # What is variable 'n' ---> instance variable
# Call methods and function
obj_a = f1()
obj_b = b
obj_b.m1()
# Print global variable
print("k (global variable) =", k)
# Print class variables
print("c1.x =", c1.x)
print("c1.m =", c1.m)
print("c1.l =", c1.l)
print("c1.q =", c1.q)
# Print instance variables
print("obj_a.y =", getattr(obj_a, 'y', 'Not set'))
print("obj_a.p =", getattr(obj_a, 'p', 'Not set'))
print("obj_b.y =", getattr(obj_b, 'y', 'Not set'))
print("obj_b.n =", getattr(obj_b, 'n', 'Not set'))

# Creates inner class object wrt outer class object and executes i * 1 = 0 . inner() inner class constuctor
Executes method of inner class as 11 inner class object 11. m1() # is
Creates inner class object thru outer class name and executes 12 outer inner() # inner class
constuctor
12 m1 () # Executes method of inner class as 12 is inner class object
constuctor
13 outer() inner() # Creates inner class object wrt outer class object and executes inner class
13.m1() # Executes method of inner as 13 class is inner class object
#i inner() # Error: Can not inner class object directly without outer class object (or) outer class
name






# Find outputs (Home work)
class emp:
def init (self): # 'e' self is object
self empno = 25 # Adds variable empno to object 'e' with value 25
self ename = 'Rama Rao # Adds variable ename to object 'e' with value 'Rama Rao'
sal 10000.0 # Adds variable sal to self object 'e' with value 10000.0
self dob = self 'e date() # Adds variable dob to object and constructor of date class
initializes object with dd 15 mm = 8 , yy = 1947
def 'e' disp(self): # self is object
print('Employee Number: self empno)
print('Employee Name : self ename)
print('Salary : self. sal)
self dob disp() # Executes method of date class as e dob is date class object
def
class date:
init (self): e is object dob # self
self dd = 15 # variable dd to object e dob with value 15 Adds
self mm to object e dob with value 8 mm = 8 # Adds variable
self to object e dob with value 15 yy = 1947 # Adds variable yy
def disp (self): # self is object
print (F'Date of birth: (self dd}-{self mm}-{self yy)')
e
dob
#End of the class
Constructor initializes object with empno 25, ename = 'Rama Rao', sal = 10000.0 and dob object e = emp () # with 3 values
e disp() # Executes method of emp class as e is emp class object






# Find outputs (Home work)
class outer:
def
# self is object '0' init (self):
'x' self. x = 25 # Adds variable to object '0' with value 25
self yself innerl() #Adds variable 'y' object with 1st to '0' inner class object
object '0' with 2nd Adds variable 'z' to inner class object self. z self inner2() #
def disp(self): # self
print(self. x) # 25
is
object
class inner1:
def disp(self): #self is object print('1st inner class method')
class inner2:
def disp(self): #self
is object o.Z
class method') print('2nd inner
#end of the class
o outer() # Constructor initializes object with x = 25 , y = 1st inner class object z = 2nd inner class
object
disp() # Executes method of outer class аз 'o' is outer class object.
Y
disp() # Executes method of 1st inner class as 1st inner class object 13
z. disp() # Executes method of inner class 2nd as 2nd inner class object 13






# Find outputs (Home work)
class c1:
def
init (self):
print('outer class c1 constructor')
class c2:
def init (self):
print('inner class c2 constructor')
#end of the class
class c2:
def __init__(self):
print('outer class c2 constructor')
#end of the class
a = c1 () #
Executes constructor of class c1
bc1 c2 ()
# Executes constructor of inner class c2
C = c2 () #
Executes constructor of outer class c2






# Find outputs (Home work)
class c1:
# Adds static variable 'x' to class c1 with value 10 x = 10
def init (self):
selfy 20 # Adds variable 'y' to object self with value 20
a = c1() # Constructor initializes object with y = 20
# b = c1 () Constructor initializes object with y = 20
a x += 1 # a.x = a x + 1 ---> a. x = 10 + 1 = 11 i.e. Adds variable 'x' to object 'a' with value 11
by+=1# Increments by by 1
'a' i.e. 11 print(ax) # Variable 'x' of object
print (a y) #Variable 'y' of object 'a' i.e. 20
print (b x) # static variable becoz there is no variable 'x' in object 'b' i.e. 10
print (b y) # Variable 'y' of object 'b' i.e. 21
print (c1 x) # static variable 'x' of class c1 i.e. 10
print (a dict) # {'y': 20, 'x': 11}
print (b dict) # {'y': 21)
print (c1 dict) # {'x': 10, Ev's)






# Find outputs (Home work)
class c1:
x = 10 # Adds static variable 'x' to class cl with value 10
def ml (self): # self 13 object 'a'
self. x = 20 # Adds variable 'x' to object 'a' with value 20
a = c1() # Empty object
'a' c1 class object a m1() # Executes method of class cl as
i.e. 10 print(cl. x) # static variable of class c1
'a' i.e. 20 print(ax) # variable 'x' is of object






# Find outputs (Home work)
class c1:
x = 10 # Adds static variable 'x' to class c1 with value 10
def init (self):
self. y = 20 # Adds variable 'y' to object self with value 20
@classmethod
def ml (cls):
cls. x = 30 # Modifies static variable 'x' to 30
cls y = 40 # Adds static variable 'y' to class c1 with value 40
#End of the class
a = c1() # Constructor initializes object with y = 20
b = c1() # Constructor initializes object with y = 20
c1 m1() # Executes class method of class c1
print(ax) # static variable becoz there 18 no variable 'x' in object 'a' 1.e. 30
print(ay) # Variable 'y' of object 'a' 20 1.e.
print (bx) # static variable becoz there variable 'x' in object 'b' is no 1.e. 30
print(by) # Variable 'y' of object 'b' i.e. 20
print (c1x, cl. y) # static variables of class c1 i.e. 30 <space> 40
#print (clsx, cls y) # Error: No cls outside the class
#print(self, selfy) # Error: No self outside the class






# Find outputs
class c1:
@staticmethod
def ml (self):
print(self)
class #End of the
# Executes c1. m1 (25) static method of class c1 and self 13 25
Empty object a = c1() #
# Executes static a m1 (35) method of class c1 and self 13 35






# Find outputs
class c1:
def m1(self):
print(self)
# End of the class
c1 m1 (25) # Treats m1 as static method becoz it is called thru classname
a = c1() # Empty object
a m1() # Treats m1 as instance method becoz it is called wrt object
#a m1 (35) #self is object 'a' and 35 is an exces3 argument






# Find outputs
class c1:
@staticmethod
def m1 (self): # Discarded: Another method 13 defined with same name print('static method')
print(self)
def
m1 (self): # Recognized: The last method
print('static / instance method')
print(self)
# End of the class
c1 m1 (25) # Treats m1 as static method as m1() 13 called thru classname
a = c1 () # Empty object
a m1 () # Treats m1 instance method as m1() is called thru object 'a'






# How to access static variable in different ways ?
class c1:
# Adds static variable 'x' to class c1 with value25 x = 25
def init (self): # self is object 'a'
print (c1 x) # Static variable 'x' of class c1 i.e. 25
print(self x) # Static variable 'x' : There is no variable 'x' in object 'a' i.e. 25
#print(x) # Error: No local variable in the constructor
def m1 (self): # self is object 'a'
print (c1 x) # Static variable 'x' of class c1 i.e. 25
print(self x) # Static variable 'x' : There is no variable 'x' in object 'a' i.e. 25
#print (cls x) # Error: No cls in ml () method
@classmethod
def m2 (cls):
print (c1 x) # Static variable 'x' of class c1 i.e. 25
print (cls x) # Static variable 'x' of class c1 i.e. 25
#print(self x) # Error: No self on m2() method
@staticmethod
def m3():
print (c1 x) # Static variable 'x' of class c1 i.e. 25
#print (cls x) # Error: No cls in m3() method
#print(self x) # Error: No self in m3 () method
#End of the class
a = c1 () # Executes constructor
print (c1 x) # Static variable 'x' of class c1 i.e. 25
x) print(a # Static variable 'x' : There 18 no variable 'x' in object 'a' i.e. 25
#print(x) # Error: No global variable 'x' in the program
#print(self x) # Error : No self outside the class
#print (cls x) # Error: No cls outside the class
m1() #
a Executes method of class c1 as 'a' is c1 class object
c1 m2 () # Executes class method of class c1
c1 m3 () # Executes static method of class c1






#Tricky program
# What are the outputs if inputs are 10 20 30 40, 50, 60, 70 (Home work)
class Test:
@classmethod
def getl (cls):
clsx int (input('Enter any number : ')) # Adds static variable to class c1 with
user input 10
def get2 (self):
selfy int(input('Enter any number : ')) # Adds instance variable 'y' to object self with
user input
self
zint (input('Enter any number : ')) #Adds instance variable 'z' to object self with
user input
def compute (self):
Test x += 1 # Increments static variable 'x' of class c1 by 1
self y += 1 # Increments instance variable 'y' of object self by 1
self. z += 1 # Increments instance variable 'z' of object self by 1
the result
self. x += 1 # self. x = self. x + 1---> # Adds instance variable 'x' to object self with
def disp (self):
print (Test x, self. y, self Z, self. x, sep = '\t')
#End of the class
Test get1() # Executes class method of class Test
a Test() # Three empty Test class objects
b = Test()
c = Test()
a get2() # Reads inputs to object 'a'
b get2() # Reads inputs to object 'b'
C get2() # Reads inputs to object 'c'
a compute()
b compute()
C compute()
21
31
12
a disp() # 13
b disp() # 13 41 51 13
c. disp()
#
13
61
71
14






Write a program to print only static variables but not environment variables of classname dict
Hint: Use startswith() and endswith() methods
class c1:
x = 10
y = 20
z = 15
#End of the class
a = {} # Empty dictionary
b = c1 dict # Dictionary of static variables of class cl and Ev's
for key in b:
if not key startswith('') and not key endswith(' '):
a [key] = b [key]
print('static variables of claзз c1: a)






# What are k, 1, x, y, z, m, n, p,q, s? (Home work)
class c1:
x = 10 # 'x' is static variable becoz it is initialized in the class
def m1 (self):
self. # 'y' 19 instance variable becoz object self is used y = 20
# 'z' is local variable becoz it is initialized in the method without any prefix z = 30
c1m 40 # 'm' 13 static variable becoz classname cl is used
#end of the class
def f1():
a = c1 ()
a. p = 50
# 'p' is instance variable becoz object 'a' is used
c1. q = 60 # 'g' is static variable becoz classname cl is used
370 # 's' is local variable becoz it is initialized in the function without any prefix
#end of the function
is global variable becoz it is initialized outsuide the class without any prefix k = 80 # 'k'
'1' is static variable becoz classname cl is used c1.190 #
b = c1 ()
# 'n' is instance variable becoz object 'b' is used n = 100