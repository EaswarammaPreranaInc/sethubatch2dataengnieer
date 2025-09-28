
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  students  import  Student
s = Student()
print(s . __dict__) #{}
s . get()
print(s . __dict__) #{'rollno': 26, 'name': 'Nanda Kishore', 'gender': 'M', 'marks': [100, 100, 100]}
s . compute()
print(s . __dict__) #{'rollno': 26, 'name': 'Nanda Kishore', 'gender': 'M', 'marks': [100, 100, 100], 'totalmarks': 300, 'avg': 100.0, 'res': 'Distinction'}

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from students import Student
n=int(input("Enter no.of students : ")) 
list=[]
for i in range(0,n):
    s=Student()
    list.append(s)
for i in range(0,n):
    print(f'Student {i+1}')
    list[i].get()
    list[i].compute()
for x in list:
    print(x.__str__())


#  dir()  function  demo  program  (Home  work)

from  arthmetic   import  rat

a = rat()

a . nr = 22

a . dr = 7

print(dir(rat)) #All the methods of class in the form of list of strings

print()

print()

print(dir(a)) #All the Instance variables of Object and Methods of Class in the form of list of Strings

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) #True
print(hasattr(a , 'dr')) #False
print(hasattr(a , 'm1')) #True
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
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) #{'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) #10 20
	except:
		print(F'Invalid  variable   name   :  {varname}')
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
e=Emp()
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
for key,value in dict.items():
    setattr(e,key,value)#How  to  convert  dictionary  to  object  'e'  with  for  loop
for key in dict.keys():
    print(getattr(e,key))#How  to  print  object  'e'  with  for  loop

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

from arthmetic import rat
a=rat()
b=rat()
c=rat()
a.get()
b.get()
c.add(a,b)
print('Addition : ',c)
c.sub(a,b)
print('Subtraction : ',c)
c.mul(a,b)
print('Multiplication : ',c)
if b.nr!=0:
    c.div(a,b)
    print('Addition : ',c)
else:
    print('Divison is not permitted')

'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from arthmetic import rat
list=[]
for i in range(6):
    list.append(rat())
list[0].get()
list[1].get()
list[2].add(list[0],list[1])
list[3].sub(list[0],list[1])
list[4].mul(list[0],list[1])
if list[1].nr!=0:
    list[5].div(list[0],list[1])
print('Addition : ',list[2])
print('Subtraction : ',list[3])
print('Multiplication : ',list[4])
if list[1].nr!=0:
    print('Divison : ',list[5])
else:
    print('Divison is not permitted')