# static variable x


# Find  outputs  (Home  work)
class outer:
    def __init__(self):
        print('Outer class constructor')

    def m1(self):
        print('Outer class method')

    class inner:
        def __init__(self):
            print('Inner class constructor')

        def m1(self):
            print('Inner class method')

# end of the class

# Several ways to create objects and call methods:
a = outer()
a.m1()  # call m1() method of outer class

# 1) Create inner using outer instance
i = a.inner()
i.m1()  # call m1() of inner instance

# 2) Create inner directly from outer class
j = outer.inner()
j.m1()

# 3) Call inner method without creating a named variable
outer.inner().m1()






# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		self.dob = emp.date(15, 8, 1947)

	def   disp(self):
		print(f'Empno: {self.empno}, Name: {self.ename}, Salary: {self.sal}')
		self.dob.disp()
  
	class   date:
		def    __init__(self, dd, mm, yy):
			self.dd = dd
			self.mm = mm
			self.yy = yy
   
		def disp(self):
			print(f'dob: {self.dd:02d}-{self.mm:02d}-{self.yy}')
# End  of  the  class
# How  to  call  disp()  method  of  emp  class
e = emp()
e.disp()



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1 = outer.inner1() # How  to  create  inner1  class  object
		self.i2 = outer.inner2() # How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer() # How  to  call   disp()  method  of outer  class
o.disp()

# How  to  call   disp()  method  of inner1  class
i1 = o.inner1()
i1.disp()

# How  to  call   disp()  method  of inner2  class
i2 = o.inner2()
i2.disp()


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
a = c1() # How  to  create  c1  class  object
b = a.c2() # How  to  create  inner  c2  class  object
c = c2() # How  to  create  outer  c2  class  object





 # Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
a = c2() # How  to  create  outer  c2  class  object
b = a.c2() # How  to  create  inner  c2  class  object
c = c2() # How  to  create  inner  c2  class  object  in  another  way

    
    
    # Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1() 
b = c1()
a . x += 1
b . y += 1
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 11
print(a . _dict_) # {'y': 20}
print(b . _dict_) # {'y': 21}
print(c1 . _dict_) # {'x': 11, '__module__': '__main__', '__init__': <function c1._init_ at 0x7f8b8c2c0af0>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}



# static   variable  --->

# Object  'a'  --->

# Object  'b'  --->


# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) # 10
print(a . x) # 20


'''
static   variable   --->

object  'a'   --->
'''


# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  _init_(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()
b = c1()
c1 . m1()
print(a . x) # 
print(a . y) # 20
print(b . x) # 30
print(b . y) #20
print(c1 . x , c1 . y) # 30 40
print(cls . x , cls . y) # Error 
print(self . x , self . y) # Error


