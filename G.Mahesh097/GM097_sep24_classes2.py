''' 1) Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''

from prog5a import Triangle 
t = Triangle()      # How  to  create  triangle  object
Triangle.get(t)     # How  to  call  get()  method  in  another  way
Triangle.test(t)    # How  to  call  test()  method  in  another  way
print('Area : ', Triangle.area(t)) # How  to  call  area()  method  in  another  way
print('Perimeter : ', Triangle.peri(t)) # How  to  call  peri()  method  in another way

'''
output:
Enter side of a: 3
Enter side of b: 4
Enter side of c: 5
Area: 6.0
Perimeter: 12.0
'''




# 2) Find outputs (Home work)

class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)        # 10   (local variable)
        print(self.x)   # 20   (instance variable)
        x += 5          # x = 15 (local, lost after method ends)
        self.x += 7     # self.x = 27 (stored in object x)
    def m2(self):
        print(x)        # Error x is not defined 
        print(self.x)   # 27 
        self.x += 6     # prints self.x = 27+6 = 33
# End of the class
a = c1()
a.m1()                  # prints: 10 20
a.m2()                  # prints: 27 33
print(a.x)              
print(self.x)           # Error self is not defined outside the class
print(x)                # Error x is not defined globally

'''
Outputs:

10
20
27
33
'''



''' 3) Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''

class Test:
    def get(self):      # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):    # How  to  add  objects  m  and  n  and  store  results  in  object  self
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self): # How  to  print  object  self
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")
        
# How  to  create  three  Test  class  objects  a , b  and  c
a = Test()
b = Test()
c = Test()

print("First Object")
a.get() # How  to  read  inputs  into  object  'a'

print("Second Object")
b.get() # How  to  read  inputs  into  object  'b'

c.add(a, b) # How  to  add  objects  a  and  b  and  store  results in  object  'c'

print("Addition Results")
c.disp() # How  to  print object 'c'

'''
Outputs:

First Object
Enter x: 10
Enter y: 20
Enter z: 30
Second Object
Enter x: 40
Enter y: 50
Enter z: 60
Addition Results
x = 50, y = 70, z = 90
'''




# 4) Find  outputs (Home  work)

class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy=1947
print(a)            # prints type and address      





# 5) Find  outputs (Home  work)

class c1:
    def _str_(self):  
        return '25'
class c2:
    def _str_(self):
        return 35      
class c3:
    def _str_(self):
        print('Hyd')   
class c4:
    def _str_(self, x):
        return f'{x}'       
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)                # prints type and address of class C1
print(b)                # prints type and address of class C2
print(c)                # prints type and address of class C3
print(d)                # prints type and address of class C4
print(b._str_())        # returns 35 => prints 35
print(c._str_())        # prints 'Hyd' inside method, returns None => prints None
print(d._str_(50))      # returns '50' => prints 50






''' 6) Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

class Student:
    def get(self):
        # Read student details and marks
        self.roll = input("Enter Roll Number: ")        # How  to  read  roll  number  into  object  self
        self.name = input("Enter Student Name: ")       # How  to  read  student  name  into  object  self
        self.gender = input("Enter Gender (M/F): ")     # How  to  read  gender  into  object  self
        print("Enter marks of 3 subjects:")             # How  to  read  marks  of  3  subjects
        self.marks = []
        for i in range(3):
            mark = int(input(f"Subject {i+1}: "))
            self.marks.append(mark)

    def compute(self):
        self.total = sum(self.marks)                    # How  to  calculate  total  marks
        self.average = self.total / len(self.marks)     # How  to  calculate  average  marks
        # Determine grade
        if any(mark < 40 for mark in self.marks):
            self.grade = "Fail"
        elif self.average >= 70:
            self.grade = "Distinction"
        elif self.average >= 60:
            self.grade = "First Class"
        elif self.average >= 50:
            self.grade = "Second Class"
        else:
            self.grade = "Third Class"

    def disp(self):
        # Display all student details
        print(f"Roll Number  : {self.roll}")
        print(f"Student Name : {self.name}")
        print(f"Gender       : {self.gender}")
        print(f"Total Marks  : {self.total}")
        print(f"Average      : {self.average:.2f}")
        print(f"Grade        : {self.grade}")

    def __str__(self):
        return (f"Roll Number: {self.roll}, Name: {self.name}, Gender: {self.gender}, Total: {self.total}, Average: {self.average:.2f}, Grade: {self.grade}")


s = Student()
s.get()
s.compute()
print("\nStudent Details:")
s.disp()
print("\nStudent Details:")
print(s)                                          
'''
output:
Enter Roll Number: 101
Enter Student Name: Maahi
Enter Gender (M/F): M
Enter marks of 3 subjects:
Subject 1: 80
Subject 2: 65
Subject 3: 90

Student Details:
Roll Number  : 101
Student Name : Maahi
Gender       : M
Total Marks  : 235
Average      : 78.33
Grade        : Distinction

Student Details:
Roll Number: 101, Name: Maahi, Gender: M, Total: 235, Average: 78.33, Grade: Distinction

'''






''' 7) Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 = (18 + 15) / 27 = 33 / 27 = 11 / 9
    What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 = 1 / 9
    What  is  the  product  ?  ---> 	2 / 3 * 5 / 9 =  10 / 27  =  10 / 27
    What  is   the  division  ?  ---> 	2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 = (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  ---> 	2 / 3 * 0 / 9 = 	0 / 27  =  	0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  ---> 	2 / 3 /  0 / 9 = 2 / 3 * 9 / 0 = 	18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  required ?  ---> When  numerator  is  non-zero
'''

import math

class Rat:   
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero! Re-enter.")
            self.den = int(input("Enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

    def simplify(self):
        """Simplify rational number if numerator is non-zero"""
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        if b.num == 0:
            self.den = 0    # mark invalid
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()


# Create 6 objects
a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat()

print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
b.get()

c.add(a, b)       # Add
d.sub(a, b)       # Subtract
e.mul(a, b)       # Multiply
f.div(a, b)       # Divide

# Display results
print("\nAddition result (a + b):", c)
print("Subtraction result (a - b):", d)
print("Multiplication result (a * b):", e)

if f.den != 0:
    print("Division result (a / b):", f)
else:
    print("Division is not permitted")

'''
output:
Enter 1st rational number:
Enter numerator: 2
Enter denominator: 3
Enter 2nd rational number:
Enter numerator: 5
Enter denominator: 9

Addition result (a + b): 11 / 9
Subtraction result (a - b): 1 / 9
Multiplication result (a * b): 10 / 27
Division result (a / b): 6 / 5

'''