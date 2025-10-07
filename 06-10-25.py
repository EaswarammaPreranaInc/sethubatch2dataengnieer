#1st program
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
	def  __add__(a , b): #  Modify  the  method
		self=Rat()
		self . nr = a . nr * b . dr + a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
		return self
	def  __sub__(a , b):   #  Modify  the  method
		self=Rat()
		self . nr = a . nr * b . dr - a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
		return self
	def  __mul__( a , b):   #  Modify  the  method
		self=Rat()
		self . nr = a . nr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
		return self
	def  __truediv__(a , b):   #  Modify  the  method
		self=Rat()
		self . nr = a . nr * b . dr
		self . dr = a . dr * b . nr
		self . simplify()
		return self
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
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
if b . nr != 0:
	print('Division  : ' , a/b)
else:
	print('Division is not permitted.')

#2nd program
# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
		print(10 + 20)#30
a = c1()
b = c1()
print(a + b)#none
#It is not a rercursion because + operator is overloaded to print 10+20


#3rd program
# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) #infinite recursion due to line 95 as there class objects are added which inturn calls __add__ again and again

#4th program
'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->      8 + 10i
   What  is  the  difference  ?  ---> -2 - 2i
   What  is  the  product  ?  --->  (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =																																							39 / 61 + 2i / 61
'''

import  math
class  complex:
	def get(self):
		self.x=int(input("enter real part: "))
		self.y=int(input("enter imag part: "))#How  to  read  real  and  imag
	def __str__(self):
		return f"{self.x}+{self.y}i"#How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		#How  to  add  objects  a  and  b
		r=complex()
		r.x=a.x+(b.x)
		r.y=a.y+(b.y)
		return r    
	def  __sub__(a ,  b):
		#How  to  subtract  objects  a  and  b
		r=complex()
		r.x=a.x-(b.x)
		r.y=a.y-(b.y)
		return r 
	def  __mul__(a ,  b):
		#How  to  multiply  objects  a  and   b
		r=complex()
		r.x=a.x*b.x - (a.y*b.y)
		r.y=a.x*b.y + (a.y*b.x)
		return r
	def  __truediv__(a ,  b):
		r=complex()
		r.x= a.x*b.x+(a.y*b.x)+(a.y*b.y)-(a.x*b.y)
		r.y= a**2 + b**2
		return r.x/r.y#How  to  divide  objects   a  and  b
# End  of  the  class
a=complex()
b=complex()#How  to  create  two  complex  class  objects
a.get()#How  to  read   inputs  into  1st  object
b.get()#How  to  read   inputs  into  2nd  object
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)

#6th  program
# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def __ge__(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)#_ge_ method : 10 20  \n False
print(a <= b)#_ge_ method : 20 10 \n True


#7th  program
# Find  outputs  (Home  work)
class   c1:
        def  __init__(self , y):
                self . x = y
        def    __eq__(m , n):
                print('_eq_ method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)  #interpreted as not (a==b)--> _eq_ method : 10 20 \n True 
print(a == b) #_eq_ method : 10 20 \n False


#8th  program
# Find  outputs  (Home  work)
class   c1:
	def __init__(self , y):
		self . x = y
	def __eq__(m , n):
		print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # _eq_ method : 25 25 \n None
print(a != b) # interpreted as not (a==b) --> _eq_ method : 25 25 \n True
print(a . x !=  b . x) #False


#9th  program
# Find  outputs  (Home  work)
class   c1:
	def __init__(self , y):
		self . x = y
	def __ne__(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)
b = a
print(a != b) #_ne_ method : 10 10 \n False
print(a == b) #True  #Here no overlloading method is executed and direct reference comparision  


#10th  program
#  Is  10 > 20  a  recursion ?
class  c1:
	def  __gt__(a , b):
		print(10 > 20) # False
		print(a > b) # recursion of above line print(10>20) occurs until max recursion depth exceeded error
a = c1()
b = c1()
print(a > b)


#11th  program
# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x)
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x)
#end of the class
a = c1(10)
b = c1(20)
a > b # c1 class _gt_ method : 10 20
a < b # c1 class _gt_ method : 20 10
m = c2(30)
n = c2(40)
a < m # c2 class _gt_ method : 30 10 
n < b # c1 class _gt_ method : 20 40 #here c1 class method is executed because the first operand -b  belongs to c1 class

#13th  program
# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)#a+b : _add_ method  of  class   c1
print('a + 7 : ' , a + 7)#a+7 : _add_ method  of  class   c1
#print(7 + a) #error because int class add method is executed and int and c1 cannot be added 
print('7 + 8 : ' , 7 + 8)#7+8 : 15
m = c2()
n = c2()
#print(m + n) #error because there is no add method in c2 class
print('a + m : ' , a + m)#a+m : _add_ method  of  class   c1
#print(m + a)# error because there is no add method in c2 class