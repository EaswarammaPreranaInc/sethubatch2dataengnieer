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
'''

#Program:
import math
class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        self.test()
    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter: '))
    def __str__(self):
        return F'{self.nr} / {self.dr}'
    def simplify(self):
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g
    def __add__(self, other):
        result = Rat()
        result.nr = self.nr * other.dr + self.dr * other.nr
        result.dr = self.dr * other.dr
        result.simplify()
        return result
    def __sub__(self, other):
        result = Rat()
        result.nr = self.nr * other.dr - self.dr * other.nr
        result.dr = self.dr * other.dr
        result.simplify()
        return result
    def __mul__(self, other):
        result = Rat()
        result.nr = self.nr * other.nr
        result.dr = self.dr * other.dr
        result.simplify()
        return result
    def __truediv__(self, other):
        result = Rat()
        result.nr = self.nr * other.dr
        result.dr = self.dr * other.nr
        result.simplify()
        return result

a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a.get()
b.get()
c = a + b
d = a - b
e = a * b
print('Sum: ', c)
print('Difference: ', d)
print('Product: ', e)
if b.nr != 0:
    f = a / b
    print('Division: ', f)
else:
    print('Division is not permitted.')






# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)					# Error





# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)					# Error





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

import  math
class  complex:
	def  get(self):
		How  to  read  real  and  imag
	def    _str_(self):
		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  _add_(a ,  b):
		How  to  add  objects  a  and  b
	def  _sub_(a ,  b):
		How  to  subtract  objects  a  and  b
	def  _mul_(a ,  b):
		How  to  multiply  objects  a  and   b
	def  _div_(a ,  b):
		How  to  divide  objects   a  and  b
# End  of  the  class
How  to  create  two  complex  class  objects
How  to  read   inputs  into  1st  object
How  to  read   inputs  into  2nd  object
print('Sum :  ' , ???)
print('Difference :  ' , ???)
print('Product :  ' ,  ??)
print('Division  : ' , ???)
'''

#Program:
import math
class complex:
    def get(self):
        self.real = float(input('Enter real part: '))
        self.imag = float(input('Enter imaginary part: '))
    def __str__(self):
        if self.imag >= 0:
            return f'{self.real} + {self.imag}i'
        else:
            return f'{self.real} - {-self.imag}i'
    def __add__(self, other):
        result = complex()
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        return result
    def __sub__(self, other):
        result = complex()
        result.real = self.real - other.real
        result.imag = self.imag - other.imag
        return result
    def __mul__(self, other):
        result = complex()
        result.real = self.real * other.real - self.imag * other.imag
        result.imag = self.real * other.imag + self.imag * other.real
        return result
    def __truediv__(self, other):
        result = complex()
        denom = other.real**2 + other.imag**2  
        result.real = (self.real * other.real + self.imag * other.imag) / denom
        result.imag = (self.imag * other.real - self.real * other.imag) / denom
        return result

a = complex()
b = complex()
print("Enter first complex number:")
a.get()
print("Enter second complex number:")
b.get()
sum_result = a + b
diff_result = a - b
prod_result = a * b
if b.real != 0 or b.imag != 0:
    div_result = a / b  
    print('Division: ', div_result)
else:
    print('Division is not permitted (division by zero).')
print('Sum: ', sum_result)
print('Difference: ', diff_result)
print('Product: ', prod_result)







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

