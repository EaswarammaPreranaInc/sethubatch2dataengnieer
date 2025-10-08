# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 10
print(a . __dict__) # {'y' : 20 , 'x' : 11}
print(b . __dict__) # {'y' : 21}
print(c1 . __dict__) # {all the Evs , 'x' : 10}


'''
static   variable  ---> x = 11

Object  'a'  ---> y = 20

Object  'b'  ---> y = 21

'''


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
static   variable   ---> x = 10

object  'a'   ---> x = 20
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
print(a . x) # 30
print(a . y) # 20
print(b . x) # 30
print(b . y) # 20
print(c1 . x , c1 . y)# 30 <space> 40
print(cls . x , cls . y) # Error as there is no object cls
print(self . x , self . y) # Error as there is no object self


'''
static   variable   ---> x = 30 , y = 40

object  'a'   ---> y = 20

object  'b'   --->  y = 20
'''



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()
a . m1(35)

'''
25
35
'''


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1() # type and address of the object
a . m1(35) # Error as there are 2 arguments




# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1 . x) # How  to  print  static  variable  'x'
		print(self . x) # How  to  print  static  variable  'x'  in  another  way
		print(x) # Error as thee is no local variable x
	def   m1(self):
		print(c1 . x) # How  to  print  static  variable  'x'
		print(self . x) # How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # Error
	@classmethod
	def   m2(cls):
		print(c1 . x) # How  to  print  static  variable  'x'
		print(cls . x) # How  to  print  static  variable  'x'  in  another  way
		#print(self . x) # Error 
	@staticmethod
	def   m3():
		print(c1 . x) # How  to  print  static  variable  'x'
		print(cls . x) # Error 
		print(self . x) # Error 
# End  of  the  class
print(c1 . x) # How  to  print  static  variable  'x'
# How  to  print  static  variable  'x'  in  another  way
c = c1()
print(c . x)
print(x) # Error as there is no global variable x
print(self . x) # Error as there is no object self
print(cls . x) # Error as there is no  object cls
c . m1() # How  to  call  method  m1()
c . m2() # How  to  call  method  m2()
c . m3() # How  to  call  method  m3()

'''
25
25
25
25
25
25
25
25
25
'''



# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 # How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1 . b = 20 # How  to  add  static  variable  'b'  with  value  20
		self . c = 30 # How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 # Error 
	def   m1(self):
		c1 . d = 40 # How  to  add  static  variable  'd'  with  value  40
		self . e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1 . f = 60 # How  to  add  static  variable  'f'  with  value  60
		cls . g = 70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 # Error
	@staticmethod
	def   m3():
		c1 . h = 80 # How  to  add  static  variable  'h'  with  value  80
		self . k = 25 # Error
		cls . k = 35 # Error
#End  of  the  class
print('Begin')
print(c1 . __dict__) # {'a' : 10}
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__) # {'a' : 10 , 'b' : 20}
print()
print()
x . m1() # How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40}
print()
print()
x . m2() # How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70}
print()
print()
x . m3() # How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h' : 80}
print()
print()
# How  to  add  static  variable  'i'  with  value  90
c1 . i = 90
# How  to  add  instance  variable  'j'  with  value  100
x . j = 100
print('Outside  the  class')
print(c1 . __dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h' : 80 , 'i' : 90} 
print()
print()
print("Object 'x' ")
print(x . __dict__) # {'c' : 30 , 'e' : 50  , 'j' : 100}



# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1 . a) # How to print variable 'a'
print(c1 . b) # How to print variable 'b'
print(c1 . c) # How to print variable 'c'

'''
1
2
3
'''

'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  --->  x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->   x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector . n = int(input('Number of Elements : ')) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self . list = eval(input('Enter a List : ')) # How  to  read  the  list  into  the  object
	def add(self , x , y):
		# How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
		self . d = []
		for i in range(vector . n):
			self.d.append(x.list[i] + y.list[i])
vector() . get1() # How  to  call  get1()  method
# How  to  read  the  list  into  1st  object
a = vector()
a . get2()
# How  to  read  the  list  into  2nd  object  'b'
b = vector()
b . get2()
# How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
c = vector()
c . add(a , b)
# How to print the list of 3rd object
print(f'Result : {c.d}')


'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
a = {}
b = c1.__dict__
for  x  in  b:
	if not x . startswith('__') and not x . endswith('__'):
		a[x] = b[x]
print(f'Result :  {a}')


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> local variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static vriable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable
