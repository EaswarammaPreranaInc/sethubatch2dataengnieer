from  prog9a  import  student
s = student()
print(s . _dict_) # {}
s . get()
print(s . _dict_) # {'rollno': 25, 'name': 'aaa', 'gender': 'm', 'm1': 55.0, 'm2': 65.0, 'm3': 75.0}
s . compute()
print(s . _dict_) # {'rollno': 25, 'name': 'aaa', 'gender': 'm', 'm1': 55.0, 'm2': 65.0, 'm3': 75.0, 'total': 195.0, 'avg': 65.0, 'grade': 'First class'}

q) Repeat  student  program  for  'n'  students
1) import  student  class  defined in  prog9a  but  do  not  rewrite
2) Use  list  of  objectsfrom  prog10a   import  Rat
Ans)  from prog9a import Student  # Assume Student class is defined in prog9a.py
n = int(input('Enter number of students: '))  # Number of students
students = []
for i in range(n):
    s = Student()
    s.get()        # Read inputs into object
    s.compute()    # Compute total, avg, grade
    students.append(s)
for s in students:
    s.disp()       # Print student details
    print(s.__str__())  # Print object as string00

a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test','__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', and other Ev’s]
print() # prints blank line
print() # prints blank line
print(dir(a)) # ['_str_', 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test','__class__', '__delattr__', '__dict__', '__dir__', and other Ev’s]

class Rat:
    def m1():
        pass
# End of the class
a = Rat()
a.nr = 22
print(hasattr(a , 'nr'))    # True
print(hasattr(a , 'dr'))    # False
print(hasattr(a , 'm1'))    # True
print(hasattr(a , 'm2'))    # False
print(hasattr(Rat , 'm1'))  # True
print(hasattr(Rat , 'm2'))  # False
print(hasattr(Rat , 'nr'))  # False

class Cat:
    def talk(self):
        print('Meow Meow Meow ....')
class Dog:
    def bark(self):
        print('Bhow Bhow Bhow ....')
class Goat:
    def talk(self):
        print('Mehar  Mehar  Mehar  ....')
# end of the class
a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x , 'talk'):
        x.talk()
    else:
        x.bark()
# Meow Meow Meow ....
# Bhow Bhow Bhow ....
# Mehar  Mehar  Mehar  ....

class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) # y,20
print(a . __dict__)  # {'x': 10, 'y': 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) # x 10
					   # y 20
	except:
		print(F'Invalid  variable   name   :  {varname}') # z invalid variable
		break
q) Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0
Ans) class Emp:
    pass
# End of the class
data = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()
for key, value in data.items():
    setattr(e, key, value)  # How  to  convert  dictionary  to  object  'e'  with  for  loop
for key in data.keys():
    print(key, ":", getattr(e, key))  # How  to  print  object  'e'  with  for  loop

q)  Repeat  prog10a  with  3  objects
Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c
Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
Ans) from prog10a import Rat       
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


q) Repeat  prog10a  with  list  of  6  objects
Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
Ans) a = [Rat() for i in range(6)]   
print("First Rational Number:")
a[0].get()
print("Second Rational Number:")
a[1].get()
a[2].add(a[0], a[1])   
a[3].sub(a[0], a[1])   
a[4].mul(a[0], a[1])  
a[5].div(a[0], a[1])
