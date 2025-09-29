 #  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from prog9a import student	     # imports the student class
s = student()	                 # creates an empty student object 's'
print(s . __dict__)	             # {} (An empty dictionary, as no attributes are set yet)
s . get()	                     # User prompts for inputs begin: "Enter Roll Number: 101", etc.
print(s . __dict__)	             # {'roll_no': '101', 'name': 'Alice', 'gender': 'F', 'sub1': 80.0, 'sub2': 85.0, 'sub3': 90.0}
s . compute()	                 # Calculates total (255.0), average (85.0), and grade ('Distinction')
print(s . __dict__)	             # {'roll_no': '101', 'name': 'Alice', 'gender': 'F', 'sub1': 80.0, 'sub2': 85.0, 'sub3': 90.0, 'total': 255.0, 'average': 85.0, 'grade': 'Distinction'}
'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''


#Program 2
from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7

print(dir(Rat))
# Output 1: List of class-level members (includes all built-in magic methods)

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# (Note: This list can vary slightly based on the Rat class's content/inheritance.)

print() # Prints a blank line

print() # Prints a blank line

print(dir(a))
# Output 2: List of instance members (includes built-ins PLUS the attributes added to the object)

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'dr', 'nr']


#Program 3
class Rat:
	def m1():
		pass
# End of the class
a = Rat()
a.nr = 22
print(hasattr(a , 'nr'))   # True
print(hasattr(a , 'dr'))   # False
print(hasattr(a , 'm1'))   # True
print(hasattr(a , 'm2'))   # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False


#Program 4
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
Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....'''

#Progam 5
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
Output:
Enter variable name to be added to object : y
Enter value of the variable : 20
# {'x': 10, 'y': 20}
10
Enter variable name whose value is to be retrieved : x
20
Enter variable name whose value is to be retrieved : y
Invalid variable name : z
'''

#Program 6
class Emp:
    pass
#End of the class
data_dict = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

e = Emp()

for key, value in data_dict.items():
    setattr(e, key, value)

print("Object Attributes:")
for key in data_dict.keys():
    print(f"{key}: {getattr(e, key)}")
	
#Program 7
# Hint: Import Rat class defined in prog10a but do not define Rat class again
from prog10a import Rat

a = Rat()
b = Rat()
c = Rat()

print("Enter Rational Number A:")
a.get()

print("\nEnter Rational Number B:")
b.get()

c.add(a, b)
print(f"\nSum ({a} + {b}) = {c}")

c.sub(a, b)
print(f"Difference ({a} - {b}) = {c}")

c.mul(a, b)
print(f"Product ({a} * {b}) = {c}")

c.div(a, b)
if c.den != 0:
    print(f"Division ({a} / {b}) = {c}")
else:
    print("Division is not permitted.")

#Program 8
# Hint: import Rat class defined in prog10a but do not rewrite the class again
from prog10a import Rat

a = [Rat() for _ in range(6)]

print("Enter Rational Number A (a[0]):")
a[0].get()
print("\nEnter Rational Number B (a[1]):")
a[1].get()

a[2].add(a[0], a[1])
print(f"\nSum (a[2]): {a[0]} + {a[1]} = {a[2]}")

a[3].sub(a[0], a[1])
print(f"Difference (a[3]): {a[0]} - {a[1]} = {a[3]}")

a[4].mul(a[0], a[1])
print(f"Product (a[4]): {a[0]} * {a[1]} = {a[4]}")

a[5].div(a[0], a[1])
if a[5].den != 0:
    print(f"Division (a[5]): {a[0]} / {a[1]} = {a[5]}")
else:
    print("Division is not permitted.")
	