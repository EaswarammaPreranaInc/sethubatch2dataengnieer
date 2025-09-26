#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)#{}
s . get()
print(s . _dict_)#{'rno':25,'sname':Rama Rao,'g':Male.'sub;[52,48,55]}
s . compute()
print(s . _dict_)#{'rno' : 25 , 'sname' : Rama Rao , 'g' : Male , 'sub' : [52 , 48 , 55] , 'marks' : 155 , 'grade' : second class}


'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''

from prog9a import *
List=[]
n=int(input('Enter number of students:'))
for i in range(n):
    s=student()
    s.get()
    s.compute()
    List.append(s)
for j in List:
    j.disp()
    print(j)    



#  dir()  function  demo  program  (Home  work)

from  prog10a   import  Rat

a = Rat()

a . nr = 22

a . dr = 7

print(dir(Rat))
print(dir(Rat)) # ['add' , 'sub' , 'div' , 'mul' , 'test' , 'get' , '__str__']

print()

print()

print(dir(a))# ['nr' , 'add' , 'sub' , 'div' , 'mul' , 'test' , 'get' , '__str__' , 'dr']
   





#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))#True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False






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
'''
Meow meow meow
Bhow Bhow Bhow
Mehar Mehar Mehar

'''
		



#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
	'''
{'x' : 10 , 'y' : 20}
10
10
20
Invalid Variable name : z
'''




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
e=Emp()#How  to  convert  dictionary  to  object  'e'  with  for  loop
#how  to  print  object  'e'  with  for  loop
for x,y in dict.items():
	setattr(e,x,y)
for a in dict:
	print(getattr(e,a))
		
	
	
	

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
from EK import *
a = Rat()
b = Rat()
c = Rat()
a . get()
b . get()
c . add(a , b)
print(F'Addition : {c}')
c . sub(a , b)
print(F'Substraction : {c}')
c . mul(a , b)
print(F'Multiplication : {c}')
if  b . nr != 0:
	c . div(a , b)
	print(F'Division : {c}')
else:
	print('Division  is  not  permitted')





'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from prog9a import Rat 

# Create a list of 6 Rat objects
a = [Rat() for _ in range(6)]
# Input for first two rationals
print("First Rational Number:")
a[0].get()
print("Second Rational Number:")
a[1].get()
# Perform operations and store results in a[2] to a[5]
a[2].add(a[0], a[1])  # addition
a[3].sub(a[0], a[1])  # subtraction
a[4].mul(a[0], a[1])  # multiplication
a[5].div(a[0], a[1])  # division
# Output results
print("\nResults:")
print("Addition:", a[2])
print("Subtraction:", a[3])
print("Multiplication:", a[4])
if a[5].den == 0:
    print("Division is not permitted")
else:
    print("Division:", a[5])



