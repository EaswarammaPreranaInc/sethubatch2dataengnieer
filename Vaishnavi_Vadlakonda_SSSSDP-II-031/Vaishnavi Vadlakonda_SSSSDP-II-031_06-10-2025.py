'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  2 / 3
   Second  rational  number ---> 5 / 9
   What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
   What  is  the  difference  ?  --->  2 / 3 - 5 / 9 = (18 - 15) / 27 =  3 / 27 = 1 / 9
   What  is  the  pro2duct  ?  ---> 2 / 3 * 5 / 9 = 10 / 27 =  10 / 27
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
import math
class Rat:
	def get(self):  #  Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def test(self): #  Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def __add__(self, a , b):  #  Modify  the  method
		self . nr = a . nr * b . dr + a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def __sub__(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr - a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def __mul__(self ,  a , b):   #  Modify  the  method
		self . nr = a . nr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def __truediv__(self, a , b):   #  Modify  the  method
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
c . __add__(a , b)
d . __sub__(a , b)
e .  __mul__(a , b)
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f . __truediv__(a , b)
	print('Division  : ' , f)
else:
	print('Division is not permitted.')
'''
Outputs
Enter  denominator : 3
Enter  numerator : 5
Enter  denominator : 9
Sum :   11 / 9
Difference :   1 / 9
Product :   10 / 27
Division  :  6 / 5
'''









# Is  10 + 20  a  recursion ?  No
class c1:
    def _add_(a , b):
	    print(10 + 20)
a = c1()
b = c1()
print(a + b)
'''
Outputs
30
None
'''

	  

    





# Is  x + y  a  recursion  ?  (Home  work)  yes
class c1:
	def __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
'''
infinite recursion
'''
	  









class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = float(real)
        self.imag = float(imag)

    def get(self):
        self.real = float(input('Enter real part: '))
        self.imag = float(input('Enter imaginary part: '))

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

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
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        a, b = self.real, self.imag
        c, d = other.real, other.imag
        r = Complex()
        r.real = a * c - b * d
        r.imag = a * d + b * c
        return r

    def __truediv__(self, other):
        # (a+bi)/(c+di) = [(ac + bd) + (bc - ad)i] / (c^2 + d^2)
        a, b = self.real, self.imag
        c, d = other.real, other.imag
        denom = c * c + d * d
        if denom == 0:
            raise ZeroDivisionError('Division by zero-complex is not allowed')
        r = Complex()
        r.real = (a * c + b * d) / denom
        r.imag = (b * c - a * d) / denom
        return r

# End of class

# Create objects and read inputs
a = Complex()
b = Complex()
a.get()
b.get()

print('Sum : ', a + b)
print('Difference : ', a - b)
print('Product : ', a * b)
try:
    print('Division : ', a / b)
except ZeroDivisionError as e:
    print('Division :', e)
'''
Outputs
Enter imaginary part: 4
Enter real part: 5
Enter imaginary part: 6
Sum :  8.0 + 10.0i
Difference :  -2.0 - 2.0i
Product :  -9.0 + 38.0i
Division :  0.639344262295082 + 0.03278688524590164i
'''









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
import math

class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero, re-enter: '))

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
# End of class
a = Rat()
b = Rat()
a.get()
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
'''
Outputs
Enter denominator: 3
Enter numerator: 5
Enter denominator: 9
>
>=
!=
'''









# Find  outputs  (Home work)
class c1:
	def _init_(self , y):
		self . x = y
	def _ge_(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10) # a ---> x = 10
b = c1(20) # b ---> x = 20
print(a >= b)
print(a <= b)
'''
Outputs
_ge_ method : 10 20
False
_ge_ method : 20 10
True
'''
	  








# Find  outputs  (Home  work)
class c1:
    def _init_(self , y):
        self . x = y
    def _eq_(m , n):
        print('_eq_ method  : ' , m . x , n . x)
        return  m . x == n . x
#end of the class
a = c1(10) # a ---> x = 10
b = c1(20) # b ---> x = 20
print(a != b)  #  not (a == b)
print(a == b)
'''
Outputs
_eq_ method  : 10 20
True
_eq_ method  : 10 20
False
'''









# Find  outputs  (Home  work)
class c1:
	def _init_(self , y):
	    self . x = y
	def _eq_(m , n):
		print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25) # a ---> x = 25
b = c1(25) # b ---> x = 25
print(a == b) 
print(a != b) # not (a == b)
print(a.x != b.x)
'''
Outputs
_eq_ method  : 25 25
True
_eq_ method  : 25 25
False
_eq_ method  : 25 25
False
'''









# Find  outputs  (Home  work)
class c1:
	def _init_(self , y):
		self . x = y
	def _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10) # a ---> x = 10
b = a # b ---> x = 10
print(a != b)
print(a == b)
'''
Outputs
_ne_ method  : 10 10
False
_ne_ method  : 10 10
True
'''









#  Is  10 > 20  a  recursion ? Yes
class c1:
	def _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a>b)
'''
Outputs
Infinite False
infinite recursion
'''
	  








# Find  outputs  (Home  work)
class c1:
	def _init_(self , y):
		self . x = y
	def _gt_(p , q):
	    print('c1  class  _gt_  method : ' , p . x , q . x)
class c2:
	def _init_(self , y):
		self . x = y
	def _gt_(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x)
