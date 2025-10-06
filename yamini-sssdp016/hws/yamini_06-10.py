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
	def  __add__(a , b):  #  Modify  the  method
		c=Rat()
		c. nr = a . nr * b . dr + a . dr * b . nr
		c. dr = a . dr * b . dr
		c . simplify()
		return c
	def  __sub__( a , b):   #  Modify  the  method
		c=Rat()
		c. nr = a . nr * b . dr - a . dr * b . nr
		c. dr = a . dr * b . dr
		c. simplify()
		return c
	def  __mul__(  a , b):   #  Modify  the  method
		c=Rat()
		c. nr = a . nr * b . nr
		c. dr = a . dr * b . dr
		c . simplify()
		return c
	def  __truediv__( a , b):   #  Modify  the  method
		c=Rat()
		c . nr = a . nr * b . dr
		c. dr = a . dr * b . nr
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
d = Rat()
e = Rat()
f = Rat()
a . get()
b . get()
c = a + b
d = a - b
e = a * b
f = a / b
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f =a/b
	print('Division  : ' , f)
else:
	print('Division is not permitted.')


# Is  10 + 20  a  recursion ?   yes recursion but calls __add__ method of int class
class   c1:
	def  __add__(a , b):
			print(10 + 20)  # prints 30 and returns None
a = c1()    # empty c1 class object
b = c1()   # empty c1 class object
print(a + b)    # __add_ method is called and prints 30 and None is printed

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()    # creates  new local  object of c1 class
		y = c1()   # creates  new local  object of c1 class
		print(x + y)    # calls __add__ method of c1 class recursion
a = c1()    # empty c1 class object
b = c1()    # empty c1 class object
print(a + b) # calls __add__ method of c1 class


'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->      8 + 10i
   What  is  the  difference  ?  ---> -2 - 2i
   What  is  the  product  ?  --->  (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
	What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =  39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		self.real=int(input())  #
		self.imag=int(input())  #How  to  read  real  and  imag
	def    __str__(self):
		return (f'{self.real} + {self.imag}i')  #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		c=complex()
		c.real=a.real+b.real
		c.imag=a.imag+b.imag   
		return c #How  to  add  objects  a  and  b
	def  __sub__(a ,  b):
		c=complex()
		c.real=a.real-b.real
		c.imag=a.imag-b.imag   
		return c    #How  to  subtract  objects  a  and  b
	def  __mul__(a ,  b):
		c=complex()
		c.real=a.real*b.real-a.imag*b.imag
		c.imag=a.real*b.imag+a.imag*b.real  
		return c    #How  to  multiply  objects  a  and   b
	def  __truediv__(a ,  b):
		c = complex()
		den = b.real**2 + b.imag**2
		c.real = (a.real*b.real + a.imag*b.imag) / den
		c.imag = (a.imag*b.real - a.real*b.imag) / den
		return c

# End  of  the  class
a=complex()  
b=complex() #How  to  create  two  complex  class  objects
a.get() #How  to  read   inputs  into  1st  object
b.get() #How  to  read   inputs  into  2nd  object
print('Sum :  ' , a+b)
print('Difference :  ' ,a-b)
print('Product :  ' ,  a*b)
print('Division  : ' ,a/b)


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

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __gt__(a, b):
        return a.num * b.den > b.num * a.den

    def __lt__(a, b):
        return a.num * b.den < b.num * a.den

    def __eq__(a, b):
        return a.num * b.den == b.num * a.den

    def __ge__(a, b):
        return a.num * b.den >= b.num * a.den

    def __le__(a, b):
        return a.num * b.den <= b.num * a.den

    def __ne__(a, b):
        return a.num * b.den != b.num * a.den


# Driver code
a = Rat()
b = Rat()

print("Enter first rational number:")
a.get()
print("Enter second rational number:")
b.get()

print(f"a = {a}, b = {b}")
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a == b :", a == b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
print("a != b :", a != b)


# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):   # m and n are a and b
		print('_ge_ method :  ' , m . x , n . x)    # prints values of x
		return  m . x > n . x   # returns True if a.x > b.x false otherwise
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)   # Calls __ge__ method
print(a <= b)   # interprets as b >= a  and calls __ge__ method with b as m and a as n

