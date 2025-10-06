'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  2 / 3
   Second  rational  number ---> 5 / 9
   What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
   What  is  the  difference  ?  --->  2 / 3 - 5 / 9 = (18 - 15) / 27 =  3 / 27 = 1 / 9
   What  is  the  product  ?  ---> 2 / 3 * 5 / 9 = 10 / 27 =  10 / 27
   What  is   the  division  ?  ---> 2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

2) First  rational  number  --->  2 / 3
   Second  rational  number ---> 0 / 9
   What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3
   What  is  the  product  ?  ---> 2 / 3 * 0 / 9 =  0 / 27 = 0 / 27  (simplification  is  not  required  becoz  numerator  is  0)
    What  is   the  division  ?  ---> 2 / 3 /  0 / 9 =  2 / 3 * 0 / 9  --->  Division  is  not  possible  becoz  b . nr  is  0

3) Modify  the  following  program  with  operator  overloding  methods

4) Leave  get() ,  test() , _str_()  and  simplify()  methods  unchanged
'''
import  math
class  Rat:
	def  get(self):  #  Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self): #  Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  __add__(x , y):  #  Modify  the  method
		r = Rat()
		r . nr = x . nr * y . dr + x . dr * y . nr
		r . dr = x . dr * y . dr
		r . simplify()
		return r
	def  __sub__(x , y):   #  Modify  the  method
		r = Rat()
		r . nr = x . nr * y . dr - x . dr * y . nr
		r . dr = x . dr * y . dr
		r . simplify()
		return r
	def  __mul__(x , y):   #  Modify  the  method
		r = Rat()
		r . nr = x . nr * y . nr
		r . dr = x . dr * y . dr
		r . simplify()
		return r
	def  __truediv__(x , y):   #  Modify  the  method
		r = Rat()
		r . nr = x . nr * y . dr
		r . dr = x . dr * y . nr
		r . simplify()
		return r
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
#  Modify  the  following  statements
a = Rat()
b = Rat()
a . get()
b . get()
print(f'Addition : {a + b}')
print(f'Substraction : {a - b}')
print('Product :  ' , a * b)
if b . nr != 0:
	print(f'Division : {a / b}')
else:
	print('Division by zero is not permited')



# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) # 30 <next line> None



# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) # Recursion error


'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->      8 + 10i
   What  is  the  difference  ?  ---> -2 - 2i
   What  is  the  product  ?  --->  (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
	What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =
																																									39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		self . real = float(input('Enter a Real number : ')) # How  to  read  real  and  imag
		self . imag = float(input('Enter a Imaginary number : '))
	def    __str__(self):
		 # How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
		if self . real > 0:
			return f'{self . real} + {self.imag}i'
		else:
			return f'{self . real} - {self.imag}i'
	def  __add__(a ,  b):
		# How  to  add  objects  a  and  b
		c = complex()
		c . real = a . real + b . real
		c . imag = a . imag + b . imag
		return c
	def  __sub__(a ,  b):
		# How  to  subtract  objects  a  and  b
		c = complex()
		c . real = a . real - b . real
		c . imag = a . imag - b . imag
		return c
	def  __mul__(a ,  b):
		# How  to  multiply  objects  a  and   b
		c = complex()
		c . real = a . real * b . real - a . imag * b . imag
		c . imag = a . real * b . imag + a . imag * b . real
		return c
	def  __truediv__(a ,  b):
		# How  to  divide  objects   a  and  b
		c = complex()
		c . real = (a . real * b . real + a . imag * b . imag) / (b . real ** 2 + b . imag ** 2)
		c . imag = (a . imag * b . real - a . real * b . imag) / (b . real ** 2 + b . imag ** 2)
		return  c
# End  of  the  class
# How  to  create  two  complex  class  objects
a = complex()
b = complex()
# How  to  read   inputs  into  1st  object
a . get()
# How  to  read   inputs  into  2nd  object
b . get()
print('Sum :  ' , a + b)
print('Difference :  ' , a - b)
print('Product : ' , a * b)
print('Division : ' , a / b)


'''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  --->False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  --->	False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  --->	True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  ---> 	False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  ---> True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  _gt_()  method ?  --->  a > b
     What  is  the  method  call  to  _lt_()  method ?  ---> a < b
     What  is  the  method  call  to  _eq_()  method ?  --->  a == b
     What  is  the  method  call  to  _ge_()  method ?  --->  a >= b
     What  is  the  method  call  to  _le_()  method ?  --->  a <= b
     What  is  the  method  call  to  _ne_()  method ?  ---> a != b
