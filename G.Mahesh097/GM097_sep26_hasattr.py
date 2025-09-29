# 1) What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)

from  prog9a  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s. __dict__)


'''
Inputs:
Enter Roll Number: 25
Enter Name: Rama Rao
Enter Gender: male
Enter Marks of Subject 1: 52
Enter Marks of Subject 2: 48
Enter Marks of Subject 3: 55


Output:
{}                                                
{'rno': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}
{'rno': 25, 'name': 'Rama Rao', 'gender': 'male', m1': 52, 'm2': 48, 'm3': 55, 'total': 155, 'avg': 51.67, 'grade': 'Pass'}
'''





''' 2) Repeat  student  program  for  'n'  students
1) import  student  class  defined in  prog9a  but  do  not  rewrite
2) Use  list of objects
'''

from prog9a import student    

n = int(input("Enter number of students : "))
students = []               

for i in range(n):
    print(f"\nStudent {i+1}")
    s = student()              # Create a new student object
    s.get()                    # Read student details
    s.compute()                # Calculate total, average, grade
    students.append(s)         # Add object to list

print("\nRollNo  Name    Gender   Total     Average     Grade")
for s in students:
    print(f"{s.rno:<7} {s.name:<7} {s.gender:<7} {s.total:<9.1f} {s.avg:<10.2f} {s.grade}")
'''
output:
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
222      BBB     f       200.0    66.67          fail
333      CCC     m       168.0    56.00          Second class
444      DDD     f       234.0    78.00          Distinction
'''




# 3) dir() function demo program (Home work)

from prog10a import Rat      # import the Rat class
a = Rat()                    # create an object of Rat

a.nr = 22                     # create a new attribute in the object
a.dr = 7                      # create another new attribute

print(dir(Rat))               # Prints all names defined for the class
print()
print()
print(dir(a))                 # Prints all names defined for the object





# 4) Find outputs (Home work)

class Rat:
    def m1():
        pass
# End of the class
a = Rat()
a.nr = 22                       
print(hasattr(a, 'nr'))         # True   → 'a' has attribute 'nr'
print(hasattr(a, 'dr'))         # False  → 'a' does NOT have 'dr'
print(hasattr(a, 'm1'))         # True   → 'a' inherits method 'm1' from class
print(hasattr(a, 'm2'))         # False  → no attribute or method 'm2'
print(hasattr(Rat, 'm1'))       # True   → class Rat has method 'm1'
print(hasattr(Rat, 'm2'))       # False  → class Rat does NOT have 'm2'
print(hasattr(Rat, 'nr'))       # False  → 'nr' exists only in object 'a', not in class





# 5) Find  outputs  (Home  work)

class Cat:
    def talk(self):
        print('Meow Meow Meow ....') 
class Dog:
    def bark(self):
        print('Bhow Bhow Bhow ....')  
class Goat:
    def talk(self):
        print('Mehar Mehar Mehar ....')
#end of the class
a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x, 'talk'):
        x.talk()  # Meow Meow Meow ....  (Cat)
                  # Mehar Mehar Mehar .... (Goat)
    else:
        x.bark()  # Bhow Bhow Bhow .... (Dog)





# 6) Find  outputs  (Home  work)

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

Enter variable name to be added to object  :  y
Enter value of the variable  :  20
Enter variable name whose value is to be retrieved  :  x
Enter variable name whose value is to be retrieved  :  y
Enter variable name whose value is to be retrieved  :  z

{'x': 10, 'y': 20}
10
10
20
Invalid variable name : z
'''




''' 7) Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict_emp = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
#How  to  convert  dictionary  to  object  'e'  with  for  loop
for key, value in dict_emp.items():
    setattr(e, key, value)
#How  to  print  object  'e'  with  for  loop
for key in dict_emp.keys():
    print(f"{key} : {getattr(e, key)}")

'''
Output:
Empno : 25
Ename : Rama Rao
Sal : 10000.0
'''





''' 8) Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''

from prog10a import Rat   # Import Rat class from prog10a

a = Rat()
b = Rat()
c = Rat()  

# Input first rational number
print("Enter 1st rational number:")
a.get()

# Input second rational number
print("Enter 2nd rational number:")
b.get()

c.add(a, b)
print("\nAddition result (a + b):", c)   

c.sub(a, b)
print("Subtraction result (a - b):", c)

c.mul(a, b)
print("Multiplication result (a * b):", c)

c.div(a, b)
if c.den != 0:
    print("Division result (a / b):", c)
else:
    print("Division is not permitted")

'''
output:
Enter 1st rational number:
Enter numerator: 1
Enter denominator: 2
Enter 2nd rational number:
Enter numerator: 1
Enter denominator: 3

Addition result (a + b): 5/6
Subtraction result (a - b): 1/6
Multiplication result (a * b): 1/6
Division result (a / b): 3/2
'''




''' 9) Repeat  prog10a  with  list  of  6  objects
Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2],.....a[5]
'''

# Repeat prog10a with list of 6 objects
from prog10a import Rat   # Import Rat class from prog10a

a = []
for i in range(6):
    a.append(Rat())# a[0], a[1], a[2], a[3], a[4], a[5]

# Read first rational number into a[0]
print("Enter 1st rational number:")
a[0].get()

# Read second rational number into a[1]
print("Enter 2nd rational number:")
a[1].get()

a[2].add(a[0], a[1])    # a[2] = a[0] + a[1]
print("\nAddition result (a[0] + a[1]):", a[2]) # a[2] = a[0] + a[1]

a[3].sub(a[0], a[1])    # a[3] = a[0] - a[1]
print("Subtraction result (a[0] - a[1]):", a[3])

a[4].mul(a[0], a[1])    # a[4] = a[0] * a[1]
print("Multiplication result (a[0] * a[1]):", a[4])

a[5].div(a[0], a[1])    # a[5] = a[0] / a[1]
if a[5].den != 0:
    print("Division result (a[0] / a[1]):", a[5])
else:
    print("Division is not permitted")

'''
output:
Enter 1st rational number:
Enter numerator: 1
Enter denominator: 2
Enter 2nd rational number:
Enter numerator: 1
Enter denominator: 3

Addition result (a[0] + a[1]): 5/6
Subtraction result (a[0] - a[1]): 1/6
Multiplication result (a[0] * a[1]): 1/6
Division result (a[0] / a[1]): 3/2
'''