'''
obj a==> x=10
obj b==> x=20


'''

# Find  outputs  (Home  work)
class   c1:
        def   __init__(self , y):
                self . x = y
        def    __eq__(m , n):
                print('_eq_ method  : ' , m . x , n . x)    #print values of x
                return  m . x == n . x  # return  True / False
#end of the class
a = c1(10)  
b = c1(20)
print(a != b)  #  not (a == b) calls a.__eq__(b)
print(a == b) # calls a.__eq__(b)


'''
obj a==> x=10
obj b==> x=20


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
print(a . x !=  b . x)
'''
obj a==> x=25
obj b==> x=25
a==b  => calls __eq__ method    
a!=b  =>not(a==b) => calls __eq__ method and here a==b is ref comp so false not(False)=>true
a.x != b.x => 25 != 25 => false

'''

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)  # Create  object with  value 10
b = a   #b points the same object as a
print(a != b)  #calls __ne__ method
print(a == b)   # reference comparison as both point to same object true

#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)  # prints  False
		print(a > b)    # calls  __gt__  method  again infinite  recursion
a = c1()    # creating  object  a  of  class  c1
b = c1()    # creating  object  b  of  class  c1
print(a > b)    # calls  __gt__  method

# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x) # p is a and q is b ,  p is b and q is a,  p is b and q is n
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x) # p is m and q is a 
#end of the class
a = c1(10)  # c1 class object with x=10
b = c1(20) # c1 class object with x=20
a > b   # calls c1 class __gt__ method as a is c1 class object
a < b   # interprets as b>a and calls c1 class __gt__ method
m = c2(30)  # c2 class object with x=30
n = c2(40)  # c2 class object with x=40
a < m   # as there is no lt method interprets as m>a and calls c2 class __gt__ method
n < b   # as there is no lt method interprets as b>n and calls c1 class __gt__ method

# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 25
	def __mul__(x , y):
		print('_mul_  method  of  class   c1')
		return  x.hr*y.noh #hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('_mul_  method  of  class   c2')
		return  x.noh*y.hr #number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()    # Create  object  of  class  c1 with  empno  25  and  hr  250
b = c2()    # Create  object  of  class  c2 with  empno  25  and  noh  8
print(a * b)    # Call  __mul__  method  of  class  c1 as 1st  operand  a is  of  class  c1
print(b * a)   # Call  __mul__  method  of  class  c2 as 1st  operand  b is  of  class  c2

# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()    # c1 class object
b = c1()    # c1 class object
print('a + b : ' , a + b)   # calls _add_ method of class c1 as 1st operand a is object of class c1
print('a + 7 : ' , a + 7)   # calls _add_ method of class  c1 as 1st operand a is object of class c1
print(7 + a) # calls __add__ method of int class as 1st operand 7 is int error as int class does not know how to add c1 object
print('7 + 8 : ' , 7 + 8)   # calls __add__ method of int class as 1st operand 7 is int 
m = c2()    # c2 class object
n = c2()    # c2 class object
print(m + n)    # calls _add_ method of class c2 as 1st operand m is object of class c2 but there is no __add__ in c2 so error
print('a + m : ' , a + m)   # calls _add_ method of class c1 as 1st operand a is object of class c1
print(m + a)    # calls _add_ method of class c2 as 1st operand m is object of class c2

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return p.x+q.x # sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)  # create c1 class object with value 10
b = c1(20)  # create c1 class object with value 20
m = c1('10')    # create c1 class object with value '10'
n = c1('20')    # create c1 class object with value '20'
print('Sum : ' , a + b) # calls __add__ of c1 class as a is c1 class object
print('Join : ' , m + n)   # calls __add__ of c1 class as m is c1 class object


