
#Find  outputs  (Home  work)
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
o=outer()
o.m1()#How  to  call  m1()  method  of  outer  class
b=o.inner()
b.m1()#How  to  call  m1()  method  of  inner  class
c=outer().inner()
c.m1()#How  to  call  m1()  method  of  inner  class  in  another  way
d=outer.inner()#How  to  call  m1()  method  of  inner  class  in  one  more  way
#i = inner()#error inner class object cannot created without outerclass





# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno=25
		self.ename='Rama Rao'
		self.sal=10000.0#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.dob=self.date()#How  to  create  date  class  object
	def   disp(self):
		print('employee number:',self.empno)
		print('employee name:',self.ename)
		print('salary:',self.sal)#How  to  print  empno , ename , sal  of  object  self
		self.dob.disp()#How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd=15
			self.mm=8
			self.yy=1947	#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(f'Date of birth:{self.dd}-{self.mm}-{self.yy}') #How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e=emp()
e.disp()#How  to  call  disp()  method  of  emp  class





# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25 #How  to  initialize  variable  'x'  of  object  self  to  25
		self.y=self.inner1()#How  to  create  inner1  class  object
		self.z=self.inner2()#How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o=outer()
o.disp()#How  to  call   disp()  method  of outer  class
o.y.disp()#How  to  call   disp()  method  of inner1  class
o.z.disp()#How  to  call   disp()  method  of inner2  class



# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
outer=c2()#How  to  create  outer  c2  class  object
i=outer.c2()#How  to  create  inner  c2  class  object
j=c2().c2()#How  to  create  inner  c2  class  object  in  another  way




# Find  outputs (Home  work)
class c1:
    x = 10#static variable
    def __init__(self):
	    self . y = 20#instance variable
a = c1()#20
b = c1()#20
a . x += 1
b . y += 1
print(a . x)#11
print(a . y)#20
print(b . x)#10
print(b . y)#21
print(c1 . x)#10
print(a . __dict__)#{'y':20,'x':11}
print(b . __dict__)#{'y':21}
print(c1 . __dict__)#{ all static variables x:10 and environmental variables}



# Find  outputs (Home  work)
class  c1:
	x = 10#sv
	def  m1(self):
		self . x = 20#iv
a = c1()#empty object
a . m1()
print(c1 . x)#10
print(a . x)#20





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
c1 . m1()#10
print(a . x)#30
print(a . y)#20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#(30,40)
print(cls . x , cls . y)#error
print(self . x , self . y)#error


#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35



#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1()#type and address
a . m1(35)#error


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
c1 . m1(25)#static method/instance method/n 25
a = c1()
a . m1()#static/instance method/n type and address



# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		#print(x)#x is not defined
	def   m1(self):
		print(self.x)#How  to  print  static  variable  'x'
		print(c1.x)#How  to  print  static  variable  'x'  in  another  way
		print(cls . x)#cls is not defined
	@classmethod
	def   m2(cls):
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls.x)#How  to  print  static  variable  'x'  in  another  way
		print(self . x)#error self is not defined
	@staticmethod
	def   m3():
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls . x)#error cls is not defined
		print(self . x)#error self s not defined
# End  of  the  class
a=c1()
print(a.x)#How  to  print  static  variable  'x'
print(cl.x)#How  to  print  static  variable  'x'  in  another  way
print(x)#error
print(self . x)#error
print(cls . x)#error
a.m1()#How  to  call  method  m1()
a.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()





# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10#How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20#How  to  add  static  variable  'b'  with  value  20
		self.c=30#How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 #error cls is not defined
	def   m1(self):
		c1.d=40#How  to  add  static  variable  'd'  with  value  40
		self.e=50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60#How  to  add  static  variable  'f'  with  value  60
		cls.g=70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25#error,cls is not defined
	@staticmethod
	def   m3():
		c1.h=80#How  to  add  static  variable  'h'  with  value  80
		self . k = 25#error,self is not defined
		cls . k = 35#error,cls is not defined
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
c1.m3()#How  to  call  m3()  method
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



#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  ')) #10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))#20
		self . z = int(input('Enter  any  number  :  '))#30
	def   compute(self):
		Test . x += 1 #11,12,13
		self . y  += 1
		self . z  += 1
		self . x  += 1#12,13,14
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
static   variable   --->x=13

Object  'a'  --->y=21 , z=31,x=12

Object  'b'  --->y=41,z=51,x=13

Object  'c'  --->y=61,y=71,x=14

'''


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->class/static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->#instance variable
		z = 30   #  What  is  variable   'z'  --->#local variable
		c1 . m = 40   #  What  is  variable   'm'  --->#static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->#instance variable
	c1 . q = 60   #  What  is  variable   'q'  --->#static variable
	s = 70   #  What  is  variable   's'  --->#local variable
#end of the function
k = 80   #  What  is  variable 'k'  --->#global variable
c1 . l = 90   #  What  is  variable  'l'  --->#static variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->#instance variable