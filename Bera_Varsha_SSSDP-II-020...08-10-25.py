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
o = outer() #
o.m1() #How  to  call  m1()  method  of  outer  class
i1 = outer .inner()
i1.m1() #How  to  call  m1()  method  of  inner  class
o.inner().m1() #How  to  call  m1()  method  of  inner  class  in  another  way
i2 = outer().inner()
i2.m1() #How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner() # Error
'''Output:
Outer  class  constructor
Outer  class  method
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method
Outer  class  constructor
Inner  class  constructor
Inner  class  method'''
# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25 
		self.ename = 'Rama Rao'
		self.sal = 10000.0 #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.dob = self.date() #How  to  create  date  class  object
	def   disp(self):
		print('Employee Number : ', self.empno) 
		print('Employee Name : ', self.ename)
		print('Employee Salary : ', self.sal)#How  to  print  empno , ename , sal  of  object  self
		self.dob.disp() #How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd = 15
			self.mm = 8
			self.yy = 1947 #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(F'Date of birth: {self.dd}-{self.mm}-{self.yy}') #How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e= emp() #
e.disp() #How  to  call  disp()  method  of  emp  class
'''Output:
Employee Number :  25
Employee Name :  Rama Rao
Employee Salary :  10000.0
Date of birth: 15-8-1947'''
# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25 #How  to  initialize  variable  'x'  of  object  self  to  25
		self.y = self.inner1() #How  to  create  inner1  class  object
		self.z = self.inner2() #How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o=outer() #
o.disp() #How  to  call   disp()  method  of outer  class
o.y.disp() #How  to  call   disp()  method  of inner1  class
o.z.disp() #How  to  call   disp()  method  of inner2  class
'''Output:
25
1st  inner  class  method
2nd  inner  class  method'''

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
a = c1() #How  to  create  c1  class  object
b = c1.c2() #How  to  create  inner  c2  class  object
c = c2() #How  to  create  outer  c2  class  object
'''Output:
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor'''

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2() #How  to  create  outer  c2  class  object
b = a.c2() #How  to  create  inner  c2  class  object
c=c2.c2() #How  to  create  inner  c2  class  object  in  another  way
'''Output:
outer  class  constructor
inner  class  constructor
inner  class  constructor'''

# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a.x += 1 
b.y += 1 
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 10
print(a . __dict__) # {'y':20, 'x': 11, Environment variables}
print(b . __dict__) # {'y':21, Environment variables}
print(c1 . __dict__) # {'x':10, Environment variables}
'''
static   variable  ---> x=10
Object  'a'  ---> y=20 , x=11
Object  'b'  ---> y=20
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
static   variable   ---> x=10, 
object  'a'   ---> x=20
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
print(c1 . x , c1 . y) # 30 40
print(cls . x , cls . y) # Error cls cannot be outside 
print(self . x , self . y) # Error self cannot be outside of the class
'''
static   variable   ---> x=30, y=40
object  'a'   --->y=20
object  'b'   --->y=20
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
#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()
a . m1()
a . m1(35) # Error
'''Output:
25
35
25
type and address of c1'''

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
'''Output:
static / instance  method
25
static / instance  method
type and address of c1'''

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def  __init__(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(x) # Error
	def   m1(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # Error
	@classmethod
	def   m2(cls):
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x) # 
	@staticmethod
	def   m3():
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls . x) # Error
		print(self . x) # Error
# End  of  the  class
a=c1()
print(c1.x) #How  to  print  static  variable  'x'
print(a.x) #How  to  print  static  variable  'x'  in  another  way
print(x) # Error
print(self . x) # Error
print(cls . x) # Error
a.m1() #How  to  call  method  m1()
c1.m2() #How  to  call  method  m2()
c1.m3() #How  to  call  method  m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b #How  to  add  static  variable  'b'  with  value  20
		self.c = 30 #How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 # Error
	def   m1(self):
		c1.d = 40 #How  to  add  static  variable  'd'  with  value  40
		self.e = 50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60 #How  to  add  static  variable  'f'  with  value  60
		cls.g = 70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 # Error
	@staticmethod
	def   m3():
		c1.h = 80 #How  to  add  static  variable  'h'  with  value  80
		self . k = 25 # Error
		cls . k = 35 # Error
