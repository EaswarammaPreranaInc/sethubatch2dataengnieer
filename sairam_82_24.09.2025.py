'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
import prog5a as a
b=a.triangle()
a.triangle.get(b)
print('Area : ', a.triangle.area(b))
print('Perimeter: ',a.triangle.peri(b))
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # 10
		print(self . x) # 20
		x += 5
		self . x += 7 
	def   m2(self):
		print(x) # error
		print(self . x) #27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) # 33
print(self . x) # error 
print(x)  # error
class Test:
    def get(self):
        self.a = int(input("Enter a value: "))
        self.b = int(input("Enter b value: "))
        self.c = int(input("Enter c value: "))

    def add(self, m, n):
        # store result of adding m and n into self
        self.a = m.a + n.a
        self.b = m.b + n.b
        self.c = m.c + n.c

    def disp(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")


# Create three objects
a = Test()
b = Test()
c = Test()

print("First Object")
a.get()
a.disp()

print("Second Object")
b.get()
b.disp()

# c = a + b (done via add method)
c.add(a, b)

print("Addition Results (Third Object)")
c.disp()

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) #<_main_.Date object at 92>
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # <_main_.c1 object at 92>
print(b) # <_main_.c2 object at 93>
print(c)  # <_main_.c3 object at 22>
print(d) # <_main_.c4 object at 452>
print(b . str()) # 35
print(c . str()) # Hyd
print(d . str(50)) # 50
class Student:
    def get(self):
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender (M/F): ")
        print("Enter marks of 3 subjects:")
        self.m1 = int(input("Subject 1: "))
        self.m2 = int(input("Subject 2: "))
        self.m3 = int(input("Subject 3: "))

    def compute(self):
        self.total = self.m1 + self.m2 + self.m3
        self.average = self.total / 3

        # Grade logic
        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
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
        print("Roll Number : ", self.roll)
        print("Student Name : ", self.name)
        print("Gender : ", self.gender)
        print("Total Marks : ", self.total)
        print("Average : ", self.average)
        print("Grade : ", self.grade)

    def _str_(self):
        return (f"Roll: {self.roll}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Avg: {self.average}, Grade: {self.grade}")
# Create object
s1 = Student()

# Read inputs into object
s1.get()

# Compute results
s1.compute()

# Print using disp()
s1.disp()

# Print using _str_()
print(s1)

import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()   # check denominator

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero. Re-enter:")
            self.den = int(input("Enter denominator again: "))

    def _str_(self):
        return f"{self.num} / {self.den}"

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
        if b.num == 0:   # division not possible
            self.num, self.den = None, None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num == 0:
            self.den = 1   # keep denominator as 1 when numerator is 0
        else:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g
# Create 6 objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# Perform operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

# Print results
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)

if f.num is None:
    print("Division is not permitted")
else:
    print("Division:", f)
