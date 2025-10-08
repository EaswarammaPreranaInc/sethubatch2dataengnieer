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
outer.m1()#How  to  call  m1()  method  of  outer  class
outer().inner().m1()#How  to  call  m1()  method  of  inner  class
x=outer().inner()
x.m1()#How  to  call  m1()  method  of  inner  class  in  another  way
a = outer()
b = a.inner()
b.m1()#How  to  call  m1()  method  of  inner  class  in  one  more  way
#i = inner() error name inner is not defined




# Find  outputs  (Home  work)
class emp:
    def __init__(self):   #Constructor of emp class
        # How to initialize empno, ename, sal of object self to 25, 'Rama Rao', 10000.0
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0

        # How to create date class object
        self.d = self.date()

    def disp(self):
        # How to print empno, ename, sal of object self
        print('Emp No:', self.empno)
        print('Emp Name:', self.ename)
        print('Emp Salary:', self.sal)

        # How to call disp() method of date class
        self.d.disp()

    class date:
        def __init__(self):   #Constructor of date class
            # How to initialize dd, mm, yy of object self to 15, 8, 1947
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            # How to print dd, mm, yy of object self
            print('Date of Joining: {}/{}/{}'.format(self.dd, self.mm, self.yy))

# End of the class

# How to call disp() method of emp class
e = emp()
e.disp()





class outer:
    def __init__(self):
        self.x = 25 # How to initialize variable 'x' of object self to 25

        self.i1 = self.inner1()# How to create inner1 class object

        self.i2 = self.inner2()# How to create inner2 class object

    def disp(self):
        print(self.x)

    class inner1:
        def disp(self):
            print('1st inner class method')

    class inner2:
        def disp(self):
            print('2nd inner class method')

# end of the class
o = outer()
o.disp() # How to call disp() method of outer class
o.i1.disp()# How to call disp() method of inner1 class
o.i2.disp()# How to call disp() method of inner2 class



# Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('outer  class  c1  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def _init_(self):
		print('outer  class  c2  constructor')
#end of the class
a=c1()#How  to  create  c1  class  object
b = c1().c2()#How  to  create  inner  c2  class  object
c = c2()#How  to  create  outer  c2  class  object



 # Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
a = c2()#How  to  create  outer  c2  class  object
b = c2().c2()#How  to  create  inner  c2  class  object
a.c2()#How  to  create  inner  c2  class  object  in  another  way



# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
        self.y = 20

a = c1()
b = c1()
a.x += 1    # creates instance variable a.x = 11
b.y += 1    # b.y = 21
print(a.x)       # 11
print(a.y)       # 20
print(b.x)       # 10 (class variable)
print(b.y)       # 21
print(c1.x)      # 10
print(a.__dict__)  # {'y': 20, 'x': 11}
print(b.__dict__)  # {'y': 21}
print(c1.__dict__) # contains class attributes including x



'''
static   variable  --->

Object  'a'  --->

Object  'b'  --->
'''

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) #10
print(a . x)#20


'''
static   variable   --->

object  'a'   --->
'''


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
a = c1()
b = c1()
c1 . m1()
print(a.x)  # 30 (class variable)
print(a.y)  # 20 (instance variable)
print(b.x)  # 30 (class variable)
print(b.y)  # 20 (instance variable)
print(c1.x, c1.y)  # 30 40 (class variables)
#print(cls . x , cls . y) #error cls is not defined outside the class method
#print(self . x , self . y) #self is not defined outside any instance


'''
static   variable   --->

object  'a'   --->

object  'b'   --->
'''

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1() 
a . m1(35) #35


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1() #<__main__.c1 object at 0x7f...>
a . m1(35) #error m1 takes only 1 positional arguement but given 2



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
c1 . m1(25) #static / instance method 
            #25
a = c1()
a . m1() #'static / instance  method'
         #<__main__.c1 object at 0x7f...>



class c1:
    x = 25  # Static / class variable

    def __init__(self):
        # How to print static variable 'x' inside constructor using instance
        print("Inside __init__ using self:", self.x)
        # How to print static variable 'x' inside constructor using class name
        print("Inside __init__ using class name:", c1.x)

    def m1(self):
        # How to print static variable 'x' inside instance method using instance
        print("Inside instance method using self:", self.x)
        # How to print static variable 'x' inside instance method using class name
        print("Inside instance method using class name:", c1.x)

    @classmethod
    def m2(cls):
        # How to print static variable 'x' inside class method using cls
        print("Inside class method using cls:", cls.x)
        # How to print static variable 'x' inside class method using class name
        print("Inside class method using class name:", c1.x)

    @staticmethod
    def m3():
        # How to print static variable 'x' inside static method using class name
        print("Inside static method using class name:", c1.x)
        # Cannot use self or cls here
        # print(self.x) wrong
        # print(cls.x) wrong

# How to print static variable 'x' outside the class using class name
print("Outside class using class name:", c1.x)

