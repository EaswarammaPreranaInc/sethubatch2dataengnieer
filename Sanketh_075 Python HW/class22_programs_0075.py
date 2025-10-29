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
	def    _str_(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  add(self, a , b):  #  Modify  the  method
		self . nr = a . nr * b . dr + a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  sub(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr - a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  mul(self ,  a , b):   #  Modify  the  method
		self . nr = a . nr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  div(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr
		self . dr = a . dr * b . nr
		self . simplify()
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self.nr = self.nr // g
			self.dr = self.dr // g
# End  of  the  class
#  Modify  the  following  statements
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a . get()
b . get()
c . add(a , b)
d . sub(a , b)
e .  mul(a , b)
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f . div(a , b)
	print('Division  : ' , f)
else:
	print('Division is not permitted.')


# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)


 # Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
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
import math

class Complex:
    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

    def __str__(self):
        # Returns output like "3 + 4i" or "3 - 4i"
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __add__(a, b):
        result = Complex()
        result.real = a.real + b.real
        result.imag = a.imag + b.imag
        return result

    def __sub__(a, b):
        result = Complex()
        result.real = a.real - b.real
        result.imag = a.imag - b.imag
        return result

    def __mul__(a, b):
        result = Complex()
        result.real = a.real * b.real - a.imag * b.imag
        result.imag = a.real * b.imag + a.imag * b.real
        return result

    def __truediv__(a, b):
        result = Complex()
        denom = b.real ** 2 + b.imag ** 2
        result.real = (a.real * b.real + a.imag * b.imag) / denom
        result.imag = (a.imag * b.real - a.real * b.imag) / denom
        return result

# --- Main Program ---
print("Enter first complex number:")
c1 = Complex()
c1.get()

print("Enter second complex number:")
c2 = Complex()
c2.get()

print("\nSum :", c1 + c2)
print("Difference :", c1 - c2)
print("Product :", c1 * c2)
print("Division :", c1 / c2)

#Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects
'''
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


import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))

    def __gt__(self, b):
        return (self.num / self.den) > (b.num / b.den)

    def __lt__(self, b):
        return (self.num / self.den) < (b.num / b.den)

    def __eq__(self, b):
        return (self.num / self.den) == (b.num / b.den)

    def __ge__(self, b):
        return (self.num / self.den) >= (b.num / b.den)

    def __le__(self, b):
        return (self.num / self.den) <= (b.num / b.den)

    def __ne__(self, b):
        return (self.num / self.den) != (b.num / b.den)

# --- Main Program ---
a = Rat()
b = Rat()

print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

if a > b:
    print(">")
if a < b:
    print("<")
if a == b:
    print("==")
if a >= b:
    print(">=")
if a <= b:
    print("<=")
if a != b:
    print("!=")


# Find  outputs  (Home work)
class c1:
    def __init__(self, y):
        self.x = y

    def __ge__(m, n):
        print('__ge__ method :', m.x, n.x)
        return m.x > n.x

a = c1(10)
b = c1(20)

print(a >= b)
print(a <= b)

'''
__ge__ method : 10 20
False
__ge__ method : 20 10
True
'''

# Find  outputs  (Home  work)
class c1:
    def __init__(self , y):
        self.x = y

    def __eq__(m , n):
        print('__eq__ method :', m.x , n.x)
        return m.x == n.x

a = c1(10)
b = c1(20)

print(a != b)   # not (a == b)
print(a == b)
'''
Output:
__eq__ method : 10 20
True
__eq__ method : 10 20
False
'''



 # Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __eq__(m , n):
		print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)
'''
Output:
__eq__ method  :   25 25
False
__eq__ method  :   25 25
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
print(a == b)
'''
Output:
_ne_ method  :   10 10
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
print(a > b)
#Yes its a recurssion



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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
''''
c1 class __gt__ method : 10 20
c1 class __gt__ method : 20 10
c2 class __gt__ method : 30 10
c1 class __gt__ method : 20 40
'''


# Overload  *  operator  to  multiply  two  different  class  objects
class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 250   # hourly rate

    def __mul__(x, y):
        print('__mul__ method of class c1')
        # Check if 'y' has 'noh' (number of hours)
        if hasattr(y, 'noh'):
            return x.hr * y.noh
        else:
            return x.hr * y.hr

class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8   # number of hours

    def __mul__(x, y):
        print('__mul__ method of class c2')
        # Check if 'y' has 'hr' (hourly rate)
        if hasattr(y, 'hr'):
            return x.noh * y.hr
        else:
            return x.noh * y.noh
a = c1()
b = c2()
print(a * b)
print(b * a)



# Find  outputs  (Home  work)
class c1:
    def __add__(x, y):
        return '__add__ method  of  class   c1'

class c2:
    pass
# end of the class
a = c1()
b = c1()
print('a + b : ', a + b) # Output  a + b :  __add__ method  of  class   c1
print('a + 7 : ', a + 7) # Output a + 7 :  __add__ method  of  class   c1
print(7 + a) # a not defined
print('7 + 8 : ', 7 + 8) # Output  7 + 8 :  15
m = c2()
n = c2()
print(m + n)# c2.__add__ not defined
print('a + m : ', a + m) # Output → a + m :  __add__ method  of  class   c1
print(m + a)# c2.__add__ not defined




# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class c1:
    def __init__(self, y):                    
        self.x = y

    def __add__(p, q):                         
        if isinstance(p.x, (int, float)) and isinstance(q.x, (int, float)):
            return p.x + q.x                  
        elif isinstance(p.x, str) and isinstance(q.x, str):
            # if both are strings
            return p.x + q.x                   
        else:
            return "Incompatible types"       

# end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum :', a + b)   # Output Sum : 30
print('Join :', m + n)  # Output Join : 1020   