'''
import  math
class  Rat:
	def  get(self):
			 # How  to  read  numerator  and  denominator  into  object
		self . nr = float(input('Enter a numerator : '))
		self . dr = float(input('Enter a denominator : '))
	def __gt__(self,b):
		if self . nr * b . dr > self . dr * b . nr:
			return True # true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
		else:
			return False
	def __lt__(self,b):
			if self . nr * b . dr < self . dr * b . nr: 
				return True  # true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
			else:
				return False
	def __eq__(self,b):
			if self . nr * b . dr == self . dr * b . nr:
				return  True  # when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
			else:
				return False
	def __ge__(self,b):
			if self . nr * b . dr >= self . dr * b . nr:
				return True
			else:
				return False  # true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			if self . nr * b . dr <= self . dr * b . nr:
				return True
			else:
				return False  # true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			if self . nr * b . dr != self . dr * b . nr:
				return True
			else:
				return False  # true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
# How  to  create  two  Rat   class  objects  'a'  and  'b'
a = Rat()
b = Rat()
# How  to  read  1st  rational   number  into  object  'a'
a . get()
# How  to  read  2nd  rational   number  into  object  'b'
b . get()
if  a > b : # 1st  rational  is  >  2nd  rational  number
	print('>')
if  a < b : # 1st  rational  is  <  2nd  rational  number
	print('<')
if  a ==b : # rational  numbers  are  same
	print('==')
if  a >= b : # 1st  rational  is  >=  2nd  rational  number
	print('>=')
if  a <= b : # 1st  rational  is  <=  2nd  rational  number
	print('<=')
if  a != b : # rational  numbers  are  different
	print('!=')



# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)

'''
__ge__ method : 10 <space> 20
False
__ge__ method : 20 <space> 10
True
'''



# Find  outputs  (Home  work)
class   c1:
        def   __init__(self , y):
                self . x = y
        def    __eq__(m , n):
                print('_eq_ method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  #  not (a == b)
print(a == b)

'''
__eq__ method : 10 <space> 20
True
__eq__ method : 20 <space> 10
False
'''


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __eq__(m , n):
		print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)

'''
__eq__ method : 25 <space> 25
None
__eq__ method : 25 <space> 25
True
False
'''


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b) 
print(a == b)

'''
__ne__ method : 10 <space> 10
False
True
'''


#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b) # Recursion error


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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b

'''
c1  class  _gt_  method : 10 <space> 20
c1  class  _gt_  method : 20 <space> 10
c2  class  _gt_  method : 30 <space> 10
c1  class  _gt_  method : 20 <space> 40
'''


# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # a + b : _add_ method  of  class   c1
print('a + 7 : ' , a + 7) # a + 7 : '_add_ method  of  class   c1'
print(7 + a) # error as we cannot add class with integer
print('7 + 8 : ' , 7 + 8) # 7 + 8 : 15
m = c2()
n = c2()
print(m + n) # Error as there is no __add__ method in class c2
print('a + m : ' , a + m) # a + m : _add_ method  of  class   c1
print(m + a) # Error as there is no __add__ method in class c2 



# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  p . x + q . x # sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)  
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) # Sum : 30
print('Join : ' , m + n) # Join : 1020




# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('_mul_  method  of  class   c1')
		return  x . hr * y . noh # hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('_mul_  method  of  class   c2')
		return  x . noh * y . hr # number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)

'''
__mul__ method of class c1
200
__mul__ method of class c2
200
'''



      