# static   variable   --->
# object  'a'   --->
# object  'b'   --->

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1() # object  created
a . m1(35) # 35


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1() #  Object created
a . m1() # type and address of Object
a . m1(35) #  TypeError: m1() takes 1 positional argument but 2 were given



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
c1 . m1(25) # static  method  
# 25
a = c1() #
a . m1() # static / instance  method 
# type and address of Object

    
    
    
# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(self.x) # How  to  print  static  variable  'x'  in  another  way
		print(x) # Error
	def   m1(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(self.x) # How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # Error
	@classmethod
	def   m2(cls):
		print(cls.x) #How  to  print  static  variable  'x'
		print(c1.x) # How  to  print  static  variable  'x'  in  another  way
		print(self . x) # Error
	@staticmethod
	def   m3():
		print(c1.x) # How  to  print  static  variable  'x'
		print(cls . x) # error
		print(self . x) # error
# End  of  the  class
print(c1.x) #How  to  print  static  variable  'x'
a = c1() 
print(a.x) # #How  to  print  static  variable  'x'  in  another  way
print(x) # error
print(self . x) # error
print(cls . x) # error
a.m1() # How  to  call  method  m1()
a.m2() # How  to  call  method  m2()
a.m3() # How  to  call  method  m3()




# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 # How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b = 20 # How  to  add  static  variable  'b'  with  value  20
		self.c = 30 # How  to  add  instance  variable  'c'  with  value  30
		cls.k = 25 # error
	def   m1(self):
		c1.d = 40 # How  to  add  static  variable  'd'  with  value  40
		self.e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60 # How  to  add  static  variable  'f'  with  value  60
		cls.g = 70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		cls.k = 25 # error
	@staticmethod
	def   m3():
		c1.h = 80 #How  to  add  static  variable  'h'  with  value  80
		self.k = 25 # error
		cls.k = 35 # error
#End  of  the  class
print('Begin')
print(c1 . _dict_) # {'a':10}
print() # 
print()
x = c1()
print('Constructor')
print(c1 . _dict_) # {'a':10, 'b':20, 'c':30}
print()
print()
 How  to  call  m1()  method
print('Instance  method  m1')
print(c1 ._dict_) # {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
print()
print()
How  to  call  m2()  method
print('class  method   m2') # 
print(c1 . _dict_) # {'a':10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70}
print()
print()
How  to  call  m3()  method
print('static   method   m3')
print(c1 . _dict_) # {'a':10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70, 'h':80}
print() # 
print()

How  to  add  static  variable  'i'  with  value  90
How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_) # {'a':10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70, 'h':80, 'i':90}
print()
print()
print("Object  'x' ")
print(x . _dict_) # {'c':30, 'e':50, 'j':100}





    
    
# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) # How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'
print(c1.__dict__) # {'a': 1, 'b': 2, 'c': 3, Ev's}
    
    
#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):
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
a . get2() # 
b . get2()
c . get2()
a . compute() # 
b . compute()
c . compute()
a . disp() # 13 21 31 12
b . disp() # 13 41 51 13
c . disp() # 13 61 71 14

static variable x = 13

object 'a' y = 21 , z = 31 , x = 12
object 'b' y = 40 , z = 50 , x = 13
object 'c' y = 60 , z = 70 , x = 14


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
class  vector:
	@staticmethod
	def get1():
		n = int(input('how many elements: ')) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a = [] # How  to  read  the  list  into  the  object
		for i in range(vector.n):
			inp = int(input(f'Enter element {i+1}: '))
			self.a.append(inp)
	def add(self , x , y):
		self.a = [] # How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
  		for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])
vector.get1() # How  to  call  get1()  method
x = vector() 
x.get2() # How  to  read  the  list  into  1st  object
y = vector() 
y.get2() # How  to  read  the  list  into  2nd  object
z = vector()
z.add(x,y)  # How  to  read  the  list  into  3rd  object
print('Result: ', z.a) # How  to  print  the  list  of  3rd   object

How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
How  to  print  the  list  of  3rd   object

    
    
    
    
    
    
'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
print(c1.__dict__)
a = {}
b = c1.__dict__
for i in b:
    	if not (i.startswith('__') and i.endswith('__')):
         a[i] = b[i]
print('static variables of class c1 : ',a) # {'x': 1, 'y': 2, 'z': 3}
# {'_module': 'main', 'firstlineno': 6, 'x': 1, 'y': 2, 'z': 3, 'static_attributes': (), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref': <attribute 'weakref' of 'c1' objects>, 'doc_': None}


static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}

    
    
    # What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->
		z = 30   #  What  is  variable   'z'  --->
		c1 . m = 40   #  What  is  variable   'm'  --->
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->
	c1 . q = 60   #  What  is  variable   'q'  --->
	s = 70   #  What  is  variable   's'  --->
#end of the function
k = 80   #  What  is  variable 'k'  --->
c1 . l = 90   #  What  is  variable  'l'  --->
b = c1()
b . n = 100   #  What  is  variable  'n' --->