
1.#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)
#Output:
# {}
# It takes the inputs from user
# Dictionary of the given inputs are printed

'''
2.Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
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
444      DDD     f       234.0    78.00          Distinction

#Program:
from prog9a import Student
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"Student {i + 1}:")
    student = Student()
    student.get()
    student.compute()
    students.append(student)
for s in students:
    print(f"{s.rollno:<9}{s.name:<9}{s.gender:<9}{s.total:<9.1f}{s.avg:<10.2f}{s.grade}")



3.#  dir()  function  demo  program  (Home  work)

from  prog10a   import  Rat

a = Rat()

a . nr = 22

a . dr = 7

print(dir(Rat))

print()

print()

print(dir(a))

#Output:
# [ list of attributes and methods, 'add', 'div',  'get', 'mul', 'simplify', 'sub', 'test']
# [ list of attributes and methods, 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test']

4.#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))	#True
print(hasattr(a , 'dr'))	#False
print(hasattr(a , 'm1'))	#True
print(hasattr(a , 'm2'))	#False
print(hasattr(Rat , 'm1'))	#True
print(hasattr(Rat , 'm2'))	#False
print(hasattr(Rat , 'nr'))	#False




5.# Find  outputs  (Home  work)
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
#Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....


6.#  Find  outputs  (Home  work)
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
#Output:
{'x': 10, 'y': 20}
10
10
20
Invalid variable name : z

'''
(Home  work)
7.Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop

'''
#Program:
class Emp:
    pass

dict = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

# Convert dictionary to object
e = Emp()
for key, value in dict.items():
    setattr(e, key, value)
# Print object values
for key in dict:
    print(f"{key} : {getattr(e, key)}")


8.Repeat  prog10a  with  3  objects

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
#Program:
# prog10a.py

class Rat:
    def __init__(self, nr=0, dr=1):
        self.nr = nr
        self.dr = dr

    def __str__(self):
        return f"{self.nr}/{self.dr}"

    # Addition
    def __add__(self, other):
        nr = self.nr * other.dr + other.nr * self.dr
        dr = self.dr * other.dr
        return Rat(nr, dr)

    # Subtraction
    def __sub__(self, other):
        nr = self.nr * other.dr - other.nr * self.dr
        dr = self.dr * other.dr
        return Rat(nr, dr)

    # Multiplication
    def __mul__(self, other):
        nr = self.nr * other.nr
        dr = self.dr * other.dr
        return Rat(nr, dr)

    # Division
    def __truediv__(self, other):
        nr = self.nr * other.dr
        dr = self.dr * other.nr
        return Rat(nr, dr)



'''
9.Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
#Program:
from prog9a import Rat  # import your Rat class from your program file

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
