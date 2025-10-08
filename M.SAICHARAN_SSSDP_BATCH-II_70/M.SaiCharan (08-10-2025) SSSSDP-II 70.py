                               NAME:M.SAICHARAN                 HOMEWORK                   
                               DATE:08-10-2025



1.# Find  outputs  (Home  work)
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
o=outer()#How  to  call  m1()  method  of  outer  class
o.m1()
i = outer.inner()#How  to  call  m1()  method  of  inner  class
i.m1()
o = outer()#How  to  call  m1()  method  of  inner  class  in  another  way
i = o.inner()
i.m1()
outer.inner().m1()#How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()#Error




2.# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
                self.empno = 25
                self.ename = 'Rama Rao'
                self.sal = 10000.0
		#How  to  create  date  class  object
                self.d = self.date()
	def   disp(self):
		#How  to  print  empno , ename , sal  of  object  self
		print('Emp No   :', self.empno)
		print('Emp Name :', self.ename)
		 print('Emp Sal  :', self.sal)
		#How  to  call  disp()  method  of  date  class
		 self.d.disp()
	class   date:
		def    __init__(self):
			#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
                        self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			#How  to  print  dd , mm , yy  of  object  self
			 print('Date of Joining :', self.dd, '/', self.mm, '/', self.yy)
# End  of  the  class
#How  to  call  disp()  method  of  emp  class
e = emp()
e.disp()



3.# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		  self.x = 25#How  to  initialize  variable  'x'  of  object  self  to  25
		 self.i1 = self.inner1()#How  to  create  inner1  class  object
		      self.i2 = self.inner2()#How  to  create  inner2  class  object
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
o.disp()#How  to  call   disp()  method  of outer  class
o.i1.disp()#How  to  call   disp()  method  of inner1  class
outer.inner1().disp()#How  to  call   disp()  method  of inner2  class




4.# Find  outputs  (Home  work)
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
a = c1()#How  to  create  c1  class  object
b = c1.c2()#How  to  create  inner  c2  class  object
c = c2()#How  to  create  outer  c2  class  object



5.# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2()#How  to  create  outer  c2  class  object
b = c2.c2()#How  to  create  inner  c2  class  object
outer_obj = c2()#How  to  create  inner  c2  class  object  in  another  way
inner_obj = outer_obj.c2()


6.# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
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
print(a . __dict__)#{'y': 20, 'x': 11}
print(b . __dict__)#{'y': 21}
print(c1 . __dict__)
{'__module__': '__main__', 'x': 10, '__init__': <function c1.__init__ at 0x...>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


'''
static   variable  --->

Object  'a'  --->

Object  'b'  --->


7.# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)#10
print(a . x)#20


'''
static   variable   --->

object  'a'   --->
'''


8.# Find  outputs  (Home  work)
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
print(a . x)#30
print(a . y)#20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#30 40
print(cls . x , cls . y)#Error
print(self . x , self . y)#Error


'''
static   variable   --->

object  'a'   --->

object  'b'   --->


9.#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)		#25
a = c1()
a . m1(35)		#35


10.#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)			#Error
a = c1()
a . m1()			#<__main__.c1 object at 0x...>
a . m1(35)			#Error

11.#  Find  outputs
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
#Output:
static / instance  method
25
static / instance  method
<__main__.c1 object at 0x...>


12.# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x)#How  to  print  static  variable  'x'
		print(c1.x)#How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
obj.c1()
print(obj.x)#How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
obj.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()


13.# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	How  to  add  static  variable  'a'  with  value  10
	# a = 10
	def    __init__(self):
		c1.b = 20#How  to  add  static  variable  'b'  with  value  20
		self.c =  30#How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25
	def   m1(self):
		c1.d = 40#How  to  add  static  variable  'd'  with  value  40
		self.e = 50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f = 60#How  to  add  static  variable  'f'  with  value  60
		c1.g = 70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25
	@staticmethod
	def   m3():
		c1.h = 80#How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Begin')
print(c1 . __dict__)#shows {'__module__', 'a': 10, ...}
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__)#shows {'__module__', 'a':10, 'b':20, 'k':25, '__init__', ...}
print()
print()
How  to  call  m1()  method#x.m1()
print('Instance  method  m1')
print(c1 .__dict__)#shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, ...}
print()
print()
How  to  call  m2()  method#c1.m2()
print('class  method   m2')
print(c1 . __dict__)# shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, ...}
print()
print()
How  to  call  m3()  method#c1.m3()
print('static   method   m3')
print(c1 . __dict__)# shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, ...}
print()
print()
c1.i = 90#How  to  add  static  variable  'i'  with  value  90
x.j = 100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')#print(c1.a)
print(c1 . __dict__)#shows {'__module__', 'a':10, 'b':20, 'k':25, 'd':40, 'f':60, 'g':70, 'h':80, 'i':90, ...}
print()
print()
print("Object  'x' ")
print(x . __dict__)#shows {'c':30, 'e':50, 'j':100}


