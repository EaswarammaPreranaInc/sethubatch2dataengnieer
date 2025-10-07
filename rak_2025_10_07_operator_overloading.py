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
# 	def __sub__(self, b): #Modify the method
# 		r = Rat()
# 		r.nr = self.nr * b.dr - self.dr * b.nr
# 		r.dr = self.dr * b.dr
# 		r.simplify()
# 		return r
# 	def __mul__(self, b):  #Modify the method
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


# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)
	  

# # Is  x + y  a  recursion  ?  (Home  work)
# class   c1:
# 	def  __add__(a , b):
# 		x = c1()
# 		y = c1()
# 		print(x + y)
# a = c1()
# b = c1()
# print(a + b)
	  


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
# 	def  get(self):
# 		How  to  read  real  and  imag
# 	def    __str__(self):
# 		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
# 	def  __add__(a ,  b):
# 		How  to  add  objects  a  and  b
# 	def  _sub_(a ,  b):
# 		How  to  subtract  objects  a  and  b
# 	def  _mul_(a ,  b):
# 		How  to  multiply  objects  a  and   b
# 	def  _div_(a ,  b):
# 		How  to  divide  objects   a  and  b
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

# 3) What  is  the  method  call  to  _gt_()  method ?  --->  a > b
#      What  is  the  method  call  to  _lt_()  method ?  ---> a < b
#      What  is  the  method  call  to  _eq_()  method ?  --->  a == b
#      What  is  the  method  call  to  _ge_()  method ?  --->  a >= b
#      What  is  the  method  call  to  _le_()  method ?  --->  a <= b
#      What  is  the  method  call  to  _ne_()  method ?  ---> a != b
# '''
# import  math
# class  Rat:
# 	def  get(self):
# 			 How  to  read  numerator  and  denominator  into  object
# 	def _gt_(self,b):
# 			return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
# 	def _lt_(self,b):
# 			return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
# 	def _eq_(self,b):
# 			return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
# 	def _ge_(self,b):
# 			return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
# 	def _le_(self,b):
# 			return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
# 	def _ne_(self,b):
# 			return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
# #  End  of   the  class
# How  to  create  two  Rat   class  objects  'a'  and  'b'
# How  to  read  1st  rational   number  into  object  'a'
# How  to  read  2nd  rational   number  into  object  'b'
# if  1st  rational  is  >  2nd  rational  number
# 	print('>')
# if  1st  rational  is  <  2nd  rational  number
# 	print('<')
# if  rational  numbers  are  same
# 	print('==')
# if  1st  rational  is  >=  2nd  rational  number
# 	print('>=')
# if  1st  rational  is  <=  2nd  rational  number
# 	print('<=')
# if  rational  numbers  are  different
# 	print('!=')



# # Find  outputs  (Home work)
# class   c1:
# 	def   _init_(self , y):
# 		self . x = y
# 	def    _ge_(m , n):
# 		print('_ge_ method :  ' , m . x , n . x)
# 		return  m . x > n . x
# # End  of  the  class
# a = c1(10)
# b = c1(20)
# print(a >= b)
# print(a <= b)
	  


# # Find  outputs  (Home  work)
# class   c1:
#         def   _init_(self , y):
#                 self . x = y
#         def    _eq_(m , n):
#                 print('_eq_ method  : ' , m . x , n . x)
#                 return  m . x == n . x
# #end of the class
# a = c1(10)
# b = c1(20)
# print(a != b)  #  not (a == b)
# print(a == b)
	  


# # Find  outputs  (Home  work)
# class   c1:
# 	def   _init_(self , y):
# 		self . x = y
# 	def    _eq_(m , n):
# 		print('_eq_ method  :  ' , m . x , n . x)
# #end of the class
# a = c1(25)
# b = c1(25)
# print(a == b)
# print(a != b)
# print(a.x != b.x)
	  

