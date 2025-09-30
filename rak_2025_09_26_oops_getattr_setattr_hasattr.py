# What are the outputs if inputs are 25, Rama Rao, male, 52, 48, 55 (Homework)
from rak_2025_09_24_oops__str__ import Student
s = Student()
print(s.__dict__)
s.get()                 #reads values to object
print(s.__dict__)       #prints rollno, name, gender, marks  
s.compute()             #adds grade total_makerks, avg_marks, grade to student objt
print(s.__dict__)       #prints rollno, name, gender, marks, total_marks, avg_marks, grade



'''
Repeat Student program for 'n' Students

1) import Student class defined in prog9a but do not rewrite

2) Use list of objects

Enter number of Students: 4
Student 1
Enter roll number: 111
Enter Student name: AAA
Enter gender (m/f): m
Enter marks of subject 1: 52
Enter marks of subject 2: 48
Enter marks of subject 3: 55
Student 2
Enter roll number: 222
Enter Student name: BBB
Enter gender (m/f): f
Enter marks of subject 1: 100
Enter marks of subject 2: 100
Enter marks of subject 3: 0
Student 3
Enter roll number: 333
Enter Student name: CCC
Enter gender (m/f): m
Enter marks of subject 1: 45
Enter marks of subject 2: 56
Enter marks of subject 3: 67
Student 4
Enter roll number: 444
Enter Student name: DDD
Enter gender (m/f): f
Enter marks of subject 1: 67
Enter marks of subject 2: 78
Enter marks of subject 3: 89
111 AAA m 155.0 51.67 Second class
222 BBB f 200.0 66.67 Fail
333 CCC m 168.0 56.00 Second class
444 DDD f 234.0 78.00 Distinction
'''
from rak_2025_09_24_oops__str__ import Student
n = int(input('Enter no. of students:  '))
students = []
for i in range(n):
    print(f'Student: {i+1}')
    s = Student()
    s.get()
    s.compute()
for s in students:
    print(s)




# dir() function demo program (Homework)
from rak_2025_09_24_oops__str__ import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat))     #methods of Rat class and Object class
print()              
print(dir(a))       #instance variables of object a, methods of Rat class and methods of Object class



# Find outputs (Homework)
class Rat:
    def m1():
        pass
# End of the class
a = Rat()
a.nr = 22
print(hasattr(a, 'nr'))     #True
print(hasattr(a, 'dr'))     #False
print(hasattr(a, 'm1'))     #True
print(hasattr(a, 'm2'))     #False
print(hasattr(Rat, 'm1'))   #True
print(hasattr(Rat, 'm2'))   #False
print(hasattr(Rat, 'nr'))   #False




# Find outputs (Homework)
class Cat:
    def talk(self):
        print('Meow Meow Meow ....')
class Dog:
    def bark(self):
        print('Bhow Bhow Bhow ....')
class Goat:
    def talk(self):
        print('Mehar Mehar Mehar ....')
# End of the class
a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x, 'talk'):
        x.talk()
    else:
        x.bark()
'''
OUTPUT:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....
'''



# Find outputs (Homework)
class c1:
    pass
# End of the class
a = c1()
a.x = 10
varname = input('Enter variable name to be added to object: ')  # Assume input is 'y'
value = eval(input('Enter value of the variable: '))  # Assume input is 20
setattr(a, varname, value)
print(a.__dict__)
print(a.x)  # 10
while True:
    try:
        varname = input('Enter variable name whose value is to be retrieved: ')
        # Assume inputs: x, y, z
        print(getattr(a, varname))
    except:
        print(f'Invalid variable name: {varname}')
        break
'''
OUTPUT:
Enter variable name to be added to object: y
Enter value of the variable: 10
{'x': 10, 'y': 10}
10
Enter variable name whose value is to be retrieved: x
10
Enter variable name whose value is to be retrieved: y
10
Enter variable name whose value is to be retrieved: z
Invalid variable name: z
'''





'''
(Home work)
Write a program to convert a dictionary {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0} to Emp class object
i.e. object should contain empno=25, ename='Rama Rao', Sal=10000.0

Hint: Use setattr() and getattr() functions
'''
class Emp:
    pass
# End of the class
d = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
# How to convert dictionary to object 'e' with for loop
e = Emp()
for k,v in d.items():
    setattr(e, k, v)
# How to print object 'e' with for loop
for k in d:
    print(getattr(e, k))



'''
Repeat prog10a with 3 objects

Eg: c = a + b
    print(c)
    c = a - b
    print(c)
    c = a * b
    print(c)
    c = a / b
    print(c)

Hint: Import Rat class defined in prog10a but do not define Rat class again
'''
from rak_2025_09_24_oops__str__ import Rat
a = Rat()
a.get()
b = Rat()
b.get()
c = Rat()
c.add(a, b)
print(c)
c.sub(a, b)
print(c)
c.mul(a, b)
print(c)
c.div(a,b)
print(c)



'''
Repeat prog10a with list of 6 objects

Hint: import Rat class defined in prog10a but do not rewrite the class again

What are the object names? ---> a[0], a[1], a[2], ..., a[5]
'''
from rak_2025_09_24_oops__str__ import Rat
a = [Rat(), Rat(), Rat(), Rat(), Rat(), Rat()]
a[0].get()
a[1].get()
a[2].add(a[0], a[1])
a[3].sub(a[0], a[1])
a[4].mul(a[0], a[1])
a[5].div(a[0], a[1])
for i in range(2, 6):
    print(a[i])