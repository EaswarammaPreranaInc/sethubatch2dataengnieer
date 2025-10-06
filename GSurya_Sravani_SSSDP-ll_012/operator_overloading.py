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
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        self.test()

    def test(self):  # Do not modify the method
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter: '))

    def __str__(self):  # Do not modify the method
        return f'{self.nr} / {self.dr}'

    def __add__(a, b):  # Modify the method
        r = Rat()
        r.nr = a.nr * b.dr + a.dr * b.nr
        r.dr = a.dr * b.dr
        r.simplify()
        return r

    def __sub__(a, b):  # Modify the method
        r = Rat()
        r.nr = a.nr * b.dr - a.dr * b.nr
        r.dr = a.dr * b.dr
        r.simplify()
        return r

    def __mul__(a, b):  # Modify the method
        r = Rat()
        r.nr = a.nr * b.nr
        r.dr = a.dr * b.dr
        r.simplify()
        return r

    def __truediv__(a, b):  # Modify the method
        r = Rat()
        r.nr = a.nr * b.dr
        r.dr = a.dr * b.nr
        r.simplify()
        return r

    def simplify(self):  # Do not modify the method
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g

# End of the class
# Main program
a = Rat()
b = Rat()
a.get()
b.get()

print("Sum is:", a + b)
print("Difference is:", a - b)
print("Product is:", a * b)
if b.nr != 0:
    print("Division is:", a / b)
else:
    print("Division is not permitted.")



# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)#30,no


# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)#error
none


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
		#How  to  read  real  and  imag
                self.x=float(input("enter a real number : ")) #How  to  read   inputs  into  1st  object
                self.y=float(input("enter a imag number : "))
                
	def    __str__(self):
		 #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
                 return F" {self.x} + {self.y}i"
	def  __add__(a ,  b):
		#How  to  add  objects  a  and  b
                c=complex()
                c.x=a.x+b.x
                c.y=a.y+b.y
                return c
	def  __sub__(a ,  b):
		#How  to  subtract  objects  a  and  b
                c=complex()
                c.x=a.x-b.x
                c.y=a.y-b.y
                return c

	def  __mul__(a ,  b):
		#How  to  multiply  objects  a  and   b
                c=complex()
                c.x=a.x*b.x
                c.y=a.y*b.y
                return c

	def  __truediv__(a ,  b):
		#How  to  divide  objects   a  and  b
                c=complex()
                c.x=a.x/b.x
                c.y=a.y/b.y
                return c

# End  of  the  class
a=complex() #How  to  create  two  complex  class  objects
b=complex() 
a.get()
b.get()
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)

enter a real number : 12
enter a imag number : 12
enter a real number : 3
enter a imag number : 4
Sum :    15.0 + 16.0i
Difference :    9.0 + 8.0i
Product :    36.0 + 48.0i
Division  :   4.0 + 3.0i


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
print(a >= b)#__ge__ method :  ' , 10, 20
false
print(a <= b)#__ge__ method :  ' , 20, 10
true






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
print(a != b)  #  not (a == b)__eq__ method  : ' , 10, 20
True
print(a == b)#__eq__ method  : ' , 10, 20
False


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __eq__(m , n):
		print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)#__eq__ method  :  ' 25,25
none
print(a != b)#true
print(a . x !=  b . x)#false



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
print(a != b)#__ne__ method  :  ' , 10,10
False
print(a == b)#true


#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)yes it is recursion

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
a > b#c1  class  __gt__  method : ' , 10 , 20
a < b#c1  class  __gt__  method : ' ,20 , 10
m = c2(30)
n = c2(40)
a < m#error
n < b#error



# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return y.hr*x.noh 
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return x.noh*y.hr
 number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()#
b = c2()
print(a * b)
print(b * a)


# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)#__add__ method  of  class   c1
print('a + 7 : ' , a + 7)#errror
print(7 + a)#error
print('7 + 8 : ' , 7 + 8)#error
m = c2()
n = c2()
print(m + n)#'__add__ method  of  class   c1
print('a + m : ' , a + m)#error
print(m + a)#error


# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return p.x+q.x
#end of the class
a = c1(10)#
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)#
print('Join : ' , m + n)


# Write  a  program  to  implement  queue  using  list
class queue:
    def __init__(q):
        q.list = []  # Create an empty queue

    def isempty(q):
        return q.list == []  # True if queue is empty

    def enqueue(q, x):
        q.list.append(x)  # Insert x into the queue

    def dequeue(q):
        if q.list == []:
            return -1
        else:
            return q.list.pop(0)  # Remove first element and return it

    def first(q):
        if q.list == []:
            return -1
        else:
            return q.list[0]  # Return first element

    def last(q):
        if q.list == []:
            return -1
        else:
            return q.list[-1]  # Return last element

    def disp(q):
        print("Queue:", q.list)  # Print the queue

    def size(q):
        return len(q.list)  # Return number of elements in queue


# End of class

def menu():
    print("\n1. Insertion")
    print("2. Deletion")
    print("3. Print queue")
    print("4. First element of queue")
    print("5. Last element of queue")
    print("6. Number of elements in the queue")
    print("7. Exit")


# --- Main program starts here ---
q = queue()  # ✅ Create queue object

menu()
ch = int(input("Enter choice: "))

while ch != 7:
    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            q.enqueue(x)  # Insert element
            q.disp()

        case 2:
            x = q.dequeue()  # Delete element
            if x == -1:
                print("Queue is empty")
            else:
                print("Deleted element:", x)
            q.disp()

        case 3:
            if q.isempty():
                print("Queue is empty")
            else:
                q.disp()

        case 4:
            x = q.first()
            if x == -1:
                print("Queue is empty")
            else:
                print("First element:", x)

        case 5:
            x = q.last()
            if x == -1:
                print("Queue is empty")
            else:
                print("Last element:", x)

        case 6:
            print("Size is:", q.size())

        case _:
            print("Invalid choice")

    menu()
    ch = int(input("Enter choice: "))

print("Program ended.")
'''
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

from stack import* #How  to  import  stack  class  from  prog1b  module
s=stack()#How  to  create  stack  class  object
x=input("enter a string: ") #How  to  read  a  string  into  a  str  object
s.push(x) #How  to  push  each  char  of  string  into  the  stack
s.disp()
print("Reverse  String :  ");
s.pop(x) #How  to  remove  each  char  of  stack  and  print  until   stack  is  empty







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
# Assume stack class is already imported from prog1b.py
# from prog1b import stack

def is_parentheses_valid(expr):
    s = stack()  # Create a stack object

    for char in expr:
        if char == '(':
            s.push(char)  # Push '(' into the stack
        elif char == ')':
            popped = s.pop()  # Pop '(' from the stack
            if popped is None:
                print(f"Invalid expression: ')' found without matching '('")
                return False

    # End of string reached
    if s.isempty():
        print("Expression is valid.")
        return True
    else:
        print("Invalid expression: '(' left unmatched in stack.")
        return False

# --- Test Cases ---
expressions = [
    "((3 + 4)",         # No
    "(3 * (4 + 5))",    # Yes
    "(3 * (4 + 5))) + 6",  # No
    "3 + 4",            # Yes
    ")3 + 4("           # No
]

for expr in expressions:
    print(f"Expression: {expr}")
    is_parentheses_valid(expr)
    print("-" * 40)


























































