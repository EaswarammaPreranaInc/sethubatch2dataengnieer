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
		s = Rat()
		s . nr = a . nr * b . dr + a . dr * b . nr
		s . dr = a . dr * b . dr
		s . simplify()
		return s
	def  __sub__(a , b):   #  Modify  the  method
		s = Rat()
		s . nr = a . nr * b . dr - a . dr * b . nr
		s . dr = a . dr * b . dr
		s . simplify()
		return s
	def  __mul__(a , b):   #  Modify  the  method
		s = Rat()
		s . nr = a . nr * b . nr
		s . dr = a . dr * b . dr
		s . simplify()
		return s
	def  __truediv__(a , b):   #  Modify  the  method
		s = Rat()
		s . nr = a . nr * b . dr
		s . dr = a . dr * b . nr
		s . simplify()
		return s
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
print('Difference :  ' , a - b)
print('Product :  ' , a * b)
if b . nr != 0:
	print('Division  : ' , a / b)
else:
	print('Division is not permitted.')


# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20) # not recursion
a = c1()
b = c1()
print(a + b) # 30  None


# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):
		x = c1() # recursion error
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) # error


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
		self. real = int(input('Enter real number:')) # How  to  read  real  and  imag
		self. imag = int(input('Enter imag number:'))
	def    __str__(self): # How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
		return F'{self.real} + {self.imag}i' if self.imag >=0 else F'{self.real} - {abs(self.imag)}i' 
	def  __add__(a ,  b): # How  to  add  objects  a  and  b
		s = complex()
		s.real = a.real + b.real
		s.imag = a.imag + b.imag
		return s
	def __sub__(a ,  b): # How  to  subtract  objects  a  and  b
		s = complex()
		s.real = a.real - b.real
		s.imag = a.imag - b.imag
		return s
	def  __mul__(a ,  b): # How  to  multiply  objects  a  and   b
		s = complex()
		s.real = a.real * b.real - a.imag * b.imag
		s.imag = a.real * b.imag + a.imag * b.real
		return s
	def  __truediv__(a ,  b): # How  to  divide  objects   a  and  b
		s = complex()
		denom = b.real**2 + b.imag**2
		s.real = (a.real * b.real + a.imag * b.imag) / denom
		s.imag = (a.imag * b.real - a.real * b.imag) / denom
		return s
		
# End  of  the  class
# How  to  create  two  complex  class  objects
c1 = complex()
c2 = complex()
# How  to  read   inputs  into  1st  object
c1.get()
# How  to  read   inputs  into  2nd  object
c2.get()
print('Sum :  ' , c1 + c2)
print('Difference :  ' , c1 - c2)
print('Product :  ' , c1 * c2)
print('Division  : ' , c1 / c2)


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
import  math
class  Rat:
	def  get(self): # How  to  read  numerator  and  denominator  into  object
		self.nr = int(input('Enter  numerator : '))
		self.dr = int(input('Enter  denominator : '))
	def __gt__(a,b):
			return a.nr * b.dr > a.dr * b.nr # return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(a,b):
			return a.nr * b.dr < a.dr * b.nr # return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(a,b):
			return a.nr * b.dr == a.dr * b.nr # return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(a,b):
			return a.nr * b.dr >= a.dr * b.nr # return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(a,b):
			return a.nr * b.dr <= a.dr * b.nr # return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(a,b):
			return a.nr * b.dr != a.dr * b.nr # return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
# How  to  create  two  Rat   class  objects  'a'  and  'b'
s = Rat()
t = Rat()
# How  to  read  1st  rational   number  into  object  'a'
s.get()
# How  to  read  2nd  rational   number  into  object  'b'
t.get()
if  s > t:
	print(F'{s > t}  due  to  {s.nr * t.dr} > {s.dr * t.nr}')
if  s < t:
	print(F'{s < t}  due  to  {s.nr * t.dr} < {s.dr * t.nr}')
if  s == t:
	print(F'{s == t}  due  to  {s.nr * t.dr} == {s.dr * t.nr}')
if  s >= t:
	print(F'{s >= t}  due  to  {s.nr * t.dr} >= {s.dr * t.nr}')
