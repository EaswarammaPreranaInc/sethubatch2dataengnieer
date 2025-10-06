: '''
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

4) Leave  get() ,  test() , str()  and  simplify()  methods  unchanged
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
	def    str(self):  #  Do  not  modify  the  method
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


###########################
import math

class Rat:
    def get(self):  # Do not modify
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        self.test()

    def test(self):  # Do not modify
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero, re-enter: '))

    def _str_(self):  # Do not modify
        return f'{self.nr} / {self.dr}'

    # Overloaded + operator
    def _add_(self, other):
        result = Rat()
        result.nr = self.nr * other.dr + self.dr * other.nr
        result.dr = self.dr * other.dr
        result.simplify()
        return result

    # Overloaded - operator
    def _sub_(self, other):
        result = Rat()
        result.nr = self.nr * other.dr - self.dr * other.nr
        result.dr = self.dr * other.dr
        result.simplify()
        return result

    # Overloaded * operator
    def _mul_(self, other):
        result = Rat()
        result.nr = self.nr * other.nr
        result.dr = self.dr * other.dr
        result.simplify()
        return result

    # Overloaded / operator
    def _truediv_(self, other):
        result = Rat()
        if other.nr == 0:
            print('Division is not permitted (denominator numerator is zero).')
            return None
        result.nr = self.nr * other.dr
        result.dr = self.dr * other.nr
        result.simplify()
        return result

    def simplify(self):  # Do not modify
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g


# --- Main program ---
a = Rat()
b = Rat()

print('\nEnter first rational number:')
a.get()
print('\nEnter second rational number:')
b.get()

print('\nFirst Rational:', a)
print('Second Rational:', b)

c = a + b
print('Sum:', c)

d = a - b
print('Difference:', d)

e = a * b
print('Product:', e)

f = a / b
if f:
    print('Division:', f)






: # Is  10 + 20  a  recursion ?
class   c1:
	def  add(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)

#### 30
Conclusion:
10 + 20 is not recursion, because it is a simple arithmetic addition, not a call to the same overloaded operator again.



: # Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  add(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)

####################
Hence, it calls itself infinitely, leading to infinite recursion (until Python stops it with an error).

 Error produced:

RecursionError: maximum recursion depth exceeded


 Conclusion:
x + y is recursion, because it calls the same overloaded operator (_add_) again inside itself.





: '''
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
		How  to  read  real  and  imag
	def    str(self):
		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  add(a ,  b):
		How  to  add  objects  a  and  b
	def  sub(a ,  b):
		How  to  subtract  objects  a  and  b
	def  mul(a ,  b):
		How  to  multiply  objects  a  and   b
	def  div(a ,  b):
		How  to  divide  objects   a  and  b
