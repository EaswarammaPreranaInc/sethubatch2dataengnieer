
#========================================
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

import math
class Rat:
	def get(self):  # Do not modify the method
		self.nr = int(input('Enter numerator : '))
		self.dr = int(input('Enter denominator : '))
		self.test()
	def test(self): # Do not modify the method
		while self.dr == 0:
			self.dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def __str__(self):  # Do not modify the method
		return F'{self.nr} / {self.dr}'
	def simplify(self):   # Do not modify the method
		if self.nr != 0:
			g = math.gcd(self.nr, self.dr)
			self.nr = self.nr // g
			self.dr = self.dr // g
	def __add__(self, other):
		res = Rat()
		res.nr = self.nr * other.dr + self.dr * other.nr
		res.dr = self.dr * other.dr
		res.simplify()
		return res
	def __sub__(self, other):
		res = Rat()
		res.nr = self.nr * other.dr - self.dr * other.nr
		res.dr = self.dr * other.dr
		res.simplify()
		return res
	def __mul__(self, other):
		res = Rat()
		res.nr = self.nr * other.nr
		res.dr = self.dr * other.dr
		res.simplify()
		return res
	def __truediv__(self, other):
		if other.nr == 0:
			raise ZeroDivisionError("Division is not permitted.")
		res = Rat()
		res.nr = self.nr * other.dr
		res.dr = self.dr * other.nr
		res.simplify()
		return res
# End of the class
a = Rat()
b = Rat()
a.get()
b.get()
print('Sum : ', a + b)
print('Difference : ', a - b)
print('Product : ', a * b)
try:
	 print('Division  : ', a / b)
except ZeroDivisionError:
	 print('Division is not permitted.')

#=========================================

# Is 10 + 20 a recursion ?
class c1:
	def __add__(a, b):
		print(10 + 20)
a = c1()
b = c1()
print(a + b)
'''
30
None
'''

#=========================================

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
 Error Stack exceeded
'''
#=========================================

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
class complex:
	def get(self):
		self.real = float(input('Enter real part : '))
		self.imag = float(input('Enter imaginary part : '))
	def __str__(self):
		if self.imag >= 0:
			return f'{self.real} + {self.imag}i'
		else:
			return f'{self.real} - {abs(self.imag)}i'
	def __add__(a, b):
		res = complex()
		res.real = a.real + b.real
		res.imag = a.imag + b.imag
		return res
	def __sub__(a, b):
		res = complex()
		res.real = a.real - b.real
		res.imag = a.imag - b.imag
		return res
	def __mul__(a, b):
		res = complex()
		res.real = a.real * b.real - a.imag * b.imag
		res.imag = a.real * b.imag + a.imag * b.real
		return res
	def __truediv__(a, b):
		denom = b.real ** 2 + b.imag ** 2
		if denom == 0:
			raise ZeroDivisionError("Division by zero is not permitted.")
		res = complex()
		res.real = (a.real * b.real + a.imag * b.imag) / denom
		res.imag = (a.imag * b.real - a.real * b.imag) / denom
		return res
# End of the class
c1 = complex()
c2 = complex()
print("Enter first complex number:")
c1.get()
print("Enter second complex number:")
c2.get()
print('Sum : ', c1 + c2)
print('Difference : ', c1 - c2)
print('Product : ', c1 * c2)
try:
	print('Division : ', c1 / c2)
except ZeroDivisionError:
	print('Division is not permitted.')

#=========================================

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
import math
class Rat:
	def get(self):
		self.nr = int(input('Enter numerator : '))
		self.dr = int(input('Enter denominator : '))
		while self.dr == 0:
			self.dr = int(input('Denominator cannot be zero, re-enter: '))
	def __gt__(self, b):
		return self.nr * b.dr > b.nr * self.dr
	def __lt__(self, b):
		return self.nr * b.dr < b.nr * self.dr
	def __eq__(self, b):
		return self.nr * b.dr == b.nr * self.dr
	def __ge__(self, b):
		return self.nr * b.dr >= b.nr * self.dr
	def __le__(self, b):
		return self.nr * b.dr <= b.nr * self.dr
	def __ne__(self, b):
		return self.nr * b.dr != b.nr * self.dr
# End of the class
a = Rat()
b = Rat()
print("Enter first rational number:")
a.get()
print("Enter second rational number:")
b.get()
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


#=========================================

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
__ge__ method :   10 20
False
__ge__ method :   20 10
True
'''
#=========================================

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
print(a != b)  #  not (a == b)
print(a == b)
'''
__eq__ method  :  10 20
True
__eq__ method  :  10 20
False
'''
#=========================================

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
__eq__ method  :   25 25
None
__eq__ method  :   25 25
True
False'''

#=========================================

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
__ne__ method  :   10 10
False
True
'''
#=========================================

 #  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)
