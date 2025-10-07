# '''
# Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

# 1) First  rational  number  --->  2 / 3
#    Second  rational  number ---> 5 / 9
#    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
#    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 = (18 - 15) / 27 =  3 / 27 = 1 / 9
#    What  is  the  product  ?  ---> 2 / 3 * 5 / 9 = 10 / 27 =  10 / 27
#    What  is   the  division  ?  ---> 2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

# 2) First  rational  number  --->  2 / 3
#    Second  rational  number ---> 0 / 9
#    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
#     What  is  the  difference  ?  --->  2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3
#    What  is  the  product  ?  ---> 2 / 3 * 0 / 9 =  0 / 27 = 0 / 27  (simplification  is  not  required  becoz  numerator  is  0)
#     What  is   the  division  ?  ---> 2 / 3 /  0 / 9 =  2 / 3 * 0 / 9  --->  Division  is  not  possible  becoz  b . nr  is  0

# 3) Modify  the  following  program  with  operator  overloding  methods

# 4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
# '''
# import  math
# class  Rat:
# 	def  get(self):  #  Do  not  modify  the  method
# 		self . nr = int(input('Enter  numerator : '))
# 		self . dr = int(input('Enter  denominator : '))
# 		self . test()
# 	def  test(self): #  Do  not  modify  the  method
# 		while  self . dr == 0:
# 			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
# 	def    __str__(self):  #  Do  not  modify  the  method
# 		return  F'{self . nr} / {self . dr}'
# 	def ___add___(self, b): #Modify the method
# 		r = Rat()
# 		r.nr = self.nr * b.dr + self.dr * b.nr
# 		r.dr = self.dr * b.dr
# 		r.simplify()
# 		return r
# 	def ___sub___(self, b): #Modify the method
# 		r = Rat()
# 		r.nr = self.nr * b.dr - self.dr * b.nr
# 		r.dr = self.dr * b.dr
# 		r.simplify()
# 		return r
# 	def ___mul___(self, b):  #Modify the method
# 		r = Rat()
# 		r.nr = self.nr * b.nr
# 		r.dr = self.dr * b.dr
# 		r.simplify()
# 		return r
# 	def __truediv__(self, b):   #  Modify  the  method
# 		r = Rat()
# 		r.nr = self.nr * b.dr
# 		r.dr = self.dr * b.nr
# 		r . simplify()
# 		return r
# 	def  simplify(self):   #  Do  not  modify  the  method
# 		if self . nr != 0:
# 			g = math . gcd(self . nr, self . dr)
# 			self . nr = self . nr // g 
# 			self . dr = self . dr // g 
# # End  of  the  class
# #  Modify  the  following  statements
# a = Rat()
# b = Rat()
# a . get()
# b . get()
# c = a + b
# d = a - b
# e = a * b
# print('Sum :  ' , c)
# print('Difference :  ' , d)
# print('Product :  ' ,  e)
# if b . nr != 0:
# 	f = a/b
# 	print('Division  : ' , f)
# else:
# 	print('Division is not permitted.')


# # Is  10 + 20  a  recursion ?  
# # No because 10 + 20 calls the __add__ method of other class int
# class   c1:
# 	def  __add__(a , b):
# 			print(10 + 20)
# a = c1()
# b = c1()
# print(a + b)
	  

# # Is  x + y  a  recursion  ?  (Home  work)
# # Yes, because x + y calls the same class __add__
# class   c1:
# 	def  __add__(a , b):
# 		x = c1()
# 		y = c1()
# 		print(x + y)
# a = c1()
# b = c1()
# print(a + b)
	  


# '''
# Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
# complex  object

