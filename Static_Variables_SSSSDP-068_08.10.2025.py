# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  constructor')  #  Outer class constructor
	def  m1(self):
		print('Outer  class  method')  #  Outer class method
	class   inner:
		def __init__(self):
			print('Inner  class  constructor')  #  Inner class constructor 
		def m1(self):
			print('Inner  class  method')  #  Innerclass method
#end of the class
a=outer()  
a.m1()  #  How  to  call  m1()  method  of  outer  class
a.inner().m1()  #  How  to  call  m1()  method  of  inner  class
outer().inner().m1()  #  How  to  call  m1()  method  of  inner  class  in  another  way
a.inner().m1()  #  How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()  #   Error due to we cant access directly inner class



class emp:
    def __init__(self):
        self.empno, self.ename, self.sal = 25, 'Rama Rao', 10000.0  # How to initialize empno , ename , sal of object self to 25 , 'Rama Rao' , 10000.0
        self.dt = self.date()  # How to create date class object

    def disp(self):
        print(self.empno)
        print(self.ename)
        print(self.sal)  # How to print empno , ename , sal of object self
        self.dt.disp()  # How to call disp() method of date class

    class date:
        def __init__(self):
            self.dd, self.mm, self.yy = 15, 8, 1947  # How to initialize dd , mm , yy of object self to 15 , 8 , 1947

        def disp(self):
            print(self.dd)
            print(self.mm)
            print(self.yy)  # How to print dd , mm , yy of object self

# End of the class
a = emp()
a.disp()  # How to call disp() method of emp class



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25  #  How  to  initialize  variable  'x'  of  object  self  to  25
		b=a.inner1()  #  How  to  create  inner1  class  object
		c=a.inner2()  #  How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
a=outer()  
a.disp()  #  How  to  call   disp()  method  of outer  class
a.inner1().disp()  #  How  to  call   disp()  method  of inner1  class
a.inner2().disp()  #  How  to  call   disp()  method  of inner2  class



# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
a=c1()  #  How  to  create  c1  class  object
b=a.c2()  #  How  to  create  inner  c2  class  object
c=c2()  #  How  to  create  outer  c2  class  object


# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')  #  Outer class constructor
	class   c2:
		def __init__(self):
			print('inner  class  constructor')  #  Inner class constructor
#end of the class
a=c2()  #  How  to  create  outer  c2  class  object
b=a.c2()  #  How  to  create  inner  c2  class  object
c=c2().c2()  #  How  to  create  inner  c2  class  object  in  another  way



# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()  #  y=20
b = c1()  #  y=20
a . x += 1  #  x=11
b . y += 1  #  y=21
print(a . x)  #  11
print(a . y)  #  20
print(b . x)  #  10
print(b . y)  #  21
print(c1 . x)  #  10
print(a . __dict__)  #  [y:20,x:11]
print(b . __dict__)  #  [y:21]
print(c1 . __dict__)  #  list of methods





# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()  #  x=20
print(c1 . x)  # 10
print(a . x)  #  20



# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()  #  y=20
b = c1()  #  y=20
c1 . m1()
print(a . x)  #  30
print(a . y)  #  20
print(b . x)  #  30
print(b . y)  #  20
print(c1 . x , c1 . y)  #  30,40
print(cls . x , cls . y)  #  Error due to we cannot access directly method inside class
print(self . x , self . y)  #   Error due to we cannot access variables with self in global



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  #  25
a = c1()
a . m1(35)  #  35


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  #  25
a = c1()
a . m1()
a . m1(35)  #  35


#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')  
		print(self)
	def   m1(self):
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25)   #  25
a = c1()  #  static / instance method
a . m1()  #  type and address



# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x)  #  How  to  print  static  variable  'x'
		print(c1.x)  #  How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(self.x)  # How  to  print  static  variable  'x'
		print(c1.x)  #  How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		print(c1.x)  #  How  to  print  static  variable  'x'
		print(cls.x)  #  How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)  #  How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
a=c1()
print(c1.x)  #  How  to  print  static  variable  'x'
print(a.x)  #   How  to  print  static  variable  'x'  in  another  way
print(x)  #   Error due to x is not defined
print(self . x)  #  Error due to we cannot access variables with self in global
print(cls . x)  #  Error due to we cannot access directly method inside class
a.m1()  #  How  to  call  method  m1()
a.m2()  #  How  to  call  method  m2()
a.m3()  #  How  to  call  method  m3()



