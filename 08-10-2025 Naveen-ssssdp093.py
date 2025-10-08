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
o=outer()           #How  to  call  m1()  method  of  outer  class
o.m1()
i=outer.inner()     #How  to  call  m1()  method  of  inner  class
i.m1()
outer.inner().m1()  #How  to  call  m1()  method  of  inner  class  in  another  way
type(outer()).inner().m1()  #How  to  call  m1()  method  of  inner  class  in  one  more  way



# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		self.empno=25
		self.ename='Rama Rao'
		self.sal=10000.0                                    #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.d=self.date()                                  #How  to  create  date  class  object
	def   disp(self):
		print('emp no:',self.empno)
		print('emp name:',self.ename)
		print('emp salary',self.sal)                #How  to  print  empno , ename , sal  of  object  self
		self.d.disp()                               #How  to  call  disp()  method  of  date  class
	class   date:
		def    _init_(self):
			self.dd=15
			self.mm=8
			self.yy=1947                            #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print('date of joining',f'{self.dd}-{self.mm}-{self.yy}')       #How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e=emp()                 
e.disp()                #How  to  call  disp()  method  of  emp  class



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25           #How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1=self.inner1()       #How  to  create  inner1  class  object
		self.i2=self.inner2()       #How  to  create  inner2  class  object
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
o.disp()          #How  to  call   disp()  method  of outer  class
o.i1.disp()            #How  to  call   disp()  method  of inner1  class
o.i2.disp()        #How  to  call   disp()  method  of inner2  class




# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def _init_(self):
		print('outer  class  c2  constructor')
#end of the class
obj1=c1()           #How  to  create  c1  class  object
obj2=c1.c2()            #How  to  create  inner  c2  class  object
obj3=c2()           #How  to  create  outer  c2  class  object



# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
obj1=c1()           #How  to  create  outer  c2  class  object
obj2=c2.c2()            #How  to  create  inner  c2  class  object
obj3=getattr(c2,'c2')       #How  to  create  inner  c2  class  object  in  another  way


# Find  outputs (Home  work)
class c1:
    x = 10                      # static variable
    def __init__(self):
	    self . y = 20           # instance variable
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)                    # 11
print(a . y)                    # 20
print(b . x)                    # 10
print(b . y)                    # 21
print(c1 . x)                   # 10
print(a . _dict_)               # {'y':20,'x':11}
print(b . _dict_)               # {'y':21}
print(c1 . _dict_)              # {'x':10}



# Find  outputs (Home  work)
class  c1:
	x = 10                          # class variable
	def  m1(self):
		self . x = 20               # instance variabel
a = c1()
a . m1()
print(c1 . x)               # 10
print(a . x)                # 20



# Find  outputs  (Home  work)
class   c1:
	x = 10                  # class variable
	def  __init__(self):
		self . y = 20       # instance variable
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()
b = c1()
c1 . m1()
print(a . x)                    # 30
print(a . y)                    # 20
print(b . x)                    # 30
print(b . y)                    # 20
print(c1 . x , c1 . y)          # 30 40
#print(cls . x , cls . y)        # error
#print(self . x , self . y)      # error



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)             # 25
a = c1()    
a . m1(35)              # 35




#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)                 # 25
a = c1()
a . m1()
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
c1 . m1(25)                     # 25
a = c1()
a . m1()


# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print('from __init__:')     #How  to  print  static  variable  'x'
		print(c1.x)                 #How  to  print  static  variable  'x'  in  another  way
		print(self.x)
	def   m1(self):
		print('from instance method m1:')     #How  to  print  static  variable  'x'
		print(c1.x)                             #How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@classmethod
	def   m2(cls):
		print('from class method m2:')          #How  to  print  static  variable  'x'
		print(c1.x)                         #How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@staticmethod
	def   m3():
		print('from static method m3:')         #How  to  print  static  variable  'x'
		print(c1 . x)
# End  of  the  class
print(c1.x)                 #How  to  print  static  variable  'x'
obj=c1()                      
print(obj.x)                  #How  to  print  static  variable  'x'  in  another  way
obj = c1()    
obj.m1()      
c1.m1(obj)    
c1.m2()       
obj.m2()      
c1.m3()       
obj.m3()       



# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10        #How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		c1.b=20            #How  to  add  static  variable  'b'  with  value  20
		self.c=30               #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d=40             #How  to  add  static  variable  'd'  with  value  40
		self.e=50           #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60            #How  to  add  static  variable  'f'  with  value  60
		c1.g=70                 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h=80             #How  to  add  static  variable  'h'  with  value  80
		#self . k = 25
		#cls . k = 35
#End  of  the  class
print('Begin')
print(c1 . _dict_)
print()
print()
x = c1()
print('Constructor')
print(c1 . _dict_)
print()
print()
x.m1()          #How  to  call  m1()  method
print('Instance  method  m1')
print(c1 ._dict_)
print()
print()
c1.m2()          #How  to  call  m2()  method
print('class  method   m2')
print(c1 . _dict_)
print()
print()
c1.m3()         #How  to  call  m3()  method
print('static   method   m3')
print(c1 . _dict_)
print()
print()
c1.i=90         #How  to  add  static  variable  'i'  with  value  90
x.j=100         #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_)
print()
print()
print("Object  'x' ")
print(x . _dict_)



# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)     #How  to  print  variable  'a'
print(c1.b)     #How  to  print  variable  'b'
print(c1.c)     #How  to  print  variable  'c'


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
		vector.n=int(input('Enter number of elements:'))        #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a=[]               #How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.a=[]               #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
		for i in range(vector.n):
			self.a.append(x.a[i]+y.a[i])
vector.get1()               #How  to  call  get1()  method
a.vector()                  
a.get2()                #How  to  read  the  list  into  1st  object
b.vector()
b.get2()                #How  to  read  the  list  into  2nd  object  'b'
c=vector()          
c.add(a,b)              #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print('resultant vector:')      
print(c.a)                      #How  to  print  the  list  of  3rd   object



'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''

class C1:
    x = 1
    y = 2
    z = 3

# Print only static variables, not environment variables
for key, value in C1.__dict__.items():
    if not (key.startswith('__') and key.endswith('__')):
        print(key, "=", value)
		


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->                    static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->        instance variable
		z = 30   #  What  is  variable   'z'  --->              local variable
		c1 . m = 40   #  What  is  variable   'm'  --->         static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->              instance variable
	c1 . q = 60   #  What  is  variable   'q'  --->             static variable
	s = 70   #  What  is  variable   's'  --->                  local variable
#end of the function
k = 80   #  What  is  variable 'k'  --->                        global variable
c1 . l = 90   #  What  is  variable  'l'  --->                  static variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->                   instance variable


'''
Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->
				                             --->   -+3*45/6^27

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   --->
				                             --->   ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->
				                              --->  ab+c+
    What  is  the  prefix  expression ?  --->
				                             --->   ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->
				                              --->         b- b 2 ^ 4 a * c * - 0.5 ^ + 2 a * /
    What  is  the  prefix  expression ?   --->
				                             --->           / + - b ^ - ^ b 2 * * 4 a c 0.5 * 2 a

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->
				                              --->      a b < b c > c d < and or
    What  is  the  prefix  expression ?   --->
				                             --->       or < a b and > b c < c d

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->
				                              --->      x y ^ 5 z * / 2 +
    What  is  the  prefix  expression ?   --->
				                             --->       + / ^ x y * 5 z 2

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->
				                              --->      a b c d ^ e - f g h * + ^ * + i -
    What  is  the  prefix  expression ?   --->
				                             --->       - + a * b ^ - ^ c d e + f * g h i
'''


'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
def  icp(operator):
	if operator in '+-':
		return  1           #when  operator  is   +  (or)  -
	if operator in '*/%':
		return  2           #when  operator  is   * , /   (or)  %
	elif operator in '(^':
		return  4           #when  operator  is   (  (or)  ^
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	if operator in'+-':
		return  1           #when  operator  is   +  (or)  -
	elif operator in'*/%':
		return  2           #when  operator  is   * , /   (or)  %
	elif operator in '^':
		return  3           #when  operator  is   ^
	elif operator in '(':
		return  0           #when  operator  is   (
	elif operator is '#':
		return  -1          #when  operator  is  #
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	s=stack()       #How  to  create  stack  class  object
	s.push('#')     #How  to  push  '#'  into  the  stack
	postfix=''      #How  to  initialize  a  postfix  object  with  an  empty  string
	for char in infix:  #How  to  iterate  infix  expression  with  for  loop:
		if  char.isalnum():        
			postfix+=char   #How  to  concatenate  the  operand  to  postfix  expression
		elif  char  is  ')':
			while s.peek():
				postfix+=s.pop()      #How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
			s.pop()                 #How  to  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			if   icp(char)  >  isp(s.peek()):
					postfix += s.pop()     
					 #How  to  push  the  operator  into  the  stack
			else:
					return postfix  
					
	#  End  of  for  loop
	while s.peek() is not '#':
		postfix+=s.pop()    #How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
	return postfix          #How  to   return  postfix  expression
#  End  of  the  function
infix = input('enter infix expression:')    #How  to  read  infix  expression
postfix=convert(infix)                      #How  to  convert  infix  expression  to  postfix expression
print('postfix expression:',postfix)        #How  to  print  postfix  expression


'''
Write  a  program  to  evaluate  postfix  expression
Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
# from prog1b import stack

def eval_postfix(postfix):
    # How to create a stack class object
    s = stack()
    
    # How to iterate postfix expression with for loop
    for char in postfix:
        # if the char is an operand
        if char.isdigit():  # for simplicity, assuming single-digit operands
            # How to push the operand into the stack
            s.push(int(char))
        else:
            # How to remove two values of the stack
            val2 = s.pop()
            val1 = s.pop()
            
            # match the operator of postfix expression
            if char == '+':
                # How to push addition result into the stack
                s.push(val1 + val2)
            elif char == '-':
                # How to push subtraction result into the stack
                s.push(val1 - val2)
            elif char == '*':
                # How to push product result into the stack
                s.push(val1 * val2)
            elif char == '/':
                # How to push division result into the stack
                s.push(val1 / val2)
            elif char == '^':
                # How to push power result into the stack
                s.push(val1 ** val2)
    # End of for loop
    
    # return result of expression
    return s.pop()
# End of the function

# How to read infix expression
infix = input("Enter infix expression: ")

# How to convert infix to postfix
# Assume convert() is defined from your previous program
postfix = convert(infix)

print("Postfix expression:", postfix)

# How to evaluate postfix expression
result = eval_postfix(postfix)
print("Result of expression:", result)



