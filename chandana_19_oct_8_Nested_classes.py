# Find  outputs 
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
o.m1() #  call  m1()  method  of  outer  class
i=outer.inner() 
i.m1() # call  m1()  method  of  inner  class
o=outer() 
i=o.inner() 
i.m1() # # call  m1()  method  of  inner  class  in  another  way
outer.inner().m1() #   call  m1()  method  of  inner  class  in  one  more  way
#i = inner() # error : cannot access inner class directly without creating outer class object
'''
o/p:
Outer  class  constructor
Outer  class  method
Inner  class  constructor
Inner  class  method
Outer  class  constructor
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method
'''



# Find  outputs 
class   emp:
	def __init__(self):
		self.empno=25 
		self.ename= 'Rama Rao'
		self.sal=10000.0 #   initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.d=self.date() #   create  date  class  object
	def   disp(self):
		print('Emp no :',self.empno) 
		print('Emp name :',self.ename)
		print('Emp salary :',self.sal) #   print  empno , ename , sal  of  object  self
		self.d.disp() #  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd=15
			self.mm=5
			self.yy=1947 #  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(f'{self.dd}-{self.mm}-{self.yy}') #   print  dd , mm , yy  of  object  self
# End  of  the  class
e=emp()
e.disp() #   call  disp()  method  of  emp  class
'''
o/p:
Emp no : 25
Emp name : Rama Rao
Emp salary : 10000.0
15-5-1947
'''


# Find outputs 
class  outer:
	def  __init__(self):
		self.x=25 #   initialize  variable  'x'  of  object  self  to  25
		self.i1=self.inner1() #   create  inner1  class  object
		self.i2=self.inner2() #  create  inner2  class  object
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
o.disp() #  call   disp()  method  of outer  class
o.i1.disp() #  call   disp()  method  of inner1  class
o.i2.disp() #  call   disp()  method  of inner2  class
'''
o/p:
25
1st  inner  class  method
2nd  inner  class  method
'''


# Find  outputs 
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
a=c1() #  create  c1  class  object
b=c1.c2() #   create  inner  c2  class  object
c=c2() #  create  outer  c2  class  object
'''
o/p:
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor
'''


# Find  outputs  
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a=c2() #   create  outer  c2  class  object
b=c2.c2() #   create  inner  c2  class  object
b=a.c2() #  create  inner  c2  class  object  in  another  way
'''
o/p:
outer  class  constructor
inner  class  constructor
inner  class  constructor
'''


# Find  outputs 
class c1:
    x = 10 # static variable
    def __init__(self):
	    self . y = 20 # instance variable 
a = c1() 
b = c1()
a . x += 1 # a.x=a.x+1 
b . y += 1 # b.y=b.y+1
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 10
print(a . __dict__) # {'y':20,'x':11}
print(b . __dict__) # {'y':21}
print(c1 . __dict__) # {'x':10} and Enviromental variables



# Find  outputs 
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) # 10
print(a . x) # 20



# Find  outputs  
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
print(a . x) # 30
print(a . y) # 20
print(b . x) # 30
print(b . y) # 20
print(c1 . x , c1 . y) # 30 40
#print(cls . x , cls . y) # error : cls is not defined outside the class
#print(self . x , self . y) # error : self is not defined outside the class



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) # 35



#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1() # type and address of c1 
#a . m1(35) # error : takes only 1 positional argument, but 2 are given self,35



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
c1 . m1(25)
a = c1()
a . m1()
'''
o/p:
static / instance  method
25
static / instance  method
type and address of c1
'''


# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) #  print  static  variable  'x'
		print(self.x) #   print  static  variable  'x'  in  another  way
		#print(x)
	def   m1(self):
		print(c1.x) #  print  static  variable  'x'
		print(self.x) # print  static  variable  'x'  in  another  way
		#print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x) #   print  static  variable  'x'
		print(c1.x) #   print  static  variable  'x'  in  another  way
		#print(self . x)
	@staticmethod
	def   m3():
		print(c1.x) #   print  static  variable  'x'
		#print(cls . x)
		#print(self . x)
# End  of  the  class
print(c1.x) #  print  static  variable  'x'
a=c1()
print(a.x) #  print  static  variable  'x'  in  another  way
#print(x)
#print(self . x)
#print(cls . x)
a.m1() #  call  method  m1()
c1.m2()
a.m2() #   call  method  m2()
c1.m3()
a.m3() #  call  method  m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 # How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20 # How  to  add  static  variable  'b'  with  value  20
		self.c=30 # How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d=40 # How  to  add  static  variable  'd'  with  value  40
		self.e=50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60 # How  to  add  static  variable  'f'  with  value  60
		c1.g=70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25 error: cannot add instance variable
	@staticmethod
	def   m3():
		c1.h=80 # How  to  add  static  variable  'h'  with  value  80
		#self . k = 25 # error : cannot use self and cls in static method directly
		#cls . k = 35
#End  of  the  class
print('Begin')
print(c1 . __dict__) # {'a':10} and EV's
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__) # {'a':10,'b':20} and EV's
print()
print()
x.m1() # How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__) # {'a':10,'b':20,'d':40} and EV's
print()
print()
c1.m2() # How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__) # {'a': 10, 'b': 20, 'd': 40, 'f': 60, 'g': 70} and Ev's
print()
print()
c1.m3() # How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__) # {'a': 10, 'b': 20, 'd': 40, 'f': 60, 'g': 70,'h':80} and Ev's
print()
print()
c1.i=90 # How  to  add  static  variable  'i'  with  value  90
c1.j=100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__) # {'a': 10, 'b': 20, 'd': 40, 'f': 60, 'g': 70,'h':80,'i':90,'j':100} and Ev's
print()
print()
print("Object  'x' ")
print(x . __dict__) # {'c': 30, 'e': 50}



# Find  outputs  
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #  How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'



# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 
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
o/p:
Enter  any  number :  10
Enter  any  number :  20
Enter  any  number :  30
Enter  any  number :  40
Enter  any  number :  50
Enter  any  number :  60
Enter  any  number :  70
13    21    31    12
13    41    51    13
13    61    71    14
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
		vector.n=int(input('Enter number of elemnts: ')) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a=[]
		print(f'enter {vector.n} elements :')
		for i in range(vector.n):
			val=int(input())
			self.a.append(val) # How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.a=[]
		for i in range(vector.n):
			self.a.append(x.a[i] + y.a[i]) # How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1() # How  to  call  get1()  method
a=vector() # How  to  read  the  list  into  1st  object
b=vector() # How  to  read  the  list  into  2nd  object  'b'
a.get2() 
b.get2()# How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
c=vector()
c.add(a,b) # How  to  print  the  list  of  3rd   object
print('sum of vectors :',c.a)
'''
o/p:
enter 5 elements :
4
7
5
6
5
enter 5 elements :
4
4
4
4
44
sum of vectors : [8, 11, 9, 10, 49]
'''


'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
a={}
b=c1.__dict__
for  x in b:
	if not x.startswith('__') and not x.endswith('__'):
		a[x]=b[x]
print("static variables :",a)


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance var
	c1 . q = 60   #  What  is  variable   'q'  ---> static var
	s = 70   #  What  is  variable   's'  ---> local var
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable





