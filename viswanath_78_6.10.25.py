q) Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects
Ans) import math
class Rat:
	def get(self):  
		self.nr = int(input('Enter numerator : '))
		self.dr = int(input('Enter denominator : '))
		self.test()
	def test(self): 
		while self.dr == 0:
			self.dr = int(input('Denominator cannot be zero and re-enter : '))
	def __str__(self):  # Do not modify
		return F'{self.nr} / {self.dr}'
	def simplify(self):  
		if self.nr != 0:
			g = math.gcd(self.nr, self.dr)
			self.nr = self.nr // g
			self.dr = self.dr // g
	# Operator overloading methods
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
			return None
		r = Rat()
		r.nr = self.nr * other.dr
		r.dr = self.dr * other.nr
		r.simplify()
		return r
# End of the class

a = Rat()
b = Rat()  # Create objects and get input
a.get()  
b.get()  
c = a + b
d = a - b
e = a * b
f = a / b  # Perform operations using overloaded operators
print('Sum :', c)        
print('Difference :', d) 
print('Product :', e)    
if f is not None:
	print('Division :', f)  
else:
	print('Division is not permitted.')

q) Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined  complex  object
Ans)  class Complex:
	def get(self):
		self.real = int(input('Enter real part : '))
		self.imag = int(input('Enter imaginary part : '))
	def __str__(self):
		if self.imag >= 0:
			return F'{self.real} + {self.imag}i'
		else:
			return F'{self.real} - {abs(self.imag)}i'
	# Operator overloading methods
	def __add__(self, other):
		r = Complex()
		r.real = self.real + other.real
		r.imag = self.imag + other.imag
		return r
	def __sub__(self, other):
		r = Complex()
		r.real = self.real - other.real
		r.imag = self.imag - other.imag
		return r
	def __mul__(self, other):
		r = Complex()
		r.real = self.real * other.real - self.imag * other.imag
		r.imag = self.real * other.imag + self.imag * other.real
		return r
	def __truediv__(self, other):
		r = Complex()
		denom = other.real**2 + other.imag**2
		r.real = (self.real * other.real + self.imag * other.imag) / denom
		r.imag = (self.imag * other.real - self.real * other.imag) / denom
		return r
# End of the class
a = Complex()
b = Complex()  # Create two complex objects
print('First object')
a.get()
print('Second object')
b.get()  # Read inputs 
c = a + b
d = a - b
e = a * b
f = a / b   # Perform operations using overloaded operators
print('Sum :', c.__str__())         
print('Difference :', d.__str__())  
print('Product :', e.__str__())     
print('Division :', f.__str__()) # Print results   
 
q) Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects
Ans)  import math
class Rat:
	def get(self):
		self.nr = int(input('Enter numerator : '))
		self.dr = int(input('Enter denominator : '))
		while self.dr == 0:
			self.dr = int(input('Denominator cannot be zero, re-enter : '))
	# Operator overloading methods using cross product
	def __gt__(self, b):   # a > b
		return self.nr * b.dr > self.dr * b.nr
	def __lt__(self, b):   # a < b
		return self.nr * b.dr < self.dr * b.nr
	def __eq__(self, b):   # a == b
		return self.nr * b.dr == self.dr * b.nr
	def __ge__(self, b):   # a >= b
		return self.nr * b.dr >= self.dr * b.nr
	def __le__(self, b):   # a <= b
		return self.nr * b.dr <= self.dr * b.nr
	def __ne__(self, b):   # a != b
		return self.nr * b.dr != self.dr * b.nr
# End of the class
a = Rat()
b = Rat()  # Create two Rat objects
a.get() 
b.get()  # Read inputs
print('a > b :', a > b)    # True
print('a < b :', a < b)    # False
print('a == b :', a == b)  # False
print('a >= b :', a >= b)  # True
print('a <= b :', a <= b)  # False
print('a != b :', a != b)  # True

# Is 10 + 20 a recursion?
class c1:
	def __add__(a, b):
		print(10 + 20)
a = c1()
b = c1()
print(a + b)  # 30 # none
# No Recursion

# Is x + y a recursion?
class c1:
	def __add__(a, b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)  # Error: RecursionError (infinite recursion occurs)

class c1:
	def __init__(self, y):
		self.x = y
	def __ge__(m, n):
		print('__ge__ method :', m.x, n.x)
		return m.x > n.x
# End of the class
a = c1(10)
b = c1(20)
print(a >= b)  # __ge__ method : 10 20 → False
print(a <= b)  # __ge__ method : 20 10 → True

class c1:
	def __init__(self, y):
		self.x = y
	def __eq__(m, n):
		print('__eq__ method :', m.x, n.x)
		return m.x == n.x
# end of the class
a = c1(10)
b = c1(20)
print(a != b)  # not (a == b) → __eq__ method : 10 20 → not False → True
print(a == b)  # __eq__ method : 10 20 → False


class c1:
	def __init__(self, y):
		self.x = y
	def __eq__(m, n):
		print('__eq__ method  : ', m.x, n.x)  
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # __eq__ method  :  25 25 # none
print(a != b)  # __eq__ method  :  25 25 →  True
print(a.x != b.x)  # False

