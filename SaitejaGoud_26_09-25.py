#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . dict)
s . get()
print(s . dict)
s . compute()
print(s . dict)

# Output :
{}
enter roll no: 25
enter name: Rama Rao
enter gender: m
enter marks: 55
enter marks: 48
enter marks: 58
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'm', 'm': [55, 48, 58]}
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'm', 'm': [55, 48, 58], 'total': 161, 'avg': 53.666666666666664, 'grade': 'Second  Class'}



'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''

# program
from prog9a import student
n=int(input("Enter number of students :"))
a=[]
for i in range(1,n+1):
  s=student()
  print("Student",i)
  s.get()
  s.compute()
  s.append(s)
for x in a:
  print(x)
  
Enter number of students : 4
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


#  dir()  function  demo  program  (Home  work)

from  prog10a   import  Rat

a = Rat()

a . nr = 22

a . dr = 7

print(dir(Rat))

print()

print()

print(dir(a))

# Output :
First Rational Number:
Enter numerator: 2
Enter denominator: 3
Second Rational Number:
Enter numerator: 5
Enter denominator: 9

Results:
Addition: 11 / 9
Subtraction: 1 / 9
Multiplication: 10 / 27
Division: 6 / 5
['_class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'firstlineno', 'format', 'ge', 'getattribute', 'getstate', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'static_attributes', 'str', 'subclasshook', 'weakref_', 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test']


['_class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'firstlineno', 'format', 'ge', 'getattribute', 'getstate', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'static_attributes', 'str', 'subclasshook', 'weakref_', 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test']   


#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))
print(hasattr(a , 'dr'))
print(hasattr(a , 'm1'))
print(hasattr(a , 'm2'))
print(hasattr(Rat , 'm1'))
print(hasattr(Rat , 'm2'))
print(hasattr(Rat , 'nr'))

# Output :
True
False
True
False
True
False
False

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
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

# Output :
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....

#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . dict)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

# Output :
Enter  variable  name  to  be  added  to  object  :  x
Enter  value  of  the  variable  :  20
{'x': 20}
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
Invalid  variable   name   :  y


'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop

# Program
class Emp:
    pass
# End of the class
data = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()
for key, value in data.items():
    setattr(e, key, value)      # set attribute dynamically
for key in data.keys():
    print(key, ":", getattr(e, key))   # get attribute dynamically

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

# Program
from prog10a import Rat       
# Create three objects
a = Rat()
b = Rat()
c = Rat()
print("First Rational Number:")
a.get()
print("Second Rational Number:")
b.get()

# Addition
c.add(a, b)
print("\nAddition :", c)

# Subtraction
c.sub(a, b)
print("Subtraction :", c)

# Multiplication
c.mul(a, b)
print("Multiplication :", c)

# Division
c.div(a, b)
if c.den == 0:          # check division by zero
    print("Division : Not permitted (division by zero)")
else:
    print("Division :", c)


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

# program :
from prog10a import Rat     

# Create a list of 6 objects
a = [Rat() for i in range(6)]   # ---> a[0], a[1], a[2], a[3], a[4], a[5]

# Input
print("First Rational Number:")
a[0].get()
print("Second Rational Number:")
a[1].get()

# Operations
a[2].add(a[0], a[1])   # addition
a[3].sub(a[0], a[1])   # subtraction
a[4].mul(a[0], a[1])   # multiplication
a[5].div(a[0], a[1])   # division

# Output
print("\nResults:")
print("Addition:", a[2])
print("Subtraction:", a[3])
print("Multiplication:", a[4])
if a[5].den == 0:
    print("Division is not permitted")
else:
    print("Division:", a[5])