# 1) First  rational  number  --->  3 + 4i
#    Second  rational  number ---> 5 + 6i
#    What  is  the  sum  ?  --->      8 + 10i
#    What  is  the  difference  ?  ---> -2 - 2i
#    What  is  the  product  ?  --->  (3 + 4i) * (5 + 6i) =  15 + 18i + 20i - 24 = -9 + 38i
# 	What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =
# 																																									39 / 61 + 2i / 61
# '''
# import  math
# class  complex:
#     def  get(self):
#         #How  to  read  real  and  imag
#         self.real = float(input('Enter the real value'))
#         self.imag = float(input('Enter the imag value'))
#     def    __str__(self):
#         #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
#         return f'{self.real}+{self.imag}i'
#     def __add__(a ,  b):
#         #How  to  add  objects  a  and  b
#         c = complex()
#         c.real = a.real + b.real
#         c.imag = a.imag + b.imag
#         return c
#     def  __sub__(a ,  b):
#         c = complex()
#         c.real = a.real + b.real
#         c.imag = a.imag + b.imag
#         return c
#     def  __mul__(a ,  b):
#     #How  to  multiply  objects  a  and   b
#         c = complex()
#         c.real = a.real * b.real + a.real * b.imag + a.imag * b.real + a.imag * b.imag
#         c.imag = 

#     def  __truediv__(a ,  b):
#     #How  to  divide  objects   a  and  b
# # End  of  the  class
# How  to  create  two  complex  class  objects
# How  to  read   inputs  into  1st  object
# How  to  read   inputs  into  2nd  object
# print('Sum :  ' , ???)
# print('Difference :  ' , ???)
# print('Product :  ' ,  ??)
# print('Division : ', ???)



# '''
# Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

# 1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
#     What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
#     What  is  the  result  of  a < b ?  --->False  due  to  18  is  not  <  15
#     What  is  the  result  of  a == b ?  --->	False  due  to  18  is  not  =  15
#     What  is  the  result  of  a >= b ?  --->	True  due  to 18 >= 15
#     What  is  the  result  of  a <= b ?  ---> 	False  due  to  18  is  not  <=  15
#     What  is  the  result  of  a != b ?  ---> True  due  to 18 != 15

# 2) Imp  point  is  cross  product

# 3) What  is  the  method  call  to  __gt__()  method ?  --->  a > b
#      What  is  the  method  call  to  __lt__()  method ?  ---> a < b
#      What  is  the  method  call  to  __eq__()  method ?  --->  a == b
#      What  is  the  method  call  to  __ge__()  method ?  --->  a >= b
#      What  is  the  method  call  to  __le__()  method ?  --->  a <= b
#      What  is  the  method  call  to  __ne__()  method ?  ---> a != b
# '''
# import  math
# class  Rat:
#     def  get(self):
#         #How  to  read  numerator  and  denominator  into  object
#         self.n = int(input('Enter the numerator:  '))
#         self.d = int(input('Enter the denominator:  '))
#     def __gt__(self,b):
#         #return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
#         return True if self.n * b.d > self.d * b.n else False
#     def __lt__(self,b):
#         #return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
#         return True if self.n * b.d < self.d * b.n else False
#     def __eq__(self,b):
#         #return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
#         return True if self.n * b.d == self.d * b.n else False
#     def __ge__(self,b):
#         #return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
#         return True if self.n * b.d >= self.d * b.n else False
#     def __le__(self,b):
#         #return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
#         return True if self.n * b.d <= self.d * b.n else False
#     def __ne__(self,b):
#         #return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#         return True if self.n * b.d != self.d * b.n else False
# #  End  of   the  class
# # How  to  create  two  Rat   class  objects  'a'  and  'b'
# a = Rat()
# b = Rat()
# # How  to  read  1st  rational   number  into  object  'a'
# a.get()
# # How  to  read  2nd  rational   number  into  object  'b'
# b.get()
# if a > b:
#     print('>')
# if a < b:
#     print('<')
# if a == b:
#     print('==')
# if a >= b:
#     print('>=')
# if a <= b:
#     print('<=')
# if a != b:
#     print('!=')


# # Find  outputs  (Home work)
# class   c1:
# 	def   __init__(self , y):
# 		self . x = y
# 	def    __ge__(m , n):
# 		print('__ge__ method :  ' , m . x , n . x)
# 		return  m . x > n . x
# # End  of  the  class
# a = c1(10)
# b = c1(20)
# print(a >= b)
# print(a <= b)
# '''
# __ge__ method :   10 20
# False
# __ge__ method :   20 10
# True
# '''
	  


