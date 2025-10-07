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
	def  get(self):  
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self): 
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    __str__(self): 
		return  F'{self . nr} / {self . dr}'
	def  __add__(self, a):
		r=Rat()  
		r.nr=self.nr * a.dr + self.dr * a.nr
		r.dr =self.dr * a.dr 
		r.simplify()
		return r
	def  __sub__(self,a):   
		r=Rat()
		r.nr=self.nr * a.dr - self.dr * a.nr
		r.dr=self.dr * a.dr
		r.simplify()
		return r
	def  __mul__(self ,  a ):  
		r=Rat()
		r.nr=self.nr * a.nr
		r.dr=self.dr * a.dr
		r.simplify()
		return r
	def  __truediv__(self, a):   
		r=Rat()
		if a.nr==0:
			print('Division is not possible ')
			return None
		r.nr=self.nr * a.dr
		r.dr=self.dr * a.nr
		r.simplify()
		return r
	def   simplify(self):   
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
a = Rat()
b = Rat()
print('first rational number ')
a.get()
print('second rational number ')
b.get()
c=a+b
d=a-b
e=a*b
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
f=a/b
if f is not None:
	print('Division : ',f) 
    


# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20) # prints 30 and return None to method call
a = c1()
b = c1()
print(a + b)
'''
o/p:
30
None
'''


# Is  x + y  a  recursion  ?  
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		#print(x + y) # recursion error because call's method add repeatedly
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
	What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 39 / 61 + 2i / 61
'''

import  math
class  complex:
	def  get(self):
		self.real=float(input('Enter real part : ')) #  read  real  and  imag
		self.imag=float(input('Enter imaginary part : '))
	def __str__(self):
		if self.imag < 0:
			 return f'{self.real} - {abs(self.imag)}i' #   return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
		else :
			return f'{self.real} + {(self.imag)}i'
	def  __add__(a ,  b):
		r=complex() #   add  objects  a  and  b
		r.real=a.real+b.real
		r.imag=a.imag+b.imag
		return r
	def  __sub__(a ,  b):
		r=complex() #   subtract  objects  a  and  b
		r.real=a.real-b.real
		r.imag=a.imag-b.imag
		return r
	def  __mul__(a ,  b):
		r=complex() # multiply  objects  a  and   b
		r.real=a.real*a.real-a.imag * b.imag
		r.imag=a.real*b.imag+a.imag * b.real
		return r
	def  __truediv__(a ,  b):
		r=complex() # divide  objects   a  and  b
		denominator=b.real**2+b.imag**2
		r.real=(a.real*b.real+a.imag*b.imag)/denominator
		r.imag=(a.imag*b.real-a.real*b.imag)/denominator
		return r
# End  of  the  class
a=complex() 
b=complex() # create  two  complex  class  objects
a.get() #   read   inputs  into  1st  object
b.get() #   read   inputs  into  2nd  object
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a / b)



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
	def  get(self):
			self.nr=int(input('Enter numerator : ')) # How  to  read  numerator  and  denominator  into  object
			self.dr=int(input('Enter denominator : '))
			while self.dr==0:
				self.dr=int(input('Denominator cannot be Zero . Re enter : '))
	def __gt__(self,b):
			return  self.nr*b.dr>self.dr*b.nr # true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return  self.nr*b.dr<self.dr*b.nr # true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return  self.nr*b.dr==self.dr*b.nr # true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return  self.nr*b.dr>=self.dr*b.nr # true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return  self.nr*b.dr<=self.dr*b.nr # true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			return  self.nr*b.dr!=self.dr*b.nr # true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a=Rat()
b=Rat() #  create  two  Rat   class  objects  'a'  and  'b'
a.get() #  read  1st  rational   number  into  object  'a'
b.get() #   read  2nd  rational   number  into  object  'b'
if  a>b: # 1st  rational  is  >  2nd  rational  number
	print('>')
if  a<b: # 1st  rational  is  <  2nd  rational  number
	print('<')
if  a==b: # rational  numbers  are  same
	print('==')
if  a>=b: # 1st  rational  is  >=  2nd  rational  number
	print('>=')
if  a<=b: # 1st  rational  is  <=  2nd  rational  number
	print('<=')
if  a!=b: # rational  numbers  are  different
	print('!=')
	


# Find  outputs 
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10) # constructor is initialized . a.x=10
b = c1(20) # constructor is initialized . b.x=20
print(a >= b)
print(a <= b)
'''
o/p:
__ge__ method :   10 20
False
__ge__ method :   20 10
True
'''


# Find  outputs  
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
o/p:
__eq__ method  :  10 20
True
__eq__ method  :  10 20
False
'''


# Find  outputs  
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
o/p:
__eq__ method  :   25 25
None
__eq__ method  :   25 25
True
False
'''


# Find  outputs  
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
o/p:
__ne__ method  :   10 10
False
True
'''


#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20) # False and return None
		#print(a > b) # recursion : calls itself again and again
a = c1()
b = c1()
print(a > b) # None



# Find  outputs 
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



# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  x.hr*y.noh # hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  x.noh*y.hr # number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)
'''
o/p:
__mul__  method  of  class   c1
2000
__mul__  method  of  class   c2
2000
'''



# Find  outputs  
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
#print(7 + a) # error : type of operand1 plays a key role in execution of method
print('7 + 8 : ' , 7 + 8) # 7 + 8 : 15
m = c2()
n = c2()
#print(m + n) # error
print('a + m : ' , a + m) # a + m :  __add__ method  of  class   c1
#print(m + a) # error



# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def  __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  p.x+q.x # sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)
'''
o/p:
Sum :  30
Join :  1020
'''