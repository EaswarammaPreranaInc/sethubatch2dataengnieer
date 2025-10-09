#Nanda Kishore Vemula
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
o = outer()                 # How  to  call  m1()  method  of  outer  class
o.m1()      
i = outer.inner()           # How  to  call  m1()  method  of  inner  class
i.m1()
o = outer()                 # How  to  call  m1()  method  of  inner  class  in  another  way
i = o.inner()
i.m1()          
outer.inner().m1()          # How  to  call  m1()  method  of  inner  class  in  one  more  way
#i=inner()                   # inner is not defined


# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		# How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		# How  to  create  date  class  object
		self.d = self.date()
	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print("Emp No:", self.empno)
		print("Emp Name:", self.ename)
		print("Salary:", self.sal)
		# How  to  call  disp()  method  of  date  class
		self.d.disp()
	class   date:
		def _init_(self):
			# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			# How  to  print  dd , mm , yy  of  object  self
			print("Date of Joining: {}/{}/{}".format(self.dd, self.mm, self.yy))
# End  of  the  class
# How  to  call  disp()  method  of  emp  class
e = emp()
e.disp()


# Find outputs (Home  work)

class  outer:
	def _init_(self):
		# How  to  initialize  variable  'x'  of  object  self  to  25
		self.x = 25
		# How  to  create  inner1  class  object
		self.i1 = self.inner1()
		# How  to  create  inner2  class  object
		self.i2 = self.inner2()
	def  disp(self):
		print(self.x)
	class inner1:
		def disp(self):
			print('1st  inner  class  method')
	class inner2:
		def disp(self):
			print('2nd  inner  class  method')
#end of the class
# How  to  call   disp()  method  of outer  class
o = outer()
o.disp()
# How  to  call   disp()  method  of inner1  class
o.i1.disp()
# How  to  call   disp()  method  of inner2  class
o.i2.disp()


# Find  outputs  (Home  work)

class c1:
	def _init_(self):
		print('outer  class  c1  constructor')
	class c2:
		def _init_(self):
			print('inner  class  c2  constructor')
#end of the class
class c2:
	def _init_(self):
		print('outer  class  c2  constructor')
#end of the class
# How  to  create  c1  class  object
o1 = c1()      # creates object of outer class c1
# How  to  create  inner  c2  class  object
i1 = c1.c2()   # creates object of inner class c2 inside class c1
# How  to  create  outer  c2  class  object
o2 = c2()      # creates object of outer (separate) class c2


# Find  outputs  (Home  work)

class c2:
	def _init_(self):
		print('outer  class  constructor')

	class c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
# How  to  create  outer  c2  class  object
o = c2()
# How  to  create  inner  c2  class  object
i = c2.c2()
# How  to  create  inner  c2  class  object  in  another  way
o1 = c2()
i1 = o1.c2()


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
print(a . y) #20
print(b . x) #10
print(b . y) #21
print(c1 . x) #10
print(a . __dict__) #{'y':20,'x':11}
print(b . __dict__) #{'y':21}
print(c1 . __dict__) #{'x':11,EVs}


'''
static   variable  ---> x=11

Object  'a'  ---> y=20

Object  'b'  ---> y=21

'''

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) #10
print(a . x) #20


'''
static   variable   ---> x=10

object  'a'   ---> x=10
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
print(a . x) #30
print(a . y) #20
print(b . x) #30
print(b . y) #20
print(c1 . x , c1 . y) #30 40
print(cls . x , cls . y) #Error
print(self . x , self . y) #Error


'''
static   variable   ---> x=30 , y=40

object  'a'   ---> y=20