14.# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)#How  to  print  variable  'a'
print(c1.b)#How  to  print  variable  'b'
print(c1.c)#How  to  print  variable  'c'



15.#  Tricky  program
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
#Output:
13	21	31	12
13	41	51	13
13	61	71	14
'''

16.Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  ---> vector . n
'''
class  vector:
	@staticmethod
	def get1():
		 vector.n = int(input("Enter number of elements : "))#How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		#How  to  read  the  list  into  the  object
                self.a = []
                print("Enter", vector.n, "elements : ")
                for i in range(vector.n):
                val = int(input())
                self.a.append(val)
	def add(self , x , y):
		#How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
                self.a = []
                for i in range(vector.n):
                self.a.append(x.a[i] + y.a[i])
vector.get1()#How  to  call  get1()  method
x = vector()#How  to  read  the  list  into  1st  object
x.get2()
y = vector()#How  to  read  the  list  into  2nd  object  'b'
y.get2()
z = vector()#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
z.add(x, y)
print("Resultant vector :", z.a)#How  to  print  the  list  of  3rd   object

'''
17.Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class

{'__module__': '__main__', '__firstlineno__': 6, 'x': 1, 'y': 2, 'z': 3, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}
static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}
#program:
class c1:
    x = 1
    y = 2
    z = 3
# End of the class
d = c1.__dict__
static_vars = {}
for key, value in d.items():
    if not (key.startswith('__') and key.endswith('__')):
        static_vars[key] = value
print("static variables of class c1 :", static_vars)



18.# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
k = 80  # What is variable 'k' ---> global variable
class c1:
    x = 10  # What is variable 'x' ---> class variable
    def m1(self):
        self.y = 20   # What is variable 'y' ---> instance variable
        z = 30        # What is variable 'z' ---> local variable
        c1.m = 40     # What is variable 'm' ---> class variable
        print("Inside m1():")
        print("z (local variable) =", z)
        print("self.y (instance variable) =", self.y)
        print("c1.m (class variable) =", c1.m)
# Adding class variable outside class
c1.l = 90  # What is variable 'l' ---> class variable
def f1():
    a = c1()
    a.p = 50       # What is variable 'p' ---> instance variable
    c1.q = 60      # What is variable 'q' ---> class variable
    s = 70         # What is variable 's' ---> local variable
    print("Inside f1():")
    print("a.p (instance variable) =", a.p)
    print("c1.q (class variable) =", c1.q)
    print("s (local variable) =", s)
    return a  # return object a to use outside

# Creating objects
b = c1()
b.n = 100  # What is variable 'n' ---> instance variable
# Call methods and function
obj_a = f1()
obj_b = b
obj_b.m1()
# Print global variable
print("k (global variable) =", k)
# Print class variables
print("c1.x =", c1.x)
print("c1.m =", c1.m)
print("c1.l =", c1.l)
print("c1.q =", c1.q)
# Print instance variables
print("obj_a.y =", getattr(obj_a, 'y', 'Not set'))
print("obj_a.p =", getattr(obj_a, 'p', 'Not set'))
print("obj_b.y =", getattr(obj_b, 'y', 'Not set'))
print("obj_b.n =", getattr(obj_b, 'n', 'Not set'))






                                                             #DATA STRUCTURE

1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				          --->  3 + (45*) - 6 / (27^)
				          --->  3 + (45*) - (627^/)
				          --->  (345*+) - (627^/)
				          --->  345*+627^/-
    What  is  the  prefix  expression ?   --->  3 + 4 * 5 - 6 / (^27)
				          --->  3 + (*45) - 6 / (^27)
					  --->  3 + (*45) - (/6^27)
					  --->  (+3*45) - (/6^27)
					  --->  -+3*45/6^27


2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				          --->  abc^^
    What  is  the  prefix  expression ?   ---> a ^ (^bc)
				          ---> ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  ---> (ab+) + c
				          ---> ab+c+
    What  is  the  prefix  expression ?  ---> (+ab) + c
				         ---> ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  ---> (-b + ((b2^) - 4 * a * c) ^ 0.5) / (2 * a)
				          ---> (-b + ((b2^) - (4ac**)) ^ 0.5) / (2 * a)
				          ---> (-b + (b2^4ac**-) ^ 0.5) / (2 * a)
				          ---> (-b + (b2^4ac**-0.5^)) / (2 * a)
				          ---> (-bb2^4ac**-0.5^+) / (2 * a)
				          ---> (-bb2^4ac**-0.5^+) / (2a*)
				          ---> -bb2^4ac**-0.5^+2a*/

    What  is  the  prefix  expression ?   ---> (-b + ((^b2) - 4 * a * c) ^ 0.5) / (2 * a)
				          ---> (-b + ((b2^) - (*4*ac)) ^ 0.5) / (2 * a)
				          ---> (-b + (-^b2*4*ac) ^ 0.5) / (2 * a)
				          ---> (-b + (^-^b2*4*ac0.5)) / (2 * a)
				          ---> (+-b^-^b2*4*ac0.5) / (2 * a)
				          ---> (+-b^-^b2*4*ac0.5) / (*2a)
				          ---> /+-b^-^b2*4*ac0.5*2a


5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->  a < b  or  b>cc<dand
                                          --->  a < b  or  bc>cd<and
				          --->  ab<bc>cd<andor
    What  is  the  prefix  expression ?   --->  a < b  or  and>bc<cd
				          --->  or<aband>bc<cd

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->  x ^ y / (5z*) + 2
				          --->  (xy^) / (5z*) + 2
				          --->  (xy^5z*/) + 2
				          --->  xy^5z*/2+

    What  is  the  prefix  expression ?   --->  x ^ y / (*5z) + 2
				          --->  (^xy) / (*5z) + 2
				          --->  /^xy*5z + 2
				          --->  +/^xy*5z2

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->  a + b * (cd^ - e) ^ (f + g * h) - i
				          --->  a + b * (cd^e-) ^ (f + g * h) - i
				          --->  a + b * (cd^e-) ^ (f + gh*) - i
				          --->  a + b * (cd^e-) ^ (fgh*+) - i
				          --->  a + b * (cd^e-fgh*+^) - i
				          --->  a + (bcd^e-fgh*+^*) - i
				          --->  (abcd^e-fgh*+^*+) - i
				          --->  abcd^e-fgh*+^*+i-

    What  is  the  prefix  expression ?   --->  a + b * (^cd - e) ^ (f + g * h) - i
				          --->  a + b * (-^cde) ^ (f + g * h) - i
				          --->  a + b * (-^cde) ^ (f + *gh) - i
				          --->  a + b * (-^cde) ^ (+f*gh) - i
				          --->  a + b * (^-^cde+f*gh) - i
				          --->  a + (*b^-^cde+f*gh) - i
				          --->  (+a*b^-^cde+f*gh) - i
				          --->  -+a*b^-^cde+f*ghi

2)'''
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

