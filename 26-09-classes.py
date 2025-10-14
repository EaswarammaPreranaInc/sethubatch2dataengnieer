# What are the outputs if inputs are 25, Rama Rao, male, 52, 48, 55 (Home work)
from prog9a import student
s = student()
print(s.__dict__)        # {}
s.get()                  # User enters: 25, Rama Rao, male, 52, 48, 55
print(s.__dict__)        # {'roll': '25', 'name': 'Rama Rao', 'gender': 'male', 'marks': [52.0, 48.0, 55.0]}
s.compute()
print(s.__dict__)        # {'roll': '25', 'name': 'Rama Rao', 'gender': 'male', 'marks': [52.0, 48.0, 55.0], 'total': 155.0, 'average': 51.666..., 'grade': 'Second class'}


'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from prog9a import student

n = int(input("Enter number of students : "))
students = []
for i in range(n):
    print(f'Student {i+1}')
    s = student()
    s.get()
    s.compute()
    students.append(s)

for stu in students:
    print(f"{stu.roll}\t{stu.name}\t{stu.gender}\t{stu.total:.1f}\t{stu.average:.2f}\t{stu.grade}")


# dir() function demo program
from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat))
print()
print()
print(dir(a))


# Find outputs (Home work)
class Rat:
    def m1():
        pass
# End of the class
a = Rat()
a.nr = 22
print(hasattr(a, 'nr'))# True
print(hasattr(a, 'dr'))# False
print(hasattr(a, 'm1'))# True
print(hasattr(a, 'm2'))# False
print(hasattr(Rat, 'm1'))# True
print(hasattr(Rat, 'm2'))# False
print(hasattr(Rat, 'nr'))# False

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
# Output:
# Meow Meow Meow ....
# Bhow Bhow Bhow ....
# Mehar  Mehar  Mehar  ....

# Find outputs (Home work)
class c1:
    pass
a = c1()
a.x = 10
varname = input('Enter variable name to be added to object : ') # 'y'
value = eval(input('Enter value of the variable : '))# 20
setattr(a, varname, value)
print(a.__dict__)# {'x': 10, 'y': 20}
print(a.x)# 10
while True:
    try:
        varname = input('Enter variable name whose value is to be retrieved : ')
        print(getattr(a, varname))
    except:
        print(f'Invalid variable name : {varname}')
	    break
	
'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''

class Emp:
    pass
dict1 = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()
for k, v in dict1.items():
    setattr(e, k, v)
for k in dict1:
    print(f"{k} : {getattr(e, k)}")


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
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog10a import Rat
a = Rat(); b = Rat(); c = Rat()
print("Enter first rational number:"); a.get()
print("Enter second rational number:"); b.get()
c.add(a, b)
print(c)
c.sub(a, b)
print(c)
c.mul(a, b)
print(c)
c.div(a, b)
if getattr(c, 'division_valid', True):
    print(c)
else:
    print("Division is not permitted")

# Repeat prog10a with list of 6 objects
from prog10a import Rat
a = [Rat() for _ in range(6)]
print("Enter first rational number:"); a[0].get()
print("Enter second rational number:"); a[1].get()
a[2].add(a[0], a[1])
a[3].sub(a[0], a[1])
a[4].mul(a[0], a[1])
a[5].div(a[0], a[1])
print("Sum:", a[2])
print("Difference:", a[3])
print("Product:", a[4])
if getattr(a[5], "division_valid", True):
    print("Division:", a[5])
else:
    print("Division is not permitted")
