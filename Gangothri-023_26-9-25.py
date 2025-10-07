#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)
'''Output:
{}
Enter  roll  number : 25
Enter  student  name :  Rama Rao
Enter  gender (m/f) : male
Enter  marks  of  subject  1  :  52
Enter  marks  of  subject  2  :  48
Enter  marks  of  subject  3  :  55
{'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
{'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'tot': 155, 'avg': 51.666666666666664, 'grade': 'Second  class'}'''

#Repeat  student  program  for  'n'  students
#1) import  student  class  defined in  prog9a  but  do  not  rewrite
#2) Use  list  of  objects
from prog9a import student
n=int(input('How many students ? :'))
a=[]
for i in range(n):
    s=student()
    a.append(s)
i=1
for s in a:
    print(F'Student {i} ')
    s.get()
    s.compute()
    i += 1
for s in a:
    print(s)

'''Output:
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
444      DDD     f       234.0    78.00          Distinction'''

#  dir()  function  demo  program  (Home  work)
from  prog10a   import  rat as Rat
a = Rat() # Creates an empty rat class object
a . nr = 22 # Adds variable nr to object 'a' with value 22
a . dr = 7 # Adds variable dr to object 'a' with value 7
print(dir(Rat)) # All the method of rat class 
print()
print()
print(dir(a)) # All the variables of object 'a' and method of rat class

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

'''Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....'''

#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
		#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''Output:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  20
{'x': 10, 'y': 20}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  z
Invalid  variable   name   :  z'''


# (Home  work) Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0
#Hint:  Use  setattr()  and  getattr()  functions
class  emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=emp() # How  to  convert  dictionary  to  object  'e'  with  for  loop
for key, value in dict.items(): #How  to  print  object  'e'  with  for  loop
    setattr(e,key,value)
for key in dict.keys():
    print(key, getattr(e, key),sep='...')

'''Repeat  prog10a  with  3  objects
Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again'''
from prog10a import rat
a = rat()
b = rat()
c = rat()
a.get()
b.get()
c.add(a,b)
print(F'Addition : {c}')
c.sub(a,b)
print(F'Subtraction : {c}')
c.mul(a,b)
print(F'Multiplication : {c}')
if b.nr == 0:
    print('Division is not permitted')
else:
    c.div(a,b)
    print(F'Division : {c}')
'''Output:
Enter  numerator :  2
Enter  denominator :  3
Enter  numerator :  4
Enter  denominator :  5
Addition : 22 / 15
Subtraction : -2 / 15
Multiplication : 8 / 15
Division : 5 / 6
'''
'''
Repeat  prog10a  with  list  of  6  objects
Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog10a import rat
a=[rat(), rat(), rat(), rat(), rat(), rat()]
a[0].get()
a[1].get()
a[2].add(a[0])
a[3].sub(a[0], a[1])
a[4].mul(a[0], a[1])
print("Sum :",a[2])
print("Difference :",a[3])
print("Product :",a[4])
if a[1].nr ==0:
    print('Division is not permitted')
else:
    a[5].div(a[0], a[1])
    print('Division : ',a[5])