# How to print static variable 'x' outside the class using instance
a = c1()
print("Outside class using instance:", a.x)
a.m1() # How to call method m1() (instance method)
c1.m2() # How to call method m2() (class method)
c1.m3() # How to call method m3() (static method)






# How to add static variable to the class at different locations of the program
class c1:
    a = 10  # How to add static variable 'a' with value 10

    def __init__(self):
        c1.b = 20 # How to add static variable 'b' with value 20
        self.c = 30 # How to add instance variable 'c' with value 30
        c1.k = 25 # How to add static variable 'k' in constructor

    def m1(self):
        c1.d = 40 # How to add static variable 'd' with value 40
        self.e = 50 # How to add instance variable 'e' with value 50

    @classmethod
    def m2(cls):
        cls.f = 60 # How to add static variable 'f' with value 60
        setattr(cls, 'g', 70) # How to add static variable 'g' with value 70 in another way
        # self.k = 25  #Not valid inside classmethod

    @staticmethod
    def m3():
        c1.h = 80 # How to add static variable 'h' with value 80
        # self.k = 25 # Not valid inside staticmethod
        # cls.k = 35 # Not valid inside staticmethod

# End of the class

print('Begin')
print(c1.__dict__)  # Print all current class members
print()

x = c1()  # Call constructor
print('Constructor')
print(c1.__dict__)
print()

x.m1()  # Call instance method
print('Instance method m1')
print(c1.__dict__)
print()

c1.m2()  # Call class method
print('Class method m2')
print(c1.__dict__)
print()

c1.m3()  # Call static method
print('Static method m3')
print(c1.__dict__)
print()

c1.i = 90# How to add static variable 'i' with value 90 outside the class
x.j = 100# How to add instance variable 'j' with value 100 outside using object


print('Outside the class')
print(c1.__dict__)
print()

print("Object 'x'")
print(x.__dict__)



 # Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
x = c1()
x.a #How  to  print  variable  'a'
x.b#How  to  print  variable  'b'
x.c#How  to  print  variable  'c'



#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  ')) #10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  ')) #20
		self . z = int(input('Enter  any  number  :  ')) #30
	def   compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1() #10
a = Test() 
b = Test()
c = Test()
a . get2() #20 #30
b . get2() #40 #50
c . get2() #60 #70
a . compute() #11 #21 #31 #a.x =1
b . compute() #12 #41 #51 #b.x = 1
c . compute() #13 #61 #71 #c.x = 1
a . disp()  #13 #21 #31 #1
b . disp()  #13 #41 #51 #1
c . disp()  #13 #61 #71 #1


'''
static   variable   --->

Object  'a'  --->

Object  'b'  --->

Object  'c'  --->
'''


'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  ---> vector . n
'''
class Vector:
    a = []  # list held by each object

    @staticmethod
    def get1():
        # How to read number of elements into variable 'n'
        Vector.n = int(input("Enter number of elements: "))  # static variable

    def get2(self):# How to read the list into the object
        self.a = []
        for i in range(Vector.n):
            val = int(input(f"Enter element {i+1}: "))
            self.a.append(val)

    def add(self, x, y):# How to add the lists held by objects 'x' and 'y' and store the results in list held by owner object
        self.a = []
        for i in range(Vector.n):
            self.a.append(x.a[i] + y.a[i])


Vector.get1() # How to call get1() method


x = Vector() # How to read the list into 1st object
x.get2()  # x.a


y = Vector() # How to read the list into 2nd object 'y'
y.get2()  # y.a


z = Vector()# How to add the lists held by objects 'x' and 'y' and store the results in list of 3rd object 'z'
z.add(x, y)  # z.a

print("Sum of vectors:", z.a) # How to print the list of 3rd object




'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods

class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
#{'_module': 'main', 'firstlineno': 6, 'x': 1, 'y': 2, 'z': 3, 'static_attributes': (), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref': <attribute 'weakref' of 'c1' objects>, 'doc_': None}
#static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}
'''


class c1:
    x = 1
    y = 2
    z = 3
# End of the class

static_vars = {} # Create a dictionary to store only static variables

for k, v in c1.__dict__.items():
    if not (k.startswith('__') or k.endswith('__') or k.startswith('_') or k.endswith('_')):
        static_vars[k] = v

print("Static variables of class c1:", static_vars)




class c1:
    x = 10       # x → Static/class variable of class c1
    def m1(self):
        self.y = 20   # y → Instance variable of object 'a' (or any object calling m1)
        z = 30        # z → Local variable inside method m1
        c1.m = 40     # m → Static/class variable of class c1

def f1():
    a = c1()
    a.p = 50       # p → Instance variable of object 'a' (created inside f1)
    c1.q = 60      # q → Static/class variable of class c1
    s = 70         # s → Local variable inside function f1

k = 80             # k → Global variable
c1.l = 90          # l → Static/class variable of class c1
b = c1()
b.n = 100          # n → Instance variable of object 'b'
