#Program 1
class Rat:
a = Rat()		# a.nr = 22, a.dr = 7 
b = Rat(9)		# b.nr = 9, b.dr = 7 
c = Rat(5, 8)		# c.nr = 5, c.dr = 8 
d = Rat(dr1 = 9)		# d.nr = 22, d.dr = 9 
e = Rat(dr1 = 3 , nr1 = 2)		# e.nr = 2, e.dr = 3 
x = eval(input('Enter numerator : '))	#11	Enter numerator : 11
y = eval(input('Enter Denominator : '))	#15	Enter Denominator : 15
f = Rat(x , y)		# f.nr = 11, f.dr = 15
print('a : ' , a)		#a : 22 / 7
print('b : ' , b)		#b : 9 / 7
print('c : ' , c)		#c : 5 / 8
print('d : ' , d)		#d : 22 / 9
print('e : ' , e)		#e : 2 / 3
print('f : ' , f)		#f : 11 / 15
c.__init__()		# Re-initializes c to defaults: c.nr = 22, c.dr = 7
print('c : ' , c)		#c : 22 / 7
a.__init__(3.8 , 4.6)# Re-initializes a: a.nr = 3.8, a.dr = 4.6
print('a : ' , a)	#a : 3.8 / 4.6
g = Rat(nr1 = 9 , 5)# SyntaxError: Positional argument (5) follows keyword argument (nr1 = 9).
h = Rat(nr = 9 , dr = 5)# TypeError: __init__ does not accept arguments named nr or dr.


#Program 2
class Date:	# Class definition
a = Date(15 , 8 , 1947)	# a.dd = 15, a.mm = 8, a.yy = 1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)	# b.dd = 26, b.mm = 1, b.yy = 1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)	# c.dd = 19, c.mm = 7, c.yy = 1985
print('a : ' , a . __dict__)	#a : {'dd': 15, 'mm': 8, 'yy': 1947}
print('b : ' , b . __dict__)	#b : {'dd': 26, 'mm': 1, 'yy': 1950}
print('c : ' , c . __dict__)	#c : {'dd': 19, 'mm': 7, 'yy': 1985}
d = Date()	# Error: __init__ is missing 3 required arguments.
e = Date(dd = 30 , mm = 4 , yy = 2022)	# Error: __init__ only accepts dd1, mm1, yy1.
f = Date(dd1 = 26 , mm1 = 8 , 2023)	# Error: Positional argument follows keyword argument (mm1=8).

#Program 3
# Find  outputs (Home  work)
class c1:
    def __init__(self):
        print('c1 class constructor') # c1 class constructor
        return 25 # Returns an integer 25
class c2:
    def __init__(self):
        print('c2 class constructor') # c2 class constructor
        return None # Returns None (which is acceptable for __init__)
class c3:
    def __init__(self):
        print('c3 class constructor') # c3 class constructor
# End of class
a = c1() # Calls c1.__init__
         # Output: c1 class constructor
b = c2()	#c2 class constructor
print(b)	#<__main__.c2 object at 0x...>
print(b.__init__())	#c2 class constructor
#None
c = c3()	#c3 class constructor
print(c.__init__())	#c3 class constructor
#None

#Program 4
class c1:	# Class definition
a = c1()	# Calls c1.__init__.
def __init__(self):	
print('Constructor')	#Constructor
b = c1()	# Calls c1.__init__ again.
print('Constructor')	#Constructor
b = c1()	# Calls c1.__init__ again.
#... This repeats thousands of times...	...
#...	RecursionError: maximum recursion depth exceeded

#Program 5
class c1:	# Class definition
class c2:	# Class definition
a = c1()	#Calls c1.__init__ automatically.
def __init__(self):	
print('Constructor')#Constructor
print(a.__dict__)	# Attributes (x and y) were set by the constructor.
#{'x': 10, 'y': 20}
b = c2()	#Calls the default, empty object.__init__. Does NOT call c2.init.
print(b.__dict__)	# The dictionary is empty because c2.init wasn't called yet.
{}
b.init()	#Calls c2.init explicitly like any other method.
def init(self):	
print('Method')	#Method
print(b.__dict__)	# Attributes are now set after the explicit call.
#{'x': 30, 'y': 40}

