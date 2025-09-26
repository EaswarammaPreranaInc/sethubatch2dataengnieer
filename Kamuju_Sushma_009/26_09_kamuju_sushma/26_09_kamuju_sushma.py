#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  student  import  student
s = student()
print(s . __dict__) #{}
s . get()
print(s . __dict__) #{rno:25,name:Rama Rao,gender:male,marks:[52,48,55]}
s . compute()
print(s . __dict__) #{'rno':25,'name':'Rama Rao','gender':'male','marks':[52,48,55],'total':155,'average':51.67,'grade':'Second class'}

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
n=int(input("Enter number of students: "))
l=[]
for i in range(n):
    print(f'Enter student {i+1}')
    t=student()
    t.get()
    l.append(t)
for i in range(n):
    print(l[i])

#  dir()  function  demo  program  (Home  work)

from  rat   import  Rat

a = Rat()

a . nr = 22

a . dr = 7

print(dir(Rat)) #{}

print()

print()

print(dir(a))#{'nr':22,'dr':7}

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) #True
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
#Meow Meow Meow ....
#Bhow Bhow Bhow ....
# Mehar  Mehar  Mehar  ....

#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) 
print(a . __dict__)#{x:10}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))  #10 20
	except:
		print(F'Invalid  variable   name   :  {varname}') #z
		break


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
# How  to  convert  dictionary  to  object  'e'  with  for  loop
e=Emp()
for x in dict:
	e.eval(x)=dict[x]
# How  to  print  object  'e'  with  for  loop
for x in dict:
	print(x,' = ',e.eval(x))
	
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
a=Rat()
b=Rat()
c=Rat()
c.add(a,b)
print(c)
c.sub(a,b)
print(c)
c.mul(a,b)
print(c)
c.div(a,b)
print(c)

'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
l=[]
for i in range(6):
	t=Rat()
	t.get()
	l.append(t)