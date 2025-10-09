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
i1=o.inner()
i1.m1(o)# How  to  call  m1()  method  of  inner  class
i2 = outer.inner()
i2.m1() # How  to  call  m1()  method  of  inner  class  in  another  way
i3=outer().inner()
i3.m1 # How  to  call  m1()  method  of  inner  class  in  one  more  way
i=inner() # error

class   emp:
	def __init__(self):
		self. empno = 25
		self. ename = 'rama rao'
		self. sal = 10000.0 # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.d = self.date() # How  to  create  date  class  object
	def   disp(self):
		print(self.empno,self.ename,self.sal) # How  to  print  empno , ename , sal  of  object  self
		self.d.disp() # How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd = 15
			self.mm = 8 
			self.yy = 1947 # How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(self.dd,self.mm, self.yy) # How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e = emp()
e.disp() # How  to  call  disp()  method  of  emp class

class  outer:
	def  __init__(self):
		self.x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self.y = self.inner1() # How  to  create  inner1  class  object
		self.z = self.inner2() # How  to  create  inner2  class  object
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
o.y.disp(o) # How  to  call   disp()  method  of inner1  class
o.z.disp(o) # How  to  call   disp()  method  of inner2  class

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
i1= c1() # How  to  create  c1  class  object
i2 = i1.c2() # How  to  create  inner  c2  class  object
i3 = c2() # How  to  create  outer  c2  class  object

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
c = c2() #How  to  create  outer  c2  class  object
a = c.c2() #How  to  create  inner  c2  class  object
i = c2 .c2()  # How  to  create  inner  c2  class  object  in  another  way

class c1:
    x = 10  # static variable
    def __init__(self):
        self.y = 20  # instance variable
a = c1()
b = c1()
a.x += 1  # modifies a's instance namespace, does not affect class variable
b.y += 1  # modifies b's instance variable
print(a.x)  # 11  # a sees x from its instance after a.x +=1
print(a.y)  # 20  # a's y remains 20
print(b.x)  # 10  # b sees class variable x
print(b.y)  # 21  # b's y incremented
print(c1.x)  # 10  # class variable remains unchanged
print(a.__dict__)  # {'y': 20, 'x': 11}  # instance namespace of a
print(b.__dict__)  # {'y': 21}          # instance namespace of b
print(c1.__dict__) # contains class variables including 'x', methods, and ev’s

class c1:
    x = 10  # static variable
    def m1(self):
        self.x = 20  # creates instance variable x in object a
a = c1()
a.m1()
print(c1.x)  # 10  # class/static variable remains unchanged
print(a.x)   # 20  # instance variable x of object a

class c1:
    x = 10  # static variable
    def __init__(self):
        self.y = 20  # instance variable
    @classmethod
    def m1(cls):
        cls.x = 30  # modifies class variable x
        cls.y = 40  # creates/updates class variable y
# End of class
a = c1()
b = c1()
c1.m1()  # call class method
print(a.x)  # 30  # class variable x updated
print(a.y)  # 20  # instance variable y remains unchanged
print(b.x)  # 30  # class variable x updated
print(b.y)  # 20  # instance variable y remains unchanged
print(c1.x, c1.y)  # 30 40  # class variables updated
print(cls.x, cls.y)  # Error: cls is undefined outside classmethod
print(self.x, self.y)  # Error: self is undefined outside instance

class c1:
    @staticmethod
    def m1(self):
        print(self)  # just prints the argument passed
# End of the class
c1.m1(25)  # 25  # static method prints the argument directly
a = c1()
a.m1(35)   # 35  # static method prints the argument directly

class c1:
    def m1(self):
        print(self)  # prints the instance object when called properly
# End of the class
# c1.m1(25)  # Error: unbound method call requires instance of c1
a = c1()
a.m1()   # <__main__.c1 object at 0xXXXXXXXX>  # prints the instance object
# a.m1(35)  # Error: method takes 1 positional argument (self) but 2 were given

class   c1:
	x = 25
	def   __init__(self):
		print(self.x) # How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(x) # error name 'x' is not defined
	def   m1(self):
		print(self.x) # How  to  print  static  variable  'x'
		print(c1.x) # How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # error name 'cls' is not defined
	@classmethod
	def   m2(cls):
		print(cls.x) # How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x) # error name 'self' is not defined
	@staticmethod
	def   m3():
		print(c1.x) # How  to  print  static  variable  'x'
		print(cls . x) # error name 'cls' is not defined
		print(self . x) # error name 'self' is not defined
# End  of  the  class
a = c1()
print(a.x) # How  to  print  static  variable  'x'
print(c1.x) # How  to  print  static  variable  'x'  in  another  way
print(x) # error name 'x' is not defined
print(self . x) # error name 'self' is not defined
print(cls . x) # error name 'cls' is not defined
a.m1() # How  to  call  method  m1()
a.m2() # How  to  call  method  m2()
a.m3() # How  to  call  method  m3()

class   c1:
	x = 10 # How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b = 20 # How  to  add  static  variable  'b'  with  value  20
		self.c = 30 #How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 # error name 'cls' is not defined 
	def   m1(self):
		c1.d = 40 # How  to  add  static  variable  'd'  with  value  40
		self. e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60 # How  to  add  static  variable  'f'  with  value  60
		c1.g = 70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 # error name 'self' is not defined
	@staticmethod
	def   m3():
		c1.h = 80 #How  to  add  static  variable  'h'  with  value  80
		self . k = 25 # error name 'self' is not defined
		cls . k = 35 # error name 'cls' is not defined