# # Find  outputs  (Home  work)
# class   c1:
# 	def   _init_(self , y):
# 		self . x = y
# 	def    _ne_(m , n):
# 		print('_ne_ method  :  ' , m . x , n . x)
# 		return  m . x != n . x
# #end of the class
# a = c1(10)
# b = a
# print(a != b)
# print(a == b)
	  


# #  Is  10 > 20  a  recursion ?
# class  c1:
# 	def   _gt_(a , b):
# 		print(10 > 20)
# 		print(a > b)
# a = c1()
# b = c1()
# print(a > b)
	  


# # Find  outputs  (Home  work)
# class  c1:
# 	def _init_(self , y):
# 		self . x = y
# 	def  _gt_(p , q):
# 		print('c1  class  _gt_  method : ' , p . x , q . x)
# class  c2:
# 	def _init_(self , y):
# 		self . x = y
# 	def _gt_(p , q):
# 		print('c2  class  _gt_  method : ' , p . x , q . x)
# #end of the class
# a = c1(10)
# b = c1(20)
# a > b
# a < b
# m = c2(30)
# n = c2(40)
# a < m
# n < b



# # Overload  *  operator  to  multiply  two  different  class  objects
# class  c1:
# 	def  _init_(self):
# 		self . empno = 25
# 		self . hr = 250
# 	def _mul_(x , y):
# 		print('_mul_  method  of  class   c1')
# 		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
# class c2:
# 	def _init_(self):
# 		self . empno = 25
# 		self . noh = 8
# 	def _mul_(x , y):
# 		print('_mul_  method  of  class   c2')
# 		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
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
# print('a + b : ' , a + b)
# print('a + 7 : ' , a + 7)
# print(7 + a)
# print('7 + 8 : ' , 7 + 8)
# m = c2()
# n = c2()
# print(m + n)
# print('a + m : ' , a + m)
# print(m + a)
	  


# # Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
# class  c1:
# 	def     _init_(self , y):
# 		self . x = y
# 	def __add__(p , q):
# 		return  sum  of  numbers  (or)  join  of  strings
# #end of the class
# a = c1(10)
# b = c1(20)
# m = c1('10')
# n = c1('20')
# print('Sum : ' , a + b)
# print('Join: ' , m + n)
	  


# # Write  a  program  to  implement  queue  using  list
# class  queue:
#         def  _init_(q):
#                  How  to  create  an  empty  queue
#         def  isempty(q):
#                 return  True  when  queue  is  empty  and  False  otherwise
#         def  enqueue(q , x):
#                 How  to  insert  'x'  into  the  queue
#         def  dequeue(q):
#                 How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
# 				(return  -1  when  deletion  is  not  possible)
#         def  first(q):
#                 How  to  return  the  first  element  of  the  queue
# 				(return  -1  when  queue  is  empty)
# 		def  last(q):
#                 How  to  return  the  first  element  of  the  queue
# 				(return   -1  when  queue  is  empty)
#         def  disp(q):
#                 How  to  print  queue
#         def  size(q):
#                 How  to  return  number   of  elements  in  the  queue
# # End  of  the  class
# def  menu():
#         print('1. Insertion')
#         print('2. Deletion')
#         print('3. Print  queue')
#         print('4. First  element of queue')
#         print('5. Last  element of queue')
#         print('6. Number  of  elements  in  the  queue')
#         print('7. Exit')
# # End of  the  function
# How  to  create  queue  class  object
# menu()
# ch = int(input('Enter  choice : ' ))
# while  repeat  until  user  input  is  7
# 	match  ch:
# 		case  1:
# 					x = eval(input('Enter  element  to  be  inserted : '))
# 					How  to  insert  'x'  into  the  queue
# 					How  to  print  queue
# 		case  2:
# 					How  to  delete  queue  element  and  print  the  deleted  element
# 					How  to  print  queue
# 		case  3:
# 					How  to  print  the  queue
# 		case  4:
# 					How  to  print  first  element  of  the  queue
# 		case  5:
# 					How  to  print  last  element  of  the  queue
# 		case  6:
# 					How  to  print  number  of  elements  in  the  queue
# 	# End  of  match
# 	menu()
# 	ch = int(input('Enter choice: '))



