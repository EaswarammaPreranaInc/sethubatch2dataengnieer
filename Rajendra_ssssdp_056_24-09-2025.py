'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again

'''

from prog5a import Triangle
t = Triangle()				#How  to  create  triangle  object
Triangle.get(t)				#How  to  call  get()  method  in  another  way
Triangle.test(t)			#How  to  call  test()  method  in  another  way
print('Area : ', Triangle.area(t))	#How  to  call  area()  method  in  another  way
print('Perimeter: ', Triangle.peri(t))	#How  to  call  peri()  method  in another way








# Find outputs (Home work)

class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)    
        print(self.x)
        x += 5          
        self.x += 7     
    def m2(self):
        print(x)        	#Throws error as x is not defined 
        print(self.x)   
        self.x += 6   

# End of the class

a = c1()
a.m1()                 		#10 20
a.m2()                 		#27 33
print(self.x)               #Throws error as self is not defined outside the class
print(x)                    #Throws error as x is not defined  








'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90

class  Test:
	def   get(self):
		 How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 How  to  print  object  self
# End  of  the  class
How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
How  to  read  inputs  into  object  'a'
print('Second  Object')
How  to  read  inputs  into  object  'b'
How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
How  to  print object 'c'
'''

class Test:
    def get(self):
        # Read inputs into object variables x, y, z
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, a, b):
        # Add objects m and n and store result in self
        self.x = a.x + b.x
        self.y = a.y + b.y
        self.z = a.z + b.z

    def disp(self):
        # Print object values
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")


# Create three Test class objects
a = Test()
b = Test()
c = Test()
print("First Object")
a.get()						#Read inputs for first object
print("Second Object")
b.get()						#Read inputs for second object
c.add(a, b)					#Add objects a and b, store results in c
print("Addition Results")
c.disp()					#Print addition results







#  Find  outputs (Home  work)

class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy=1947
print(a)            # prints type and address      







#  Find  outputs (Home  work)

class c1:
    def __str__(self):  
        return '25'
class c2:
    def __str__(self):
        return 35      
class c3:
    def __str__(self):
        print('Hyd')   
class c4:
    def __str__(self, x):
        return f'{x}'       
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)                	#prints type and address of c1 class object
print(b)                	#prints type and address of c2 class object
print(c)                	#prints type and address of c3 class object
print(d)                	#prints type and address of c4 class object
print(b.__str__())        	#35
print(c.__str__())        	#None
print(d.__str__(50))      	#50








'''
Write a program to determine total, average and grade of a student
Inputs: Roll Number, Student Name, Marks of 3 subjects, Gender
'''

class Student:
    def get(self):
        # Read student details and marks
        self.roll = int(input("Enter Roll Number: "))             # Read roll number
        self.name = input("Enter Student Name: ")                 # Read student name
        self.gender = input("Enter Gender (M/F): ")               # Read gender
        print("Enter marks of 3 subjects:")                       # Read marks of 3 subjects
        self.marks = []
        for i in range(3):
            mark = int(input(f"Subject {i+1}: "))
            self.marks.append(mark)

    def compute(self):
        self.total = sum(self.marks)                              # Calculate total marks
        self.average = self.total / 3                             # Calculate average marks
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
        # Return all values as a single string
        return (f"Roll Number: {self.roll}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.average:.2f}, Grade: {self.grade}")



S = Student()				# Create Student object
S.get()					# Read inputs
# Calculate results
S.compute()
S.disp()				#Display using disp()
print(S)       				# Display using __str__()                                     







'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

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
        self.num = int(input("Enter numerator: "))         # How to read numerator into object self
        self.den = int(input("Enter denominator: "))       # How to read denominator into object self
        self.test()                                        # How to call test() method

    def test(self):
        # Ask user to reenter denominator if zero
        while self.den == 0:
            print("Denominator cannot be zero! Re-enter.")
            self.den = int(input("Enter denominator: "))

    def _str_(self):
        # Return value as string in form 'num / den'
        return f"{self.num} / {self.den}"                 # values of object in rational form

    def simplify(self):
        # Simplify the rational number
        if self.num != 0:                                  # Simplification required only if numerator != 0
            g = math.gcd(self.num, self.den)              # Find GCD
            self.num //= g                                 # Simplify numerator
            self.den //= g                                 # Simplify denominator

    def add(self, a, b):
        # Add two rational numbers a and b
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()                                   # Simplify the result

    def sub(self, a, b):
        # Subtract b from a
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()                                   # Simplify the result

    def mul(self, a, b):
        # Multiply two rational numbers
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()                                   # Simplify the result

    def div(self, a, b):
        # Divide a by b
        if b.num == 0:
            self.den = 0                                  # Mark division as invalid
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()                               # Simplify the result

# Create 6 objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# Read rational numbers into a and b
print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
b.get()

# Perform operations
c.add(a, b)       # Add
d.sub(a, b)       # Subtract
e.mul(a, b)       # Multiply
f.div(a, b)       # Divide

# Display results
print("\nAddition result (a + b):", c._str_())
print("Subtraction result (a - b):", d._str_())
print("Multiplication result (a * b):", e._str_())

if f.den != 0:
    print("Division result (a / b):", f._str_())
else:
    print("Division is not permitted")              