#End  of  the  class
print('Begin')
print(c1 .__dict__)
print()
print()
x = c1()
print('Constructor')
print(c1 .__dict__)
print()
print()
x.m1() # How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
x.m2() # How  to  call  m2()  method
print('class  method   m2')
print(c1 .__dict__)
print()
print()
x.m3() # How  to  call  m3()  method
print('static   method   m3')
print(c1 .__dict__)
print()
print()
c1.i = 90 # How  to  add  static  variable  'i'  with  value  90
x.j = 100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 .__dict__)
print()
print()
print("Object  'x' ")
print(x .__dict__)

class  c1:
        a,b,c = range(1 , 4)
# End  of  the  class
c1 = c1()
print(c1.a) # How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'

q) Write  a  program  to  add  two  Vector  objects
Ans)  class vector:
    @staticmethod
    def get1():
        vector.n = int(input('Enter number of elements: '))  # static variable
    def get2(self):
        self.a = []
        for i in range(vector.n):
            val = int(input(f'Enter element {i+1}: '))
            self.a.append(val)
    def add(self, x, y):
    self.a = []
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])
# End of class
vector.get1()
x = vector()
y = vector()
z = vector() # Create objects
x.get2()
y.get2()# Read lists into objects x and y
z.add(x, y) # Add lists of x and y, store in z
print('Resultant vector list:', z.a)  # Print list of 3rd object z

q) Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_
Ans) class c1:
    x = 1
    y = 2
    z = 3
# End of class
for key in c1.__dict__:
    if not (key.startswith('__') and key.endswith('__')):
        print(key, '=', c1.__dict__[key])

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
# a.compute():
Test.x += 1 → 10 + 1 = 11
a.y += 1 → 20 + 1 = 21
a.z += 1 → 30 + 1 = 31
a.x += 1 → creates instance variable a.x = 1
# b.compute():
Test.x += 1 → 11 + 1 = 12
b.y += 1 → 40 + 1 = 41
b.z += 1 → 50 + 1 = 51
b.x += 1 → creates instance variable b.x = 1
# c.compute():
Test.x += 1 → 12 + 1 = 13
c.y += 1 → 60 + 1 = 61
c.z += 1 → 70 + 1 = 71
c.x += 1 → creates instance variable c.x = 1
a.disp() → prints:
Test.x = 13
a.y = 21
a.z = 31
a.x = 1
# Output: 13    21    31    1
b.disp() → prints:
Test.x = 13
b.y = 41
b.z = 51
b.x = 1
# Output: 13    41    51    1
c.disp() → prints:
Test.x = 13
c.y = 61
c.z = 71
c.x = 1
# Output: 13    61    71    1

DSA programming


1) Infix: 3 + 4 * 5 - 6 / 2 ^ 7
   Postfix: 345*+627^/-
   Prefix: -+3*45/^6 2 7
2) Infix: a ^ b ^ c
   Postfix: abc^^
   Prefix: ^a^bc
3) Infix: a + b + c
   Postfix: ab+c+
   Prefix: ++abc
4) Infix: (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
   Postfix: b- b2^4ac*-0.5^+2a*/
   Prefix: / + -b ^ - ^b 2 * 4 a c 0.5 * 2 a
5) Infix: a < b or b > c and c < d
   Postfix: ab< bc> cd< and or
   Prefix: or <ab and >bc <cd
6) Infix: x ^ y / (5 * z) + 2
   Postfix: xy^5z* / 2 +
   Prefix: + / ^xy * 5 z 2
7) Infix: a + b * (c ^ d - e) ^ (f + g * h) - i
   Postfix: acd^e- fgh*+^b*+i-
   Prefix: -+a* b ^ - ^ c d e + f * g h i

q) Write  a  program  to  convert  infix  to  postfix
Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
Ans) from prog1b import stack
def icp(operator):
    if operator in '+-':
        return 1
    elif operator in '*/%':
        return 2
    elif operator == '^' or operator == '(':
        return 4
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
def convert(infix):
    s = stack()            # Create stack object
    s.push('#')            # Push '#' as sentinel
    postfix = ''           # Initialize postfix string
    for ch in infix:
        if ch.isalnum():   # Operand
            postfix += ch
        elif ch == ')':
            while s.list[-1] != '(':
                postfix += s.pop()
            s.pop()        # Remove '(' but do not add to postfix
        else:               # Operator
            while icp(ch) <= isp(s.list[-1]):
                postfix += s.pop()
            s.push(ch)
    while s.list[-1] != '#':
        postfix += s.pop()
    return postfix
infix_expr = input("Enter infix expression: ") # Read infix expression
postfix_expr = convert(infix_expr) # Convert infix to postfix
print("Postfix expression:", postfix_expr) # Print postfix expression

q) Write  a  program  to  evaluate  postfix  expression
Posifix  expression  --->    3 4 5 * + 6 2 / -
Ans) from prog1b import stack
From prog 7b import convert
def eval_postfix(postfix):
    s = stack()  # Create stack object
    for ch in postfix:
        if ch.isdigit():        # Operand
            s.push(int(ch))
        else:                   # Operator
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
    return s.pop()  # Result of expression
infix = input(‘enter  the infi exp : ’)
postfix = convert(infix)
result = eval_postfix(postfix_expr)
print("Result of postfix expression:", result)
