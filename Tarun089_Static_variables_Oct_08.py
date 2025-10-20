#Tarun Banala       08-10-2025
# Find  outputs  (Home  work)

class   outer:
	def  _init_(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def _init_(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
o = outer()                 
o.m1()                      # How  to  call  m1()  method  of  outer  class
i = outer.inner()           
i.m1()                      # How  to  call  m1()  method  of  inner  class
o = outer()                 
i = o.inner()               
i.m1()                      # How  to  call  m1()  method  of  inner  class  in  another  way
outer.inner().m1()          # How  to  call  m1()  method  of  inner  class  in  one  more  way
i=inner()                   # inner is not defined
'''
output:
Outer class method
next line output:
Inner class method
next line output:
1st inner class method
next line output:
Inner class method
next line output:
Inner class method
'''




# Find  outputs  (Home  work)

class   emp:
	def _init_(self):           # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		self.d = self.date()    # How  to  create  date  class  object
	def   disp(self):           # How  to  print  empno , ename , sal  of  object  self
		print("Emp No:", self.empno)
		print("Emp Name:", self.ename)
		print("Salary:", self.sal)
		self.d.disp()           # How  to  call  disp()  method  of  date  class
	class   date:
		def _init_(self):       # How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):         # How  to  print  dd , mm , yy  of  object  self
			print("Date of Joining: {}/{}/{}".format(self.dd, self.mm, self.yy))
# End  of  the  class
e = emp()
e.disp()    # How  to  call  disp()  method  of  emp  class
'''
output:
Emp No: 25
next line output:
Emp Name: Rama Rao
next line output:
Salary: 10000.0
next line output:
Date of Joining: 15/8/1947
'''




# Find outputs (Home  work)

class  outer:
	def _init_(self):
		self.x = 25                 # How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1 = self.inner1()     # How  to  create  inner1  class  object
		self.i2 = self.inner2()     # How  to  create  inner2  class  object
	def  disp(self):
		print(self.x)
	class inner1:
		def disp(self):
			print('1st  inner  class  method')
	class inner2:
		def disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer()     # How  to  call   disp()  method  of outer  class
o.disp()
o.i1.disp()     # How  to  call   disp()  method  of inner1  class
o.i2.disp()     # How  to  call   disp()  method  of inner2  class
'''
output:
25
next line output:
1st inner class method
next line output:
2nd inner class method
'''





# Find  outputs  (Home  work)

class c1:
	def _init_(self):
		print('outer  class  c1  constructor')
	class c2:
		def _init_(self):
			print('inner  class  c2  constructor')
#end of the class
class c2:
	def _init_(self):
		print('outer  class  c2  constructor')
#end of the class
o1 = c1()       # How  to  create  c1  class  object
i = c1.c2()     # How  to  create  inner  c2  class  object
o2 = c2()       # How  to  create  outer  c2  class  object
'''
output:
outer class c1 constructor
next line output:
inner class c2 constructor
next line output:
outer class c2 constructor
'''




# Find  outputs  (Home  work)

class c2:
	def _init_(self):
		print('outer  class  constructor')

	class c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
o = c2()    # How  to  create  outer  c2  class  object
i = c2.c2() # How  to  create  inner  c2  class  object
o1 = c2()   # How  to  create  inner  c2  class  object  in  another  way
i1 = o1.c2()
'''
output:
outer class constructor
next line output:
inner class constructor
next line output:
outer class constructor
next line output:
inner class constructor
'''





# Find  outputs (Home  work)
class c1:
    x = 10                     # static variable (class variable)
    def _init_(self):
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
print(a._dict_)  # {'y': 20, 'x': 11}
print(b._dict_)  # {'y': 21}
print(c1._dict_) # {Environmental Variables and static variable}

'''
static   variable  --->  x
Object  'a'  --->  y , x (instance copy)
Object  'b'  --->  y
'''
'''
output:
11
20
10
21
10
{'y': 20, 'x': 11}
{'y': 21}
# {Environmental Variables and static variable}
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
'''
output:
10
20
'''





# Find  outputs (Home  work)

class c1:
    x = 10
    def _init_(self):
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
print(cls.x , cls.y)  # Error cls is not defined 
print(self.x , self.y)  # Error self is not defined 

'''
output:
static   variable   --->  x = 30 , y = 40
object  'a'   --->  y = 20
object  'b'   --->  y = 20
'''
'''
output:
30
20
30
20
30 40
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
'''
output:
25
35
'''





#  Find  outputs

class c1:
	def m1(self):
		print(self)
#  End  of  the   class
c1.m1(25)                           # Error cannot call instance method on class without instance
a = c1()
a.m1()                              # type and address of object 'a'
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
    def _init_(self):
        print(c1.x)     # How  to  print  static  variable  'x'
        print(self.x)   # How  to  print  static  variable  'x'  in  another  way
    def m1(self):        
        print(c1.x)     # How  to  print  static  variable  'x'        
        print(self.x)   # How  to  print  static  variable  'x'  in  another  way
    @classmethod
    def m2(cls):        
        print(cls.x)    # How  to  print  static  variable  'x'
        print(c1.x)     # How  to  print  static  variable  'x'  in another way
    @staticmethod
    def m3():        
        print(c1.x)     # How  to  print  static  variable  'x'
# End  of  the  class
print(c1.x)        # How  to  print  static  variable  'x'
obj = c1()         # _init_ prints x via class and self
print(obj.x)       # How  to  print  static  variable  'x'  in  another  way
obj.m1()           # How  to  call  method  m1()
c1.m2()            # How  to  call  method  m2()
c1.m3()            # How  to  call  method  m3()





# How  to  add  static  variable  to  the  class  at  different  locations  of  the program

class c1:
    a = 10          # How  to  add  static  variable  'a'  with  value  10
    def _init_(self):
        c1.b = 20   # How  to  add  static  variable  'b'  with  value  20
        self.c = 30 # How  to  add  instance  variable  'c'  with  value  30
        c1.k = 25   # cls.k = 25 → use class name
    def m1(self):        
        c1.d = 40   # How  to  add  static  variable  'd'  with  value  40
        self.e = 50 # How  to  add  instance  variable  'e'  with  value  50
    @classmethod
    def m2(cls):
        cls.f = 60  # How  to  add  static  variable  'f'  with  value  60        
        c1.g = 70   # How  to  add  static  variable  'g'  with  value  70  in  another  way
    @staticmethod
    def m3():        
        c1.h = 80   # How  to  add  static  variable  'h'  with  value  80
#End  of  the  class
print('Begin')
print(c1._dict)     # {'module_', 'a': 10, ...}
print()
print()
x = c1()
print('Constructor')
print(c1._dict)     # shows {'a':10, 'b':20, 'k':25, 'init_', ...}
print()
print()
x.m1()      # How  to  call  m1()  method
print('Instance  method  m1')
print(c1._dict)     #{'module_', 'a':10, 'b':20, 'k':25, 'd':40, ...}
print()
print()
c1.m2()     # How  to  call  m2()  method
print('class  method   m2')
print(c1._dict)     #{'module_', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, ...}
print()
print()
c1.m3()     # How  to  call  m3()  method
print('static   method   m3')
print(c1._dict)     #{'module_', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, ...}
print()
print()
c1.i = 90   # How  to  add  static  variable  'i'  with  value  90
x.j = 100   # How  to  add  instance  variable  'j'  with  value  100


# End  of  the  class
# How  to  print  variable  'a'
print(c1.a)         # 1print('Outside  the  class')
print(c1._dict)     # shows {'module_', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, 'i':90, ...}
print()
print()
print("Object  'x' ")
print(x._dict_)     # shows {'c':30, 'e':50, 'j':100}





# Find  outputs  (Home  work)

class c1:
    a, b, c = range(1, 4)
print(c1.b)   # How  to  print  variable  'b'
print(c1.c)   # How  to  print  variable  'c'





#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)

class Test:
    @classmethod
    def get1(cls):
        cls.x = int(input('Enter any number   :  '))   
    def get2(self):
        self.y = int(input('Enter any number  :  '))   
        self.z = int(input('Enter any number  :  '))   
    def compute(self):
        Test.x += 1         
        self.y += 1        
        self.z += 1        
        self.x = Test.x + 1
    def disp(self):
        print(Test.x, self.y, self.z, self.x, sep='\t')
# End of the class
Test.get1()       
a = Test()
b = Test()
c = Test()
a.get2()          
b.get2()          
c.get2()          
a.compute()
b.compute()
c.compute()
a.disp()          
b.disp()          
c.disp()          

'''
static variable ---> Test.x = 13
Object 'a' ---> y=21, z=31, x=14
Object 'b' ---> y=41, z=51, x=14
Object 'c' ---> y=61, z=71, x=14
'''
'''
output:
Enter any number    :  10
Enter any number  :  20
Enter any number  :  30
Enter any number  :  40
Enter any number  :  50
Enter any number  :  60
Enter any number  :  70
13      21      31      12
13      41      51      13
13      61      71      14
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
print("object 2:")
x.get2()        # reads x.a
# How to read the list into 2nd object 'y'
y = vector()
print("object 2:")
y.get2()        # reads y.a
# How to add the lists held by objects 'x' and 'y' and store the results in list of 3rd object 'z'
z = vector()
z.add(x, y)
# How to print the list of 3rd object
print("Sum of two vectors:")
print(z.a)     # prints sum of two vectors in list 
'''
output:
Enter number of elements: 4
object 2:
Enter 4 elements for the vector:
20
40
60
80
object 2:
Enter 4 elements for the vector:
10
30
50
70
Sum of two vectors:
[30, 70, 110, 150]
'''




'''
Write a program to print only static variables but not environment variables of classname._dict_
Hint: Use startswith() and endswith() methods
'''

class c1:
    x = 1
    y = 2
    z = 3
# End of the class
static_vars = {}
for key, value in c1._dict_.items():
    if not (key.startswith('') and key.endswith('')):
        static_vars[key] = value
print("static variables of class c1 :", static_vars)

'''
output:
static variables of class c1 : {'x': 1, 'y': 2, 'z': 3}
'''






# What are k, l, x, y, z, m, n, p, q, s? (Home work)

class c1:
    x = 10  # What is variable 'x' --->  'x' is static variable because it is initialized in the class
    def m1(self):
        self.y = 20  # What is variable 'y' --->  'y' is instance variable because object self is used
        z = 30       # What is variable 'z' --->  'z' is local variable because it is initialized in the method without any prefix
        c1.m = 40    # What is variable 'm' --->  'm' is static variable because classname c1 is used
# end of the class
def f1():
    a = c1()
    a.p = 50    # What is variable 'p' --->  'p' is instance variable because object 'a' is used
    c1.q = 60   # What is variable 'q' --->  'q' is static variable because classname c1 is used
    s = 70      # What is variable 's' --->  's' is local variable because it is initialized in the function without any prefix
# end of the function
k = 80       # What is variable 'k' --->  'k' is global variable because it is initialized outside the class without any prefix
c1.l = 90    # What is variable 'l' --->  'l' is static variable because classname c1 is used
b = c1()
b.n = 100    # What is variable 'n' --->  'n' is instance variable because object 'b' is used
