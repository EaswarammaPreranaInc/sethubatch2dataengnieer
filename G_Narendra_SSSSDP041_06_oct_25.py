'''Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

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
4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged'''

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
	def  __add__(self, other):  #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other. dr + self . dr * other . nr
		result . dr = self. dr * other . dr
		result . simplify()
		return result
	def  __sub__(self, other):   #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other . dr - self . dr * other . nr
		result . dr = self.dr * other.dr
		result . simplify()
		return result
	def  __mul__(self ,  other):   #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other. nr
		result . dr = self . dr * other . dr
		result . simplify()
		return result
	def  __truediv__(self, other):   #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other . dr
		result . dr = self . dr * other . nr
		result . simplify()
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

c = a + b
print('sum:',c)

d = a - b
print('diffrence:',d)

e = a * b
print('product:',e)

f = a / b
if f is not None:
	print('division:',f)
	
	
# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) 
'''
outputs: 
30
None'''

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
'''
output:
recursion error
'''



'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
Second  rational  number ---> 5 + 6i
What  is  the  sum  ?  --->      8 + 10i
What  is  the  difference  ?  ---> -2 - 2i
What  is  the  product  ?  --->  (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =
'''																																							39 / 61 + 2i / 61

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Method to read real and imaginary parts
    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

    # Display in the form a + bi or a - bi
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    # Addition: (a+bi) + (c+di) = (a+c) + (b+d)i
    def __add__(self, b):
        return Complex(self.real + b.real, self.imag + b.imag)

    # Subtraction: (a+bi) - (c+di) = (a-c) + (b-d)i
    def __sub__(self, b):
        return Complex(self.real - b.real, self.imag - b.imag)

    # Multiplication: (a+bi)*(c+di) = (ac - bd) + (ad + bc)i
    def __mul__(self, b):
        real_part = self.real * b.real - self.imag * b.imag
        imag_part = self.real * b.imag + self.imag * b.real
        return Complex(real_part, imag_part)

    # Division: (a+bi)/(c+di) = [(a+bi)*(c-di)] / (c^2 + d^2)
    def __truediv__(self, b):
        denominator = b.real**2 + b.imag**2
        real_part = (self.real * b.real + self.imag * b.imag) / denominator
        imag_part = (self.imag * b.real - self.real * b.imag) / denominator
        return Complex(real_part, imag_part)
# Create two Complex objects
a = Complex()
b = Complex()
# Read complex numbers into objects
print("Enter 1st complex number:")
a.get()
print("Enter 2nd complex number:")
b.get()
# Perform operations
print("Sum        :", a + b)
print("Difference :", a - b)
print("Product    :", a * b)
print("Division   :", a / b)


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

3) What  is  the  method  call  to  __gt__()  method ?  --->  a > b
What  is  the  method  call  to  __lt__()  method ?  ---> a < b
What  is  the  method  call  to  __eq__()  method ?  --->  a == b
What  is  the  method  call  to  __ge__()  method ?  --->  a >= b
What  is  the  method  call  to  __le__()  method ?  --->  a <= b
What  is  the  method  call  to  __ne__()  method ?  ---> a != b
'''
import  math
class  Rat:
	def  get(self,numerator =0, denominator =1):
			 self.num = numerator#How  to  read  numerator  and  denominator  into  object
             self.den = denominator
    def  get(self):
            self.num = int(input("Enter numerator :"))
            self.den = int(input("Enter denominator:"))
	def __gt__(self,b):
			return self.num * b.den > b.num * self.den#return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return self.num * b.den < b.num * self.den#return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return self.num * b.den == b.num * self.den#return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return self.num * b.den >= b.num * self.den#return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return self.num * b.den <= b.num * self.den#return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			return self.num * b.den != b.num * self.den#return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat()
b = Rat()
#Read rational numbers into objects
print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
b.get()
# Perform comparisons
if a > b:
    print('>')
if a < b:
    print('<')
if a == b:
    print('==')
if a >= b:
    print('>=')
if a <= b:
    print('<=')
if a != b:
    print('!=')


# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)
'''
output:
__ge__ method : 10 20
False
__ge__ method : 20 10
True
'''

# Find  outputs  (Home  work)
class   c1:
        def   __init__(self , y):
                self . x = y
        def    __eq__(m , n):
                print('__eq__ method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  
print(a == b)
'''
output:
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
output:
__eq__ method : 25 25
None
__eq__ method : 25 25
True
False
'''


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b)
print(a == b)
'''
output:
__ne__ method  :   10 10
False
True
'''


 Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)#False
		print(a > b)#recursion error
a = c1()
b = c1()
print(a > b)#recursion error

# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  __gt__  method : ' , p . x , q . x)
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  __gt__  method : ' , p . x , q . x)
#end of the class
a = c1(10)
b = c1(20)
a > b#'c1 class __gt__ method :',10 20
a < b# 'c1 class __gt__ method :',20 10
m = c2(30)
n = c2(40)
a < m#c2 class __gt__method : 30 10
n < b#c1 class __gt__ method : 20 40

# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)
'''
output:
__mul__ method of class c1
2000
__mul__ method of class c2
2000'''


# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)#__add__ method of class c1
print('a + 7 : ' , a + 7)#__add__ method of class c1
print(7 + a)#error
print('7 + 8 : ' , 7 + 8)#15
m = c2()
n = c2()
print(m + n)#error
print('a + m : ' , a + m)#__add__ method of class c1
print(m + a)#error


#Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):		
        return p . x + q . x
    def __str__(self):
        return str(self.x)

#end of the class       
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)    