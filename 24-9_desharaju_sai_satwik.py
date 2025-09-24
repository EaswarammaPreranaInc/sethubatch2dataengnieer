# Reuse triangle class defined in prog5a (do not define again)

# create triangle object
t = Triangle()

# call get() method in another way
Triangle.get(t)

# call test() method in another way
Triangle.test(t)

print("Area:", Triangle.area(t))        # call area() in another way
print("Perimeter:", Triangle.peri(t))   # call peri() in another way


class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)        # 10
        print(self.x)   # 20
        x += 5          # x = 15 (local)
        self.x += 7     # self.x = 27

    def m2(self):
        print(x)        #  ERROR 
        print(self.x)
        self.x += 6

a = c1()
a.m1()
a.m2()   # Error: 
print(a.x)
print(self.x)  #  ERROR
print(x)       #  ERROR

'''
10
20
NameError: name 'x' is not defined

'''



class Test:
    def get(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(self.x, self.y, self.z)

# create 3 objects
a = Test()
b = Test()
c = Test()

print("First Object")
a.get()
print("Second Object")
b.get()

c.add(a, b)

print("Addition results")
c.disp()


class Date:
    pass

a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)
#<__main__.Date object at 0x0000021ABF...>


class c1:
    def __str__(self):   # correct method is __str__
        return '25'

class c2:
    def __str__(self):
        return '35'      # must return string, not int

class c3:
    def __str__(self):
        print('Hyd')
        return ''        # return something, else error

class c4:
    def __str__(self):
        return 'Object of c4'

# Objects
a = c1()
b = c2()
c = c3()
d = c4()

print(a)            # 25
print(b)            # 35
print(c)            # Hyd (from inside), then ''
print(d)            # Object of c4
print(b.__str__())  # 35
print(c.__str__())  # Hyd
print(d.__str__())  # Object of c4


class Student:
    def get(self):
        self.rno = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")
        self.marks = []
        for i in range(3):
            self.marks.append(int(input(f"Enter mark {i+1}: ")))

    def compute(self):
        self.total = sum(self.marks)
        self.avg = self.total / 3

        if any(m < 40 for m in self.marks):
            self.grade = "Fail"
        elif self.avg >= 70:
            self.grade = "Distinction"
        elif self.avg >= 60:
            self.grade = "First class"
        elif self.avg >= 50:
            self.grade = "Second class"
        else:
            self.grade = "Third class"

    def disp(self):
        print("Roll Number:", self.rno)
        print("Student Name:", self.name)
        print("Gender:", self.gender)
        print("Total Marks:", self.total)
        print("Average:", self.avg)
        print("Grade:", self.grade)

    def __str__(self):
        return f"{self.rno} {self.name} {self.gender} {self.total} {self.avg} {self.grade}"

# Main
s = Student()
s.get()
s.compute()
s.disp()
print(s)  # uses __str__



import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            self.den = int(input("Denominator cannot be 0. Re-enter: "))

    def __str__(self):
        return f"{self.num}/{self.den}"

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
            self.den = 0   # invalid
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

# Main
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("First Rational Number")
a.get()
print("Second Rational Number")
b.get()

c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

print("Sum =", c)
print("Difference =", d)
print("Product =", e)

if f.den != 0:
    print("Division =", f)
else:
    print("Division is not permitted")

