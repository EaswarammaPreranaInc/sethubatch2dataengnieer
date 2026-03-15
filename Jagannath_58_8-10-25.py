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
How  to  call  m1()  method  of  outer  class                                                  o=outer()
                                                                                               o.m1()
How  to  call  m1()  method  of  inner  class                                                  i=outer.inner()
                                                                                               i.m1()
How  to  call  m1()  method  of  inner  class  in  another  way                                o=outer()
                                                                                               i=o.inner()
                                                                                               i.m1()
How  to  call  m1()  method  of  inner  class  in  one  more  way                              outer.inner().m1()
i = inner()                                                                                    Error

# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0                         self.empno=25
                                                                                                                        self.ename='Rama Rao'
                                                                                                                        self.sal=10000.0
		How  to  create  date  class  object                                                                                self.d=self.date()
	def   disp(self):
		How  to  print  empno , ename , sal  of  object  self                                                               print('Emp No:',self.empno)
                                                                                                                        print('Emp Name:',self.ename)
                                                                                                                        print('Emp Salary:',self.sal)
		How  to  call  disp()  method  of  date  class                                                                      self.d.disp()
	class   date:
		def    __init__(self):
			How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947                                           self.dd=15
                                                                                                                        self.mm=8
                                                                                                                        self.yy=1947
		def disp(self):
			How  to  print  dd , mm , yy  of  object  self                                                                    print('Date of joining:{}/{}/{}'.format(self.dd,self.mm,self.yy))
# End  of  the  class
How  to  call  disp()  method  of  emp  class                                                                           e=emp()
                                                                                                                        e.disp()

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		How  to  initialize  variable  'x'  of  object  self  to  25                                               self.x=25
		How  to  create  inner1  class  object                                                                     self.i1=self.inner1()
		How  to  create  inner2  class  object                                                                     self.i2=self.inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
How  to  call   disp()  method  of outer  class                                                                 o=outer()
                                                                                                                o.disp()
How  to  call   disp()  method  of inner1  class                                                                o.i1.disp()
How  to  call   disp()  method  of inner2  class                                                                o.i2.disp()

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
How  to  create  c1  class  object                                                      o1=c1()
How  to  create  inner  c2  class  object                                               inner_obj=c1.c2()
How  to  create  outer  c2  class  object                                               outer_obj=c2()

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
How  to  create  outer  c2  class  object                                              o=c2()
How  to  create  inner  c2  class  object                                              i=c2.c2()
How  to  create  inner  c2  class  object  in  another  way                            o=c2()
                                                                                       i=o.c2()

# Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)                                       11
print(a . y)                                       20
print(b . x)                                       10
print(b . y)                                       21
print(c1 . x)                                      10
print(a . _dict_)                                  {'y':20,'x':11}
print(b . _dict_)                                  {'y':21}
print(c1 . _dict_)                                 {Environmental variables,'x':10}

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)                                      10
print(a . x)                                       20

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
print(a . x)                                        30
print(a . y)                                        40
print(b . x)                                        30
print(b . y)                                        40
print(c1 . x , c1 . y)                              30 40
print(cls . x , cls . y)                            Error
print(self . x , self . y)                          Error

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)                                        25
a = c1()
a . m1(35)                                         35

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)                                       25
                                                  <__main__.c1 object at 0x....>
a = c1()
a . m1()                                          Error
a . m1(35)

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
c1 . m1(25)                                          static/instance method
                                                     25
a = c1()
a . m1()                                             static/instance method
                                                     <__main__.c1 object at 0x...>

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		How  to  print  static  variable  'x'                                               print('From __init__ using self:',self.x)
		How  to  print  static  variable  'x'  in  another  way                             print('From __init__ using classname:',c1.x)
		print(x)
	def   m1(self):
		How  to  print  static  variable  'x'                                               print('From instance method using self:',self.x)
		How  to  print  static  variable  'x'  in  another  way                             print('From instance method using classname:',c1.x)
		print(cls . x)
	@classmethod
	def   m2(cls):
		How  to  print  static  variable  'x'                                              print('From class method using cls:',cls.x)
		How  to  print  static  variable  'x'  in  another  way                            print('From class method using classname:',c1.x)
		print(self . x)
	@staticmethod
	def   m3():
		How  to  print  static  variable  'x'                                             print('From static method using classname:',c1.x)
		print(cls . x)                                                                    cannot use cls or self unless here unless passed explicitly
		print(self . x)
