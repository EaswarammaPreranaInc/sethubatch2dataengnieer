# Find  outputs  (Home  work)
class outer:
	def _init_(self):
		print('Outer  class  constructor')
	def m1(self):
		print('Outer  class  method')
	class inner:
		def _init_(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
o = outer() 
o.m1() # How  to  call  m1()  method  of  outer  class
i1 = o.inner() 
i1.m1() # How  to  call  m1()  method  of  inner  class
i2 = outer.inner()
i2.m1() # How  to  call  m1()  method  of  inner  class  in  another  way
i3 = outer().inner() 
i3.m1() # How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner() # Error
'''
Outputs
Outer  class  constructor
Outer  class  method
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method
Outer  class  constructor
Inner  class  constructor
Inner  class  method
'''









# Find  outputs  (Home  work)
class emp:
	def _init_(self):
		self.empno = 25 
		self.empname = 'Rama Rao'
		self.sal = 10000.0 # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.dob = self.date() # How  to  create  date  class  object
	def disp(self):
		print("employee number:",self.empno) 
		print("employee name:",self.empname)
		print("Salary:",self.sal) #How  to  print  empno , ename , sal  of  object  self
		self.dob.disp() # How  to  call  disp()  method  of  date  class
	class date:
		def _init_(self):
			self.dd = 15
			self.mm = 8
			self.yy = 1947 #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(F'{self.dd}-{self.mm}-{self.yy}') # How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e = emp()
e.disp() # How  to  call  disp()  method  of  emp  class
'''
Outputs
employee number: 25
employee name: Rama Rao
Salary: 10000.0
15-8-1947
'''









# Find outputs (Home  work)
class outer:
	def _init_(self):
		self.x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self.y = self.inner1() # How  to  create  inner1  class  object
		self.z = self.inner2() # How  to  create  inner2  class  object
	def disp(self):
		print(self . x)
	class  inner1:
		def disp(self):
			print('1st  inner  class  method')
	class inner2:
		def disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer() 
o.disp() # How  to  call   disp()  method  of outer  class
o.y.disp() # How  to  call   disp()  method  of inner1  class
o.z.disp() # How  to  call   disp()  method  of inner2  class
'''
Outputs
25
1st  inner  class  method
2nd  inner  class  method
'''









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
a = c1() # How  to  create  c1  class  object
b = a.c1() # How  to  create  inner  c2  class  object
c = c2 # How  to  create  outer  c2  class  object
'''
Outputs
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor
'''









# Find  outputs  (Home  work)
class c2:
	def _init_(self):
		print('outer  class  constructor')
	class c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
a = c2() # How  to  create  outer  c2  class  object
b = a.c2() # How  to  create  inner  c2  class  object
c = c2.c2() # How  to  create  inner  c2  class  object  in  another  way
'''
Outputs
outer  class  constructor
inner  class  constructor
inner  class  constructor
'''









# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1  # Error
b . y += 1
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) #10
print(a . __dict__) # {'y' : 20, 'x' : 11}
print(b . __dict__) # {'y' : 21}
print(c1 . __dict__) # {'x': 10, and all environment variables}

'''
object a ---> y = 20
object b ---> y = 21
Outputs
11
20
10
21
10
{'y' : 20, 'x' : 11}
{'y' : 21}
{'x': 10, and all environment variables}
'''









# Find  outputs (Home  work)
class c1:
	x = 10
	def m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) # 10
print(a . x) # 20
'''
static   variable   --->

object 'a' ---> x = 20
Outputs
10
20
'''









# Find  outputs  (Home  work)
class c1:
	x = 10
	def __init__(self):
		self . y = 20
	@classmethod
	def m1(cls):
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
#print(cls . x , cls . y) # Error
#print(self . x , self . y) # Error
'''
static   variable   --->

object  'a'   ---> x = 30  y = 40

object 'b' ---> x = 30  y = 40

Outputs
30
20
30
20
30 40
'''









