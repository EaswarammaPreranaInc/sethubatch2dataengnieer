 '''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  		# 2 / 3
   Second  rational  number ---> 		# 5 / 9
   What  is  the  sum  ?  ---> 			# 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
   What  is  the  difference  ?  --->  		# 2 / 3 - 5 / 9 = (18 - 15) / 27 =  3 / 27 = 1 / 9
   What  is  the  product  ?  ---> 		# 2 / 3 * 5 / 9 = 10 / 27 =  10 / 27
   What  is   the  division  ?  ---> 		# 2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

2) First  rational  number  --->  		# 2 / 3
   Second  rational  number ---> 		# 0 / 9
   What  is  the  sum  ?  --->  		# 2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  ---> 		# 2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3
   What  is  the  product  ?  ---> 		# 2 / 3 * 0 / 9 =  0 / 27 = 0 / 27  (simplification  is  not  required  becoz  numerator  is  0)
    What  is   the  division  ?  ---> 		# 2 / 3 /  0 / 9 =  2 / 3 * 0 / 9  --->  Division  is  not  possible  becoz  b . nr  is  0


3) Modify  the  following  program  with  operator  overloding  methods


4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
'''
import  math
class  Rat:
    def  get(self):  						#  Do  not  modify  the  method
        self . nr = int(input('Enter  numerator : '))
        self . dr = int(input('Enter  denominator : '))
        self . test()
    def  test(self): 						#  Do  not  modify  the  method
        while  self . dr == 0:
            self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
    def __str__(self):  					#  Do  not  modify  the  method
        return  F'{self . nr} / {self . dr}'
    def __add__(a , b):  					#  Modify  the  method
        self = Rat()
        self.nr = a.nr * b.dr + a.dr * b.nr
        self.dr = a.dr* b.dr
        self.simplify()
        return self
    def __sub__(a , b):   					#  Modify  the  method
        self = Rat()
        self . nr = a . nr * b . dr - a . dr * b . nr
        self . dr = a . dr * b . dr
        self . simplify()
        return self
    def __mul__(a , b):   					#  Modify  the  method
        self = Rat()
        self . nr = a . nr * b . nr
        self . dr = a . dr * b . dr
        self . simplify()
        return self
    def __truediv__(a , b):   					#  Modify  the  method
        self = Rat()
        self . nr = a . nr * b . dr
        self . dr = a . dr * b . nr
        self . simplify()
        return self
    def   simplify(self):   					#  Do  not  modify  the  method
        if self . nr != 0:
            g = math . gcd(self . nr, self . dr)
            self . nr = self . nr // g
            self . dr = self . dr // g
# End  of  the  class
#  Modify  the  following  statements
a = Rat()
b = Rat()
a.get()
b.get()
c = a+b
d = a-b
e = a*b
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f = a/b
	print('Division  : ' , f)
else:
	print('Division is not permitted.')




# Is  10 + 20  a  recursion ?
class   c1:
	def __add__(a , b):
		print(10 + 20) 						# since 10 and 20 are not c1 class objects, __add__ is not called again. so no recursion occurs
a = c1()
b = c1()
print(a + b)




# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)            		# since both x and y are c1 class objects, __add__ is called again and again infinitely
a = c1()
b = c1()
print(a + b)




'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  			# 3 + 4i
   Second  rational  number ---> 			# 5 + 6i
   What  is  the  sum  ?  --->      			# 8 + 10i
   What  is  the  difference  ?  ---> 			# -2 - 2i
   What  is  the  product  ?  --->  			# (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
	What  is   the  division  ?  --->  		# (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =39 / 61 + 2i / 61
