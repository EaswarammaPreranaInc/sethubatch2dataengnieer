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
o = outer()
o.m1()#How  to  call  m1()  method  of  outer  class
i = outer.inner()
i.m1()#How  to  call  m1()  method  of  inner  class
outer.inner().m1()#How  to  call  m1()  method  of  inner  class  in  another  way
i = outer().inner()
outer().inner().m1()#How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()#error

# # Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		self.d=self.date()#How  to  create  date  class  object
	def  disp(self):
		print('Emp No:',self.empno)#How  to  print  empno , ename , sal  of  object  self
		print('ename:',self.ename)
		print('sal:',self.sal)
		self.d.disp()#How  to  call  disp()  method  of  date  class
	class  date:
		def    __init__(self):
			self.dd=25#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.mm=8
			self.yy=1947
		def disp(self):
			print(self.d.dd)#How  to  print  dd , mm , yy  of  object  self
			print(self.d.mm)
			print(self.d.yy)
# End  of  the  class
e=emp()
e.disp()#How  to  call  disp()  method  of  emp  class
	

# # Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25#How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1=self.inner1()#How  to  create  inner1  class  object
		self.i2=self.inner2#How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer()
o.disp()#How  to  call   disp()  method  of outer  class
o.i1.disp()#How  to  call   disp()  method  of inner1  class
o.i2.disp#How  to  call   disp()  method  of inner2  class


# # Find  outputs  (Home  work)
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
obj = c1#How  to  create  c1  class  object
obj2=c1.c2()#How  to  create  inner  c2  class  object
obj3 = c2()#How  to  create  outer  c2  class  object


# # Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
obj1=c2()#How  to  create  outer  c2  class  object
obj2=c2.c2()#How  to  create  inner  c2  class  object
obj_outer=c2()
obj3=obj_outer.c2()#How  to  create  inner  c2  class  object  in  another  way


# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)#11
print(a . y)#20
print(b . x)#10
print(b . y)#21
print(c1 . x)#10
print(a . __dict__)#{'y':20}
print(b . __dict__)#{'y':21}
print(c1 . __dict__)#dictionary of static variable and environment variables of class c1 {'x':11}


'''
static   variable  --->

Object  'a'  --->

Object  'b'  --->

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)#10
print(a . x)#10


'''
static   variable   ---> x= 10

object  'a'   ---> x =20
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
print(a . x)#10
print(a . y)#20
print(b . x)#10
print(b . y)#20
print(c1 . x , c1 . y)#10 40
print(cls . x , cls . y)#30 40
print(self . x , self . y)#10 20


'''
static   variable   --->x=10

object  'a'   --->y =20

object  'b'   --->y=20


#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#calling m1 static method of class c1 with self as 25
a = c1()#c1 class object a is created
a . m1(35)#calling m1 static method of class c1 with self as 35

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
c1 . m1(25)#calling m1 static method of class c1 with self as 25
a = c1()#c1 class object a is created
a . m1()#calling m1 instance method of object a

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(cls . x)#error
	@classmethod
	def   m2(cls):
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls.x)#How  to  print  static  variable  'x'  in  another  way
		print(self . x)#error
	@staticmethod
	def   m3():
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls . x)#error
		print(self . x)#error
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
obj = c1()
print(obj.x)#How  to  print  static  variable  'x'  in  another  way
print(x)
print(self .x)#error
print(cls.x)#error
obj.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	c1.a=10#How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20#How  to  add  static  variable  'b'  with  value  20
		self.c=30#How  to  add  instance  variable  'c'  with  value  30
		c1 . k = 25#(using cls name instead works the same)
	def   m1(self):
		c1.d=40#How  to  add  static  variable  'd'  with  value  40
		self.e=50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60#How  to  add  static  variable  'f'  with  value  60
		c1.g#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25#not valid
	@staticmethod
	def   m3():
		c1.h=80#How  to  add  static  variable  'h'  with  value  80
		self . k = 25#not valid
		cls . k = 35#not valid
#End  of  the  class
print('Begin')
print(c1 . __dict__)
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__)
print()
print()
x.m1()#How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
x.m2()#How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
x.m3()#How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90#How  to  add  static  variable  'i'  with  value  90
x.j=100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)#How  to  print  variable  'a'
print(c1.b)#How  to  print  variable  'b'
print(c1.c)#How  to  print  variable  'c'


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
a . get2()
b . get2()
c . get2()
a . compute()
b . compute()
c . compute()
a . disp()
b . disp()
c . disp()


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
		How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		How  to  read  the  list  into  the  object
	def add(self , x , y):
		How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
How  to  call  get1()  method
How  to  read  the  list  into  1st  object
How  to  read  the  list  into  2nd  object  'b'
How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
How  to  print  the  list  of  3rd   object


'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class

{'__module__': '__main__', '__firstlineno__': 6, 'x': 1, 'y': 2, 'z': 3, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}
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
