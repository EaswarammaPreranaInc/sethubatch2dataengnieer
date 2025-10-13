#================================================== # Find  outputs  (Home  work)

class outer:
   def ____init____(self):
      print('Outer class constructor')
   def m1(self):
      print('Outer class method')
   class inner:
      def ____init____(self):
         print('Inner class constructor')
      def m1(self):
         print('Inner class method')
# end of the class

# How to call m1() method of outer class
o = outer()
o.m1()

# How to call m1() method of inner class
i = outer.inner()
i.m1()

# How to call m1() method of inner class in another way
outer.inner().m1()

# How to call m1() method of inner class in one more way
j = outer.inner()
j.m1()

'''
Outer class constructor
Outer class method
Inner class constructor
Inner class method
Inner class constructor
Inner class method
Inner class constructor
Inner class method
'''

#================================================== # Find  outputs  (Home  work)
class emp:
   def __init__(self):
      self.empno = 25
      self.ename = 'Rama Rao'
      self.sal = 10000.0
      self.dob = self.date()
   def disp(self):
      print(self.empno, self.ename, self.sal)
      self.dob.disp()
   class date:
      def __init__(self):
         self.dd = 15
         self.mm = 8
         self.yy = 1947
      def disp(self):
         print(self.dd, self.mm, self.yy)
# End of the class
e = emp()
e.disp()
'''
25 Rama Rao 10000.0
15 8 1947
'''
#================================================== # Find outputs (Home  work)

class  outer:
	def  __init__(self):
		self.x=25# How  to  initialize  variable  'x'  of  object  self  to  25
		self.y=self.inner1()# How  to  create  inner1  class  object
		self.z=self.inner2()# How  to  create  inner2  class  object
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
o=outer()
o.disp()
# How  to  call   disp()  method  of inner1  class
o.y.disp()
# How  to  call   disp()  method  of inner2  class
o.z.disp()
'''
25
1st  inner  class  method
2nd  inner  class  method
'''
#================================================== # Find  outputs  (Home  work)

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
# #end of the class
# How  to  create  c1  class  object
a=c1()
# How  to  create  inner  c2  class  object
b=a.c2()
# How  to  create  outer  c2  class  object
c=c2()
'''
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor
'''

#================================================== # Find  outputs  (Home  work)

class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
# How  to  create  outer  c2  class  object
a=c2()
# How  to  create  inner  c2  class  object
c=c2.c2()
# How  to  create  inner  c2  class  object  in  another  way
b=a.c2()

'''
outer  class  constructor
inner  class  constructor
inner  class  constructor
'''


#================================================== # Find  outputs (Home  work)

class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)
print(a . y)
print(b . x)
print(b . y)
print(c1 . x)
print(a . __dict__)
print(b . __dict__)
print(c1 . __dict__)

'''
11
20
10
21
10
{'y': 20, 'x': 11}
{'y': 21}
{'__module__': '__main__', '__firstlineno__': 2, 'x': 10,
'__init__': <function c1.__init__ at 0x000001EF89900E00>, '__static_attributes__': ('y',), '__dict__': <attribute '__dict__' of 'c1' objects>,
 '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}
'''

'''
static   variable  --->

Object  'a'  --->

Object  'b'  --->
'''
#================================================== # Find  outputs (Home  work)

class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)
print(a . x)
'''
10
20
'''

'''
static   variable   --->

object  'a'   --->
'''

#================================================== # Find  outputs  (Home  work)

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
print(a . x)
print(a . y)
print(b . x)
print(b . y)
print(c1 . x , c1 . y)
print(cls . x , cls . y)
print(self . x , self . y)


'''
static   variable   --->

object  'a'   --->

object  'b'   --->
'''
#================================================== #  Find  outputs

class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()
a . m1(35)

#================================================== #  Find  outputs

class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()
a . m1()
a . m1(35)

#================================================== #  Find  outputs

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

#================================================== # How  to  access  static  variable  in  different  ways  ?

class   c1:
	x = 25
	def   __init__(self):
		How  to  print  static  variable  'x'
		How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		How  to  print  static  variable  'x'
		How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		How  to  print  static  variable  'x'
		How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
How  to  print  static  variable  'x'
How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
How  to  call  method  m1()
How  to  call  method  m2()
How  to  call  method  m3()

#================================================== # How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?

class   c1:
	How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		How  to  add  static  variable  'b'  with  value  20
		How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25
	def   m1(self):
		How  to  add  static  variable  'd'  with  value  40
		How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		How  to  add  static  variable  'f'  with  value  60
		How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25
	@staticmethod
	def   m3():
		How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
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

#================================================== # Find  outputs  (Home  work)

class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
How  to  print  variable  'a'
How  to  print  variable  'b'
How  to  print  variable  'c'

#================================================== #  Tricky  program

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



#==================================================
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

#==================================================
'''

Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class

#==================================================
{'__module': 'main', 'firstlineno': 6, 'x': 1, 'y': 2, 'z': 3, 'static__attributes': (), 'dict': <attribute 'dict' of 'c1' objects>,
                         'weakref': <attribute 'weakref' of 'c1' objects>, 'doc__': None}

static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}

#================================================== # What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)

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