'''
stack exceeded
'''
#=========================================

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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
'''
c1  class  __gt__  method :  10 20
c1  class  __gt__  method :  20 10

c2  class  __gt__  method :  30 10
c1  class  __gt__  method :  20 40
'''
#=========================================
# Overload  *  operator  to  multiply  two  different  class  objects
class c1:
	def __init__(self):
		self.empno = 25
		self.hr = 250
	def __mul__(self, other):
		print('__mul__  method  of  class   c1')
		if isinstance(other, c2):
			return self.hr * other.noh
		return NotImplemented

class c2:
	def __init__(self):
		self.empno = 25
		self.noh = 8
	def __mul__(self, other):
		print('__mul__  method  of  class   c2')
		if isinstance(other, c1):
			return self.noh * other.hr
		return NotImplemented

# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)
'''
__mul__  method  of  class   c1
2000
__mul__  method  of  class   c2
2000
'''
#=========================================

 # Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) #a + b :  __add__ method  of  class   c1
print('a + 7 : ' , a + 7) #a + 7 :  __add__ method  of  class   c1
# print(7 + a)  #Error unsupported operand
print('7 + 8 : ' , 7 + 8) #7 + 8 :  15
m = c2()
n = c2()
# print(m + n)
print('a + m : ' , a + m) #a + m :  __add__ method  of  class   c1
# print(m + a)
'''

'''
#=========================================

 # Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class c1:
	def __init__(self, y):
		self.x = y
	def __add__(p, q):
		if isinstance(p.x, (int, float)) and isinstance(q.x, (int, float)):
			return p.x + q.x
		elif isinstance(p.x, str) and isinstance(q.x, str):
			return p.x + q.x
		else:
			return NotImplemented
# end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ', a + b)
print('Join : ', m + n)
'''
Sum :  30
Join :  1020'''

#=========================================
# Write  a  program  to  implement  queue  using  list
class queue:
	def __init__(q):
		q.list = []  # How to create an empty queue
	def isempty(q):
		return q.list == []  # return True when queue is empty and False otherwise
	def enqueue(q, x):
		q.list.append(x)  # How to insert 'x' into the queue
	def dequeue(q):
		if q.isempty():
			return -1  # return -1 when deletion is not possible
		return q.list.pop(0)  # How to remove first element of the queue and return the deleted element
	def first(q):
		if q.isempty():
			return -1  # return -1 when queue is empty
		return q.list[0]  # How to return the first element of the queue
	def last(q):
		if q.isempty():
			return -1  # return -1 when queue is empty
		return q.list[-1]  # How to return the last element of the queue
	def disp(q):
		print('Queue : ', q.list)  # How to print queue
	def size(q):
		return len(q.list)  # How to return number of elements in the queue
# End of the class

def menu():
	print('1. Insertion')
	print('2. Deletion')
	print('3. Print queue')
	print('4. First element of queue')
	print('5. Last element of queue')
	print('6. Number of elements in the queue')
	print('7. Exit')
# End of the function

