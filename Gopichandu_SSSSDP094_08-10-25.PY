
# Find  outputs  (Home  work)

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
outer.inner().m1()          # How  to  call  m1()  method  of  inner  class  in  one  more  way
#i=inner()                   # inner is not defined


# Find  outputs  (Home  work)

class   emp:
	def __init__(self):
		# How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		# How  to  create  date  class  object
		self.d = self.date()
	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print("Emp No:", self.empno)
		print("Emp Name:", self.ename)
		print("Salary:", self.sal)
		# How  to  call  disp()  method  of  date  class
		self.d.disp()
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
		# How  to  initialize  variable  'x'  of  object  self  to  25
		self.x = 25
		# How  to  create  inner1  class  object
		self.i1 = self.inner1()
		# How  to  create  inner2  class  object
		self.i2 = self.inner2()
	def  disp(self):
		print(self.x)
	class inner1:
		def disp(self):
			print('1st  inner  class  method')
	class inner2:
		def disp(self):
			print('2nd  inner  class  method')
#end of the class
# How  to  call   disp()  method  of outer  class
o = outer()
o.disp()
# How  to  call   disp()  method  of inner1  class
o.i1.disp()
# How  to  call   disp()  method  of inner2  class
o.i2.disp()


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
# How  to  create  outer  c2  class  object
o = c2()
# How  to  create  inner  c2  class  object
i = c2.c2()
# How  to  create  inner  c2  class  object  in  another  way
o1 = c2()
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

'''
static   variable  --->  x
Object  'a'  --->  y , x (instance copy)
Object  'b'  --->  y
'''


# Find  outputs (Home  work)

class c1:
	x = 10
	def m1(self):
		self.x = 20     # creates instance variable x for object 'a'.
a = c1()
a.m1()
print(c1.x)   # 10
print(a.x)    # 20

'''
static   variable   --->  x = 10
object 'a' ---> x = 20 
'''


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

# print(cls.x , cls.y)  # Error cls is not defined 
# print(self.x , self.y)  # Error self is not defined 

'''
static   variable   --->  x = 30 , y = 40
object  'a'   --->  y = 20
object  'b'   --->  y = 20
'''


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
c1.m1(25)                           # Error cannot call instance method on class without instance
a = c1()
a.m1()                              # prints the instance reference
a.m1(35)                            # Error m1() takes 1 positional argument but 2 were given


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
    # How  to  add  static  variable  'a'  with  value  10
    a = 10

    def __init__(self):
        # How  to  add  static  variable  'b'  with  value  20
        c1.b = 20

        # How  to  add  instance  variable  'c'  with  value  30
        self.c = 30

        # cls.k = 25 → use class name
        c1.k = 25

    def m1(self):
        # How  to  add  static  variable  'd'  with  value  40
        c1.d = 40

        # How  to  add  instance  variable  'e'  with  value  50
        self.e = 50

    @classmethod
    def m2(cls):
        # How  to  add  static  variable  'f'  with  value  60
        cls.f = 60

        # How  to  add  static  variable  'g'  with  value  70  in  another  way
        c1.g = 70

    @staticmethod
    def m3():
        # How  to  add  static  variable  'h'  with  value  80
        c1.h = 80

#End  of  the  class

print('Begin')
print(c1.__dict__)     # shows {'__module__', 'a': 10, ...}
print()
print()

x = c1()
print('Constructor')
print(c1.__dict__)     # shows {'__module__', 'a':10, 'b':20, 'k':25, '__init__', ...}
print()
print()

# How  to  call  m1()  method
x.m1()
print('Instance  method  m1')
print(c1.__dict__)     # shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, ...}
print()
print()

# How  to  call  m2()  method
c1.m2()
print('class  method   m2')
print(c1.__dict__)     # shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, ...}
print()
print()

# How  to  call  m3()  method
c1.m3()
print('static   method   m3')
print(c1.__dict__)     # shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, ...}
print()
print()

# How  to  add  static  variable  'i'  with  value  90
c1.i = 90

# How  to  add  instance  variable  'j'  with  value  100
x.j = 100


# End  of  the  class
# How  to  print  variable  'a'
print(c1.a)   # 1print('Outside  the  class')
print(c1.__dict__)     # shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, 'i':90, ...}
print()
print()

print("Object  'x' ")
print(x.__dict__)      # shows {'c':30, 'e':50, 'j':100}


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
static variable ---> Test.x = 13
Object 'a' ---> y=21, z=31, x=14
Object 'b' ---> y=41, z=51, x=14
Object 'c' ---> y=61, z=71, x=14
'''


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
