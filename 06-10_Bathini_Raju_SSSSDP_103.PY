# BATHINI RAJU SSSSDP 103
# 06-09-2025

'''Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

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
4) Leave  get() ,  test() , _str_()  and  simplify()  methods  unchanged'''

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
	def  _add_(self, other):  #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other. dr + self . dr * other . nr
		result . dr = self. dr * other . dr
		result . simplify()
		return result
	def  _sub_(self, other):   #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other . dr - self . dr * other . nr
		result . dr = self.dr * other.dr
		result . simplify()
		return result
	def  _mul_(self ,  other):   #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other. nr
		result . dr = self . dr * other . dr
		result . simplify()
		return result
	def  _truediv_(self, other):   #  Modify  the  method
		result = Rat()
		result . nr = self . nr * other . dr
		result . dr = self . dr * other . nr
		result . simplify()
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

c = a + b
print('sum:',c)

d = a - b
print('diffrence:',d)

e = a * b
print('product:',e)

f = a / b
if f is not None:
	print('division:',f)
	
	
# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) 
'''
outputs: 
30
None'''

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
'''
output:
recursion error
'''



'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
Second  rational  number ---> 5 + 6i
What  is  the  sum  ?  --->      8 + 10i
What  is  the  difference  ?  ---> -2 - 2i
What  is  the  product  ?  --->  (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =
'''																																							39 / 61 + 2i / 61

class Complex:
    def _init_(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Method to read real and imaginary parts
    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

    # Display in the form a + bi or a - bi
    def _str_(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    # Addition: (a+bi) + (c+di) = (a+c) + (b+d)i
    def _add_(self, b):
        return Complex(self.real + b.real, self.imag + b.imag)

    # Subtraction: (a+bi) - (c+di) = (a-c) + (b-d)i
    def _sub_(self, b):
        return Complex(self.real - b.real, self.imag - b.imag)

    # Multiplication: (a+bi)*(c+di) = (ac - bd) + (ad + bc)i
    def _mul_(self, b):
        real_part = self.real * b.real - self.imag * b.imag
        imag_part = self.real * b.imag + self.imag * b.real
        return Complex(real_part, imag_part)

    # Division: (a+bi)/(c+di) = [(a+bi)*(c-di)] / (c^2 + d^2)
    def _truediv_(self, b):
        denominator = b.real*2 + b.imag*2
        real_part = (self.real * b.real + self.imag * b.imag) / denominator
        imag_part = (self.imag * b.real - self.real * b.imag) / denominator
        return Complex(real_part, imag_part)
# Create two Complex objects
a = Complex()
b = Complex()
# Read complex numbers into objects
print("Enter 1st complex number:")
a.get()
print("Enter 2nd complex number:")
b.get()
# Perform operations
print("Sum        :", a + b)
print("Difference :", a - b)
print("Product    :", a * b)
print("Division   :", a / b)


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
	def  get(self,numerator =0, denominator =1):
			 self.num = numerator#How  to  read  numerator  and  denominator  into  object
             self.den = denominator
    def  get(self):
            self.num = int(input("Enter numerator :"))
            self.den = int(input("Enter denominator:"))
	def _gt_(self,b):
			return self.num * b.den > b.num * self.den#return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def _lt_(self,b):
			return self.num * b.den < b.num * self.den#return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def _eq_(self,b):
			return self.num * b.den == b.num * self.den#return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def _ge_(self,b):
			return self.num * b.den >= b.num * self.den#return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def _le_(self,b):
			return self.num * b.den <= b.num * self.den#return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def _ne_(self,b):
			return self.num * b.den != b.num * self.den#return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat()
b = Rat()
#Read rational numbers into objects
print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
b.get()
# Perform comparisons
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
'''
output:
_ge_ method : 10 20
False
_ge_ method : 20 10
True
'''

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
print(a != b)  
print(a == b)
'''
output:
_eq_ method : 10 20
True
_eq_ method : 10 20
False
'''


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
'''
output:
_eq_ method : 25 25
None
_eq_ method : 25 25
True
False
'''


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
'''
output:
_ne_ method  :   10 10
False
True
'''


 Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)#False
		print(a > b)#recursion error
a = c1()
b = c1()
print(a > b)#recursion error

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
a > b#'c1 class _gt_ method :',10 20
a < b# 'c1 class _gt_ method :',20 10
m = c2(30)
n = c2(40)
a < m#c2 class _gt_method : 30 10
n < b#c1 class _gt_ method : 20 40

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
'''
output:
_mul_ method of class c1
2000
_mul_ method of class c2
2000'''


# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)#_add_ method of class c1
print('a + 7 : ' , a + 7)#_add_ method of class c1
print(7 + a)#error
print('7 + 8 : ' , 7 + 8)#15
m = c2()
n = c2()
print(m + n)#error
print('a + m : ' , a + m)#_add_ method of class c1
print(m + a)#error


#Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):		
        return p . x + q . x
    def _str_(self):
        return str(self.x)

#end of the class       
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)

# Write  a  program  to  implement  queue  using  list


class  queue:
        def  _init_(q):
                q.items=[]      #How  to  create  an  empty  queue
        def  isempty(q):
                return  len(q.items)==0
        def  enqueue(q , x):
                q.items.append(x)         #How  to  insert  'x'  into  the  queue
        def  dequeue(q):
            if q.isempty():    #How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
                    return -1
            else:
                    return q.items.pop(0)
        def  first(q):
                if q.isempty():
                    return -1
                else:
                    return q.items[0]
        def  last(q):
                if q.isempty():
                        return -1
                else:
                        return q.items[-1]
        def  disp(q):
                print('Queue:',q.items)     #How  to  print  queue
        def  size(q):
                return len(q.items)        #How  to  return  number   of  elements  in  the  queue
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
q=queue()       #How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while  ch!=7:
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					q.enqueue(x)      #How  to  insert  'x'  into  the  queue
					q.disp()      #How  to  print  queue
		case  2:
					deleted=q.dequeue()
                    q=disp()#How  to  print  queue
		case  3:
					q.disp()        #How  to  print  the  queue
		case  4:
					print('First element :', q.first())    #How  to  print  first  element  of  the  queue
		case  5:
					print('Last element :', q.last())       #How  to  print  last  element  of  the  queue
		case  6:
					print('Number of elements :', q.size())     #How  to  print  number  of  elements  in  the  queue
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))
     




----------------------------------------------------------------------------------------------------------------------------------------





Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

# Program 
from prog1b import stack    #How  to  import  stack  class  from  prog1b  module

s=stack()    #How  to  create  stack  class  object

str_input=input('Enter a string:')    #How  to  read  a  string  into  a  str  object
for ch in str_input:
    s.push(ch)          #How  to  push  each  char  of  string  into  the  stack
print("Reverse  String :  ")

while not s.isempty():
    print(s.pop(), end='')          #How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
print()




----------------------------------------------------------------------------------------------------------------------------------------






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


# Program
from prog1b import stack
s = stack()
expr = input('Enter an expression : ')
valid = True
for ch in expr:
    if ch == '(':
        s.push(ch)
    elif ch == ')':
        popped = s.pop()
        if popped is None:
            print('Invalid expression: ")" before "("')
            valid = False
            break
if valid:
    if s.isempty():
        print('Expression is valid')
    else:
        print('Invalid expression: excess "("')

     


----------------------------------------------------------------------------------------------------------------------------



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
			case  6:  exit()
	




#Object  's'   --->  list = [25 , 10.8 , 'Hyd']




'''
What  is  the  difference  between  's'  and  s . list ?  --->


's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack  object
'''