#  Find  outputs
class c1:
	@staticmethod
	def m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) # 35
'''
Outputs
25
35
'''









#  Find  outputs
class c1:
	def m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1() # Type and address of c1 class object
a . m1(35) # Error
'''
Outputs
25
Type and address of c1 class object
'''









#  Find  outputs
class c1:
	@staticmethod
	def m1(self):
		print('static  method')
		print(self)
	def m1(self):
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) 
a = c1()
a . m1()
'''
Outputs
staticmethod
25
static / instance  method
Type and address of c1 class object
'''









# How  to  access  static  variable  in  different  ways  ?
class c1:
	x = 25
	def _init_(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(cls.x) # How  to  print  static  variable  'x'  in  another  way
		print(x) # Error, cannot access static variavle without any prefix
	def m1(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(c1().x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # Error, cannot access static variable using cls
	@classmethod
	def m2(cls):
		print(cls.x) # How  to  print  static  variable  'x'
		print(c1.x) # How  to  print  static  variable  'x'  in  another  way
		print(self . x) # Error, cannot access static variable using cls
	@staticmethod
	def m3():
		print(c1.x) # How  to  print  static  variable  'x'
		#print(cls . x)
		#print(self . x)
# End  of  the  class
print(c1.x) # How  to  print  static  variable  'x'
print(c1().x) # How  to  print  static  variable  'x'  in  another  way
#print(x)
#print(self . x) # Error
#print(cls . x) # Error
a = c1()
a.m1() # How  to  call  method  m1()
c1.m2() # How  to  call  method  m2()
c1.m3() # How  to  call  method  m3()
'''
Outputs
25
25
25
25
25
25
25
'''









# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class c1:
	a = 10 # How  to  add  static  variable  'a'  with  value  10
	def __init__(self):
		c1.b = 20 # How  to  add  static  variable  'b'  with  value  20
		self.c = 30 # How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25
	def m1(self):
		c1.d = 40 # How  to  add  static  variable  'd'  with  value  40
		self.e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def m2(cls):
		c1.f = 60 # How  to  add  static  variable  'f'  with  value  60
		cls.g = 70 #nHow  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25
	@staticmethod
	def m3():
		c1.h = 80 # How  to  add  static  variable  'h'  with  value  80
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
x.m1() # How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
y = x.c1()
y.m2() # How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
z = x.c1()
z.m3() # How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i = 90 # How  to  add  static  variable  'i'  with  value  90
x.j = 100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x.__dict__)
'''
Outputs
Begin
{'a':10, methods and functions of class c1}


Consructor
{'a':10, methods and functions of class c1}


Instance method m1
{'a' : 10, 'b' : 20, 'd' : 40}


class method m2
{'a' : 10, 'b' : 20, 'd' : 40, 'f' : 60, 'g' : 70, functions and methods of class c1}


static method m3
{'a' : 10, 'b' : 20, 'd' : 40, 'f' : 60, 'g' : 70, 'h'  : 80, functions and methods of class c1}


Outside the class
{'a' : 10, 'b' : 20, 'd' : 40, 'f' : 60, 'g' : 70, 'h' : 80}


Object 'x'
{'c' : 30, 'e' : 50, 'j' : 100}
'''









# Find  outputs  (Home  work)
class c1:
    a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'









#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class Test:
	@classmethod
	def get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def get2(self):
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def compute(self):
		Test . x += 1 
		self . y  += 1 
		self . z  += 1 
		self . x  += 1
	def disp(self):
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

Object  'a'  ---> y = 21, z = 31, x = 12

Object  'b'  --->y = 4, z = 51, x = 13

Object  'c'  ---> y = 61, z = 71, x = 14

Outputs:
Enter any number:10
Enter any number:20
Enter any number:30
Enter any number:40
Enter any number:50
Enter any number:60
Enter any number:70
13 21 31 12
13 41 51 13
13 61 71 14
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
		vector.n = int(input("Enter number of elements:")) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self. a = []
		for i in range(vector.n):
			inp = int(input("Enter any number:"))
			self.a.append(inp) # How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.a = []
		for i in range(vector.n):
			self.a.append(x.a[i] + y.a[i]) #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1() # How  to  call  get1()  method
x = vector()
y = vector()
z = vector()
print('1st object')
x.get2() # How  to  read  the  list  into  1st  object 'a'
print('2nd object')
y.get2() # How  to  read  the  list  into  2nd  object  'b'
z.add(x, y) # How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(z.a)  # How  to  print  the  list  of  3rd   object
'''
Outputs
Enter number of elements:4
1st object
Enter any number:10
Enter any number:20
Enter any number:15
Enter any number:18
2nd object
Enter any number:30
Enter any number:40
Enter any number:35
Enter any number:12
[40, 60, 50, 30]
'''









'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
a = {}
b = c1.__dict__
for i in b:
	if not i.startswith('__') and not i.endswith('__'):
		a[i] = b[i]
print(a)
#  End  of  the  class
'''
{'_module': 'main', 'firstlineno': 6, 'x': 1, 'y': 2, 'z': 3, 'static_attributes': (), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref': <attribute 'weakref' of 'c1' objects>, 'doc_': None}
static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}

Outputs
{'x' : 1, 'y' : 2, 'z' : 3}
'''









# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> local variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable









'''
Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   ---> 3 + 4 * 5 - 6 / (^27)
				                          ---> 3 + (*45) -6 / (^27)
                                          ---> 3 + (*45) - (/6^27)
										  ---> (+3*45) - (/6^27)
										  ---> -+3*45/6^27
2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                          --->  abc^^
    What  is  the  prefix  expression ?   ---> a ^(^bc)
				                          ---> ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  ---> (ab+)+c
				                          ---> ab+c+
    What  is  the  prefix  expression ?  ---> (+ab) + c
				                         ---> ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  ---> (-b + ((b2^) - 4 * a * c) ^ 0.5) / (2 * a)
				                          ---> (-b + ((b2^) - (4a*) * c) ^ 0.5) / (2 * a)
										  ---> (-b + ((b2^) -(4a*c*) ^ 0.5) / (2 * a)
										  ---> (-b + (b2^a*c*-) ^ 0.5) / (2 * a)
										  ---> (-b + (b2^a*c*-0.5^) / (2 * a)
										  ---> (-bb2^a*c*-0.5^+) / (2 * a)
										  ---> (-bb2^a*c*-0.5^+) / (2a*)
										  ---> -bb2^a*c*-0.5^+2a*/
    What  is  the  prefix  expression ?   ---> (-b + ((^b2) - 4 * a * c) ^ 0.5) / (2 * a)
				                          ---> (-b + ((^b2) - (*4a) * c) ^ 0.5) / (2 * a)
										  ---> (-b + ((^b2) - (**4ac)) ^ 0.5) / (2 * a)
										  ---> (-b + ((^b2) - (^**4ac0.5)) / (2 * a)
										  ---> (-b + (-^b2^**4ac0.5)) / (2 * a)
										  ---> (+-b-^b2^**4ac0.5) / (2 * a)
										  ---> (+-b-^b2^**4ac0.5) / (*2a)
										  ---> /+-b-^b2^**4ac0.5*2a

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  ---> ab< or bc> and cd<
				                          ---> ab< or (bc>cd<and)
										  ---> ab<bc>cd<andor
    What  is  the  prefix  expression ?   ---> <ab or <bc and <cd
				                          ---> <ab or (and<bc<cd)
										  ---> or<aband<bc<cd

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  ---> x^y/(5z*)+2
				                          ---> (xy^)/(5z*)+2
										  ---> (xy^5z*/)+2
										  ---> xy^5z*/2+
    What  is  the  prefix  expression ?   ---> x^y/(*5z)+2
				                          ---> (^xy)/(*5z)+2
										  ---> (/^xy*5z)+2
										  ---> +/^xy*5z2

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  ---> a+b*((cd^)-e)^(f+g*h)-i
				                          ---> +b*(cd^e-)^(f+g*h)-i
										  ---> +b*(cd^e-)^(f+(gh*))-i
										  ---> +b*(cd^e-)^(fgh*+)-i
										  ---> +b*(cd^e-fgh*+)-i
										  ---> (+bcd^e-fgh*+*)-i
										  ---> +bcd^e-fgh*+*i-
    What  is  the  prefix  expression ?   ---> a+b*((^cd)-e)^(f+g*h)-i
				                          ---> a+b*(-^cde)^(f+g*h)-i
										  ---> a+b*(-^cde)^(f+(*gh))-i
										  ---> a+b*(-^cde)^(+f*gh)-i
										  ---> a+b*(^-^cde+f*gh)-i
										  ---> a+(*b^-^cde+f*gh)-i
										  ---> (+a*b^-^cde+f*gh)-i
										  ---> -+a*b^-^cde+f*ghi

'''









Conversion  of  Infix  to  Postfix
---------------------------------------
Operator          Icp(Incoming  priority)   Isp(In  stack  priority)
---------------------------------------------------------------------------
     + ,  -			1					1   --->  icp = isp  due  to  left  to  right  conversion

     * ,  / ,  %		2					2  --->  icp = isp  due  to  left  to  right  conversion

     ^			        4				        3   --->  icp > isp  due  to  right  to  left  conversion

     (				4					0

     #				-					-1
---------------------------------------------------------------------------
Let  infix  expression  be  3 + 4 * 5 - (6 + 7 * 8) / 9 + 2 * 5

    Character       Stack         Postfix  expression
-----------------------------------------------------------
                              #                    ''
          3                  #                    '3'
          +                  #+                   '3'
          4                 #+                   '34'
          *                 #+*                 '34'
          5                 #+*                 '345'
          -                 #-                    '345*+'
          (                 #-(                   '345*+'
          6                #-(                   '345*+6'
          +                #-(+                  '345*+6'
          7                #-(+                  '345*+67'
          *                #-(+*                '345*+67'
          8                #-(+*                '345*+678'
          )                #-                      '345*+678*+'
          /                #-/                    '345*+678*+'
          9                #-/                    '345*+678*+9'
          +                #+                      '345*+678*+9/-'
          2                #+                      '345*+678*+9/-2'
          *                #+*                    '345*+678*+9/-2'
          5                #+*                    '345*+678*+9/-25'
          End            #                        '345*+678*+9/-25*+'
          --------------------------------------------------------------
	Postfix  expression :  345*+678*+9/-25*+


1) Which  object  has  infix  expression  ?   ---> A  str  object
    Which  object  has  postfix  expression ? ---> Another  str  object

2) Why  is  '#'  pushed  into  the  stack   ?  --->  In  view  of  1st  comparison

3) What  action  to  be  made  when  character  is  operand(i.e. '0'  to  '9' )  ?  --->
														Concatenate  the  operand  to  postfix  expression