# '''
# Write  a  program  to  reverse  a  string  using  stack

# str  object  --->  R     A      M      A
#                            0     1       2       3

# Stack   --->

# Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
# '''
# How  to  import  stack  class  from  prog1b  module
# How  to  create  stack  class  object
# How  to  read  a  string  into  a  str  object
# How  to  push  each  char  of  string  into  the  stack
# printf("Reverse  String :  ");
# How  to  remove  each  char  of  stack  and  print  until   stack is empty



# '''
# Write  a  program  to  perform  parentheses  match

# 1) Is  ((3 + 4)  valid ?  ---> No  due  to  excess  (

# 2) Is  (3 * (4 + 5))  valid ?  --->  Yes

# 3) Is  (3 * (4 + 5))) + 6 valid ? --->No  due  to  excess  ')'

# 4) Is  3 + 4  valid ? --->  Yes

# 5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (

# 6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack

# 7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack

# 8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  invalid  msg  and  stop  execution

# 9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->
# 																						Print  valid  msg  when  stack  is   empty  and  invalid  otherwise

# 10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not rewrite
# '''




# # Write  a  program  to  implement  stack  using  list
# class  stack:
# 	def  _init_(s):
# 		s . list = []   #  How  to  create  an  empty  stack
# 	def  isempty(s):
# 		return  s . list ==  []   #  return  True  when  stack  is  empty  and  False  otherwise
# 	def  push(s , x):
# 		s . list . append(x)  #  How  to  insert  'x'  into  the  stack
# 	def  pop(s):
# 		try:
# 			return  s . list . pop()  #  How  to  delete  last  element  of  the  stack  and  return  the  deleted  element
# 		except:
# 			return  None  #  return  None  when  deletion  is  not  possible
# 	def  peek(s):
# 		try:
# 			return  s . list[-1]  #   How  to  return  the  last  element  of  the  stack
# 		except:
# 			return  None
# 	def  disp(s):
# 		print('Stack :  ' , s . list)  #  How  to  print  stack
# 	def   size(s):
# 		return  len(s . list) #   How  to  return  number   of  elements  in  the  stack
# # End  of  the  class
# def  menu():
#         print('1. Insertion')
#         print('2. Deletion')
#         print('3. Print  Stack')
#         print('4. Last  element of stack')
#         print('5. Number  of  elements  in  the  stack')
#         print('6. Exit')
# # End of  the  function
# if  _name_  ==  '_main_':
# 	s = stack()   #  How  to  create  stack  class  object
# 	while  True:
# 		menu()
# 		ch = int(input('Enter  choice : ' ))
# 		match  ch:
# 			case  1:
# 						x = eval(input('Enter  element  to  be  inserted : '))
# 						s . push(x)   #  How  to  insert  'x'  into  the  stack
# 						s . disp()   #  How  to  print  stack
# 			case  2:
# 						x = s . pop() #  How  to  delete  stack  element  and  print  the  deleted  element
# 						if  x  ==  None:
# 							print('Stack  is  empty  , deletion  is  not  permitted')
# 						else:
# 							print('Deleted  element : '  , x)
# 						s . disp()  #   How  to  print  stack
# 			case  3:
# 						s . disp() #   How  to  print  the  stack
# 			case  4:
# 						x = s . peek()  #  How  to  print  last  element  of  the  stack
# 						if  x == None:
# 							print('Stack  is  empty')
# 						else:
# 							print('Last  element :  ' , x)
# 			case  5:
# 						print('Number  of  elements  :  ' ,  s . size())   #  How  to  print  number  of  elements  in  the  stack
# 			case  6:  exit()
# 		# End  of  match




# #Object  's'   --->  list = [25 , 10.8 , 'Hyd']




# '''
# What  is  the  difference  between  's'  and  s . list ?  --->


# 's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack object
# '''