#Program6
x = c1()	# Creates object x, calling c1.__init__ which sets x.a = 10.
print(x . __dict__)	#{'a': 10}
x . m1()	# Calls c1.m1(x) which sets x.b = 20.
print(x . __dict__)	#{'a': 10, 'b': 20}
f1()	# Calls f1(). Inside f1, x.c = 30 is executed, adding c to object x.
print(x . __dict__)	#{'a': 10, 'b': 20, 'c': 30}
x . d = 40	# Directly adds attribute d to object x.
print(x . __dict__)	#{'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()	# Creates object y. (Not used, but exists.)
y . m3()	# Calls c2.m3(y). Inside, it executes x.e = 50, adding e to object x.
print(x . __dict__)	#{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()	# Creates object z, calling c1.__init__ which sets z.a = 10.
print(z . __dict__) #{'a': 10}

#Program 7
# Find outputs (Home work)
class c1:
	def __init__(self):
		self.x = 10
		self.y = 20
		self.z = 30
#end of the class
a = c1()       # Creates object 'a': a.__dict__ is {'x': 10, 'y': 20, 'z': 30}
b = c1()       # Creates object 'b': b.__dict__ is {'x': 10, 'y': 20, 'z': 30}
print(a.__dict__) # {'x': 10, 'y': 20, 'z': 30}
print(b.__dict__) # {'x': 10, 'y': 20, 'z': 30}
del a.x        # Deletes 'x' from object 'a'. a.__dict__ is now {'y': 20, 'z': 30}
del b.y        # Deletes 'y' from object 'b'. b.__dict__ is now {'x': 10, 'z': 30}
print(a.__dict__) # {'y': 20, 'z': 30}
print(b.__dict__) # {'x': 10, 'z': 30}
print(a.x)     # ERROR: Tries to access the deleted attribute 'x'
               # Output: AttributeError: 'c1' object has no attribute 'x'
               # Execution STOPS here.
#print(b.y)    # This line is not reached due to the error above.

#Program 8
# Find outputs (Home work)
class c1:
	def __init__(self):
		print('1st constructor')
	def __init__(self):
		print('2nd constructor')
	def __init__(self):
		print('3rd constructor') # This is the final and only __init__ method available.
# End of the class
a = c1() # Calls the 3rd __init__
         # Output: 3rd constructor

#Program 9
# Find outputs (Home work)
class c1:
	def __init__(self):
		print('No argument constructor')
	def __init__(self, x):
		print('single argument constructor : ', x)
	def __init__(self, x, y): # This is the final and active constructor.
		print('Two argument constructor : ', x, y)
# End of the class
a = c1(10, 20) # Calls the last __init__ with x=10, y=20.
               # Output: Two argument constructor : 10 20
b = c1(30)     # Calls the last __init__ but is missing the 'y' argument.
               # Output: TypeError: c1.__init__ missing 1 required positional argument: 'y'
               # Execution STOPS here.
#c = c1()      # This line is not reached due to the TypeError above.
               #Also because no args are given
			   

#Program 10
# Find outputs
class c1:
	def __init__(self):
		print('No argument constructor')
	def __init__(self, x):
		print('single argument constructor : ', x)
	def __init__(self, x = 100, y = 200): # This is the final and active constructor.
		print('Two argument constructor : ', x, y)
# End of the class
a = c1(10, 20) # Calls the last __init__ with x=10, y=20.
               # Output: Two argument constructor : 10 20
b = c1(30)     # Calls the last __init__ with x=30, y=200 (default).
               # Output: Two argument constructor : 30 200
c = c1()       # Calls the last __init__ with x=100, y=200 (defaults).
               # Output: Two argument constructor : 100 200
			   
#Program 11
# What happens when function and class have same name ?
def f1():
	print('Function')
	return 25
class f1: # This class definition overwrites the function f1 above it.
	def __init__(self):
		print('Constructor')
#end of the class
a = f1() # This now calls the constructor of the CLASS f1.
         # Output: Constructor
print(a) # Prints the string representation of the object 'a'.
         # Output: <__main__.f1 object at 0x...>
		 
#Program 12
class c1:	# Class definition (Overwritten by the function below)
def c1():	# This function overwrites the class c1.
a = c1()	# Calls the function c1().
def c1():	# Executes the function's body.
print('Function')	#Function
# a is assigned the return value of the function, which is None (default).
print(a)	#None

#Program 13
class c1:	# Class definition (Overwritten by the function below)
def c1(x):	# This function overwrites the class c1.
a = c1()	# Calls the function c1() with no arguments.
TypeError: c1() #missing 1 required positional argument: 'x'
b = c1(25)	# This line is not reached due to the TypeError above.
print(b)	# This line is not reached due to the TypeError above.

