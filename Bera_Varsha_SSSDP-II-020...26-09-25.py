# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student  #  Imports  student  class  and  the  if  statement  outside  the  student  class  in  prog9a
s = student()  #  Creates  an  empty  student  class  object
print(s . _dict_) #  {}  :  's'  is  an  empty  object
s . get()  #   Adds  variables  rno , sname ,  gender  and  list  'm'  to  object  's'  with  user   inputs
print(s . _dict_) #  {'rno': 25, 'sname': 'Rama Rao', 'gender': 'm', 'm': [52, 48, 55]}
s . compute() # Adds  variables  tot , avg ,  grade  to  object  's'  with  results
print(s . _dict_)  #  {rno': 25, 'sname': 'Rama Rao', 'gender': 'm', 'm': [52, 48, 55], 'tot': 155, 'avg': 51.66, 'grade': 'Second  class'}


'''
Repeat  student  program  for  'n'  students

1) Reuse  Student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student  #  Imports  student  class  and  the  if  statement  outside  the  student  class  in  prog9a
n = int(input('How  many  students ?  :  '))  #  Read  number  of  students  to   variable  'n'
a = []   #  Empty  list
for  i  in  range(n):  #  Appends  'n'  student  class  objects  to   list  'a'
	s = student()  #  Creates  an  empty  student  class  object
	a . append(s)  #  Appends  object  's'  to list  'a'
i = 1
for  s  in   a:   #  's'  is  each  student  class  object  of  list  'a'
	print(F'Student  {i}')
	s . get()  #   Reads  roll  number , student  name  , gender  and  marks  to   object  's'
	s . compute()  #  Stores  total , average  and  grade  in  object  's'
	i += 1
for  s  in  a:  #  's'  is  each  student  class  object  of  list  'a'
	print(s)  #   __str__()  method  returns  values  of  object  's'  in  the  form  of  string
	
#dir()  function  demo  program  (Home  work)
from  prog10a   import  rat #   imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = rat()  #  Creates  an  empty  rat  class  object
a . nr = 22  #   Adds  variable  nr  to  object  'a'  with  value   22
a . dr = 7  #   Adds  variable  dr  to  object  'a'  with  value   7
print(dir(rat))  #  All  the  method  of  rat  class  i.e.  ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '_str_']
print()
print()
print(dir(a))   #  All  the   variables  of  object  'a'  and  method  of  rat  class  i.e.  ['nr' , 'dr' , 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '_str']#   ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , 'str_']

#  Find  outputs  (Home  work)
class   rat:
	def    m1():
		pass
# End  of  the  class
a = rat() #  Creates  an  empty  rat  class  object
a . nr = 22  # Adds  variable  nr  to  object  'a'  with   value  22
print(hasattr(a , 'nr')) #   True : Variable  'nr'  exists  in  object  'a'
print(hasattr(a , 'dr'))  #   False : Variable  'dr'  does  not  exist  in  object  'a'
print(hasattr(a , 'm1'))  #   True :  Method  'm1'  exists  in  rat  class
print(hasattr(a , 'm2'))  #  False :  Method  'm2'  does  not  exist  in  rat  class
print(hasattr(rat , 'm1'))  #   True :  Method  'm1'  exists  in   rat  class
print(hasattr(rat , 'm2'))  #  False :  Method  'm2'  does  not  exist  in   rat  class
print(hasattr(rat , 'nr'))   #  False :  Method  'nr'  does  not  exist  in  rat  class

# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()] #  List  of  3   objects
for  x  in   a: #  'x'  is  each  object  of  list  'a'
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''

#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()  #  Creates  an  empty  c1  class  object
a . x = 10 #  Adds  variable  'x'  to  object  'a'  with  value  10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)  #  Adds  variable  'y'  to  object  'a'  with  value   20
print(a . _dict_)  #  {'x' : 10 , 'y' : 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')   #  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break


'''
{'x': 10, 'y': 20}
10
10  if  user  input  is  'x'
20  if  user  input  is  'y'
Invalid  variable   name   :  z  if  user  input  is  'z'
'''

'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = emp() #   Creates  an  empty  emp  class  object
for  key , value  in  dict . items(): #   Converts  dict  to  object  'e'
		   setattr(e , key , value)
for  key   in  dict . keys():
	          print(key , getattr(e , key) , sep = '...')


#object  'e'   --->  Empno = 25 , Ename = RamaRao , Sal = 10000.0

'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Reuse   rat  class  defined  in  prog10a  but  do  not  define  rat  class   again
'''
from  prog10a  import  rat  #   imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = rat()  #  Creates  3  empty  rat  class  objects
b = rat()
c = rat()
a . get()  #  Reads  numerator  and  denominator  into   object  'a'
b . get()  #  Reads  numerator  and  denominator  into   object  'b'
c . add(a , b)  #  Adds  rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Addition : {c}') #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
c . sub(a , b)  #  Subtracts  rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Substraction : {c}')  #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
c . mul(a , b)  #  Multiplies   rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Multiplication : {c}')   #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
if  b . nr == 0:
	print('Division  is  not  permitted')
else:
	c . div(a , b)  #  Divides   rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
	print(F'Division : {c}')  #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
	
'''
Repeat  prog10a  with  list  of  6  objects

Hint: Reuse  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from  prog10a  import  rat   #   imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = [rat()  , rat() , rat() , rat() , rat() , rat()]  #  Creates  a  list  of  6  rat  class  objects
a[0] . get()   #  Reads  numerator  and  denominator  into   object  a[0]
a[1] . get()   #  Reads  numerator  and  denominator  into   object  a[1]
a[2] . add(a[0] , a[1]) #  Adds  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[2]
a[3] . sub(a[0] , a[1]) #  Subtracts  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[3]
a[4] . mul(a[0] , a[1]) #  Multiplies  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[4]
print('Sum : ' , a[2])  #   _str_()  method  returns  values  of  object   a[2]  in  the  form  of   string
print('Difference :  ' , a[3])  #   _str_()  method  returns  values  of  object   a[3]  in  the  form  of   string
print('Product :  '  ,  a[4])  #   _str_()  method  returns  values  of  object   a[4]  in  the  form  of   string
if  a[1] . nr == 0:
	print('Division  is  not  permitted')
else:
	a[5] . div(a[0] , a[1])  #  Divides  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[5]
	print('Division :  ' , a[5])  #   _str_()  method  returns  values  of  object   a[5]  in  the  form  of   string