if __name__ == '__main__':
	q = queue()  # How to create queue class object
	menu()
	ch = int(input('Enter choice : '))
	while ch != 7:  # repeat until user input is 7
		match ch:
			case 1:
				x = eval(input('Enter element to be inserted : '))
				q.enqueue(x)  # How to insert 'x' into the queue
				q.disp()      # How to print queue
			case 2:
				x = q.dequeue()  # How to delete queue element and print the deleted element
				if x == -1:
					print('Queue is empty, deletion is not permitted')
				else:
					print('Deleted element : ', x)
				q.disp()      # How to print queue
			case 3:
				q.disp()      # How to print the queue
			case 4:
				x = q.first()  # How to print first element of the queue
				if x == -1:
					print('Queue is empty')
				else:
					print('First element : ', x)
			case 5:
				x = q.last()  # How to print last element of the queue
				if x == -1:
					print('Queue is empty')
				else:
					print('Last element : ', x)
			case 6:
				print('Number of elements : ', q.size())  # How to print number of elements in the queue
			case 7:
				break
		# End of match
		menu()
		ch = int(input('Enter choice : '))

#=========================================

'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                   0     1      2      3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog10a import stack
s=stack()
str=input("enter the string: ")
for ch in str:
	s.push(ch)
result=''
while not s.isempty():
	result+=s.pop()
print('Reverse string : ',result)

# How  to  import  stack  class  from  prog1b  module
# How  to  create  stack  class  object
# How  to  read  a  string  into  a  str  object
# How  to  push  each  char  of  string  into  the  stack
# printf("Reverse  String :  ");
# How  to  remove  each  char  of  stack  and  print  until   stack  is  empty

#=========================================

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

from prog10a import stack
exp=input("enter the expression: ")
a=stack()
for ch in exp:
	if ch=='(':
		a.push("(")
	elif ch==")":
		x=a.pop()
		if x==None:
			print("invalid")
			exit()
if a.isempty():
	print('valid')
else:
	print('invalid')
#=========================================

 # Write  a  program  to  implement  stack  using  list
class  stack:
	def  __init__(s):
		s . list = []   #  How  to  create  an  empty  stack
	def  isempty(s):
		return  s . list ==  []   #  return  True  when  stack  is  empty  and  False  otherwise
	def  push(s , x):
		s . list . append(x)  #  How  to  insert  'x'  into  the  stack
	def  pop(s):
		try:
			return  s . list . pop()  #  How  to  delete  last  element  of  the  stack  and  return  the  deleted  element
		except:
			return  None  #  return  None  when  deletion  is  not  possible
	def  peek(s):
		try:
			return  s . list[-1]  #   How  to  return  the  last  element  of  the  stack
		except:
			return  None
	def  disp(s):
		print('Stack :  ' , s . list)  #  How  to  print  stack
	def   size(s):
		return  len(s . list) #   How  to  return  number   of  elements  in  the  stack
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Stack')
        print('4. Last  element of stack')
        print('5. Number  of  elements  in  the  stack')
        print('6. Exit')
# End of  the  function
if  __name__  ==  '__main__':
	s = stack()   #  How  to  create  stack  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						s . push(x)   #  How  to  insert  'x'  into  the  stack
						s . disp()   #  How  to  print  stack
			case  2:
						x = s . pop() #  How  to  delete  stack  element  and  print  the  deleted  element
						if  x  ==  None:
							print('Stack  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						s . disp()  #   How  to  print  stack
			case  3:
						s . disp() #   How  to  print  the  stack
			case  4:
						x = s . peek()  #  How  to  print  last  element  of  the  stack
						if  x == None:
							print('Stack  is  empty')
						else:
							print('Last  element :  ' , x)
			case  5:
						print('Number  of  elements  :  ' ,  s . size())   #  How  to  print  number  of  elements  in  the  stack
			case  6:  exit()
		# End  of  match

#Object  's'   --->  list = [25 , 10.8 , 'Hyd']

'''
What  is  the  difference  between  's'  and  s . list ?  --->


's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack  object
 This  is  stack  program  already  done  in  the  class
'''