#End  of  the  class
print('Begin')
print(c1 . __dict__) # {'a': 10, Ev's}
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__) # {'a': 10, 'b': 20, Ev's}
print()
print()
x.m1() #How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
c1.m2() #How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
c1.m3() #How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i = 90 #How  to  add  static  variable  'i'  with  value  90
x.j = 100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)
'''Output:
Begin
{'a': 10}


Constructor
{'a': 10,'b': 20,Ev's}


Instance  method  m1
{'a': 10, 'b': 20, 'd': 40,Ev's}


class  method   m2
{'a': 10,'b': 20, 'd': 40, 'f': 60, 'g': 70,Ev's}


static   method   m3
{'a': 10, 'b': 20, 'd': 40, 'f': 60, 'g': 70, 'h': 80,Ev's}


Outside  the  class
{'a': 10,'b': 20, 'd': 40, 'f': 60, 'g': 70, 'h': 80, 'i': 90}


Object  'x'
{'c': 30, 'e': 50, 'j': 100}'''

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
'''Output:
Enter  any  number    :  10
Enter  any  number  :  20
Enter  any  number  :  30
Enter  any  number  :  40
Enter  any  number  :  50
Enter  any  number  :  60
Enter  any  number  :  70
13      21      31      12
13      41      51      13
13      61      71      14'''
'''
static   variable   ---> X=13
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
		vector.n = int(input('How many elements ? : '))#How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a = [] 
		for i in range(vector.n):
			inp = int(input('Enter any number: ')) 
			self.a.append(inp) #How  to  read  the  list  into  the  object
	def add(self, x , y):
		self.a = [] 
		for i in range(vector.n):
			self.a.append(x.a[i]+y.a[i]) #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1() #How  to  call  get1()  method
x=vector() 
y=vector() 
z=vector()
x.get2() #How  to  read  the  list  into  1st  object
y.get2() #How  to  read  the  list  into  2nd  object  'b'
z.add(x,y) #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print('Result: ',z.a) #How  to  print  the  list  of  3rd   object
'''Output:
How many elements ? : 4
Enter any number: 10
Enter any number: 20
Enter any number: 15
Enter any number: 18
Enter any number: 30
Enter any number: 40
Enter any number: 35
Enter any number: 12
Result:  [40, 60, 50, 30]'''
'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_
Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
a = {}
b=c1._dict_
for key in b:
	if not key.startswith('') and not key.endswith(''):
		a[key] = b=[key]
print('static variables of class c1 :',a) # static variables of class c1 : {'x': ['x'], 'y': ['y'], 'z': ['z']}

# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instace variable
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instace variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> local variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instace variable

'''Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   ---> 3 + 4 * 5 - 6 / (^27)
				                             ---> 3 + (*45) - 6 / (^27)
											 ---> 3 + (*45) - (/6^27)
											 ---> (+3*45) - (/6^27)
											 --> -+3*45/6^27