#Program 14
from prog9a import c1	# Imports c1 (from prog9a) into the namespace.
class c1:	# Locally defines a new class c1, overwriting the imported name.
a = c1()	# Calls the constructor of the local c1 class.
#c1 class of prog9b

#Program 15
class c1:	# Locally defines c1 (Constructor prints 'c1 class of prog9c').
from prog9a import c1	# Imports c1 (from prog9a), overwriting the local definition.
a = c1()	# Calls the constructor of the imported c1 class.
#c1 class of prog9a

#Program 16
# How to use both the classes (i.e. c1 of prog9a and c1 of current program)

# How to import class c1 from prog9a
from prog9a import c1 as c1_from_prog9a

class c1: # This remains the local c1
	def __init__(self):
		print('c1 class of prog9d')

# How to create c1 class object of current module
a = c1()
# Output: c1 class of prog9d

# How to create c1 class object of prog9a
b = c1_from_prog9a()
# Output (assuming prog9a has the same constructor): c1 class of prog9a

#program 17
# How to use both the classes (i.e. c1 of prog9a and c1 of current program)

# How to import prog9a
import prog9a

class c1: # This remains the local c1
	def __init__(self):
		print('c1 class of prog9e')

# How to create c1 class object of current module
a = c1()
# Output: c1 class of prog9e

# How to create c1 class object of prog9a
b = prog9a.c1()
# Output (assuming prog9a has the same constructor): c1 class of prog9a

#Program 18
# Public and Private members demo program
class Test:
    def __init__(self):
        # How to initialize public variable 'x' to 10
        self.x = 10
        # How to initialize private variable 'y' to 20
        self.__y = 20  # Double underscore triggers name mangling
        print("Constructor")

    def m1(self):
        print('m1 method')
        # How to print variable 'x'
        print('Public x from m1:', self.x)
        # How to print private variable 'y'
        print('Private __y from m1:', self.__y)
        # How to call private method m2()
        self.__m2()
        print('Back to m1 method')

    def __m2(self): # Double underscore triggers name mangling
        print('__m2 method')
        # How to print variable 'x'
        print('Public x from __m2:', self.x)
        # How to print private variable 'y'
        print('Private __y from __m2:', self.__y)

# End of the class

t = Test()
# Output: Constructor
print('Outside')

# How to print variable 'x'
print('Public x outside:', t.x)

# How to print variable 'y'
# Accessing mangled '__y' via its mangled name:
print('Mangled __y outside:', t._Test__y)

# The following line will fail with an AttributeError because Python renamed '__y' to '_Test__y'.
# print(t.__y)

print('Current dict:', t.__dict__)
# Output: Current dict: {'x': 10, '_Test__y': 20}

# How to call method m1()
t.m1()
# Output: m1 method
# Output: Public x from m1: 10
# Output: Private __y from m1: 20
# Output: __m2 method
# Output: Public x from __m2: 10
# Output: Private __y from __m2: 20
# Output: Back to m1 method

# How to call method m2()
# Accessing mangled '__m2' via its mangled name:
print('Calling mangled __m2 outside:')
t._Test__m2()
# Output: Calling mangled __m2 outside:
# Output: __m2 method
# Output: Public x from __m2: 10
# Output: Private __y from __m2: 20

# The following line would fail with an AttributeError because Python renamed '__m2' to '_Test__m2'.
# t.__m2()

print('End')
# Output: End

#Program 19
# Find outputs
class c1:
	def __init__(self):
		# How to initialize public variable 'x' with 10
		self.x = 10
		# How to initialize private variable 'x' with 20 (Name Mangling)
		self.__x = 20
		# How to initialize public dunder variable 'x' with 30 (Public)
		self.__x__ = 30
	def m1(self):
		print('public method')
	def __m1(self): # Name-mangled to _c1__m1
		print('private method')
	def __m1__(self): # Public dunder method (NOT mangled)
		print('public Dunder method')
# End of the class

a = c1()
# Output: (No output from constructor, just initialization)

# How to print variable 'x' (Public)
print('Public x:', a.x)
# Output: Public x: 10

# How to print public dunder variable 'x' (Public)
print('Dunder x:', a.__x__)
# Output: Dunder x: 30

# How to print private variable 'x' (Accessing via Name Mangling)
print('Private x (Mangled):', a._c1__x)
# Output: Private x (Mangled): 20

# print(a.__x) # This is the line that would cause the AttributeError
# Output: (AttributeError: 'c1' object has no attribute '__x' if uncommented)

# How to call public method m1()
a.m1()
# Output: public method

