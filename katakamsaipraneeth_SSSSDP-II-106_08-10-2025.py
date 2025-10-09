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
o.m1() # How  to  call  m1()  method  of  outer  class
i = o.inner() 
i.m1() # How  to  call  m1()  method  of  inner  class
o.inner().m1() # How  to  call  m1()  method  of  inner  class  in  another  way
outer.inner().m1() # How  to  call  m1()  method  of  inner  class  in  one  more  way
# i = inner()


#Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25 # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.ename = 'Rama Rao' 
		self.sal = 10000.0
		self.d = self.date() # How  to  create  date  class  object
	def   disp(self):
		print('empno:',self.empno) # How  to  print  empno , ename , sal  of  object  self
		print('ename:',self.ename)
		print('sal:',self.sal)
		self.d.disp() # How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd = 15 # How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.mm = 8
			self.yy = 1947
		def disp(self):
			print(F'Date : {self.dd}-{self.mm}-{self.yy}') # How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e = emp() 
e.disp() # How  to  call  disp()  method  of  emp  class



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1 = self.inner1() # How  to  create  inner1  class  object
		self.i2 = self.inner2() # How  to  create  inner2  class  object
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
o.disp() # How  to  call   disp()  method  of outer  class
o.inner1().disp() # How  to  call   disp()  method  of inner1  class
o.inner2().disp() # How  to  call   disp()  method  of inner2  class


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
c = c1() # How  to  create  c1  class  object
a = c.c2() #How  to  create  inner  c2  class  object
b = c2() # How  to  create  outer  c2  class  object


# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2() # How  to  create  outer  c2  class  object
a.c2() # How  to  create  inner  c2  class  object
c2.c2() # How  to  create  inner  c2  class  object  in  another  way


# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1() # y = 20
b = c1() # y = 20
a . x += 1 # y = 20 , x = 11
b . y += 1 # y = 21
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 10
print(a . __dict__) # {y : 20 , x : 11}
print(b . __dict__) # {y : 21}
print(c1 . __dict__) # {x : 10, ..environment veriables..}


'''
static   variable  - 10

Object  'a'  - y = 20 , x = 11

Object  'b'  - y = 21
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
static   variable   - x = 10

object  'a'   - x = 20
'''


# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def  m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()
b = c1()
c1 . m1() # x = 30  y = 40
print(a . x) # 30
print(a . y) # 20
print(b . x) # 30
print(b . y) # 20
print(c1 . x , c1 . y) # 30  40
#print(cls . x , cls . y) # error
#print(self . x , self . y) # error


'''
static   variable   - 10

object  'a'   - y = 20

object  'b'   - y = 20
'''


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
a . m1() # <__main__.c1 object at 0x7f8b8c2c0d60>
a . m1(35) # error


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
c1 . m1(25) # static  method  25
a = c1() 
a . m1() # static / instance  method  <__main__.c1 object at 0x7f8b8c2c0d60>


# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(self.x) # How  to  print  static  variable  'x'  in  another  way
		#print(x)
	def   m1(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(self.x) # How  to  print  static  variable  'x'  in  another  way
		#print(cls . x)
	@classmethod
	def   m2(cls):
		print(c1.x) # How  to  print  static  variable  'x'
		print(cls.x) # How  to  print  static  variable  'x'  in  another  way
		#print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)# How  to  print  static  variable  'x'
		#print(cls . x)
		#print(self . x)
# End  of  the  class
c = c1()
print(c1.x) # How  to  print  static  variable  'x'
print(c.x) # How  to  print  static  variable  'x'  in  another  way
#print(x)
#print(self . x)
#print(cls . x)
c.m1() # How  to  call  method  m1()
c.m2() # How  to  call  method  m2()
c.m3() # How  to  call  method  m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 # How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b = 20 # How  to  add  static  variable  'b'  with  value  20
		self.c = 30 # How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d = 40 # How  to  add  static  variable  'd'  with  value  40
		self.e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f = 60 # How  to  add  static  variable  'f'  with  value  60
		cls.g = 70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h = 80 # How  to  add  static  variable  'h'  with  value  80
		#self . k = 25
		#cls . k = 35
#End  of  the  class
print('Begin') # Begin
print(c1 . __dict__) # {a : 10}
print()
print()
x = c1()
print('Constructor') # Constructor
print(c1 . __dict__) # {# {a : 10, b : 20}
print()
print()
x.m1() # How  to  call  m1()  method
print('Instance  method  m1') # Instance method m1
print(c1 .__dict__) # {a : 10, b : 20, d : 40}
print()
print()
c1.m2() # How  to  call  m2()  method
print('class  method   m2') # class method m2
print(c1 . __dict__) # # {a : 10, b : 20, d : 40, f : 60}
print()
print()
c1.m3() # How  to  call  m3()  method
print('static   method   m3') # static method m3
print(c1 . __dict__) # # {a : 10, b : 20, d : 40, f : 60, h : 80}
print()
print()
c1.i = 90 # How  to  add  static  variable  'i'  with  value  90
c1.j = 100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__) # # {a : 10, b : 20, d : 40, f : 60, h : 80, i : 90, j : 100}
print()
print()
print("Object  'x' ")
print(x . __dict__) # {c : 30, e : 50}


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) # How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'