import  math
class  Rat:
	def  get(self):
			 How  to  read  numerator  and  denominator  into  object
	def _gt_(self,b):
			return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def _lt_(self,b):
			return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def _eq_(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def _ge_(self,b):
			return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def _le_(self,b):
			return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def _ne_(self,b):
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
'''

#Program:
import math
class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter denominator: '))
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
print("Enter the first rational number:")
a.get()
print("Enter the second rational number:")
b.get()
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')
elif a >= b:
    print('>=')
elif a <= b:
    print('<=')
elif a != b:
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
print(a >= b)
print(a <= b)

#Output:
__ge__ method :   10 20
False
__ge__ method :   20 10
True





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
print(a != b)  #  not (a == b)
print(a == b)

#Output:
__eq__ method  :  10 20
True
__eq__ method  :  10 20
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
print(a == b)
print(a != b)
print(a . x !=  b . x)

#Output:
__eq__ method  :   25 25
None
__eq__ method  :   25 25
True
False





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
print(a != b)
print(a == b)

#Output:
__ne__ method  :   10 10
False
True





#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)				# Recursion Error






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

#Output:
c1  class  __gt__  method :  10 20
c1  class  __gt__  method :  20 10
c2  class  __gt__  method :  30 10
c1  class  __gt__  method :  20 40






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
print(a * b)
print(b * a)

#Program:
class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 250
    def __mul__(self, other):
        if isinstance(other, c2):
            print('_mul_ method of class c1')
            return self.empno * other.noh  
        else:
            return NotImplemented
class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8
    def __mul__(self, other):
        if isinstance(other, c1):
            print('_mul_ method of class c2')
            return self.noh * other.empno  
        else:
            return NotImplemented 
a = c1()
b = c2()
print(a * b)  # c1 * c2
print(b * a)  # c2 * c1






# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)
print('a + 7 : ' , a + 7)
print(7 + a)
print('7 + 8 : ' , 7 + 8)
m = c2()
n = c2()
print(m + n)
print('a + m : ' , a + m)
print(m + a)

#Program:
class c1:
    def __add__(self, other):
        if isinstance(other, c1):
            return '__add__ method of class c1 (Adding two c1 objects)'
        elif isinstance(other, int):
            return f'Adding c1 object and an integer: {other + 10}'
        else:
            return NotImplemented  
class c2:
    def __add__(self, other):
        return 'c2 objects cannot be added directly'
a = c1()
b = c1()
print('a + b : ', a + b)
print('a + 7 : ', a + 7)
print(7 + a)
print('7 + 8 : ', 7 + 8)
m = c2()
n = c2()
print(m + n)
print('a + m : ', a + m)
print(m + a)






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
print('Sum : ' , a + b)
print('Join : ' , m + n)

#Program:
class c1:
    def __init__(self, y):
        self.x = y
    def __add__(self, other):
        if isinstance(self.x, (int, float)) and isinstance(other.x, (int, float)):
            return self.x + other.x 
        elif isinstance(self.x, str) and isinstance(other.x, str):
            return self.x + other.x 
        else:
            return "Incompatible types for addition" 
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum :', a + b)  
print('Join :', m + n) 







Data Structures:
# Write  a  program  to  implement  queue  using  list
class  queue:
        def  _init_(q):
                 How  to  create  an  empty  queue
        def  isempty(q):
                return  True  when  queue  is  empty  and  False  otherwise
        def  enqueue(q , x):
                How  to  insert  'x'  into  the  queue
        def  dequeue(q):
                How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
				(return  -1  when  deletion  is  not  possible)
        def  first(q):
                How  to  return  the  first  element  of  the  queue
				(return  -1  when  queue  is  empty)
		def  last(q):
                How  to  return  the  first  element  of  the  queue
				(return   -1  when  queue  is  empty)
        def  disp(q):
                How  to  print  queue
        def  size(q):
                How  to  return  number   of  elements  in  the  queue
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  queue')
        print('4. First  element of queue')
        print('5. Last  element of queue')
        print('6. Number  of  elements  in  the  queue')
        print('7. Exit')
# End of  the  function
How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while  repeat  until  user  input  is  7
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					How  to  insert  'x'  into  the  queue
					How  to  print  queue
		case  2:
					How  to  delete  queue  element  and  print  the  deleted  element
					How  to  print  queue
		case  3:
					How  to  print  the  queue
		case  4:
					How  to  print  first  element  of  the  queue
		case  5:
					How  to  print  last  element  of  the  queue
		case  6:
					How  to  print  number  of  elements  in  the  queue
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))

#Program:
class Queue:
    def __init__(self):
        self.queue = []
    def isempty(self):
	return len(self.queue) == 0
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if self.isempty():
            return -1
        return self.queue.pop(0)
    def first(self):
        if self.isempty():
            return -1
        return self.queue[0]
    def last(self):
        if self.isempty():
            return -1
        return self.queue[-1]
    def disp(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue)
    def size(self):
        return len(self.queue)
def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print queue')
    print('4. First element of queue')
    print('5. Last element of queue')
    print('6. Number of elements in the queue')
    print('7. Exit')
q = Queue()
menu()
ch = int(input('Enter choice: '))
while ch != 7:
    if ch == 1:
        x = eval(input('Enter element to be inserted: '))
        q.enqueue(x)
        q.disp()
    elif ch == 2:
        deleted = q.dequeue()
        if deleted == -1:
            print("Queue is empty. Deletion not possible.")
        else:
            print(f"Deleted element: {deleted}")
        q.disp()
    elif ch == 3:
        # Print the queue
        q.disp()
    elif ch == 4:
        first = q.first()
        if first == -1:
            print("Queue is empty.")
        else:
            print(f"First element: {first}")
    elif ch == 5:
        last = q.last()
        if last == -1:
            print("Queue is empty.")
        else:
            print(f"Last element: {last}")
    elif ch == 6:
        print(f"Number of elements in the queue: {q.size()}")
    menu()
    ch = int(input('Enter choice: '))







'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                   0     1      2      3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
How  to  import  stack  class  from  prog1b  module
How  to  create  stack  class  object
How  to  read  a  string  into  a  str  object
How  to  push  each  char  of  string  into  the  stack
printf("Reverse  String :  ");
How  to  remove  each  char  of  stack  and  print  until   stack  is  empty

#Program:
from prog1b import Stack
def reverse_string(input_str):
    stack = Stack()
    for char in input_str:
        stack.push(char)
    print("Reverse String: ", end="")
    while not stack.isempty():
        print(stack.pop(), end="")
input_str = input("Enter a string to reverse: ")
reverse_string(input_str)






'''
Write  a  program  to  perform  parentheses  match

1) Is  ((3 + 4)  valid ?  ---> No  due  to  excess  (

2) Is  (3 * (4 + 5))  valid ?  --->  Yes

3) Is  (3 * (4 + 5))) + 6 valid ? --->No  due  to  excess  ')'

4) Is  3 + 4  valid ? --->  Yes

5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (

6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack

7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack

8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  invalid  msg  and  stop  execution

9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->
																						Print  valid  msg  when  stack  is   empty  and  invalid  otherwise

10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

#Program:
from prog1b import Stack
def parentheses_match(expression):
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            popped = stack.pop()
            if popped == -1: 
                print("Invalid: Too many closing parentheses")
                return
    if stack.isempty():
        print("Valid: Parentheses are balanced")
    else:
        print("Invalid: Too many opening parentheses")
expression = input("Enter an expression to check parentheses: ")
parentheses_match(expression)