# How to call public dunder method m1()
a.__m1__()
# Output: public Dunder method

# How to call private method m1() (Accessing via Name Mangling)
a._c1__m1()
# Output: private method

# a.__m1() # This is the line that would cause the AttributeError
# Output: (AttributeError: 'c1' object has no attribute '__m1' if uncommented)

#Program 20
# Tricky program
# Find outputs
# Assume that addresses of objects 'a', 'b', 'c', 'd' and 'e' are 1000, 2000, 3000, 4000 and 5000 respectively
class c1:
	def __init__(self):
		print('Object is created at address : ', id(self))
	def __del__(self):
		print(F'Object at address {id(self)} is lost')
# End of the class

a = c1()
# Output: Object is created at address : 1000  (# Object at 1000 is created)

a = None
# The reference count for the object at 1000 drops to zero.
# Output: Object at address 1000 is lost

b = c1()
# Output: Object is created at address : 2000  (# Object at 2000 is created)

del b
# The reference count for the object at 2000 drops to zero.
# Output: Object at address 2000 is lost

c = c1()
# Output: Object is created at address : 3000  (# Object at 3000 is created)

c = c1()
# Output: Object is created at address : 4000  (# Object at 4000 is created)
# The variable 'c' is reassigned. The original object at 3000 is now unreferenced.
# Output: Object at address 3000 is lost

d = c1()
# Output: Object is created at address : 5000  (# Object at 5000 is created)

e = c1()
# Output: Object is created at address : 6000  (# Object at 6000 is created, address is implied to be next available)

# Program ends. Python's garbage collector destroys the remaining objects (c, d, e).
# The order of final destruction is not strictly guaranteed, but typically happens upon exit.

# Output: Object at address 4000 is lost
# Output: Object at address 5000 is lost
# Output: Object at address 6000 is lost

#Program 21
# Identify Error (Home work)
class c1:
	def __del__(self, x): # ERROR: __del__ MUST NOT take arguments besides self
		print('destructor : ', x)
a = c1()
a.__del__(25)
# Output:
# TypeError: c1.__del__() takes 2 positional arguments but 3 were given

#Program 22
# Find outputs (Home work)
class c1:
	def __del__(self, x = 35): # This signature is invalid for the destructor mechanism
		print('destructor : ', x)
a = c1()
# Output: (No output from creation)

a.__del__(25)
# Output: destructor : 25

#Program 23
# Find outputs (Home work)
class c1:
	def __del__(self):
			print('destructor')
			b = c1()
a = c1()
# Output:
# (Object 'a' is created, no output from __init__)
# (Program ends, destructor for 'a' is called)
# destructor

#Program 24
# Find outputs (Home work)
class c1:
	def __init__(self):
		print('constructor')
		del self # ERROR: Cannot delete 'self' (the instance) inside the constructor.
                 # The object hasn't been fully constructed yet.
	def __del__(self):
		print('destructor')
		b = c1()
a = c1()
# Output:
# constructor
# Traceback (most recent call last):
#   File "<stdin>", line X, in <module>
#   File "<stdin>", line Y, in __init__
# AttributeError: __del__ method has already been called
# (The interpreter detects that deleting 'self' in __init__ causes an immediate, illegal call to __del__
# before the object exists, leading to a critical error.)

#Program 25
# Find outputs( Home work)
class c1:
	def __del__(self):
		print('1st destructor')
	def __del__(self):
		print('2nd destructor')
	def __del__(self):
		print('3rd destructor') # This is the final and active destructor.
# End of the class
a = c1()
# Output: (No output yet)
# (Program ends, destructor for 'a' is called)
# 3rd destructor

#Program 26
# Find outputs(Home work)
class c1:
	def __init__(self):
		print('Object is created at address : ', id(self))
	def __del__(self):
		print(F'Object at address {id(self)} is lost ')
#End of the class
list = [c1() , c1() , c1()]
# Output:
# Object is created at address : 1000  (Address 1)
# Object is created at address : 2000  (Address 2)
# Object is created at address : 3000  (Address 3)

del list
# Output:
# Object at address 1000 is lost
# Object at address 2000 is lost
# Object at address 3000 is lost

#Program 27
# Find outputs (Home work)
class c1:
	def __del__(self):
		print('destructor')
		return 25
a = c1()
# Output: (Object 'a' is created, no output)

print(a.__del__())
# Output:
# destructor
# 25

print('Hello')
# Output:
# Hello

del a
# Output: (Reference count drops to 0, destructor is called by the garbage collector)
# destructor
