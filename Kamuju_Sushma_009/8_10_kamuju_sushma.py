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
obj_outer=outer() 
obj_outer.m1() #How  to  call  m1()  method  of  outer  class
obj_inner=obj_outer.inner() 
obj_inner.m1()#How  to  call  m1()  method  of  inner  class
obj_inner2=outer.inner()
obj_inner2.m1()#How  to  call  m1()  method  of  inner  class  in  another  way
i = inner() #error
outer.inner().m1() #How  to  call  m1()  method  of  inner  class  in  one  more  way

# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno=25
		self.ename='Rama Rao' 
		self.sal=10000.0 #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		obj=emp.date() #How  to  create  date  class  object
	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print(self.empno)
		print(self.ename)
		print(self.sal)
		emp.date().disp()
		# How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd=15
			self.mm=8
			self.yy=1947
			
		def disp(self):
			# How  to  print  dd , mm , yy  of  object  self
			print(self.dd,self.mm,self.yy,sep=':')
# End  of  the  class
# How  to  call  disp()  method  of  emp  class
emp().disp()

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		# How  to  initialize  variable  'x'  of  object  self  to  25
		self.x=25
		# How  to  create  inner1  class  object
		obj1=outer.inner1()
		# How  to  create  inner2  class  object
		obj2=outer.inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
# How  to  call   disp()  method  of outer  class
outer().disp()
# How  to  call   disp()  method  of inner1  class
outer.inner1().disp()
# How  to  call   disp()  method  of inner2  class
outer.inner2().disp()

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
# How  to  create  c1  class  object
obj1=c1()
# How  to  create  inner  c2  class  object
obj2=c1.c2()
# How  to  create  outer  c2  class  object
obj3=c2()

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
# How  to  create  outer  c2  class  object
obj1=c2()
# How  to  create  inner  c2  class  object
obj2=c2.c2()
# How  to  create  inner  c2  class  object  in  another  way
obj3=obj1.c2()


# static x=11 
# a=> y=20
# b=> y=21
# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x) #11
print(a . y)#20
print(b . x)#11
print(b . y)#21
print(c1 . x)#11
print(a . __dict__) #{y :20}
print(b . __dict__)#{y:21}
print(c1 . __dict__) #{x:11}


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
static   variable   ---> x= 10

object  'a'   ---> x= 20 
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
# static var: x=30, y=40
# a=> y= 20
# b=> y=20 
print(a . x) #30
print(a . y)#20
print(b . x) #30
print(b . y)#20
print(c1 . x , c1 . y)#30 40
print(cls . x , cls . y) #error there is no class 'cls'
print(self . x , self . y)# there is no object self


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
a . m1(35) #error m1 is expecting 0 args

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1()#__main__c1 address
a . m1(35)#error m1 is expecting 0 args

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
c1 . m1(25) #static/instance method 25
a = c1()
a . m1()# static/ instance method __main__c1, address

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		# How  to  print  static  variable  'x'
		print(c1.x)
		# How  to  print  static  variable  'x'  in  another  way
		print(self.x)
		print(x) #there is no object x
	def   m1(self):
		# How  to  print  static  variable  'x'
		print(self.x)
		# How  to  print  static  variable  'x'  in  another  way
		print(c1.x)
		print(cls . x) # there is ref cls here
	@classmethod
	def   m2(cls):
		# How  to  print  static  variable  'x'
		print(c1.x)
		# How  to  print  static  variable  'x'  in  another  way
		print(cls.x)
		print(self . x) # we cannot treat it as static method and instance method at the same time
	@staticmethod
	def   m3():
		# How  to  print  static  variable  'x'
		print(c1.x)
		print(cls . x) #0 formal parameters so it cannot be instace method or class method
		print(self . x) #
# End  of  the  class
# How  to  print  static  variable  'x'
print(c1.x)
# How  to  print  static  variable  'x'  in  another  way
obj=c1()
print(obj.x)
print(x)# no ref x 
print(self . x)# no ref self
print(cls . x) #no ref cls 
obj =c1()
obj.m1()
c1.m1()
# How  to  call  method  m1()
# How  to  call  method  m2()
c1.m2()
# How  to  call  method  m3()
c1.m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	# How  to  add  static  variable  'a'  with  value  10
	a=10
	def    __init__(self):
		c1.b=20
		# How  to  add  static  variable  'b'  with  value  20
		# How  to  add  instance  variable  'c'  with  value  30
		c1.c=30
		cls . k = 25 # no cls here 
	def   m1(self):
		# How  to  add  static  variable  'd'  with  value  40
		c1.d=40
		# How  to  add  instance  variable  'e'  with  value  50
		c1.e=50
	@classmethod
	def   m2(cls):
		# How  to  add  static  variable  'f'  with  value  60
		c1.f=60
		# How  to  add  static  variable  'g'  with  value  70  in  another  way
		c1.g=70
		self . k = 25 # no self here 
	@staticmethod
	def   m3():
		# How  to  add  static  variable  'h'  with  value  80
		c1.h=80
		self . k = 25 # it is a static method so it cannot be instance method or class method because it 
		cls . k = 35# has 0 args
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
How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
How  to  add  static  variable  'i'  with  value  90
How  to  add  instance  variable  'j'  with  value  100
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
# How  to  print  variable  'a'
print(c1.a)
# How  to  print  variable  'b'
print(c1.b)
# How  to  print  variable  'c'
print(c1.c)


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
# static x=13
# a= y=1 z=1 x=1
# b= y=1 z=1 x=1
# c= y=1 z=1 x=1
# Test . get1()
# a = Test()
# b = Test()
# c = Test()
# a . get2()
# b . get2()
# c . get2()
# a . compute()
# b . compute()
# c . compute()
# a . disp()# 13 1 1 1
# b . disp()#13 1 1 1
# c . disp()# 13 1 1 1
# Test . x , self . y , self . z ,  self . x , sep = '\t
# static x=13
# a= y=1 z=1 x=1
# b= y=1 z=1 x=1
# c= y=1 z=1 x=1

'''
static   variable   --->

Object  'a'  --->g

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
		vector.n=int(input("n: ")) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		# How  to  read  the  list  into  the  object
		self.a=eval(input("Enter list: "))
	def add(self , x , y):
		# How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
		for i in range(len(x)):
			self.a[i]=x[i]+y[i]
# How  to  call  get1()  method
vector.get1()
# How  to  read  the  list  into  1st  object
obj1=vector()
obj1.get2()
# How  to  read  the  list  into  2nd  object  'b'
obj2=vector()
obj2.get2()
# How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
obj3=vector()
obj3.add(obj1,obj2)
# How  to  print  the  list  of  3rd   object
print(obj3.a)

'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
l=c1.__dict__.keys()
res=[]
for x in l:
	if not (x.startswith('__') and x.endswith('__')):
		res.append(x)
print(res)

# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static 
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> can be static or instance variable
		z = 30   #  What  is  variable   'z'  ---> static
		c1 . m = 40   #  What  is  variable   'm'  ---> static
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance
	c1 . q = 60   #  What  is  variable   'q'  ---> static 
	s = 70   #  What  is  variable   's'  ---> local
#end of the function
k = 80   #  What  is  variable 'k'  ---> global
c1 . l = 90   #  What  is  variable  'l'  ---> static
b = c1()
b . n = 100   #  What  is  variable  'n' --->  instance variable