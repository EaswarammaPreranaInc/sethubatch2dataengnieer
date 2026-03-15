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

4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
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
			self . nr = self . nr // g
			self . dr = self . dr // g
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

import math
class Rat:
    def get(self):  
        self.nr = int(input('Enter numerator : '))
        self.dr = int(input('Enter denominator : '))
        self.test()
    def test(self):  
        while self.dr == 0:
            self.dr = int(input('Denominator can not be zero, re-enter : '))
    def __str__(self):  
        return f'{self.nr} / {self.dr}'
    def __add__(self, other):   
        r = Rat()
        r.nr = self.nr * other.dr + self.dr * other.nr
        r.dr = self.dr * other.dr
        r.simplify()
        return r
    def __sub__(self, other):  
        r = Rat()
        r.nr = self.nr * other.dr - self.dr * other.nr
        r.dr = self.dr * other.dr
        r.simplify()
        return r
    def __mul__(self, other):   
        r = Rat()
        r.nr = self.nr * other.nr
        r.dr = self.dr * other.dr
        r.simplify()
        return r
    def __truediv__(self, other):   
        if other.nr == 0:
            raise ZeroDivisionError("Division by zero rational number is not permitted.")
        r = Rat()
        r.nr = self.nr * other.dr
        r.dr = self.dr * other.nr
        r.simplify()
        return r
    def simplify(self):  
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g
a = Rat()
b = Rat()
a.get()
b.get()
c = a + b
d = a - b
e = a * b
print("Sum : ", c)
print("Difference : ", d)
print("Product : ", e)
try:
    f = a / b
    print("Division : ", f)
except ZeroDivisionError as ex:
    print(ex)


# Is  10 + 20  a  recursion ?                   No
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)                                    30  None

# Is  x + y  a  recursion  ?  (Home  work)          yes
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)                                     recursion error

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
		How  to  read  real  and  imag                                                                  self.real = int(input("Enter real part : "))
                                                                                                    self.imag = int(input("Enter imaginary part : "))
	def    __str__(self):
		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i                      if self.imag >= 0:
                                                                                                        return f"{self.real} + {self.imag}i"
                                                                                                    else:
                                                                                                        return f"{self.real} - {-self.imag}i"
	def  __add__(a ,  b):
		How  to  add  objects  a  and  b                                                               r = Complex()
                                                                                                   r.real = self.real + other.real
                                                                                                   r.imag = self.imag + other.imag
                                                                                                   return r
	def  __sub__(a ,  b):
		How  to  subtract  objects  a  and  b                                                         r = Complex()
                                                                                                  r.real = self.real - other.real
                                                                                                  r.imag = self.imag - other.imag
                                                                                                  return r

	def  __mul__(a ,  b):
		How  to  multiply  objects  a  and   b                                                       r = Complex()
                                                                                                 r.real = self.real * other.real - self.imag * other.imag
                                                                                                 r.imag = self.real * other.imag + self.imag * other.real
                                                                                                 return r
	def  __div__(a ,  b):
		How  to  divide  objects   a  and  b                                                         r = Complex()
                                                                                                 denom = other.real ** 2 + other.imag ** 2
                                                                                                 if denom == 0:
                                                                                                     raise ZeroDivisionError("Division by zero complex number is not allowed")
                                                                                                 r.real = (self.real * other.real + self.imag * other.imag) / denom
                                                                                                 r.imag = (self.imag * other.real - self.real * other.imag) / denom
                                                                                                 return r
# End  of  the  class
How  to  create  two  complex  class  objects                                                    a = Complex()
                                                                                                 b = Complex()
How  to  read   inputs  into  1st  object                                                        print("Enter first complex number:")
                                                                                                 a.get()
How  to  read   inputs  into  2nd  object                                                        print("Enter second complex number:")
                                                                                                 b.get()
print('Sum :  ' , ???)                                                                           print("Sum: ", a + b)
print('Difference :  ' , ???)                                                                    print("Difference: ", a - b)
print('Product :  ' ,  ??)                                                                       print("Product: ", a * b)
print('Division  : ' , ???)                                                                      print("Division: ", a / b)

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
	def  get(self):
			 How  to  read  numerator  and  denominator  into  object
	def __gt__(self,b):
			return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
How  to  create  two  Rat   class  objects  'a'  and  'b'
How  to  read  1st  rational   number  into  object  'a'
How  to  read  2nd  rational   number  into  object  'b'
if  1st  rational  is  >  2nd  rational  number
	print('>')
if  1st  rational  is  <  2nd  rational  number
	print('<')
if  rational  numbers  are  same
	print('==')
if  1st  rational  is  >=  2nd  rational  number
	print('>=')
if  1st  rational  is  <=  2nd  rational  number
	print('<=')