# End  of  the  class
How  to  create  two  complex  class  objects
How  to  read   inputs  into  1st  object
How  to  read   inputs  into  2nd  object
print('Sum :  ' , ???)
print('Difference :  ' , ???)
print('Product :  ' ,  ??)
print('Division  : ' , ???)
#######################
class Complex:
    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

    def _str_(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    # Overload +
    def _add_(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        return result

    # Overload -
    def _sub_(self, other):
        result = Complex()
        result.real = self.real - other.real
        result.imag = self.imag - other.imag
        return result

    # Overload *
    def _mul_(self, other):
        result = Complex()
        result.real = self.real * other.real - self.imag * other.imag
        result.imag = self.real * other.imag + self.imag * other.real
        return result

    # Overload /
    def _truediv_(self, other):
        result = Complex()
        denom = other.real*2 + other.imag*2
        if denom == 0:
            print("Division not possible (denominator is zero).")
            return None
        result.real = (self.real * other.real + self.imag * other.imag) / denom
        result.imag = (self.imag * other.real - self.real * other.imag) / denom
        return result


# --- Main program ---
a = Complex()
b = Complex()

print("Enter first complex number:")
a.get()
print("Enter second complex number:")
b.get()

print("\nFirst Complex Number:", a)
print("Second Complex Number:", b)

c = a + b
print("Sum:", c)

d = a - b
print("Difference:", d)

e = a * b
print("Product:", e)

f = a / b
if f:
    print("Division:", f)




: '''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  --->False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  --->	False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  --->	True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  ---> 	False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  ---> True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  gt()  method ?  --->  a > b
     What  is  the  method  call  to  lt()  method ?  ---> a < b
     What  is  the  method  call  to  eq()  method ?  --->  a == b
     What  is  the  method  call  to  ge()  method ?  --->  a >= b
     What  is  the  method  call  to  le()  method ?  --->  a <= b
     What  is  the  method  call  to  ne()  method ?  ---> a != b
'''
import  math
class  Rat:
	def  get(self):
			 How  to  read  numerator  and  denominator  into  object
	def gt(self,b):
			return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def lt(self,b):
			return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def eq(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def ge(self,b):
			return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def le(self,b):
			return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def ne(self,b):
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

###########################
import math

class Rat:
    def get(self):
        self.nr = int(input("Enter numerator: "))
        self.dr = int(input("Enter denominator: "))
        while self.dr == 0:
            self.dr = int(input("Denominator cannot be zero, re-enter: "))

    def _str_(self):
        return f"{self.nr} / {self.dr}"

    # Overload >
    def _gt_(self, b):
        return self.nr * b.dr > b.nr * self.dr

    # Overload <
    def _lt_(self, b):
        return self.nr * b.dr < b.nr * self.dr

    # Overload ==
    def _eq_(self, b):
        return self.nr * b.dr == b.nr * self.dr

    # Overload >=
    def _ge_(self, b):
        return self.nr * b.dr >= b.nr * self.dr

    # Overload <=
    def _le_(self, b):
        return self.nr * b.dr <= b.nr * self.dr

    # Overload !=
    def _ne_(self, b):
        return self.nr * b.dr != b.nr * self.dr


# --- Main Program ---
a = Rat()
b = Rat()

print("Enter first rational number:")
a.get()
print("Enter second rational number:")
b.get()

print("\nFirst Rational:", a)
print("Second Rational:", b)
print()

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





: # Find  outputs  (Home work)
class   c1:
	def   init(self , y):
		self . x = y
	def    ge(m , n):
		print('ge method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)
##############
prints: _ge_ method : 10 20
returns: 10 > 20 → False
so prints False


print(a <= b)
###############
prints: _ge_ method : 20 10
returns: 20 > 10 → True
so prints True



: # Find  outputs  (Home  work)
class   c1:
        def   init(self , y):
                self . x = y
        def    eq(m , n):
                print('eq method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  #  not (a == b)
print(a == b)
#############
_eq_ method : 10 20
True
_eq_ method : 10 20
False





: # Find  outputs  (Home  work)
class   c1:
	def   init(self , y):
		self . x = y
	def    eq(m , n):
		print('eq method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)
###############
_eq_ method : 25 25
False
_eq_ method : 25 25
True
False




: # Find  outputs  (Home  work)
class   c1:
	def   init(self , y):
		self . x = y
	def    ne(m , n):
		print('ne method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b)
print(a == b)
################
_ne_ method : 10 10
False
True




: #  Is  10 > 20  a  recursion ?
class  c1:
	def   gt(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)### False





: # Find  outputs  (Home  work)
class  c1:
	def init(self , y):
		self . x = y
	def  gt(p , q):
		print('c1  class  gt  method : ' , p . x , q . x)
class  c2:
	def init(self , y):
		self . x = y
	def gt(p , q):
		print('c2  class  gt  method : ' , p . x , q . x)
#end of the class
a = c1(10)
b = c1(20)
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
#####################
Problems:

Method names should be _init_ and _gt_ (not single underscore).

No < method (_lt_), so Python will give TypeError for < operations.

Corrected & Working Version:

class c1:
	def _init_(self , y):
		self.x = y
	def _gt_(p , q):
		print('c1 class _gt_ method :', p.x, q.x)
		return p.x > q.x

class c2:
	def _init_(self , y):
		self.x = y
	def _gt_(p , q):
		print('c2 class _gt_ method :', p.x, q.x)
		return p.x > q.x

a = c1(10)
b = c1(20)
print(a > b)  # Calls c1 _gt_
m = c2(30)
n = c2(40)
print(m > n)  # Calls c2 _gt_





: # Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  init(self):
		self . empno = 25
		self . hr = 250
	def mul(x , y):
		print('mul  method  of  class   c1')
		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def init(self):
		self . empno = 25
		self . noh = 8
	def mul(x , y):
		print('mul  method  of  class   c2')
		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)### # calls c1._mul_

print(b * a) ### # calls c2._mul_ 
##########
_mul_ method of class c1
2000
_mul_ method of class c2
2000



: # Find  outputs  (Home  work)
class c1:
	def add(x , y):
		return 'add method  of  class   c1'
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

##################
Output Explanation:

a + b → calls c1._add_ →  prints _add_ method of class c1

a + 7 → also calls same →  prints _add_ method of class c1

7 + a → error →  TypeError (int has no _add_ for c1)

7 + 8 →  15

m + n →  TypeError (c2 has no _add_)

a + m →  calls c1’s _add_

m + a →  TypeError (c2 has no _add_)






: # Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     init(self , y):
		self . x = y
	def add(p , q):
		return  sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) ### 30
print('Join : ' , m + n) ### 1020



: # Write  a  program  to  implement  queue  using  list
class  queue:
        def  init(q):
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

###################
# Queue implementation using list
class queue:
    def _init_(q):                                  # create empty queue
        q.data = []

    def isempty(q):                                   # check empty or not
        return len(q.data) == 0

    def enqueue(q, x):                                # insert element
        q.data.append(x)

    def dequeue(q):                                   # delete first element
        if q.isempty():
            return -1
        else:
            return q.data.pop(0)

    def first(q):                                     # return first element
        if q.isempty():
            return -1
        else:
            return q.data[0]

    def last(q):                                      # return last element
        if q.isempty():
            return -1
        else:
            return q.data[-1]

    def disp(q):                                      # display queue
        if q.isempty():
            print("Queue is empty")
        else:
            print("Queue :", q.data)

    def size(q):                                      # number of elements
        return len(q.data)


# Menu function
def menu():
    print("\n1. Insertion")
    print("2. Deletion")
    print("3. Print queue")
    print("4. First element of queue")
    print("5. Last element of queue")
    print("6. Number of elements in the queue")
    print("7. Exit")


# --- Main Program ---
q = queue()       # create queue object

menu()
ch = int(input("Enter choice : "))

while ch != 7:
    match ch:
        case 1:
            x = eval(input("Enter element to be inserted : "))
            q.enqueue(x)
            q.disp()

        case 2:
            val = q.dequeue()
            if val == -1:
                print("Deletion not possible (queue empty)")
            else:
                print("Deleted element :", val)
            q.disp()

        case 3:
            q.disp()

        case 4:
            val = q.first()
            if val == -1:
                print("Queue is empty")
            else:
                print("First element :", val)

        case 5:
            val = q.last()
            if val == -1:
                print("Queue is empty")
            else:
                print("Last element :", val)

        case 6:
            print("Number of elements in queue :", q.size())

        case _:
            print("Invalid choice!")

    menu()
    ch = int(input("Enter choice : "))

print("Program terminated.")







: '''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
How  to  import  stack  class  from  prog1b  module
How  to  create  stack  class  object
How  to  read  a  string  into  a  str  object
How  to  push  each  char  of  string  into  the  stack
printf("Reverse  String :  ");
How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
####################
# Reuse stack class from prog1b.py
from prog1b import stack   #  import stack class

# create stack object
s = stack()

# read input string
st = input("Enter a string : ")

# push each character into stack
for ch in st:
    s.push(ch)

print("Reverse String : ", end="")

# pop and print each character until stack is empty
while not s.isempty():
    print(s.pop(), end="")

print()   # for newline





: '''
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
###########################
# Reuse stack class from prog1b.py
from prog1b import stack   #  import stack class

# create stack object
s = stack()

expr = input("Enter an expression : ")

valid = True

for ch in expr:
    if ch == '(':                   # push on '('
        s.push(ch)
    elif ch == ')':                 # pop on ')'
        val = s.pop()
        if val is None:             # nothing to pop → invalid
            print("Invalid: extra ')' found")
            valid = False
            break

# after scanning string
if valid:
    if s.isempty():
        print("Valid expression")
    else:
        print("Invalid: extra '(' found")






: # Write  a  program  to  implement  stack  using  list
class  stack:
	def  init(s):
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
if  name  ==  'main':
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
'''
