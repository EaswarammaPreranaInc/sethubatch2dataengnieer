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

# Is  10 + 20  a  recursion ?
class   c1:
	def __add__(a , b):
		print(10 + 20) # 30
a = c1()
b = c1()
print(a + b) # None is returned, no recursion

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y) # recursion
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
import  math
class  complex:
	def  get(self):
		self.real = float(input("Enter real part: ")) 
		self.imag = float(input("Enter imaginary part: ")) #How  to  read  real  and  imag
	def __str__(self):
		if self.imag >= 0:
			return f"{self.real} + {self.imag}i" 
		else:
			return f"{self.real} - {abs(self.imag)}i" #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def __add__(a ,  b):
		r=complex()
		r.real = a.real + b.real 
		r.imag = a.imag + b.imag  
		return r #How  to  add  objects  a  and  b
	def  __sub__(a ,  b):
		r=complex()
		r.real = a.real - b.real 
		r.imag = a.imag - b.imag  
		return r #How  to  subtract  objects  a  and  b
	def  __mul__(a ,  b):
		r=complex()
		r.real = a.real*b.real - a.imag * b.imag 
		r.imag = a.real*b.imag + a.imag * b.real 
		return r #How  to  multiply  objects  a  and   b
	def  __truediv__(a ,  b):
		r = complex()
		denom = b.real ** 2 + b.imag ** 2
		r.real = (a.real * b.real + a.imag * b.imag) / denom
		r.imag = (a.imag * b.real - a.real * b.imag) / denom
		return r #How  to  divide  objects   a  and  b
# End  of  the  class
x=complex() 
y=complex() #How  to  create  two  complex  class  objects
x.get() #How  to  read   inputs  into  1st  object
y.get() #How  to  read   inputs  into  2nd  object
print('Sum :  ' , x+y)
print('Difference :  ' , x-y)
print('Product :  ' ,  x*y)
print('Division  : ' , x/y)

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
			self.nr = int(input("Enter numerator: "))
			self.dr = int(input("Enter denominator: ")) #How  to  read  numerator  and  denominator  into  object
	def __gt__(self,b):
			return  self.nr * b.dr > self.dr * b.nr #true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return  self.nr * b.dr < self.dr * b.nr #true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return  self.nr * b.dr == self.dr * b.nr #true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return  self.nr * b.dr >= self.dr * b.nr #true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return  self.nr * b.dr <= self.dr * b.nr #true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			return  self.nr * b.dr != self.dr * b.nr #true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat() 
b = Rat() #How  to  create  two  Rat   class  objects  'a'  and  'b'
a.get() #How  to  read  1st  rational   number  into  object  'a'
b.get() #How  to  read  2nd  rational   number  into  object  'b'
if  a  >  b:
	print('>')
if  a  <  b:
	print('<')
if  a == b:
	print('==')
if  a  >=  b:
	print('>=')
if  a  <=  b:
	print('<=')
if  a != b:
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
print(a >= b) # __ge__ method :   10 20
                       #False
print(a <= b) # __ge__ method :   20 10
                        #True

# Find  outputs  (Home  work)
class   c1:
        def __init__(self , y):
             self . x = y
        def __eq__(m , n):
            print('__eq__ method  : ' , m . x , n . x)
            return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  #  not (a == b) __eq__ method  :  10 20 True
print(a == b) # __eq__ method  :  10 20 False

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __eq__(m , n):
		print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # __eq__ method  :   25 25 None
print(a != b) # __eq__ method  :   25 25 True
print(a.x != b.x) # False

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
print(a != b) # __ne__ method  :   10 10 False
print(a == b) # True
#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20) 
		print(a > b) # recursion
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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
''' Output:
c1  class  __gt__  method :  10 20
c1  class  __gt__  method :  20 10
c2  class  __gt__  method :  30 10
c1  class  __gt__  method :  20 40'''

# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  x.hr * y.noh #hourly-rate(i.e.  250) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  x.noh * y.hr #number-of-hours (i.e.  8) *  hourly-rate(i.e.  250)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)
'''Output:
__mul__  method  of  class   c1
2000
__mul__  method  of  class   c2
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
print('a + b : ' , a + b) # a + b : __add__ method  of  class   c1
print('a + 7 : ' , a + 7) # a + 7 : __add__ method  of  class   c1
print(7 + a) # Error because 7 is int object and a is class object
print('7 + 8 : ' , 7 + 8) # 7 + 8 :  15
m = c2()
n = c2()
print(m + n) # Error Because c2 object does not have dunder add method 
print('a + m : ' , a + m) # a + m :  __add__ method  of  class   c1
print(m + a) # Error

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  p.x+q.x#sum  of  numbers  (or)  join  of  strings #
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) # 30
print('Join : ' , m + n) # 1020

# Write  a  program  to  implement  deque  using  list
class queue:
    def __init__(q):
        q.list = []  # create an empty queue

    def isempty(q):
        return q.list == []  # True when queue is empty, False otherwise

    def enqueue(q, x):
        q.list.append(x)  # insert 'x' into the queue

    def dequeue(q):
        try:
            return q.list.pop(0)  # remove first element and return it
        except IndexError:
            return -1  # return -1 when deletion is not possible (empty queue)

    def first(q):
        try:
            return q.list[0]  # return first element
        except IndexError:
            return -1  # return -1 when queue is empty

    def last(q):
        try:
            return q.list[-1]  # return last element
        except IndexError:
            return -1  # return -1 when queue is empty

    def disp(q):
        print("Queue:", q.list)  # print the whole queue

    def size(q):
        return len(q.list)  # return number of elements in the queue

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
q= queue #How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while  True:
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					q.enqueue(x) #How  to  insert  'x'  into  the  queue
					q.disp() #How  to  print  queue
		case  2:
					x = q.dequeue() #How  to  delete  queue  element  and  print  the  deleted  element
					if x == None:
						print('Queue is empty.')
					else:
						print('Deleted element: ',x)
					q.disp() #How  to  print  queue
		case  3:
					q.disp() #How  to  print  the  queue
		case  4:
					x=q.first() #How  to  print  first  element  of  the  queue
					if x == None:
						print('Queue is empty.')
					else:
						print('first  element  of  the  queue:',x)
		case  5:
					x=q.last() #How  to  print  last  element  of  the  queue
					if x == None:
						print('Queue is empty.')
					else:
						print('last  element  of  the  queue:',x)
		case  6:
					print('number  of  elements  in  the  queue:', q.size()) #How  to  print  number  of  elements  in  the  queue
		case  7:	exit()
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))
'''Output:
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 1
Enter  element  to  be  inserted : 25
Queue: [25]
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 1
Enter  element  to  be  inserted : 10.8
Queue: [25, 10.8]
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 1
Enter  element  to  be  inserted : 'hyd'
Queue: [25, 10.8, 'hyd']
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 1
Enter  element  to  be  inserted : 3+4j
Queue: [25, 10.8, 'hyd', (3+4j)]
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 2
Deleted element:  25
Queue: [10.8, 'hyd', (3+4j)]
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 3
Queue: [10.8, 'hyd', (3+4j)]
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 4
first  element  of  the  queue: 10.8
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 5
last  element  of  the  queue: (3+4j)
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 6
number  of  elements  in  the  queue: 3
1. Insertion
2. Deletion
3. Print  queue
4. First  element of queue
5. Last  element of queue
6. Number  of  elements  in  the  queue
7. Exit
Enter  choice : 7'''
'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                   0     1       2       3

Stack   --->
Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

from stack import stack #How  to  import  stack  class  from  prog1b  module
s= stack() #How  to  create  stack  class  object
str = input('Enter any string: ') #How  to  read  a  string  into  a  str  object
for ch in str:
	s.push(ch) #How  to  push  each  char  of  string  into  the  stack
result = ''
while not s.isempty():
	result += s.pop()  #How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
print('Reverse string: ', result)

#Write  a  program  to  perform  parentheses  match
from stack import stack
expr = input('Enter parentheses expression: ')
a=stack()
for ch in expr:
	if ch == '(':
		a.push('(')
	elif ch == ')':
		x = a.pop()
		if x == None:
			print("Invalid: 'Excess ')'")
			exit()
if a.isempty():
	print('Valid: ( and ) are matching ')
else:
	print("Invalid: Excess ' '('")
'''Output:
Enter parentheses expression: (4+8)
Valid: ( and ) are matching
Enter parentheses expression: ((3+4)
Invalid: Excess ' '(' '''
'''
1) Is  ((3 + 4)  valid ?  ---> No  due  to  excess  (
2) Is  (3 * (4 + 5))  valid ?  --->  Yes
3) Is  (3 * (4 + 5))) + 6 valid ? --->No  due  to  excess  ')'
4) Is  3 + 4  valid ? --->  Yes
5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (
6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack
7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack
8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  invalid  msg  and  stop  execution
9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->	Print  valid  msg  when  stack  is   empty  and  invalid  otherwise
10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
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
'''Output:
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 1
Enter element to be inserted: 25
Stack:  [25]
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 1
Enter element to be inserted: 10.8
Stack:  [25, 10.8]
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 1
Enter element to be inserted: 'hyd'
Stack:  [25, 10.8, 'hyd']
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 2
Deleted element:  hyd
Stack:  [25, 10.8]
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 3
Stack:  [25, 10.8]
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 4
Last element:  10.8
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 5
Number of elements:  2
1. Insertion
2. deletion
3. print Stack
4. Last element of stack
5. Number of elements in stack
6. Exit
Enter your choice: 6'''

#Object  's'   --->  list = [25 , 10.8 , 'Hyd']
'''
What  is  the  difference  between  's'  and  s . list ?  --->

's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack  object
'''