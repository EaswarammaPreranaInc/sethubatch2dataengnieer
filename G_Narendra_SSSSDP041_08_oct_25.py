## Find  outputs  (Home  work)
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
#How  to  call  m1()  method  of  outer  class
o = outer()
o . m1()
#How  to  call  m1()  method  of  inner  class
i = o . inner()
i . m1()
#How  to  call  m1()  method  of  inner  class  in  another  way
outer . inner(). m1()
#How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()
i . m1()


# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
        self.sal = 10000.0
        #How  to  create  date  class  object
		self.dob = self . date()
	def   disp(self):
		#How  to  print  empno , ename , sal  of  object  self
		print(self . empno , self . ename , self . sal)
        #How  to  call  disp()  method  of  date  class
		self . dob . disp()
	class   date:
		def    _init_(self):
			#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self . dd = 15
            self . mm = 8
            self . yy = 1947	
		def disp(self):
			#How  to  print  dd , mm , yy  of  object  self
			print(self . dd , self . mm , self . yy)
# End  of  the  class
#How  to  call  disp()  method  of  emp  class
e = emp()
e . disp()  
	

# Find  outputs  (Home  work)
class  outer:
	def  _init_(self):
		#How  to  initialize  variable  'x'  of  object  self  to  25
		self . x = 25
        #How  to  create  inner1  class  object
		self . i1 = self . inner1()
        #How  to  create  inner2  class  object
		self
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
#How  to  call   disp()  method  of outer  class
o = outer()
o . disp()
#How  to  call   disp()  method  of inner1  class
o . i1 . disp()
#How  to  call   disp()  method  of inner2  class
o . i2 . disp()
	

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
#How  to  create  c1  class  object
c = c1()
#How  to  create  c2  class  object
c = c2()
#How  to  create  outer  c2  class  object
c = c1 . c2()
	

# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
#How  to  create  outer  c2  class  object
c = c2()
#How  to  create  inner  c2  class  object
c = c2 . c2()
#How  to  create  inner  c2  class  object  in  another  way
c = c2() . c2()
	


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
print(a . _dict_)#{'x': 11, 'y': 20}
print(b . _dict_)#{'y': 21}
print(c1 . _dict_)#{'x': 10, }


'''
static   variable  --->

Object  'a'  --->

Object  'b'  --->'''

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
static   variable   ---> x
object  'a'   --->  x
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
print(a . x)#30
print(a . y)#20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#30 40
print(cls . x , cls . y)#30 40
print(self . x , self . y)#20 20
'''
static   variable   --->x

object  'a'   --->

object  'b'   --->'''
	
#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)# 35
	

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#TypeError
a = c1()
a . m1()#some address
a . m1(35)#TypeError
	

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
c1 . m1(25)#static  method
a = c1()
a . m1()#static / instance  method
	


# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		#How  to  print  static  variable  'x'
		print(x)
		#How  to  print  static  variable  'x'  in  another  way
		print(self . x)
		print(x)
	def   m1(self):
		#How  to  print  static  variable  'x'
		print(x)
        #How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		#How  to  print  static  variable  'x'
		print(x)
		#How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@staticmethod
	def   m3():
		#How  to  print  static  variable  'x'
		print(x)
		print(cls . x)
		print(self . x)
# End  of  the  class
#How  to  print  static  variable  'x'
print(c1 . x)
#How  to  print  static  variable  'x'  in  another  way
a = c1()
print(a . x)
print(x)
print(self . x)
print(cls . x)
#How  to  call  method  m1()
a . m1()
#How  to  call  method  m2()
c1 . m2()
#How  to  call  method  m3()
c1 . m3()
# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	#How  to  add  static  variable  'a'  with  value  10
	a = 10
	def    _init_(self):
		#How  to  add  static  variable  'b'  with  value  20
		c1 . b = 20
        #How  to  add  instance  variable  'c'  with  value  30
		self . c = 30
		cls . k = 25
	def   m1(self):
		#How  to  add  static  variable  'd'  with  value  40
		c1 . d = 40
        #How  to  add  instance  variable  'e'  with  value  50
		self . e = 50
	@classmethod
	def   m2(cls):
		#How  to  add  static  variable  'f'  with  value  60
		cls . f = 60
        #How  to  add  static  variable  'g'  with  value  70  in  another  way
		cls . g = 70
		self . k = 25
	@staticmethod
	def   m3():
		#How  to  add  static  variable  'h'  with  value  80
		c1 . h = 80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Begin')#Begin
print(c1 . _dict_)#{a:10}
print()#/n
print()#/n
x = c1()
print('Constructor')#Constructor
print(c1 . _dict_)#{a:10 , b:20 , k:25}
print()#/n
print()#/n
#How  to  call  m1()  method
x . m1()
print('Instance  method  m1')#Instance  method  m1
print(c1 ._dict_)#{a:10 , b:20 , d:40 , k:25}
print()#/n
print()#/n
#How  to  call  m2()  method
c1 . m2()
print('class  method   m2')#class  method   m2
print(c1 . _dict_)#{a:10 , b:20 , d:40 , f:60 , g:70 , k:25}
print()#/n
print()#/n
#How  to  call  m3()  method
c1 . m3()
print('static   method   m3')#static   method   m3
print(c1 . _dict_)#{a:10 , b:20 , d:40 , f:60 , g:70 , h:80 , k:25}
print()#/n
print()#/n
#How  to  add  static  variable  'i'  with  value  90
c1 . i = 90
#How  to  add  instance  variable  'j'  with  value  100
x . j = 100
print('Outside  the  class')#Outside  the  class
print(c1 . _dict_)#{a:10 , b:20 , d:40 , f:60 , g:70 , h:80 , i:90 , k:25}
print()#/n
print()#/n
print("Object  'x' ")#Object  'x'
print(x . _dict_)#{c:30 , e:50 , j:100}
	

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
#How  to  print  variable  'a'
print(c1 . a)#1
#How  to  print  variable  'b'
print(c1 . b)#2
#How  to  print  variable  'c'
print(c1 . c)#3
	

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
a . get2()# inputs  20 , 30
b . get2()# inputs  40 , 50
c . get2()# inputs  60 , 70
a . compute()# inputs  None
b . compute()# inputs  None
c . compute()# inputs  None
a . disp()# outputs  12 21 31 13
b . disp()# outputs  12 41 51 13
c . disp()# outputs  12 61 71 13


'''
static   variable   ---> x

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
		#How  to  read  number  of  elements  into  variable  'n'
		vector . n = int(input('Enter  number  of  elements  :  '))
	def get2(self):
		#How  to  read  the  list  into  the  object
		self . a = [eval(x) for x in input('Enter  elements  of  the  list  :  ').split()]
	def add(self , x , y):
		#How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
		self . a = [x . a[i] + y . a[i] for i in range(vector . n)]
#How  to  call  get1()  method
vector . get1()
#How  to  read  the  list  into  1st  object
x = vector()
#How  to  read  the  list  into  2nd  object  'b'
y = vector()
#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
z = vector()
#How  to  print  the  list  of  3rd   object
print(z . a)
	

'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
import  sys
for  i  in  c1 . _dict_:
    if  not  (i . startswith('__')  and  i . endswith('__')):
        print(i , ' : ' , c1 . _dict_[i])
#o/p
# x  :  1
# y  :  2
# z  :  3


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static  variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance  variable
		z = 30   #  What  is  variable   'z'  ---> local  variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static  variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance  variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static  variable
	s = 70   #  What  is  variable   's'  ---> local  variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> # global  variable
c1 . l = 90   #  What  is  variable  'l'  ---># static  variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---># instance  variable