class c1:
    def __init__(self, y):
        self.x = y
    def __ne__(m, n):
        print('__ne__ method  : ', m.x, n.x)   # __ne__ method : 10 10
        return m.x != n.x                      # False
# end of the class
a = c1(10)
b = a
print(a != b)  # False
print(a == b)  # True

# Is 10 > 20 a recursion?
class c1:
	def __gt__(a , b):
		print(10 > 20)  # False
		print(a > b)    # Error: infinite recursion
a = c1()
b = c1()
print(a > b)        # Error: RecursionError

class c1:
	def __init__(self , y):
		self.x = y
	def __gt__(p , q):
		print('c1 class __gt__ method :', p.x , q.x)
class c2:
	def __init__(self , y):
		self.x = y
	def __gt__(p , q):
		print('c2 class __gt__ method :', p.x , q.x)
#end of the class
a = c1(10)
b = c1(20)
a > b  # c1 class __gt__ method : 10 20
a < b  # c1 class __gt__ method : 20 10 
m = c2(30)
n = c2(40)
a < m  # c1 class __gt__ method : 30 10
n < b  # c2 class __gt__ method : 20 40

class c1:
	def __init__(self):
		self.empno = 25
		self.hr = 250
	def __mul__(x , y):
		print('__mul__ method of class c1')
		return x.hr * y.noh
class c2:
	def __init__(self):
		self.empno = 25
		self.noh = 8
	def __mul__(x , y):
		print('__mul__ method of class c2')
		return x.noh * y.hr
# End of the class
a = c1()
b = c2()
print(a * b)  # __mul__ method of class c1 → 2000
print(b * a)  # __mul__ method of class c2 → 2000

class c1:
	def __add__(x , y):
		return '__add__ method of class c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b :', a + b)  #  a + b :  __add__ method  of  class   c1
print('a + 7 :', a + 7)  #  a + 7 :  __add__ method  of  class   c1
print(7 + a)  # Error: int has no __radd__ in c1 → TypeError
print('7 + 8 :', 7 + 8)  # 7 + 8 :  15
m = c2()
n = c2()
print(m + n)  # Error: __add__ not defined → TypeError
print('a + m :', a + m)  # a + m : __add__ method of class c1
print(m + a)  # Error: __add__ not defined for c2 → TypeError

class c1:
	def __init__(self , y):
		self.x = y
	def __add__(p , q):
		return p.x + q.x  # sum of numbers or join of strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum :', a + b)  # Sum : 30
print('Join :', m + n)  # Join :  '1020' 

                          DSA programming
q) Write  a  program  to  implement  queue  using  list
 Ans) class queue:
    def __init__(q):
        q.q = []  # Create an empty queue
    def isempty(q):
        return len(q.q) == 0  # True if queue is empty
    def enqueue(q, x):
        q.q.append(x)  # Insert x at end of queue
    def dequeue(q):
        if q.isempty():
            return None  # Deletion not possible
        return q.q.pop(0)  # Remove first element
    def first(q):
        if q.isempty():
            return None
        return q.q[0]  # Return first element
    def last(q):
        if q.isempty():
            return None
        return q.q[-1]  # Return last element
    def disp(q):
        print(q.q)  # Print queue
    def size(q):
        return len(q.q)  # Number of elements
# End of class
def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print queue')
    print('4. First element of queue')
    print('5. Last element of queue')
    print('6. Number of elements in the queue')
    print('7. Exit')
# Create queue object
q = queue()
menu()
ch = int(input('Enter choice : '))
while ch != 7:
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            q.enqueue(x)  # Insert element
            q.disp()      # Print queue
        case 2:
            deleted = q.dequeue()  # Delete first element
            print('Deleted element :', deleted)
            q.disp()               # Print queue
        case 3:
            q.disp()  # Print queue
        case 4:
            print('First element :', q.first())  # First element
        case 5:
            print('Last element :', q.last())    # Last element
        case 6:
            print('Number of elements :', q.size())  # Queue size
    # End of match
    menu()
    ch = int(input('Enter choice : '))

q) Write  a  program  to  reverse  a  string  using  stack
 Ans) from prog1b import stack  # How  to  import  stack  class  from  prog1b  module
s = stack()  # How  to  create  stack  class  object
str1 = input('Enter string to reverse : ')  # How  to  read  a  string  into  a  str  object
for ch in str1:
    s.push(ch)  #  How  to  push  each  char  of  string  into  the  stack
print('Reverse String : ', end='')  # printf("Reverse  String :  ");
while not s.isempty():
    print(s.pop(), end='')  # How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
print()  # for newline

q) Write  a  program  to  perform  parentheses  match
Ans) from prog1b import stack  # Import stack class from previous program
s = stack()  # Create stack object
expr = input('Enter expression starting with parentheses : ')  # Read input expression
valid = True
# Traverse each character in the expression
for ch in expr:
    if ch == '(':            # Action when '(' encountered
        s.push(ch)
    elif ch == ')':          # Action when ')' encountered
        if s.isempty():      # Pop returns None / stack empty
            valid = False
            break
        s.pop()
if not s.isempty():          # Stack not empty → excess '('
    valid = False
if valid:
    print('Parentheses are balanced (Valid)')
else:
    print('Parentheses are not balanced (Invalid)')  # Print result