# End  of  the  class
How  to  print  static  variable  'x'                                                 print('Outside class using classname:',c1.x)
How  to  print  static  variable  'x'  in  another  way                               a=c1()
                                                                                      print('Outside class using instance:',a.x)
print(x)
print(self . x)
print(cls . x)
How  to  call  method  m1()                                                           a=c1()
                                                                                      a.m1()
How  to  call  method  m2()                                                           c1.m2()
                                                                                      a.m2()
How  to  call  method  m3()                                                           c1.m3()
                                                                                      a.m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	How  to  add  static  variable  'a'  with  value  10                                                                    a=10
	def    __init__(self):
		How  to  add  static  variable  'b'  with  value  20                                                                  c1.b=20
		How  to  add  instance  variable  'c'  with  value  30                                                                self.c=30
		cls . k = 25
	def   m1(self):
		How  to  add  static  variable  'd'  with  value  40                                                                  c1.d=40
		How  to  add  instance  variable  'e'  with  value  50                                                                self.e=50
	@classmethod
	def   m2(cls):
		How  to  add  static  variable  'f'  with  value  60                                                                  cls.f=60
		How  to  add  static  variable  'g'  with  value  70  in  another  way                                                c1.g=70
		self . k = 25
	@staticmethod
	def   m3():
		How  to  add  static  variable  'h'  with  value  80                                                                  c1.h=80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Begin')                                                                                                            Begin
print(c1 . __dict__)                                                                                                      {'a':10,Environmental variables,address of function and method}
print()
print()
x = c1()
print('Constructor')                                                                                                      Constructor
print(c1 . __dict__)                                                                                                      {'a':10,'b':20,'k':25,Environmental variables,address of function and method}
                                                                                                                          {'c':30}
print()
print()
How  to  call  m1()  method                                                                                               x.m1()
print('Instance  method  m1')                                                                                             Instance method m1
print(c1 .__dict__)                                                                                                       {'a': 10, 'b': 20, 'k': 25, 'd': 40,Environmental variables,address of function and method}
                                                                                                                          {'c':30,'e':50}
print()
print()
How  to  call  m2()  method                                                                                               c1.m2()                                                                           
print('class  method   m2')                                                                                               class method m2
print(c1 . __dict__)                                                                                                      {'a': 10, 'b': 20, 'k': 25, 'd': 40, 'f': 60, 'g': 70,Environmental variables,Address of function and method}
print()
print()
How  to  call  m3()  method                                                                                               c1.m3()
print('static   method   m3')                                                                                             static method m3
print(c1 . __dict__)                                                                                                      {'a': 10, 'b': 20, 'k': 25, 'd': 40, 'f': 60, 'g': 70, 'h': 80,Environmental variables,Address of function and method}
print()
print()
How  to  add  static  variable  'i'  with  value  90                                                                      c1.i=90
How  to  add  instance  variable  'j'  with  value  100                                                                   x.j=100
print('Outside  the  class')                                                                                              Outside the class
print(c1 . __dict__)                                                                                                      {'a': 10, 'b': 20, 'k': 25, 'd': 40, 'f': 60, 'g': 70, 'h': 80, 'i': 90,Environmental variables,Address of function and method}
print()
print()
print("Object  'x' ")                                                                                                     Object 'x'
print(x . __dict__)                                                                                                       {'c':30,'e':50,'j':100}

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
How  to  print  variable  'a'                                                         print(c1.a)
How  to  print  variable  'b'                                                         print(c1.b)
How  to  print  variable  'c'                                                         print(c1.c)

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

13	21	31	12
13	41	51	13
13	61	71	14

Write  a  program  to  add  two  Vector  objects
class Vector:
    n = 0
    @staticmethod
    def get1():
        Vector.n = int(input("Enter number of elements in vector: "))
    def get2(self):
        self.a = []
        print(f"Enter {Vector.n} elements:")
        for i in range(Vector.n):
            self.a.append(int(input()))
    def add(self, x, y):
        self.a = []
        for i in range(Vector.n):
            self.a.append(x.a[i] + y.a[i])