'''
import  math
class  complex:
    def  get(self):
        self.r = int(input('Enter the real part '))	# How to read real and imag
        self.i = int(input('Enter the imagimary part '))
    def __str__(self):
        if self.i < 0:
            return f'{self.r} - {abs(self.i)}i'
        return f'{self.r} + {self.i}i'      		# How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
    def __add__(a, b):
        t = complex()       				# How  to  add  objects  a  and  b
        t.r = a.r + b.r
        t.i = a.i + b.i
        return t
    def __sub__(a, b):
        t = complex()       				# How  to  subtract  objects  a  and  b
        t.r = a.r - b.r
        t.i = a.i - b.i
        return t
    def __mul__(a, b):
        t = complex()       				# How  to  multiply  objects  a  and   b
        t.r = a.r * b.r - a.i*b.i
        t.i = a.r * b.i + a.i*b.r
        return t
    def __truediv__(a, b):
        t = complex()       				# How  to  divide  objects   a  and  b
        if b.r**2 + b.i**2 != 0:
            t.r = (a.r * b.r - a.i*b.i) / b.r**2 + b.i**2
            t.i = (a.r * b.i + a.i*b.r) / b.r**2 + b.i**2
            return t
        return 'Division not possible'
# End  of  the  class
#How  to  create  two  complex  class  objects
a = complex()
b = complex()
#How  to  read   inputs  into  1st  object
a.get()
#How  to  read   inputs  into  2nd  object
b.get()
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)




'''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  				# True  due  to 18 > 15
    What  is  the  result  of  a < b ?  --->				# False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  --->				# False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  --->				# True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  ---> 				# False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  ---> 				# True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  _gt_()  	method ?  --->  	# a > b
     What  is  the  method  call  to  _lt_()  	method ?  ---> 		# a < b
     What  is  the  method  call  to  _eq_()  	method ?  --->  	# a == b
     What  is  the  method  call  to  _ge_()  	method ?  --->  	# a >= b
     What  is  the  method  call  to  _le_()  	method ?  --->  	# a <= b
     What  is  the  method  call  to  _ne_()  	method ?  ---> 		# a != b
'''
import  math
class  Rat:
    def  get(self):
        self . nr = int(input('Enter  numerator : '))
        self . dr = int(input('Enter  denominator : '))
    def __gt__(self,b):
        return  self.nr*b.dr > self.dr*b.nr
    def __lt__(self,b):
        return  self.nr*b.dr < self.dr*b.nr
    def __eq__(self,b):
        return  self.nr*b.dr == self.dr*b.nr
    def __ge__(self,b):
        return  self.nr*b.dr >= self.dr*b.nr
    def __le__(self,b):
        return  self.nr*b.dr <= self.dr*b.nr
    def __ne__(self,b):
        return  self.nr*b.dr != self.dr*b.nr
#  End  of   the  class
a = Rat()       				# How  to  create  two  Rat   class  objects a  and b
b = Rat()
a.get()     					# How  to  read  1st  rational   number  into  object  a
b.get()     					# How  to  read  2nd  rational   number  into  object  b
if  a>b:
	print('>')
if  a<b:
	print('<')
if  a==b:
	print('==')
if  a>=b:
	print('>=')
if  a<=b:
	print('<=')
if  a!=b:
	print('!=')




# Find  outputs  (Home work)
class   c1:
	def  __init__(self , y):
		self . x = y
	def __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)               				# __ge__ method : 10 20 nxtline False
print(a <= b)              				# __ge__ method : 20 10 nxtline True




# Find  outputs  (Home  work)
class   c1:
    def  __init__(self , y):
        self . x = y
    def  __eq__(m , n):
        print('__eq__ method  : ' , m . x , n . x)
        return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)       					# __eq__ method  : 10 20 nxtline True
print(a == b)       					# __eq__ method  : 10 20 nxtline False




# Find  outputs  (Home  work)
class   c1:
    def __init__(self , y):
        self . x = y
    def __eq__(m , n):
        print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)                   		# __eq__ method : 25 25 nxtline None
print(a != b)                   		# __eq__ method : 25 25 nxtline True
print(a.x != b.x)               		# False




# Find  outputs  (Home  work)
class   c1:
    def  __init__(self , y):
        self . x = y
    def  __ne__(m , n):
        print('__ne__ method  :  ' , m . x , n . x)
        return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b)               			# __ne__ method  :  10 10<next_line>False
print(a == b)               			# True




# Find  outputs  (Home  work)
class  c1:
    def __init__(self , y):
        self . x = y
    def  __gt__(p , q):
        print('c1  class  _gt_  method : ' , p . x , q . x)
class  c2:
    def __init__(self , y):
        self . x = y
    def __gt__(p , q):
        print('c2  class  _gt_  method : ' , p . x , q . x)
#end of the class
a = c1(10)
b = c1(20)
a > b                           		# c1  class  _gt_  method : 10 20
a < b                           		# c1  class  _gt_  method : 20 10
m = c2(30)
n = c2(40)
a < m                           		# c2  class  _gt_  method : 30 10
n < b                           		# c1  class  _gt_  method : 20 40




# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
    def __init__(self):
        self . empno = 25
        self . hr = 250
    def __mul__(x , y):
        print('_mul_  method  of  class   c1')
        return  x.empno * y.noh         		# hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
    def __init__(self):
        self . empno = 25
        self . noh = 8
    def __mul__(x , y):
        print('_mul_  method  of  class   c2')
        return  x.noh * y.empno#number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)




# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
    def __init__(self , y):
        self . x = y
    def __add__(p , q):
        return  p.x + q.x				# sum  of  numbers  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)