4) What  action  to  be  made  when  character  is  operator ? --->
									Compare  icp   of   the  operator  with  isp  of  last  element  of  the  stack

5) What  action  to  be  made  when  icp(operator) > isp(last-element-of-the-stack) ?  --->  Push  the  operator  into  the  stack

6) What  action  to  be  made  when  icp(operator)  <=  isp(last-element-of-the-stack)  ?  --->
					Pop  the  operator  from  the  stack  and  concatenate  the  deleted  operator  to  postfix  expression

7) How  long  is  the  deletion  continued ?  ---> Until  icp > isp

8) What  action  to  be  made  when  icp > isp ?  ---> Push  the  operator  into  the  stack

9) What  action  to  be  made  when  character  is  ')' ?  --->  Pop  the  operator  from  the  stack  and
											         concatenate  the  deleted  operator  to  postfix  expression

10) How  long  is  the  deletion  continued ?  --->  Until  '('  becomes  last  element  of  stack

11) What  action  to  be  made  when  '('  is  the  last  element  of  stack ?  --->
										Pop  '('   also  but  do  not  concatenate  '('  to  postfix  expression
										as  postfix  expression  is  bracket  free  expression

12) What  action  to  be  made  when  end  of  infix  expression  is  reached  ?  --->
												Pop  the  operator  from  the  stack  and
												concatenate  the  deleted  operator  to  postfix  expression

