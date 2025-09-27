Q1) What are the outputs if inputs are 25 , Rama Rao , male , 52 , 48 , 55 (Home work)

Code:
from prog9a import student
s = student()
print(s._dict_)
s.get()
print(s._dict_)
s.compute()
print(s._dict_)

Output:
{}
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55, 'total': 155.0, 'avg': 51.67, 'class': 'Second class'}


Q2) Repeat student program for 'n' students

Input / Execution:
Enter number of students : 4
Student 1 → 111, AAA, m, 52, 48, 55
Student 2 → 222, BBB, f, 100, 100, 0
Student 3 → 333, CCC, m, 45, 56, 67
Student 4 → 444, DDD, f, 67, 78, 89

Output:
111   AAA   m   155.0   51.67   Second class
222   BBB   f   200.0   66.67   Fail
333   CCC   m   168.0   56.00   Second class
444   DDD   f   234.0   78.00   Distinction


Q3) dir() function demo program (Home work)

Code:
from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat))
print()
print(dir(a))

Output:
dir(Rat) → default class attributes + 'm1'
dir(a)   → default object attributes + 'nr', 'dr'


Q4) Find outputs (Home work)

Code:
class Rat:
    def m1():
        pass
a = Rat()
a.nr = 22
print(hasattr(a , 'nr'))
print(hasattr(a , 'dr'))
print(hasattr(a , 'm1'))
print(hasattr(a , 'm2'))
print(hasattr(Rat , 'm1'))
print(hasattr(Rat , 'm2'))
print(hasattr(Rat , 'nr'))

Output:
True
False
False
False
True
False
False


Q5) Find outputs (Home work)

Code:
class Cat:
    def talk(self):
        print('Meow Meow Meow ....')
class Dog:
    def bark(self):
        print('Bhow Bhow Bhow ....')
class Goat:
    def talk(self):
        print('Mehar  Mehar  Mehar  ....')
a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x , 'talk'):
        x.talk()
    else:
        x.bark()

Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar ....


Q6) Find outputs (Home work)

Code:
class c1:
    pass
a = c1()
a.x = 10
varname = input('Enter variable name to be added to object : ')   # y
value = eval(input('Enter value of the variable : '))             # 20
setattr(a , varname , value)
print(a._dict_)
print(a.x)
while True:
    try:
        varname = input('Enter variable name whose value is to be retrieved : ')
        # assume inputs: x, y, z
        print(getattr(a , varname))
    except:
        print(f'Invalid variable name : {varname}')
        break

Output:
{'x': 10, 'y': 20}
10
10
20
Invalid variable name : z


Q7) Convert dictionary to Emp object (Home work)

Question:
Write a program to convert a dictionary {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 10000.0}
to Emp class object using setattr() and print using getattr().

Code:
class Emp:
    pass
d = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()
for k, v in d.items():
    setattr(e, k, v)
for k in d.keys():
    print(k, "=", getattr(e, k))

Output:
Empno = 25
Ename = Rama Rao
Sal = 10000.0