class c1:
    # Adding static variable 'a' at class level
    a = 10

    def __init__(self):
        # Adding static variable 'b' inside constructor
        c1.b = 20
        # Adding instance variable 'c'
        self.c = 30
        # Adding static variable 'k' inside constructor
        c1.k = 25

    def m1(self):
        # Adding static variable 'd' inside instance method
        c1.d = 40
        # Adding instance variable 'e'
        self.e = 50

    @classmethod
    def m2(cls):
        # Adding static variable 'f' inside class method
        cls.f = 60
        # Another way to add static variable 'g'
        c1.g = 70
        # Cannot use 'self' inside classmethod

    @staticmethod
    def m3():
        # Adding static variable 'h' inside static method
        c1.h = 80
        # Cannot use self or cls directly unless passed

# End of the class

print('Begin')
print(c1.__dict__)
print()

# Create object
x = c1()
print('Constructor')
print(c1.__dict__)
print()

# Call instance method
x.m1()
print('Instance method m1')
print(c1.__dict__)
print()

# Call class method
c1.m2()
print('Class method m2')
print(c1.__dict__)
print()

# Call static method
c1.m3()
print('Static method m3')
print(c1.__dict__)
print()

# Adding static variable outside class
c1.i = 90
# Adding instance variable outside class for object x
x.j = 100
print('Outside the class')
print(c1.__dict__)
print()
print("Object 'x'")
print(x.__dict__)





# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class c1:
    a = 10  # How to add static variable 'a' with value 10

    def __init__(self):
        c1.b = 20  # How to add static variable 'b' with value 20
        self.c = 30  # How to add instance variable 'c' with value 30
        c1.k = 25  # How to add static variable 'k' with value 25

    def m1(self):
        c1.d = 40  # How to add static variable 'd' with value 40
        self.e = 50  # How to add instance variable 'e' with value 50

    @classmethod
    def m2(cls):
        cls.f = 60  # How to add static variable 'f' with value 60
        c1.g = 70   # Another way to add static variable 'g'
        # Cannot use self inside classmethod

    @staticmethod
    def m3():
        c1.h = 80  # How to add static variable 'h' with value 80
        # Cannot use self or cls unless passed

# End of the class

print('Begin')
print(c1.__dict__)
print()

# Create object
x = c1()
print('Constructor')
print(c1.__dict__)
print()

# Call instance method
x.m1()
print('Instance method m1')
print(c1.__dict__)
print()

# Call class method
c1.m2()
print('Class method m2')
print(c1.__dict__)
print()

# Call static method
c1.m3()
print('Static method m3')
print(c1.__dict__)
print()

# Adding static variable outside class
c1.i = 90
# Adding instance variable outside class for object x
x.j = 100
print('Outside the class')
print(c1.__dict__)
print()
print("Object 'x'")
print(x.__dict__)




# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)  #  How  to  print  variable  'a'
print(c1.b)  #  How  to  print  variable  'b'
print(c1.c)  #  How  to  print  variable  'c'



#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))  #  10
		self . z = int(input('Enter  any  number  :  '))  #  20
	def  compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()
b = Test()
c = Test()
a . get2() #  10,20
b . get2()  #  30,40
c . get2()  #  50,60
a . compute()  #  x=12 , y=21 , z=21
b . compute()  #  x=13 , y=41 , z=41
c . compute()  #  x=14 , y=61 , z=61
a . disp()  #  13 , 21 , 21 , 12
b . disp()  #  13 , 41 , 41 , 13
c . disp()  #  13 , 61 , 61 , 14




'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  ---> vector . n
'''
class vector:
    @staticmethod
    def get1():
        # How to read number of elements into variable 'n'
        vector.n = int(input("Enter number of elements: "))

    def get2(self):
        # How to read the list into the object
        self.a = []
        for i in range(vector.n):
            val = int(input(f"Enter element {i+1}: "))
            self.a.append(val)

    def add(self, x, y):
        # How to add the lists held by objects 'x' and 'y' and store results in list held by owner object
        self.a = []
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])
# How to call get1() method
vector.get1()
# How to read the list into 1st object
x = vector()
x.get2()
# How to read the list into 2nd object 'y'
y = vector()
y.get2()
# How to add the lists held by objects 'x' and 'y' and store the results in list of 3rd object 'z'
z = vector()
z.add(x, y)
# How to print the list of 3rd object
print("Resultant Vector:", z.a)

'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
for i,j in c1.__dict__.items():
    if not(i.startswith('__')):
        print(i,'=',j)
class c1:
    x = 10          # What is variable 'x'?
    def m1(self):
        self.y = 20  # What is variable 'y'?
        z = 30       # What is variable 'z'?
        c1.m = 40    # What is variable 'm'?
# end of class
def f1():
    a = c1()
    a.p = 50         # What is variable 'p'?
    c1.q = 60        # What is variable 'q'?
    s = 70           # What is variable 's'?
# end of function
k = 80               # What is variable 'k'?
c1.l = 90            # What is variable 'l'?
b = c1()
b.n = 100            # What is variable 'n'?