13) How  long  is  the  deletion  continued ?  --->  Until  '#'  becomes  last  element  of  stack


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
'''

#Program:
from prog1b import stack
def icp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/', '%'):
        return 2
    elif operator == '^':
        return 4
    elif operator == '(':
        return 4
    return -1
def isp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/', '%'):
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
    return -1
def convert(infix):
    s = stack()
    s.push('#')
    postfix = ""
    for char in infix:
        if char.isdigit():
            postfix += char 
        elif char == ')':  
            while s.peek() != '(': 
                postfix += s.pop()
            s.pop()
        else:
            while icp(char) <= isp(s.peek()):
                postfix += s.pop()
            s.push(char)
    while s.peek() != '#':
        postfix += s.pop()
    return postfix 
infix = input("Enter infix expression: ")
postfix = convert(infix)
print("Postfix Expression:", postfix)






3.#)'''
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
'''

#Program:
from prog1b import stack
def eval(a):
    s = stack()
    for char in a:
        if char.isdigit():
            s.push(int(char))
        else:
            y = s.pop()
            x = s.pop()
            match char:
                case '+':
                    s.push(x + y)
                case '-':
                    s.push(x - y)
                case '*':
                    s.push(x * y)
                case '/':
                    s.push(x / y)
                case '^':
                    s.push(x ** y)
    return s.pop()
a = input("Enter postfix expression: ")
result = eval(a)
print("Result of postfix expression:", result)