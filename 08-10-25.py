#1st program
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
o=outer()
o.m1()#How  to  call  m1()  method  of  outer  class
o.inner().m1()#How  to  call  m1()  method  of  inner  class
outer.inner().m1()#How  to  call  m1()  method  of  inner  class  in  another  way
outer().inner().m1()#How  to  call  m1()  method  of  inner  class  in  one  more  way
#i = inner()#Error cannot directly call inner class without outer class


#2nd program
# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		self.empno=25
		self.ename='Rama Rao'
		self.sal=10000.0#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.d=self.date()#How  to  create  date  class  object
	def   disp(self):
		print('emp No: ',self.empno)
		print('ename: ',self.ename)
		print('salary: ',self.sal)#How  to  print  empno , ename , sal  of  object  self
		self.d.disp()#How  to  call  disp()  method  of  date  class
	class   date:
		def    _init_(self):
			self.dd=15
			self.mm=8
			self.yy=1947#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(f'Date: {self.dd}-{self.mm}-{self.yy}')#How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e=emp()
e.disp()#How  to  call  disp()  method  of  emp  class


#3rd program
# Find outputs (Home  work)
class  outer:
	def  _init_(self):
		self.x=25#How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1=self.inner1()#How  to  create  inner1  class  object
		self.i2=self.inner2()#How  to  create  inner2  class  object
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
o.inner1().disp()#How  to  call   disp()  method  of inner1  class
o.inner2().disp()#How  to  call   disp()  method  of inner2  class


#4th program
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
b=a.c2()#How  to  create  inner  c2  class  object
c=c2()#How  to  create  outer  c2  class  object


#5th program
# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
a=c2()#How  to  create  outer  c2  class  object
b=a.c2()#How  to  create  inner  c2  class  object
c=c2.c2()#How  to  create  inner  c2  class  object  in  another  way


#6th program
# Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
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
print(a . _dict_)#{'y': 20, 'x': 11}
print(b . _dict_)#{'y': 21}
print(c1 . _dict)#{'module': 'main', 'x': 10, 'init': <function c1.init_ at 0x7db0a3e0c220>, '_dict': <attribute 'dict' of 'c1' objects>, 'weakref': <attribute 'weakref' of 'c1' objects>, 'doc_': None}

'''
static   variable  --->x=10

Object  'a'  --->y=20,x=11

Object  'b'  --->y=21 
'''


#7th program
# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)#10
print(a . x)#20
'''
static   variable   --->x=10

object  'a'   --->x=20
'''


#8th program
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
print(a . x)#30
print(a . y)#20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#30 40
#print(cls . x , cls . y)#error
#print(self . x , self . y)#error
'''
static   variable   --->x=10--->30

object  'a'   --->y=20

object  'b'   --->y=20
'''


#9th program
#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35


#10th program
#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1()#type and address of "a"
a . m1(35)#error,extra arg is passed


#11th program
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
c1 . m1(25)#static method/instance method  /n 25
a = c1()
a . m1()#static/instance method /n type and address of obj"a"


#12th program 
# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		#print(x)#x is not defined error
	def   m1(self):
		print(self.x)#How  to  print  static  variable  'x'
		print(c1.x)#How  to  print  static  variable  'x'  in  another  way
		#print(cls . x)#error,cls is not defined
	@classmethod
	def   m2(cls):
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls.x)#How  to  print  static  variable  'x'  in  another  way
		#print(self . x)#error,self is not defined
	@staticmethod
	def   m3():
		print(c1.x)#How  to  print  static  variable  'x'
		#print(cls . x)#error cls is not defined
		#print(self . x)#self is not defined
# End  of  the  class
a=c1()
print(a.x)#How  to  print  static  variable  'x'
print(c1.x)#How  to  print  static  variable  'x'  in  another  way
#print(x)#error,there is no gv x defined in pgm
#print(self . x)#error,self is not defined
#print(cls . x)#error,cls is not defined
a.m1()#How  to  call  method  m1()
a.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()


#13th program
# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10#How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		c1.b=20#How  to  add  static  variable  'b'  with  value  20
		self.c=30#How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25#error,cls is not defined
	def   m1(self):
		c1.d=40#How  to  add  static  variable  'd'  with  value  40
		self.e=50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60#How  to  add  static  variable  'f'  with  value  60
		c1.g=70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25#error,self is not defined
	@staticmethod
	def   m3():
		c1.h=80#How  to  add  static  variable  'h'  with  value  80
		#self . k = 25#error,self is not defined
		#cls . k = 35#error,cls is not defined
#End  of  the  class
print('Begin')
print(c1 . _dict_)
print()
print()
x = c1()
print('Constructor')
print(c1 . _dict_)
print()
print()
x.m1()#How  to  call  m1()  method
print('Instance  method  m1')
print(c1 ._dict_)
print()
print()
x.m2()#How  to  call  m2()  method
print('class  method   m2')
print(c1 . _dict_)
print()
print()
c1.m3()#How  to  call  m3()  method
print('static   method   m3')
print(c1 . _dict_)
print()
print()
c1.i=90#How  to  add  static  variable  'i'  with  value  90
x.j=100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_)
print()
print()
print("Object  'x' ")
print(x . _dict_)


#14th program
# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)#How  to  print  variable  'a'
print(c1.b)#How  to  print  variable  'b'
print(c1.c)#How  to  print  variable  'c'


#15th program
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

#16th program
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


# 17th Write  a  program  to  add  two  Vector  objects
'''
1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  ---> vector . n
'''
class  vector:
	@staticmethod
	def get1():
		n=2#How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a=eval(input('Enter the list: '))#How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.a=[]
		for i in range(min(len(x.a),len(y.a))):
			self.a.append(x.a[i]+y.a[i])
		return self#How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1()#How  to  call  get1()  method
x=vector()
y=vector()
z=vector()
x.get2()#How  to  read  the  list  into  1st  object
y.get2()#How  to  read  the  list  into  2nd  object  'b'
z.add(x,y)#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(z.a)#How  to  print  the  list  of  3rd   object


#18th program
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
res={}
for  i  in  c1.__dict__:
    if  not(i.startswith('__')  and  i.endswith('__')):
        res[i]=c1.__dict__[i]
print("static  variables  of  class  c1 : ",res)  