13) How  long  is  the  deletion  continued ?  --->  Until  '#'  becomes  last  element  of  stack









'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
def  icp(operator):
	return  1  when  operator  is   +  (or)  -
	return  2  when  operator  is   * , /   (or)  %
	return  4  when  operator  is   (  (or)  ^
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	return  1  when  operator  is   +  (or)  -
	return  2  when  operator  is   * , /   (or)  %
	return  3  when  operator  is   ^
	return  0  when  operator  is   (
	return  -1  when  operator  is  #
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	How  to  create  stack  class  object
	How  to  push  '#'  into  the  stack
	How  to  initialize  a  postfix  object  with  an  empty  string
	How  to  iterate  infix  expression  with  for  loop:
		if  char  is  an  operand:
			How  to  concatenate  the  operand  to  postfix  expression
		elif  char  is  ')':
			How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
			How  to  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			if   icp(operator)  >  isp(last-element-of-stack):
					How  to  push  the  operator  into  the  stack
			else:
					How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  icp > isp
					How  to  push  the  operator  into  the  stack  when  icp > isp
	#  End  of  for  loop
	How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
	How  to   return  postfix  expression
#  End  of  the  function
How  to  read  infix  expression
How  to  convert  infix  expression  to  postfix expression
How  to  print  postfix  expression







Evaluation  of  Postfix  Expression
----------------------------------------
1) Infix  :  3 + 4 * 5 - 6 / 2
    Postfix :  3 + (45*) - 6 / 2
                 :  3 + (45*) - (62/)
                 :  (345*+) - (62/)
                 :  345*+62/-

2)  character   Stack
   -----------------------
            '3'             '3'
            '4'              3 , 4
            '5'              3 , 4 , 5
            '*'              3 ,  4 * 5 = 20
            '+'              3 + 20 = 23
            '6'              23 , 6
            '2'              23 , 6 , 2
            '/'              23 , 6 / 2 = 3
            '-'              23 - 3 = 20