# Tricky  program
#What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
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
Test . get1() # x = 10
a = Test() 
b = Test()
c = Test()
a . get2() # y = 20, z = 30
b . get2() # y = 40, z = 50
c . get2() # y = 60, z = 70
a . compute() # x = 12 , y = 21 , z = 31
b . compute() # x = 13 , y = 41 , z = 51
c . compute() # x = 14 , y = 61 , z = 71
a . disp() # 13  21  31  12
b . disp() # 13  41  51  13
c . disp() # 13  61  71  14


'''
static   variable   - 14

Object  'a'  -  y = 21 , z = 31

Object  'b'  - y = 41 , z = 51

Object  'c'  - y = 61 , z = 71
'''


'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  - x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  -  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  - x . a[i]
    How  to  access  elements  of  2nd  list ?  - y . a[i]

4) How  to  access  static  variable  'n' ?  - vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector.n = int(input('Enter  number  of  elements  :  '))
	def get2(self):
		self.a = []
		for i in range(vector.n):
			self.a.append(input(f'Enter element {i+1} : '))
	def add(self , x , y):
		self.a = []
		for i in range(vector.n):
			self.a.append(x.a[i] + y.a[i])
g = vector()
g.get1()
g.get2()
g2 = vector()
g2.get1()
g2.get2()
g3 = vector()
g3.add(g, g2)
print(g3.a)


'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
print(c1 . __dict__)
print('static  variables  of  class  c1 :  ')
static_attributes = ()
for  key  in  c1 . __dict__:
	if  key .startswith('__')  and  key .endswith('__'):
		continue
	static_attributes += (key,)
print({key : c1 . __dict__[key]  for  key  in  static_attributes})

{'_module': 'main', 'firstlineno': 6, 'x': 1, 'y': 2, 'z': 3, 'static_attributes': (), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref': <attribute 'weakref' of 'c1' objects>, 'doc_': None}
static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}



# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  - Static  variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  - Instance  variable
		z = 30   #  What  is  variable   'z'  - Local  variable
		c1 . m = 40   #  What  is  variable   'm'  - Static  variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  - Instance  variable
	c1 . q = 60   #  What  is  variable   'q'  - Static  variable
	s = 70   #  What  is  variable   's'  - Local  variable
#end of the function
k = 80   #  What  is  variable 'k'  - global  variable
c1 . l = 90   #  What  is  variable  'l'  - Static  variable
b = c1()
b . n = 100   #  What  is  variable  'n' - Instance  variable



Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  -  3 + 4 * 5 - 6 / (27^)
				                              -  3 + (45*) - 6 / (27^)
				                              -  3 + (45*) - (627^/)
				                              -  (345*+) - (627^/)
				                              -  345*+627^/-
    What  is  the  prefix  expression ?   - 7 ^ 2 / 6 - 5 * 4 + 3
				                             - 72^/6-5*4+3
				                             - 72^6/5-4*3+
				                             - 72^6/5*4-3+
				                             - ^72/6-*54+3
				                             - +3-*54/6^72
				                             - -+3*45/^627

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  - a ^ (bc^)
				                              -  abc^^
    What  is  the  prefix  expression ?   - ^a^bc
				                             - ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  - a b + c +
				                              - ab+c+
    What  is  the  prefix  expression ?  - +a+b+c
				                             - +a+b+c

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  - -b + (b2^ 4ac** - 0.5^) / (2a*)
				                              - -b + (b2^ 4ac** - 0.5^) / (2a*)
    What  is  the  prefix  expression ?   - / + -b ^ b2 - * 4ac ^ 0.5 2a
				                             - / + -b ^ b2 - * 4ac ^ 0.5 2a

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  - a b < c d <
				                              - ab<c d<
    What  is  the  prefix  expression ?   - < a b > b c < c d
				                             -

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  - x y ^ 5 z * / 2 +
				                              - xy^5z*/2+
    What  is  the  prefix  expression ?   - +/xy^*5z2
				                             - +/xy^*5z2

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  - a b c d ^ e - f g h * + ^ * + i -
				                              - abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   - - + a b * ^ c d - + f * g h i
				                             - - + a b * ^ c d - + f * g h i



