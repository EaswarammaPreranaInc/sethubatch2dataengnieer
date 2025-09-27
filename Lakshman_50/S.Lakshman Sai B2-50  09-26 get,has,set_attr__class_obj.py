
#========================================= #  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)

from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)

#=========================================
'''

Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
# prog9 in 09-25
from prog9 import Student
n=int(input("enter the num: "))
a=[]
for i in range(n):
	s=Student()
	a.append(s)
ctr=1
for x in a:
	print(f'student {ctr}')
	x.get()
	x.compute()
	ctr+=1
for y in a:
	print(y)
#========================================= Enter number of students : 4
'''
Student  1
Enter  roll  number : 111
Enter  student  name : AAA
Enter gender (m/f) : m
Enter  marks  of  subject 1 : 52
Enter  marks  of  subject 2 : 48
Enter  marks  of  subject 3 : 55
Student  2
Enter  roll  number : 222
Enter  student  name : BBB
Enter gender (m/f) : f
Enter  marks  of  subject 1 : 100
Enter  marks  of  subject 2 : 100
Enter  marks  of  subject 3 : 0
Student  3
Enter  roll  number : 333
Enter  student  name : CCC
Enter gender (m/f) : m
Enter  marks  of  subject 1 : 45
Enter  marks  of  subject 2 : 56
Enter  marks  of  subject 3 : 67
Student  4
Enter  roll  number : 444
Enter  student  name : DDD
Enter gender (m/f) : f
Enter  marks  of  subject 1 : 67
Enter  marks  of  subject 2 : 78
Enter  marks  of  subject 3 : 89
111      AAA     m       155.0    51.67          Second class
222      BBB     f       200.0    66.67          Fail
333      CCC     m       168.0    56.00          Second class
444      DDD     f       234.0    78.00          Distinction
'''
#=========================================

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

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''

from  prog10a   import  Rat

a = Rat()
b = Rat()
c = Rat()
a.get()
b.get()
c.add(a,b)
print(f'addtion: {c}')
c.sub(a,b)
print(f'subtraction: {c}')
c.mul(a,b)
print(f'multiplication: {c}')
c.div(a,b)
print(f'divided: {c}')

#=============================================
#  dir()  function  demo  program  (Home  work)
a=Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))

#========================================= #  Find  outputs  (Home  work)

class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))	# True
print(hasattr(a , 'dr'))	#Flase
print(hasattr(a , 'm1'))	#True
print(hasattr(a , 'm2'))	#False
print(hasattr(Rat , 'm1'))	#True
print(hasattr(Rat , 'm2'))	#False
print(hasattr(Rat , 'nr'))	#False

#========================================= # Find  outputs  (Home  work)

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
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''

#========================================= #  Find  outputs  (Home  work)

class    c1:
        pass
# End of the class
a = c1()
a . x = 10
val = eval(input('Enter nuum of values:  '))   #  Assume  that  input  is   20
for i in range(val):
	varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
	value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
	setattr(a , varname , value)
print(a . __dict__)  #{'x': 10, 'y': 20}
print(a . x) 			# 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  c
Invalid variable name : c
'''
#=========================================
'''

(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
e=Emp()
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
# How  to  convert  dictionary  to  object  'e'  with  for  loop
for key,value in dict.items():
	setattr(e,key,value)
# How  to  print  object  'e'  with  for  loop
for key in dict.keys():
	print(key,getattr(e,key),sep='...')

#=========================================

#=========================================
'''

Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''