
''' 1) Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

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
4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
'''
import  math
class  Rat:
	def  get(self):         # Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self):        # Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    __str__(self):   #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  __add__(a , b):    #  Modify  the  method
		result = Rat()
		result . nr = a . nr * b. dr + a . dr * b . nr
		result . dr = a. dr * b . dr
		result . simplify()
		return result
	def  __sub__(a , b):    #  Modify  the  method
		result = Rat()
		result . nr = a . nr * b . dr - a . dr * b . nr
		result . dr = a.dr * b.dr
		result . simplify()
		return result
	def  __mul__(a , b):    #  Modify  the  method
		result = Rat()
		result . nr = a . nr * b. nr
		result . dr = a . dr * b . dr
		result . simplify()
		return result
	def  __truediv__(a , b): #  Modify  the  method
		result = Rat()
		result . nr = a . nr * b . dr
		result . dr = a . dr * b . nr
		result . simplify()
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
a = Rat()
b = Rat()
a . get()
b . get()

print('sum:', a+b)
print('diffrence:', a-b)
print('product:', a*b)
if b . nr != 0:
	print('Division  : ' , a/b)
else:
	print('Division is not permitted.')
	
	
    
    
    
    
# 2) Is  10 + 20  a  recursion ?

class   c1:
	def  __add__(a , b):
        print(10 + 20)  # since 10 and 20 are not c1 class objects, __add__() is not called again. hence recursion doesn't occurs
a = c1()
b = c1()
print(a + b) 
'''
outputs: 
30
None
'''






# 3) Is  x + y  a  recursion  ?  (Home  work)

class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)    # recursion error as we calling the __add__() of cl class method in it self
a = c1()
b = c1()
print(a + b)






''' 4) Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

First  rational  number  --->  3 + 4i
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

    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"
            
    def __add__(a, b):
        c=Complex()
        c.real = a.real + b.real
        c.imag = a.imag + b.imag
        return c

    def __sub__(a, b):
        c=Complex()
        c.real = a.real - b.real
        c.imag = a.imag - b.imag
        return c

    def __mul__(a, b):
        c=Complex()
        c.real = a.real * b.real - a.imag * b.imag
        c.imag = a.real * b.imag + a.imag * b.real
        return c

    def __truediv__(a, b):
        c=Complex()
        c.real = (a.real * b.real + a.imag * b.imag) / (b.real*b.real + b.imag*b.imag)
        c.imag = (a.imag * b.real - a.real * b.imag) / (b.real*b.real + b.imag*b.imag)
        return c
        
a = Complex()
b = Complex()
a.get()
b.get()

print("Sum        :", a + b)
print("Difference :", a - b)
print("Product    :", a * b)
print("Division   :", a / b)

'''
output:
Enter real part: 3
Enter imaginary part: 4
Enter real part: 5
Enter imaginary part: 6
Sum        : 8 + 10i
Difference : -2 - 2i
Product    : -9 + 38i
Division   : 0.639344262295082 + 0.03278688524590164i

'''





''' 5) Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

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
class Rat:
    def get(self):
        self.nr = int(input("Enter numerator :"))
        self.dr = int(input("Enter denominator:"))
    def __gt__(a, b):
        return a.nr * b.dr > b.nr * a.dr

    def __lt__(a, b):
        return a.nr * b.dr < b.nr * a.dr

    def __eq__(a, b):
        return a.nr * b.dr == b.nr * a.dr

    def __ge__(a, b):
        return a.nr * b.dr >= b.nr * a.dr

    def __le__(a, b):
        return a.nr * b.dr <= b.nr * a.dr

    def __ne__(a, b):
        return a.nr * b.dr != b.nr * a.dr

a = Rat()
b = Rat()

print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
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

'''
output:
Enter numerator : 2
Enter denominator: 3
Enter numerator : 5
Enter denominator: 9
>
>=
!=
'''






# 6) Find  outputs  (Home work)

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






# 7) Find  outputs  (Home  work)

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






# 8) Find  outputs  (Home  work)

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






# 9) Is  10 > 20  a  recursion ?

class  c1:
	def   __gt__(a , b):
		print(10 > 20)  # False
		print(a > b)    # recursion error
a = c1()
b = c1()
print(a > b)           






# 10) Find  outputs  (Home  work)

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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
'''
output:
c1 class __gt__ method : 10 20
c1 class __gt__ method : 20 10
c2 class __gt__ method : 30 10
c1 class __gt__ method : 20 40
'''





# 11) Overload  *  operator  to  multiply  two  different  class  objects

class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  a.hr * b.noh    # hourly-rate(i.e.  250) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  b.noh * a.hr    # number-of-hours (i.e.  8) *  hourly-rate(i.e.  250)
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
2000
'''





# 12) Find  outputs  (Home  work)

class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)   # __add__ method of class c1
print('a + 7 : ' , a + 7)   # __add__ method of class c1
print(7 + a)                # error as 2nd operand should be int only
print('7 + 8 : ' , 7 + 8)   # 15
m = c2()
n = c2()
print(m + n)                # error as there is no __add__ method in c2 class
print('a + m : ' , a + m)   # __add__ method of class c1
print(m + a)                # error as there is no __add__ method in c2 class






# 13) Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined

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
'''
output:
Sum : 30
Join : 1020
'''