Vector.get1()
x = Vector()
y = Vector()
z = Vector()  
x.get2()
y.get2()
z.add(x, y)
print("Sum of vectors:")
for i in range(Vector.n):
    print(z.a[i], end=' ')
print()

Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_
class c1:
    x = 1
    y = 2
    z = 3
for key, value in c1.__dict__.items():
    if not (key.startswith("__") and key.endswith("__")):
        print(f"{key} = {value}")

# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->class/static variable of c1
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable (created by m1)
		z = 30   #  What  is  variable   'z'  --->local variable inside m1
		c1 . m = 40   #  What  is  variable   'm'  --->class/static variable of c1
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->instance variable of object a (inside f1)
	c1 . q = 60   #  What  is  variable   'q'  --->class/static variable of c1 (inside f1)
	s = 70   #  What  is  variable   's'  --->local variable inside function f1
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable
c1 . l = 90   #  What  is  variable  'l'  --->class/static variable of c1
b = c1()
b . n = 100   #  What  is  variable  'n' --->instance variable of object b

Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->3 + (*45) - 6 / 2 ^ 7
				                                  --->3 + (*45) - 6 /(^27)
                                          --->3 + (*45) - (/6^27)
                                          --->(+3*45) - (/6^27)
                                          --->-+3*45/6^27
2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   --->^a^bc
				                             

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->ab+c+
				            
    What  is  the  prefix  expression ?  --->++abc
				                             

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->b- b2^4a*c*-0.5^+ 2a*/
				                              --->
    What  is  the  prefix  expression ?   --->/ + - b ^ - b2^ *4 a c 0.5 * 2 a
				                             --->

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->ab<bc>cd<&|
				                              --->
    What  is  the  prefix  expression ?   --->| <ab & >bc <cd
				                             --->

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->xy^5z*/2+
				                              --->
    What  is  the  prefix  expression ?   --->+ / ^xy *5z 2
				                             --->

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->a + b * ((cd^) - e) ^ (f + g * h) - i
				                                  --->a + b * ((cd^e-)) ^ (f + g * h) - i
                                          --->a + b * (cd^e-) ^ (f + (gh*)) - i
                                          --->a + b * (cd^e-) ^ (fgh*+) - i
                                          --->a + b * (cd^e-fgh*+^) - i
                                          --->a + (bcd^e-fgh*+^*) - i
                                          --->(abcd^e-fgh*+^*+) - i
                                          --->abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   --->- + a * b ^ - ^ c d e + f * g h i
				                             --->
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
How  to  print  postfix  expression

from prog1b import Stack  
def icp(operator):
    if operator in '+-':
        return 1
    elif operator in '*/%':
        return 2
    elif operator in '^(':
        return 4
    return 0
def isp(operator):
    if operator in '+-':
        return 1
    elif operator in '*/%':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
    return 0
def convert(infix):
    s = Stack()       
    s.push('#')        
    postfix = ''       
    for ch in infix:
        if ch.isalnum():       
            postfix += ch
        elif ch == ')':         
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()             
        else:                   
            while icp(ch) <= isp(s.peek()):
                postfix += s.pop()
            s.push(ch)
    while s.peek() != '#':
        postfix += s.pop()
    return postfix
infix_expr = input("Enter infix expression: ")
postfix_expr = convert(infix_expr)
print("Postfix expression:", postfix_expr)

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
How  to  evaluate  postfix  expression

from prog1b import Stack  
def eval_postfix(postfix):
    s = Stack()  
    for ch in postfix.split():  
        if ch.isdigit():        
            s.push(int(ch))
        else:                  
            b = s.pop()         
            a = s.pop()         
            if ch == '+':
                s.push(a + b)
            elif ch == '-':
                s.push(a - b)
            elif ch == '*':
                s.push(a * b)
            elif ch == '/':
                s.push(a / b)   
            elif ch == '^':
                s.push(a ** b)
    return s.pop() 
postfix_expr = input("Enter postfix expression (space-separated): ")
result = eval_postfix(postfix_expr)
print("Result of postfix expression:", result)
