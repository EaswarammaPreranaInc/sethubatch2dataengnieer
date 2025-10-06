'''#1. Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects
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
		c = Rat()
		c . nr = a . nr * b . dr + a . dr * b . nr
		c . dr = a . dr * b . dr
		c . simplify()
		return c
	def  __sub__( a , b):   #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . dr - a . dr * b . nr
		c . dr = a . dr * b . dr
		c . simplify()
		return c
	def  __mul__( a , b):   #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . nr
		c . dr = a . dr * b . dr
		c . simplify()
		return c
	def  __truediv__( a , b):   #  Modify  the  method
		c = Rat()
		c . nr = a . nr * b . dr
		c . dr = a . dr * b . nr
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
a . get()
b . get()
print('Sum :  ' , a + b)
print('Difference :  ', a - b)
print('Product :  ' , a * b)
if b . nr != 0:
	print('Division  : ' , a / b)
else:
	print('Division is not permitted.')







#2. Is  10 + 20  a  recursion ? No
class   c1:
	def  __add__(a , b):
			print(10 + 20) # 30
a = c1()
b = c1()
print(a + b) # None





#3. Is  x + y  a  recursion  ? Yes (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
# RecursionError





#4. Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object
import  math
class  complex:
	def  get(self):
		self.x = float(input("Enter real part : ")) # How  to  read  real  and  imag
		self.y = float(input("Enter imag part : "))
	def    __str__(self):
		if self.i > 0:
			return f'{self.r} + {self.i}'
		else:
			return f'{self.r} - {self.i}'# How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		c = complex()
		c.r = a.x + b.x
		c.i = a.y + b.y # How  to  add  objects  a  and  b
		return c
	def  __sub__(a ,  b):
		c = complex()
		c.r = a.x - b.x
		c.i = a.y - b.y # How  to  subtract  objects  a  and  b
		return c
	def  __mul__(a ,  b):
		c = complex()
		c.r = a.x * b.x - a.y * b.y
		c.i = a.x * b.y + b.x * a.y # How  to  multiply  objects  a  and   b
		return c
	def  __truediv__(a ,  b):
		c = complex()
		den = b.x**2 + b.y**2  
		c.r = (a.x * b.x + a.y * b.y) / den
		c.i = (a.y * b.x - a.x * b.y) / den # How  to  divide  objects   a  and  b
		return c
# End  of  the  class
a = complex()
b = complex() # How  to  create  two  complex  class  objects
a.get() # How  to  read   inputs  into  1st  object
b.get() # How  to  read   inputs  into  2nd  object
print('Sum :  ' , a + b)
print('Difference :  ' , a - b)
print('Product :  ' ,  a * b)
print('Division  : ' , a / b)





#5. Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

import  math
class  Rat:
	def  get(self):
			self.x = int(input("Enter Numerator :")) 
			self.y =  int(input("Enter Denominator :")) # How  to  read  numerator  and  denominator  into  object
	def __gt__(self,b):
			return  (a.x * b.y) > (a.y * b.x) # true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return (a.x * b.y) < (a.y * b.x) # true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return (a.x * b.y) == (a.y * b.x) # true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return (a.x * b.y) >= (a.y * b.x) # true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return (a.x * b.y) <= (a.y * b.x) # true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			return (a.x * b.y) != (a.y * b.x) # true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat()
b = Rat() # How  to  create  two  Rat   class  objects  'a'  and  'b'
a.get() # How  to  read  1st  rational   number  into  object  'a'
b.get() # How  to  read  2nd  rational   number  into  object  'b'
if  a > b: # 1st  rational  is  >  2nd  rational  number
	print('>')
if  a < b: # 1st  rational  is  <  2nd  rational  number
	print('<')
if  a == b: # rational  numbers  are  same
	print('==')
if  a >= b: # 1st  rational  is  >=  2nd  rational  number
	print('>=')
if  a <= b: # 1st  rational  is  <=  2nd  rational  number
	print('<=')
if  a != b: # rational  numbers  are  different
	print('!=')





#6. Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b) # __ge__ method :   10 20 <nextline> False
print(a <= b) # __ge__ method :   20 10 <nextline> True





#7. Find  outputs  (Home  work)
class   c1:
        def   __init__(self , y):
                self . x = y
        def    __eq__(m , n):
                print('__eq__ method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  #  not (a == b) # __eq__ method  :  10 20 <nextline> True
print(a == b) # __eq__ method  :  10 20 <netxline> False





#8. Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __eq__(m , n):
		print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # __eq__ method  :   25 25 <nextline> None
print(a != b) # __eq__ method  :   25 25 <nextline> True
print(a . x !=  b . x) # False




#9. Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b) # __ne__ method  :   10 10 <nextline> False
print(a == b) # True





#10. Is  10 > 20  a  recursion ? Yes
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)
# RecursionError





#11. Find  outputs  (Home  work)
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
a > b # c1  class  __gt__  method :  10 20
a < b # c1  class  __gt__  method :  20 10
m = c2(30)
n = c2(40)
a < m # c2  class  __gt__  method :  30 10
n < b # c1  class  __gt__  method :  20 40





#12. Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # a + b :  __add__ method  of  class   c1
print('a + 7 : ' , a + 7) # a + 7 :  __add__ method  of  class   c1
#print(7 + a) # Error
print('7 + 8 : ' , 7 + 8) # 7 + 8 :  15
m = c2()
n = c2()
#print(m + n) # Error
#print('a + m : ' , a + m)
#print(m + a) # Error





#13. Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return p.x + q.x # sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) # Sum : 30
print('Join : ' , m + n) # Join : 1020




#14. Write  a  program  to  implement  queue  using  list
class  queue:
    def  __init__(q):
        q.list = [] # How  to  create  an  empty  queue
    def  isempty(q):
        return q.list == [] # True  when  queue  is  empty  and  False  otherwise
    def  enqueue(q , x):
        q.list.append(x) # How  to  insert  'x'  into  the  queue
    def  dequeue(q):
        try:
            return q.list.pop(0) # How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
        except:
            return None
            # (return None  when  deletion  is  not  possible)
    def  first(q):
        try:
            return q.list[0] # How  to  return  the  first  element  of  the  queue
        except:
            return None # 	(return  -1  when  queue  is  empty)
    def  last(q):
        try:
            return q.list[-1] # How  to  return  the  first  element  of  the  queue
        except:
            return None	#	(return   -1  when  queue  is  empty)
    def  disp(q):
        return q.list # How  to  print  queue
    def  size(q):
        return len(q.list) # How  to  return  number   of  elements  in  the  queue
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
q = queue() # How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while  ch != 7:
    match  ch:
        case  1:
            x = eval(input('Enter  element  to  be  inserted : '))
            q.enqueue(x) # How  to  insert  'x'  into  the  queue
            print("Queue : " ,q.list) # How  to  print  queue
        case  2:
            h = q.dequeue() # How  to  delete  queue  element  and  print  the  deleted  element
            if h == None:
                print("Queue is empty, deletion is not possible") 
            else:
                print("Deleted element : ",h)
            print("Queue : ", q.list) # How  to  print  queue
        case  3:
            print("Queue : " ,q.list) # How  to  print  the  queue
        case  4:
            h = q.first() # How  to  print  first  element  of  the  queue
            if h == None:
                print("Queue is empty") 
            else:
                print("First element : ",h)
        case  5:
            h = q.last() # How  to  print  last  element  of  the  queue
            if h == None:
                print("Queue is empty") 
            else:
                print("Last element : ",h)
        case  6:
            print("Number of elements in queue : ", q.size()) # How  to  print  number  of  elements  in  the  queue
    # End  of  match
    menu()
    ch = int(input('Enter  choice : ' ))






#15. Write  a  program  to  reverse  a  string  using  stack
from Stack import stack # How  to  import  stack  class  from  prog1b  module
a = stack() # How  to  create  stack  class  object
k = ''
str = input("Enter a string : ") # How  to  read  a  string  into  a  str  object
for i in str:
    a.push(i) # How  to  push  each  char  of  string  into  the  stack
for i in range(a.size()):
    try:
        k += a.pop()
    except:
        break # How  to  remove  each  char  of  stack  and  print  until   stack is empty
print("Reverse  String :  ", k)


'''



#16. Write  a  program  to  perform  parentheses  match
from Stack import stack
a = stack()
exp = input("Enter a Expression : ")
for i in exp:
    if a.list == [] and i == ')':
        print("Invalid")
        exit()
    elif i == '(':
        a.push(i)
    elif i == ')':
        k = a.pop()
        if k == None:
            print("invalid")
            exit()
        else:
            continue
    else:
        continue
if a.list == []:
    print("Valid")
else:
    print("Invalid")