# Conversion  of  Infix  to  Postfix
# ---------------------------------------
# Operator          Icp(Incoming  priority)   Isp(In  stack  priority)
# ---------------------------------------------------------------------------
#      + ,  -			1					1   -  icp = isp  due  to  left  to  right  conversion

#      * ,  / ,  %		2					2  -  icp = isp  due  to  left  to  right  conversion

#      ^			        4				        3   -  icp > isp  due  to  right  to  left  conversion

#      (				4					0

#      #				-					-1
# ---------------------------------------------------------------------------
# Let  infix  expression  be  3 + 4 * 5 - (6 + 7 * 8) / 9 + 2 * 5

#     Character       Stack         Postfix  expression
# -----------------------------------------------------------
#                               #                    ''
#           3                  #                    '3'
#           +                  #+                   '3'
#           4                 #+                   '34'
#           *                 #+*                 '34'
#           5                 #+*                 '345'
#           -                 #-                    '345*+'
#           (                 #-(                   '345*+'
#           6                #-(                   '345*+6'
#           +                #-(+                  '345*+6'
#           7                #-(+                  '345*+67'
#           *                #-(+*                '345*+67'
#           8                #-(+*                '345*+678'
#           )                #-                      '345*+678*+'
#           /                #-/                    '345*+678*+'
#           9                #-/                    '345*+678*+9'
#           +                #+                      '345*+678*+9/-'
#           2                #+                      '345*+678*+9/-2'
#           *                #+*                    '345*+678*+9/-2'
#           5                #+*                    '345*+678*+9/-25'
#           End            #                        '345*+678*+9/-25*+'
#           --------------------------------------------------------------
# 	Postfix  expression :  345*+678*+9/-25*+


# 1) Which  object  has  infix  expression  ?   - A  str  object
#     Which  object  has  postfix  expression ? - Another  str  object

# 2) Why  is  '#'  pushed  into  the  stack   ?  -  In  view  of  1st  comparison

# 3) What  action  to  be  made  when  character  is  operand(i.e. '0'  to  '9' )  ?  -
# 														Concatenate  the  operand  to  postfix  expression

# 4) What  action  to  be  made  when  character  is  operator ? -
# 									Compare  icp   of   the  operator  with  isp  of  last  element  of  the  stack

# 5) What  action  to  be  made  when  icp(operator) > isp(last-element-of-the-stack) ?  -  Push  the  operator  into  the  stack

# 6) What  action  to  be  made  when  icp(operator)  <=  isp(last-element-of-the-stack)  ?  -
# 					Pop  the  operator  from  the  stack  and  concatenate  the  deleted  operator  to  postfix  expression

# 7) How  long  is  the  deletion  continued ?  - Until  icp > isp

# 8) What  action  to  be  made  when  icp > isp ?  - Push  the  operator  into  the  stack

# 9) What  action  to  be  made  when  character  is  ')' ?  -  Pop  the  operator  from  the  stack  and
# 											         concatenate  the  deleted  operator  to  postfix  expression

# 10) How  long  is  the  deletion  continued ?  -  Until  '('  becomes  last  element  of  stack

# 11) What  action  to  be  made  when  '('  is  the  last  element  of  stack ?  -
# 										Pop  '('   also  but  do  not  concatenate  '('  to  postfix  expression
# 										as  postfix  expression  is  bracket  free  expression