#end of the class
a = c1(10) # a ---> x = 10
b = c1(20) # b ---> x = 20
a > b
a < b
m = c2(30) # m ---> x = 30
n = c2(40) # n ---> x = 40
a < m # m > a
n < b # b > n
'''
Outputs
c1  class  _gt_  method : 10 20
c1  class  _gt_  method : 20 10
c2  class  _gt_  method : 30 10 
c2  class  _gt_  method : 20 40
'''









# Overload  *  operator  to  multiply  two  different  class  objects
class c1:
	def _init_(self):
		self . empno = 25
		self . hr = 250
	def _mul_(x , y):
		print('_mul_  method  of  class   c1')
		return  a . empno  * b . noh #hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def _init_(self):
		self . empno = 25
		self . noh = 8
	def _mul_(x , y):
		print('_mul_  method  of  class   c2')
		return  b . empno * b . noh # number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1() # a ---> empno = 25   hr = 250
b = c2() # b ---> empno = 25   noh = 8
print(a * b) 
print(b * a)
'''
Outputs 
_mul_  method  of  class   c1
200
_mul_  method  of  class   c2
200
'''










# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # a + b : _add_ method  of  class   c1
print('a + 7 : ' , a + 7) # a + 7 : _add_ method  of  class   c1
print(7 + a) # Error because can't add int and c1
print('7 + 8 : ' , 7 + 8) # 7 + 8 : 15
m = c2()
n = c2()
print(m + n) # Error cannot add c2 and c2  because there is no __add__ method in c2 class
print('a + m : ' , a + m) # a + m : _add_ method  of  class   c1
print(m + a) # Error cannot add c2 and c1  because there is no __add__ method in c2 class



	  





# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class c1:
	def _init_(self , y):
		self . x = y
	def _add_(p , q):
		return  p.x + q.x # sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10) # a ---> x = 10
b = c1(20) # b ---> x = 20
m = c1('10') # m ---> x = '10'
n = c1('20') # n ---> x = '20'
print('Sum : ' , a + b)
print('Join:',m + n)
'''
Outputs
Sum : 30
Join: '1020'
'''	   









# Write  a  program  to  implement  queue  using  list
class queue:
    def __init__(self):
        self.list = []  # create an empty queue

    def isempty(self):
        return self.list == []  # True when queue is empty

    def enqueue(self, x):
        self.list.append(x)  # insert x into the queue

    def dequeue(self):
        if self.isempty():
            return -1  # deletion not possible
        return self.list.pop(0)  # remove and return first element

    def first(self):
        if self.isempty():
            return -1
        return self.list[0]  # return first element

    def last(self):
        if self.isempty():
            return -1
        return self.list[-1]  # return last element

    def disp(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Queue:", ' '.join(str(x) for x in self.list))

    def size(self):
        return len(self.list)  # number of elements in the queue
def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print queue')
    print('4. First element of queue')
    print('5. Last element of queue')
    print('6. Number of elements in the queue')
    print('7. Exit')


q = queue()  # create queue object
menu()
ch = int(input('Enter choice : '))

while ch != 7:  # repeat until user input is 7
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            q.enqueue(x)
            q.disp()
        case 2:
            deleted = q.dequeue()
            if deleted == -1:
                print("Deletion not possible, queue is empty")
            else:
                print("Deleted element:", deleted)
            q.disp()
        case 3:
            q.disp()
        case 4:
            first_elem = q.first()
            if first_elem == -1:
                print("Queue is empty")
            else:
                print("First element of queue:", first_elem)
        case 5:
            last_elem = q.last()
            if last_elem == -1:
                print("Queue is empty")
            else:
                print("Last element of queue:", last_elem)
        case 6:
            print("Number of elements in queue:", q.size())
        case _:
            print("Invalid choice")

    menu()
    ch = int(input('Enter choice : '))
'''
Outputs
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 1
Enter element to be inserted : 25
Queue: 25
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 1
Enter element to be inserted : 10.8
Queue: 25 10.8
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 1
Enter element to be inserted : 'Hyd'
Queue: 25 10.8 Hyd
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 3
Queue: 25 10.8 Hyd
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 4
First element of queue: 25
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 5
Last element of queue: Hyd
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 6
Number of elements in queue: 3
1. Insertion
2. Deletion
3. Print queue
4. First element of queue
5. Last element of queue
6. Number of elements in the queue
7. Exit
Enter choice : 7
'''









'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                   0     1      2      3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog1b import stack  # How  to  import  stack  class  from  prog1b  module
s = stack() # How  to  create  stack  class  object
input_str = input("Enter string to reverse: ") # How  to  read  a  string  into  a  str  object
for ch in input_str: 
    s.push(ch) # How  to  push  each  char  of  string  into  the  stack
print("Reverse String : ", end='')
while not s.isempty():
    print(s.pop(), end='') # How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
print() 









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

10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog1b import stack   
s = stack()                
a = input("Enter expression: ")
for ch in a:
    if ch == '(':
        s.push('(')         
    elif ch == ')':
        if s.isempty():    
            print("Invalid")
            break
        s.pop()            
else:                       
    if s.isempty():
        print("Valid")
    else:
        print("Invalid")









# Write  a  program  to  implement  stack  using  list
class  stack:
	def  _init_(s):
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
if  _name_  ==  '_main_':
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
			case  6:  
                exit()
		# End  of  match




#Object  's'   --->  list = [25 , 10.8 , 'Hyd']




'''
What  is  the  difference  between  's'  and  s . list ?  --->


's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack  object
'''