# # Find  outputs  (Home  work)
# class   c1:
#         def   __init__(self , y):
#                 self . x = y
#         def    __eq__(m , n):
#                 print('__eq__ method  : ' , m . x , n . x)
#                 return  m . x == n . x
# #end of the class
# a = c1(10)
# b = c1(20)
# print(a != b)  #  not (a == b)
# print(a == b)
# '''
# __eq__ method  :  10 20
# True
# __eq__ method  :  10 20
# False
# '''
	  

# # Find  outputs  (Home  work)
# class   c1:
# 	def   __init__(self , y):
# 		self . x = y
# 	def    __eq__(m , n):
# 		print('__eq__ method  :  ' , m . x , n . x)
# #end of the class
# a = c1(25)
# b = c1(25)
# print(a == b)          #__eq__method: 25 25
# print(a != b)          #False
# print(a.x != b.x)      #False
	  

# # Find  outputs  (Home  work)
# class   c1:
# 	def   __init__(self , y):
# 		self . x = y
# 	def    __ne__(m , n):
# 		print('__ne__ method  :  ' , m . x , n . x)
# 		return  m . x != n . x
# #end of the class
# a = c1(10)
# b = a
# print(a != b)       #False
# print(a == b)       #True
	  


# #  Is  10 > 20  a  recursion ?
# # 10 > 20 is not recursion because it calls int class __gt__
# # but a > b is recursion because it calss same __gt__
# class  c1:
# 	def   __gt__(a , b):
# 		print(10 > 20)
# 		print(a > b)
# a = c1()
# b = c1()
# print(a > b)
	  


# # Find  outputs  (Home  work)
# class  c1:
# 	def __init__(self , y):
# 		self . x = y
# 	def  __gt__(p , q):
# 		print('c1  class  __gt__  method : ' , p . x , q . x)
# class  c2:
# 	def __init__(self , y):
# 		self . x = y
# 	def __gt__(p , q):
# 		print('c2  class  __gt__  method : ' , p . x , q . x)
# #end of the class
# a = c1(10)
# b = c1(20)
# a > b
# a < b
# m = c2(30)
# n = c2(40)
# a < m
# n < b
# '''
# c1  class  __gt__  method :  10 20
# c1  class  __gt__  method :  20 10
# c2  class  __gt__  method :  30 10
# c1  class  __gt__  method :  20 40
# '''



# # Overload  *  operator  to  multiply  two  different  class  objects
# class  c1:
# 	def  __init__(self):
# 		self . empno = 25
# 		self . hr = 250
# 	def __mul__(x , y):
# 		print('__mul__  method  of  class   c1')
# 		#return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
# 		return x.hr * y.noh
# class c2:
# 	def __init__(self):
# 		self . empno = 25
# 		self . noh = 8
# 	def __mul__(x , y):
# 		print('__mul__  method  of  class   c2')
# 		#return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# 		return x.noh * y.hr
# # End of the class
# a = c1()
# b = c2()
# print(a * b)
# print(b * a)
	  


# # Find  outputs  (Home  work)
# class c1:
# 	def __add__(x , y):
# 		return '__add__ method  of  class   c1'
# class c2:
# 	pass
# #end of the class
# a = c1()
# b = c1()
# print('a + b : ' , a + b)    #__add__ method  of  class   c1
# print('a + 7 : ' , a + 7)    #__add__ method  of  class   c1
# # print(7 + a)                 #error, int cannot be added to class c1
# print('7 + 8 : ' , 7 + 8)    #15
# m = c2()
# n = c2()
# # print(m + n)                 #error, no __add__ in class c2
# print('a + m : ' , a + m)    #__add__ method  of  class   c1
# # print(m + a)                 #error, no __add in class c2
	  


# # Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
# class  c1:
# 	def     __init__(self , y):
# 		self . x = y
# 	def __add__(p , q):
# 		#return  sum  of  numbers  (or)  join  of  strings
# 		return p.x + q.x
# #end of the class
# a = c1(10)
# b = c1(20)
# m = c1('10')
# n = c1('20')
# print('Sum : ' , a + b)
# print('Join: ' , m + n)
	  