if  rational  numbers  are  different
	print('!=')

import math
class Rat:
    def get(self):   
        self.nr = int(input("Enter numerator : "))
        self.dr = int(input("Enter denominator : "))
        while self.dr == 0:  
            self.dr = int(input("Denominator cannot be zero, re-enter : "))
    def __gt__(self, b):
        return self.nr * b.dr > self.dr * b.nr
    def __lt__(self, b):
        return self.nr * b.dr < self.dr * b.nr
    def __eq__(self, b):
        return self.nr * b.dr == self.dr * b.nr
    def __ge__(self, b):
        return self.nr * b.dr >= self.dr * b.nr
    def __le__(self, b):
        return self.nr * b.dr <= self.dr * b.nr
    def __ne__(self, b):
        return self.nr * b.dr != self.dr * b.nr
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
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)                                               __ge__ method :  10 20
                                                            False
print(a <= b)                                               __ge__ method :  20 10
                                                            True

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
print(a != b)  #  not (a == b)                                         __eq__ method  :  10 20
                                                                       True
print(a == b)                                                          __eq__ method  :  10 20
                                                                       False

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _eq_(m , n):
		print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)                                                   False
print(a != b)                                                   True
print(a . x !=  b . x)                                          Error

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
print(a != b)                                          False
print(a == b)                                          True

#  Is  10 > 20  a  recursion ?                           No
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)

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
a > b                                                                c1  class  __gt__  method :  10 20
a < b                                                                c1  class  __gt__  method :  20 10
m = c2(30)
n = c2(40)
a < m                                                                c2  class  __gt__  method :  30 10
n < b                                                                c1  class  __gt__  method :  20 40

# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  _init_(self):
		self . empno = 25
		self . hr = 250
	def _mul_(x , y):
		print('_mul_  method  of  class   c1')
		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def _init_(self):
		self . empno = 25
		self . noh = 8
	def _mul_(x , y):
		print('_mul_  method  of  class   c2')
		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)                                                              __mul__ method of class c1
                                                                          2000
print(b * a)                                                              __mul__ method of class c2
                                                                         2000

# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)                             Error
print('a + 7 : ' , a + 7)                             Error
print(7 + a)                                          Error
print('7 + 8 : ' , 7 + 8)                             15
m = c2()
n = c2()
print(m + n)                                         Error
print('a + m : ' , a + m)                            Error
print(m + a)                                         Error

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):
		return  sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)                                                     sum:30
print('Join : ' , m + n)                                                    Join:1020

# Write  a  program  to  implement  queue  using  list
class queue:
    def __init__(q):
        q.list = []
    def isempty(q):
        return q.list == []
    def enqueue(q, x):
        q.list.append(x)
    def dequeue(q):
        try:
            return q.list.pop(0)
        except:
            return None
    def first(q):
        if q.isempty():
            return None
        return q.list[0]
    def last(q):
        if q.isempty():
            return None
        return q.list[-1]
    def disp(q):
        if q.isempty():
            print("Queue is empty")
        else:
            print("Queue:", q.list)
    def size(q):
        return len(q.list)
def menu():
    print("1. Insertion")
    print("2. Deletion")
    print("3. Print queue")
    print("4. First element of queue")
    print("5. Last element of queue")
    print("6. Number of elements in the queue")
    print("7. Exit")
q = queue()
menu()
ch = int(input("Enter choice: "))

while ch != 7:
    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            q.enqueue(x)
            q.disp()

        case 2:
            deleted = q.dequeue()
            if deleted is None:
                print("Queue is empty, nothing to delete")
            else:
                print("Deleted element:", deleted)
            q.disp()

        case 3:
            q.disp()

        case 4:
            print("First element:", q.first())

        case 5:
            print("Last element:", q.last())

        case 6:
            print("Number of elements:", q.size())

        case _:
            print("Invalid choice")
    menu()
    ch = int(input("Enter choice: "))

Write  a  program  to  reverse  a  string  using  stack
from Stack import stack
s=stack()
string=input('Enter a string:')
for ch in string:
    s.push(ch)
print("Reverse  String :",end='');
while not s.isempty():
    print(s.pop(),end='')

Write  a  program  to  perform  parentheses  match
from Stack import stack   
def is_parentheses_valid(expr):
    Stack = stack()
    for ch in expr:
        if ch == '(':
            Stack.push(ch)
        elif ch == ')':
            popped = Stack.pop()
            if popped is None:    
                print(f"Invalid: Extra ')' found in expression: {expr}")
                return False
    if Stack.isempty():
        print(f"Valid: {expr}")
        return True
    else:
        print(f"Invalid: Extra '(' found in expression: {expr}")
        return False
expr=input('Enter an expression:')
is_parentheses_valid(expr)