# 12) What  action  to  be  made  when  end  of  infix  expression  is  reached  ?  -
# 												Pop  the  operator  from  the  stack  and
# 												concatenate  the  deleted  operator  to  postfix  expression

# 13) How  long  is  the  deletion  continued ?  -  Until  '#'  becomes  last  element  of  stack


'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
def  icp(operator):
	if operator in  ('+' , '-'):
		return  1
	if operator in  ('*' , '/' , '%'):
		return  2
	if operator in  ('(' , '^'):
		return  4

'''
def  isp(operator):
	return  1  when  operator  is   +  (or)  -
	return  2  when  operator  is   * , /   (or)  %
	return  3  when  operator  is   ^
	return  0  when  operator  is   (
	return  -1  when  operator  is  #
'''
def  isp(operator):
	if operator in  ('+' , '-'):
		return  1
	if operator in  ('*' , '/' , '%'):
		return  2
	if operator in  ('^'):
		return  3
	if operator in  ('('):
		return  0
	if operator in  ('#'):
		return  -1

from prog1a import stack

def  convert(infix):
	stack = stack()
	stack.push('#')
	postfix = ''
	for char in infix:
		if  char.isalnum(): #char  is  an  operaand:
			postfix += char
		elif  char  is  ')':
			while stack.peek() != '(':
				postfix += stack.pop() 
			stack.pop() #  remove  '('  from  stack
			#How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
		else:
			if   icp(char)  >  isp(stack.peek()):
				stack.push(char)
			else:
				while icp(char) <= isp(stack.peek()):
					postfix += stack.pop()
				stack.push(char)
	#  End  of  for  loop
	#How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
	while stack.peek() != '#':
		postfix += stack.pop()
	#How  to   return  postfix  expression
	return postfix
#  End  of  the  function
a = input('Enter  infix  expression  :  ')
postfix = convert(a)
print("Postfix expression  :", postfix)




# Evaluation  of  Postfix  Expression
# ----------------------------------------
# 1) Infix  :  3 + 4 * 5 - 6 / 2
#     Postfix :  3 + (45*) - 6 / 2
#                  :  3 + (45*) - (62/)
#                  :  (345*+) - (62/)
#                  :  345*+62/-

# 2)  character   Stack
#    -----------------------
#             '3'             '3'
#             '4'              3 , 4
#             '5'              3 , 4 , 5
#             '*'              3 ,  4 * 5 = 20
#             '+'              3 + 20 = 23
#             '6'              23 , 6
#             '2'              23 , 6 , 2
#             '/'              23 , 6 / 2 = 3
#             '-'              23 - 3 = 20

# 3) Which  object  has  postfix  expression ? - A  str  object

# 4) What  action  to  be  made  when  character  is  operand(i.e. '0'  to  '9' )  ?  - Push  int(operand)  into  the  stack

# 5) What  action  to  be  made  when  character  is  operator ? -  Pop  the  last  two  elements  of  the  stack ,
# 													 save  them  in  'y'  and  'x'  and
# 													 push  the  result  of  x  operator  y  into  the  stack

# 6) What  does  stack  finally  contain ?  - Result  of  the  postfix  expression

# 7) Postfix  expression  is  bracket  free  expression



'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  -    3 4 5 * + 6 2 / -
'''
def  eval(a):
	stack = stack() 
	# How  to  create  a  stack  class  object
	for char in a: 
		if  char.isalnum(): # char is an operand
			stack.push(int(char)) 
		
	# How  to  iterate  postfix  expression  with  for  loop:
	for char in a:
		if char.isalnum():  # char is an operand
			stack.push(int(char))
		else:
			# How  to  remove  two  values  of  the  stack
			y = stack.pop()
			x = stack.pop()
			# match  the  operator  of  postfix  expression:
			if char == '+':
				stack.push(x + y)
			elif char == '-':
				stack.push(x - y)
			elif char == '*':
				stack.push(x * y)
			elif char == '/':
				stack.push(x / y)
			elif char == '^':
				stack.push(x ** y)
	#  End  of  for  loop
	return stack.pop()
#  End  of  the  function
a = input('Enter  postfix  expression  :  ')
result = eval(a)
print("Result  of  postfix  expression  :", result)

# How  to  read  infix  expression
# How  to  convert infix  to  postfix
# How  to  evaluate  postfix  expression