3) Which  object  has  postfix  expression ? ---> A  str  object

4) What  action  to  be  made  when  character  is  operand(i.e. '0'  to  '9' )  ?  ---> Push  int(operand)  into  the  stack

5) What  action  to  be  made  when  character  is  operator ? --->  Pop  the  last  two  elements  of  the  stack ,
													 save  them  in  'y'  and  'x'  and
													 push  the  result  of  x  operator  y  into  the  stack

6) What  does  stack  finally  contain ?  ---> Result  of  the  postfix  expression

7) Postfix  expression  is  bracket  free  expression







'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
def  eval(a):
	How  to  create  a  stack  class  object
	How  to  iterate  postfix  expression  with  for  loop:
		if  the  char  is  an  operand:
				How  to  push  the  operand  into  the  stack
		else:
				How  to  remove  two  values  of  the  stack
				match  the  operator  of  postfix  expression:
					case   '+':  How to  push  addition  result  into  the  stack
					case   '-':  How to  push  subtraction  result  into  the  stack
					case   '*':  How to  push  product  result  into  the  stack
					case   '/':  How to  push  division  result  into  the  stack
					case   '^':  How to  push  power  result  into  the  stack
	#  End  of  for  loop
	return  result  of  expression
#  End  of  the  function
How  to  read  infix  expression
How  to  convert infix  to  postfix
How  to  evaluate  postfix  expression
