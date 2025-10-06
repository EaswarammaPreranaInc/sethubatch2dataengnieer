Dabbiru Sai Harsha Vardhan
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)

from  prog9a  import  student
s = student()
print(s . dict) # {}
s . get() 
print(s . dict) # {'rno':25,'sname':'Rama Rao','gender':'male',m:[52,48,55]}
s . compute()
print(s . dict) # {'rno':25,'sname':'Rama Rao','gender':'male',m:[52,48,55],'total':155,'average':51.66,'grade':'Second class'}




'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects

from prog9a import student
'''
n=int(input('Enter the number of times you  want to repeat : '))
a=[]
for i in range(n):
    l.append(input(f"Enter {n} object names : "))
for i in range(len(a)):
    a[i]=student()
    a[i].get()
    a[i].compute()
    a[i].disp()


#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # [a,b,c,d,sum,sub,mul,div]
print()
print()
print(dir(a)) # [nr,dr,sum,sub,mul,div]




#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False





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
		
'''Meow Meow Meow ....'
'Bhow Bhow Bhow ....'
'Mehar  Mehar  Mehar  ....'''




#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) # a.y=20
print(a . dict) # {x:10,y:20}
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
{x:10,y:20}
10
10
20
Invalid  variable   name   :  z
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
e=Emp()
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
for x,y in dict.items():
    setattr(e,x,y)
    print(f'{x} = {getattr(e,x)}',end=' , ')
    
'''How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop'''




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

from prog10a import Rat
l=[x,y,z]
for c in l:
    c=Rat()
    c.sum()
    print(f'{c.nr}/{c.dr}')
    c.sub()
    print(f'{c.nr}/{c.dr}')
    c.mul()
    print(f'{c.nr}/{c.dr}')
    c.div()
    print(f'{c.nr}/{c.dr}')
    
    
from prog10a import Rat
a=[m,n,o,p,q,r]
for c in a:
    c=Rat()
    c.sum()
    print(f'{c.nr}/{c.dr}')
    c.sub()
    print(f'{c.nr}/{c.dr}')
    c.mul()
    print(f'{c.nr}/{c.dr}')
    c.div()
    print(f'{c.nr}/{c.dr}')