2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   ---> a^(^bc)
				                             ---> ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  ---> a+(bc+)
				                              ---> ab+c+
    What  is  the  prefix  expression ?  ---> a+(+bc)
				                             ---> +ab+c

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  ---> (-b + ((b2^) - (4a*) * c) ^ 0.5) / (2 * a)
				                              ---> (-b + ((b2^) - (4a*c*) ^ 0.5) / (2 * a)
											  ---> (-b + ((b2^4a*c*-) ^ 0.5) / (2 * a)
											  ---> (-bb2^4a*c*-0.5^+) / (2 * a)
											  ---> (-bb2^4a*c*-0.5^+) / (2a*)
											  ---> -bb2^4a*c*-0.5^+2a*/
    What  is  the  prefix  expression ?   ---> (-b + ((^b2) - (*4a) * c) ^ 0.5) / (2 * a)
				                             ---> (-b + ((^b2) - **4ac ^ 0.5) / (2 * a)
											 ---> / + - b ^ - ^ b 2 * 4 * a c 0.5 * 2 a
5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  ---> (ab<) or (bc>) and (cd<)
				                              ---> ab<bc>cd<andor
    What  is  the  prefix  expression ?   ---> (<ab) or (>bc) and (>cd) 
				                             ---> or < a b and > b c < c d
6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  ---> xy^ / ( 5z*) + 2
				                              ---> xy^5z*/ + 2
											  ---> xy^5z*/2+
    What  is  the  prefix  expression ?   ---> ^xy / ( *5z) + 2
				                             ---> +/^xy*5z2

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  ---> a + b * ((cd^) - e) ^ (f + (gh*)) - i
				                              ---> abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   ---> a + b * (c ^ d - e) ^ (f + g * h) - i
				                             ---> -+a*b^-^cde+f*ghi

Conversion  of  Infix  to  Postfix
---------------------------------------
Operator          Icp(Incoming  priority)   Isp(In  stack  priority)
---------------------------------------------------------------------------
     + ,  -			1					1   --->  icp = isp  due  to  left  to  right  conversion

     * ,  / ,  %	2					2  --->  icp = isp  due  to  left  to  right  conversion

     ^			    4				    3   --->  icp > isp  due  to  right  to  left  conversion

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

13) How  long  is  the  deletion  continued ?  --->  Until  '#'  becomes  last  element  of  stack
'''
#Write  a  program  to  convert  infix  to  postfix
#Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
from  stack   import  stack
def  icp(operator):
	if   operator   in  '+-':
			return  1  #  icp  of  '+'  and  '-'  is   1
	if   operator   in  '*/%':
			return  2  #  icp  of  '*' ,  '/'   and  '%'  is   2
	if   operator   in  '(^':
			return  4  #  icp  of  '('  and  '^'  is    4
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	match  operator:
		case   '+' | '-':
				return  1  #  isp  of  '+'  and  '-'  is   1
		case   '*' | '/' | '%':
				return  2  #  isp  of  '*' ,  '/'   and  '%'  is   2
		case   '^':
				return  3   #  isp  of   '^'   is   3
		case   '(':
				return  0  #  isp  of   '('   is   0
		case   '#':
				return  -1  #  isp  of   '#'   is   -1
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	s = stack()   #   Constructor  initializes  object  with  list  =  []
	s . push('#')   #  Pushes  '#'  into  the  stack
	postfix = ''  #   Empty  string
	for  ch  in  infix:  #  ch  is  each  chat   of  infix  expression
		if  ch . isalnum():  #  Is  ch  an  operand
			postfix +=  ch   #  Concatenates  the  operand  to  postfix  expression
		elif  ch == ')':
			while  s . peek()  !=  '(':  #  Repeat  until  '('  is  last  element  of  the  stack
					postfix  += s . pop()  #  Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  postfix  expression
			s . pop() #   Removes  '('  from  stack  and  is  ignored  (not  concatenated  to  postfix  expression)
		elif   icp(ch)  >  isp(s . peek()):
			s . push(ch)  #  Pushes  the  operator  into  the  stack  when  icp  of  the  operator  >  isp  of  last  element  of  the  stack
		else:
			while  icp(ch) <= isp(s . peek()):  #  Repeat  until  icp  of  the  operator  >  isp  of  last  element  of  the  stack
				postfix += s . pop()  #  Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  postfix  expression
			s . push(ch)  #  Pushes  the  operator  into  the  stack  as  soon  as   icp  >  isp
	#  End  of  for  loop
	while  s . peek() !=  '#':   #  Repeat  until  '#'  is  last  element  of  the  stack
			postfix += s . pop()  #  Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  postfix  expression
	return  postfix
#  End  of  the  function
if  _name_ ==  '_main_':
	infix = input('Enter  infix  expression  :  ')  #  Reads  infix  expression
	postfix = convert(infix)  #  Converts  infix  expression  to  postfix  expression
	print('Postfix  expression :  ' , postfix)
'''Output:
Enter  infix  expression  :  3+4*5-6/2^7
Postfix  expression :   345*+627^/-'''

'''
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

7) Postfix  expression  is  bracket  free  expression
'''
#Write  a  program  to  evaluate  postfix  expression
#Posifix  expression  --->    3 4 5 * + 6 2 / -
from infix_postfix import *
def  eval(postfix):
	s=stack() #How  to  create  a  stack  class  object
	for ch in postfix: #How  to  iterate  postfix  expression  with  for  loop
		if ch.isdigit(): # the  char  is  an  operand
			s.push(int(ch)) #How  to  push  the  operand  into  the  stack
		else:
			y=s.pop() 
			x=s.pop() #How  to  remove  two  values  of  the  stack
			match  ch: #the  operator  of  postfix  expression
				case   '+':  s.push(x + y) #How to  push  addition  result  into  the  stack
				case   '-':  s.push(x - y) #How to  push  subtraction  result  into  the  stack
				case   '*':  s.push(x * y) #How to  push  product  result  into  the  stack
				case   '/':  s.push(x // y) #How to  push  division  result  into  the  stack
				case   '^':  s.push(x ** y) #How to  push  power  result  into  the  stack
	#  End  of  for  loop
	return  s.pop() #result  of  expression
#  End  of  the  function
infix = input('Enter infix expression: ')#How  to  read  infix  expression
postfix = convert(infix) #How  to  convert infix  to  postfix
print('Result: ', eval(postfix)) #How  to  evaluate  postfix  expression
'''Output:
Enter infix expression: 345*+62/
Result:  23
'''