if  s <= t:
	print(F'{s <= t}  due  to  {s.nr * t.dr} <= {s.dr * t.nr}')
if  s != t:
	print(F'{s != t}  due  to  {s.nr * t.dr} != {s.dr * t.nr}')



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
print(a >= b) # False
print(a <= b) # True


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
print(a == b)  # '_eq_ method  : 10 20  False


# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _eq_(m , n):
		print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # _eq_ method  :  25  25  None
print(a != b) # __eq__ method  :   25 25    True
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
print(a != b) # _ne_ method  : 10 10  False
print(a == b) # True


#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b) # recursion error
a = c1()
b = c1()
print(a > b) # 10 > 20   error



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
a > b # c1  class  __gt__  method :  10 20
a < b # c1  class  __lt__  method :  10 20
m = c2(30)
n = c2(40)
a < m # c1  class  __lt__  method :  10 30
n < b # c2  class  __lt__  method :  40 20


class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		s = c2()
		return  s.noh * x.hr
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		s = c1()
		return  x.noh * s.hr
# End of the class
a = c1()
b = c2()
print(a * b) # __mul__  method  of  class   c1    2000
print(b * a) # __mul__  method  of  class   c2    2000



# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2: # empty  class
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # __add__ method  of  class   c1
print('a + 7 : ' , a + 7) # __add__ method  of  class   c1
print(7 + a) # __add__ method  of  class   c1
print('7 + 8 : ' , 7 + 8) # 15
m = c2() # object  of  class  c2
n = c2()
print(m + n) # TypeError: unsupported operand type(s) for +: 'c2' and 'c2'
print('a + m : ' , a + m) # __add__ method  of  class   c1
print(m + a) # TypeError: unsupported operand type(s) for +: 'c2' and 'c1'



# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  c1(p.x + q.x)
	def __str__(self):
		return  str(self.x)
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) # 30
print('Join : ' , m + n) # 1020



# Write  a  program  to  implement  queue  using  list
class  queue:
        def  __init__(q):
                 # How  to  create  an  empty  queue
                 q.list = []
        def  isempty(q):
                return  True  if q.list  else  False
        def  enqueue(q , x):
                q.list.append(x)
        def  dequeue(q):
                if not q.list:
                        return -1
                q.list.pop(0)
                return q.list
        def  first(q):
                if not q.list:
                        return -1
                return q.list[0]
        def  last(q):
                if not q.list:
                        return -1
                return q.list[-1]
        def  disp(q):
                if not q.list:
                        return -1
                print('Elements  in  the  queue  are : ', q.list)
                print()
        def  size(q):
                return len(q.list)
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
# How  to  create  queue  class  object
q = queue()
menu()
ch = int(input('Enter  choice : ' ))
while ch != 7:
	match ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					q.enqueue(x)
					q.disp()
		case  2:
					x = q.dequeue()
					if x == -1:
						print('Queue is empty')
					else:
						print('Element in queue : ', x)
		case  3:
					q.disp()
		case  4:
					x = q.first()
					if x == -1:
						print('Queue is empty')
					else:
						print('First element is : ', x)
		case  5:
					x = q.last()
					if x == -1:
						print('Queue is empty')
					else:
						print('Last element is : ', x)
		case  6:
					print('Number of elements in the queue is : ', q.size())
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))



'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
import  prog1b #How  to  import  stack  class  from  prog1b  module

s = prog1b.stack() # How  to  create  stack  class  object
str = input("Enter  a  string  :  ") # How  to  read  a  string  into  a  str  object
for  c  in  str: # How  to  push  each  char  of  string  into  the  stack
    s.push(c)
print("Reverse  String :  ", end = "") # printf("Reverse  String :  ");
while  not  s.isempty(): # How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
    print(s.pop(), end = "")



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
def  is_valid_expression(expr):
    s = prog1b.stack()  # Create stack object
    for c in expr:
        if c == '(':
            s.push(c)
        elif c == ')':
            if s.pop() is None:
                print("Invalid expression")
                return
    if s.isempty():
        print("Valid expression")
    else:
        print("Invalid expression")