object  'b'   ---> y=20

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
a . m1() #Type and address of 'a'
a . m1(35) #Error

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
static / instance  method
25
static / instance  method
Type and address of 'a'
'''

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(x) #Error
	def   m1(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x) #Error
	@classmethod
	def   m2(cls):
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x) #Error
	@staticmethod
	def   m3():
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls . x) #Error
		print(self . x) #Error
# End  of  the  class
print(c1.x) #How  to  print  static  variable  'x'
a=c1()
print(a.x) #How  to  print  static  variable  'x'  in  another  way
print(x) #Error
print(self . x) #Error
print(cls . x) #Error
a.m1() #How  to  call  method  m1()
c1.m2() #How  to  call  method  m2()
c1.m3() #How  to  call  method  m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30 #How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 #Error
	def   m1(self):
		c1.d=40 #How  to  add  static  variable  'd'  with  value  40
		self.e=50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60 #How  to  add  static  variable  'f'  with  value  60
		cls.g=70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 #Error
	@staticmethod
	def   m3():
		c1.h=80 #How  to  add  static  variable  'h'  with  value  80
		self . k = 25 #Error
		cls . k = 35 #Error
#End  of  the  class
print('Begin')
print(c1 . __dict__) #{'a':10}
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__) #{'a':10,'b':20}
print()
print()
x.m1() #How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__) #{'a':10,'b':20,'d':40}
print()
print()
c1.m2() #How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__) #{'a':10,'b':20,'d':40,'f':60,'g':70}
print()
print()
c1.m3() #How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__) #{'a':10,'b':20,'d':40,'f':60,'g':70,'h':80}
print()
print()
c1.i=90 #How  to  add  static  variable  'i'  with  value  90
x.j=100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__) #{'a':10,'b':20,'d':40,'f':60,'g':70,'h':80,'i':90}
print()
print()
print("Object  'x' ")
print(x . __dict__) #{'c':30,'e':50,'j':100}


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) #How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'

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
13	21	31	12
13	41	51	13
13	61	71	14
'''

'''
static   variable   ---> x=13

Object  'a'  ---> y=21 z=31 x=12

Object  'b'  ---> y=41 z=51 x=13

Object  'c'  ---> y=61 z=71 x=14
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
		vector.n=int(input("Number  of  elements : ")
	def get2(self):
		self.a=[]#How  to  read  the  list  into  the  object
		print(f'Enter {vector.n} elements : ')
		for i in range(vector.n):
			self.a.append(int(input()))
	def add(self , x , y):
		self.a=[] #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
		for i in range(vector.n):
			self.a.append(x.a[i]+y.a[i])
vector.get1() #How  to  call  get1()  method
x=vector() 
x.get2() #How  to  read  the  list  into  1st  object
y=vector() 
y.get2() #How  to  read  the  list  into  2nd  object  'b'
z=vector()
z.add(x,y) #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(z.a)

'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
staticvar={}
for x,y in c1.__dict__.items():
    if not (x.startswith('__') and x.endswith('__')):
        staticvar[x]=y
print('static variables of c1 class : ',staticvar)

# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> Static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> Instance variable
		z = 30   #  What  is  variable   'z'  ---> Local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> Static Variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> Instance Variable
	c1 . q = 60   #  What  is  variable   'q'  ---> Static Variable
	s = 70   #  What  is  variable   's'  ---> Local Variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> Global Variable
c1 . l = 90   #  What  is  variable  'l'  ---> Static Variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> Instance Variable

'''
Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->3 + 4 * 5 - 6 / (^27)
				                         --->3 + (*45) - 6 / (^27)
				                         --->3 + (*45) - /6^27
				                         --->(+3*45) - /6^27
				                         --->-+3*45/6^27
                            

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   --->a ^ b ^ c
				                             --->a^(^bc)
				                             --->^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  ---> ab+ + c
				                              --->ab+c+
    What  is  the  prefix  expression ?  --->+ab + c
				                             --->++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->(-b + (b2^ - 4 * a * c) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^ - 4a* * c) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^ - 4a*c*) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^4a*c*-) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^4a*c*-) ^ 0.5) / (2 * a)
				                          --->(-b + b2^4a*c*-0.5^) / (2 * a)
				                          --->(-bb2^4a*c*-0.5^+) / (2 * a)
                                          ---->(-bb2^4a*c*-0.5^+) / 2a*
                                          ---->-bb2^4a*c*-0.5^+2a*/

What  is  the  prefix  expression ?   --->/+-b^-^b2**4ac0.5*2a
                                          
                                          

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->ab<bc>cd< and or
    What  is  the  prefix  expression ?   --->or<ab and >bc<cd

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->xy^5Z*/2+
    What  is  the  prefix  expression ?   --->+/^xy*5z2
				                            

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->abcd^e-fgh*+^*+i-
				                        
    What  is  the  prefix  expression ?   --->-+a*b^-^cde+f*ghi
				                    
 '''