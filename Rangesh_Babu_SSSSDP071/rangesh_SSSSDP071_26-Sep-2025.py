
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__) #{}
s . get()
print(s . __dict__) #{'rollno': 25, 'name': 'Rama Rao', 'gender': 'm', 'm': [52, 48, 55]}
s . compute()
print(s . __dict__) #{'rollno': 25, 'name': 'Rama Rao', 'gender': 'm', 'm': [52, 48, 55], 'total': 155, 'avg': 51.666666666666664, 'grade': 'Second  Class'}



'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from prog9a import Student
s=Student()
n=int(input("no of students"))
a=[]
for i in range(n):
    print(f'Student {i+1}')
    s.get()
    s.compute()
    a.append([s.rollno,s.name,s.gender,s.total,s.avg,s.grade])
for i in a:
    print(*i)

#  dir()  function  demo  program  (Home  work)

from  prog10a   import  Rat

a = Rat()

a . nr = 22

a . dr = 7

print(dir(Rat))

print()

print()

print(dir(a))#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) #True
print(hasattr(a , 'dr'))    #False
print(hasattr(a , 'm1')) #False
print(hasattr(a , 'm2')) #False           
print(hasattr(Rat , 'm1')) #True
print(hasattr(Rat , 'm2')) #False
print(hasattr(Rat , 'nr')) #False

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
		x . talk() #for cat and goat class
	else:
		x . bark() #for  dog class
'''
output
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) # {'x': 10, 'y': 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) #for x 10 for y 20
	except:
		print(F'Invalid  variable   name   :  {varname}') #for z invalid 
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
e=Emp()
for i in dict:
    setattr(e,i,dict[i])
print(getattr(e,'Empno'),getattr(e,'Ename'),getattr(e,'Sal'))
#How  to  convert  dictionary  to  object  'e'  with  for  loop
#How  to  print  object  'e'  with  for  loop

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
a = Rat()
b = Rat()
c = Rat()
a.get()
b.get() 
c.add(a, b)
print(c)
c.sub(a, b)
print(c)
c.mul(a, b)
print(c)
c.div(a, b)
print(c)
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog10a import Rat
a=[]
for i in range(6):
    print(f'Object {i+1}')
    r=Rat()
    r.get()
    a.append(r)
for i in a:
    print(i)
