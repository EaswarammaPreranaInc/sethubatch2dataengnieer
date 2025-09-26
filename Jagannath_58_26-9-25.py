#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)
{}
enter roll no: 25
enter name: Rama Rao
enter gender: m
enter marks: 55
enter marks: 48
enter marks: 58
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'm', 'm': [55, 48, 58]}
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'm', 'm': [55, 48, 58], 'total': 161, 'avg': 53.666666666666664, 'grade': 'Second  Class'}


Repeat  student  program  for  'n'  students
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

#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
Print()
print()
print(dir(a))
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
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test'] 

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))                          True
print(hasattr(a , 'dr'))                          False
print(hasattr(a , 'm1'))                          True
print(hasattr(a , 'm2'))                          False
print(hasattr(Rat , 'm1'))                        True
print(hasattr(Rat , 'm2'))                        False
print(hasattr(Rat , 'nr'))                        False

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
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....

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

(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0
class Emp:
    pass
# End of the class
data = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()
for key, value in data.items():
    setattr(e, key, value)      
for key in data.keys():
    print(key, ":", getattr(e, key))  

Repeat  prog10a  with  3  objects
from prog10a import Rat       
a = Rat()
b = Rat()
c = Rat()
print("First Rational Number:")
a.get()
print("Second Rational Number:")
b.get()
c.add(a, b)
print("\nAddition :", c)
c.sub(a, b)
print("Subtraction :", c)
c.mul(a, b)
print("Multiplication :", c)
c.div(a, b)
if c.den == 0:          
    print("Division : Not permitted (division by zero)")
else:
    print("Division :", c)

Repeat  prog10a  with  list  of  6  objects
a = [Rat() for i in range(6)]   
print("First Rational Number:")
a[0].get()
print("Second Rational Number:")
a[1].get()
a[2].add(a[0], a[1])   
a[3].sub(a[0], a[1])   
a[4].mul(a[0], a[1])  
a[5].div(a[0], a[1])  
