# Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

import  math
class  Rat:
	def  get(self):  #  Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self): #  Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    _str_(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  _add_(a , b):  #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . dr + a . dr * b . nr
		c . dr = a . dr * b . dr
		c . simplify()
		return c
	def  _sub_( a , b):   #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . dr - a . dr * b . nr
		c . dr = a . dr * b . dr
		c . simplify()
		return c
	def  _mul_( a , b):   #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . nr
		c . dr = a . dr * b . dr
		c . simplify()
		return c
	def  _truediv_( a , b):   #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . dr
		c . dr = a . dr * b . nr
		c . simplify()
		return c
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
print('Sum :  ' , a + b)
print('Difference :  ', a - b)
print('Product :  ' , a * b)
if b . nr != 0:
	print('Division  : ' , a / b)
else:
	print('Division is not permitted.')


# Is  10 + 20  a  recursion ? No

class   c1:
	def  _add_(a , b):
			print(10 + 20) # 30
a = c1()
b = c1()
print(a + b) # None


# Is  x + y  a  recursion  ? Yes (Home  work)

class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)   # RecursionError


# Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined complex  object

import  math
class  complex:
	def  get(self):
		self.x = float(input("Enter real part : ")) # How  to  read  real  and  imag
		self.y = float(input("Enter imag part : "))
	def    _str_(self):
		if self.i > 0:
			return f'{self.r} + {self.i}'
		else:
			return f'{self.r} - {self.i}'# How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  _add_(a ,  b):
		c = complex()
		c.r = a.x + b.x
		c.i = a.y + b.y # How  to  add  objects  a  and  b
		return c
	def  _sub_(a ,  b):
		c = complex()
		c.r = a.x - b.x
		c.i = a.y - b.y # How  to  subtract  objects  a  and  b
		return c
	def  _mul_(a ,  b):
		c = complex()
		c.r = a.x * b.x - a.y * b.y
		c.i = a.x * b.y + b.x * a.y # How  to  multiply  objects  a  and   b
		return c
	def  _truediv_(a ,  b):
		c = complex()
		den = b.x*2 + b.y*2  
		c.r = (a.x * b.x + a.y * b.y) / den
		c.i = (a.y * b.x - a.x * b.y) / den # How  to  divide  objects   a  and  b
		return c
# End  of  the  class
a = complex()
b = complex() # How  to  create  two  complex  class  objects
a.get() # How  to  read   inputs  into  1st  object
b.get() # How  to  read   inputs  into  2nd  object
print('Sum :  ' , a + b)
print('Difference :  ' , a - b)
print('Product :  ' ,  a * b)
print('Division  : ' , a / b)


# Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

import  math
class  Rat:
	def  get(self):
			self.x = int(input("Enter Numerator :")) 
			self.y =  int(input("Enter Denominator :")) # How  to  read  numerator  and  denominator  into  object
	def _gt_(self,b):
			return  (a.x * b.y) > (a.y * b.x) # true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def _lt_(self,b):
			return (a.x * b.y) < (a.y * b.x) # true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def _eq_(self,b):
			return (a.x * b.y) == (a.y * b.x) # true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def _ge_(self,b):
			return (a.x * b.y) >= (a.y * b.x) # true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def _le_(self,b):
			return (a.x * b.y) <= (a.y * b.x) # true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def _ne_(self,b):
			return (a.x * b.y) != (a.y * b.x) # true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat()
b = Rat() # How  to  create  two  Rat   class  objects  'a'  and  'b'
a.get() # How  to  read  1st  rational   number  into  object  'a'
b.get() # How  to  read  2nd  rational   number  into  object  'b'
if  a > b: # 1st  rational  is  >  2nd  rational  number
	print('>')
if  a < b: # 1st  rational  is  <  2nd  rational  number
	print('<')
if  a == b: # rational  numbers  are  same
	print('==')
if  a >= b: # 1st  rational  is  >=  2nd  rational  number
	print('>=')
if  a <= b: # 1st  rational  is  <=  2nd  rational  number
	print('<=')
if  a != b: # rational  numbers  are  different
	print('!=')


# Find  outputs  (Home work)

class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ge_(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b) # _ge_ method :   10 20 <nextline> False
print(a <= b) # _ge_ method :   20 10 <nextline> True


# Find  outputs  (Home  work)

class   c1:
        def   _init_(self , y):
                self . x = y
        def    _eq_(m , n):
                print('_eq_ method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  #  not (a == b) # _eq_ method  :  10 20 <nextline> True
print(a == b) # _eq_ method  :  10 20 <netxline> False


# Find  outputs  (Home  work)

class   c1:
	def   _init_(self , y):
		self . x = y
	def    _eq_(m , n):
		print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # _eq_ method  :   25 25 <nextline> None
print(a != b) # _eq_ method  :   25 25 <nextline> True
print(a . x !=  b . x) # False


# Find  outputs  (Home  work)

class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b) # _ne_ method  :   10 10 <nextline> False
print(a == b) # True


#  Is  10 > 20  a  recursion ? Yes

class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)
# RecursionError


# Find  outputs  (Home  work)

class  c1:
	def _init_(self , y):
		self . x = y
	def  _gt_(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x)
class  c2:
	def _init_(self , y):
		self . x = y
	def _gt_(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x)
#end of the class
a = c1(10)
b = c1(20)
a > b # c1  class  _gt_  method :  10 20
a < b # c1  class  _gt_  method :  20 10
m = c2(30)
n = c2(40)
a < m # c2  class  _gt_  method :  30 10
n < b # c1  class  _gt_  method :  20 40


# Overload  *  operator  to  multiply  two  different  class  objects

class c1:
    def _init_(self):
        self.empno = 25
        self.hr = 250

    def _mul_(self, other):
        print('_mul_ method of class c1')
        return self.hr * other.noh

class c2:
    def _init_(self):
        self.empno = 25
        self.noh = 8

    def _mul_(self, other):
        print('_mul_ method of class c2')
        return self.noh * other.hr

a = c1()
b = c2()

print(a * b)  # _mul_ method of class c1, returns 2000
print(b * a)  # _mul_ method of class c2, returns 2000


# Find  outputs  (Home  work)

class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # a + b :  _add_ method  of  class   c1
print('a + 7 : ' , a + 7) # a + 7 :  _add_ method  of  class   c1
#print(7 + a) # Error
print('7 + 8 : ' , 7 + 8) # 7 + 8 :  15
m = c2()
n = c2()
#print(m + n) # Error
#print('a + m : ' , a + m)
#print(m + a) # Error


# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined

class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):
		return p.x + q.x # sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) # Sum : 30
print('Join : ' , m + n) # Join : 1020