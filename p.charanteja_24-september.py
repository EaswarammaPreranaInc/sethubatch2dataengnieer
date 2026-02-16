# Create the triangle object
t = triangle()

# Call get() method using class name
triangle.get(t)

# Call test() method using class name
triangle.test(t)

# Call area() and peri() methods using class name and print results
print('Area :', triangle.area(t))
print('Perimeter :', triangle.peri(t))






# `c1` Class Output Analysis

class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)
        print(self.x)
        x += 5
        self.x += 7
    def m2(self):
        print(x)
        print(self.x)
        self.x += 6

a = c1()
a.m1()
a.m2()
print(a.x)
print(self.x)
print(x)
'''
Outputs & Explanations:
- `a.m1()`:  
    - prints `10` (`x`)  
    - prints `20` (`self.x`)  
    - Then `x` becomes 15 and `self.x` becomes 27, but only updated in instance attribute and local variable.
- `a.m2()`:  
    - Error: `x` is not defined globally or in the method, so `print(x)` will raise a `NameError`.
'''




# Program to Add Two Objects (Object Contains Three Values)
## Class and Methods Structure

class Test:
    def get(self):
        self.x = int(input('Enter x: '))
        self.y = int(input('Enter y: '))
        self.z = int(input('Enter z: '))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(f'x = {self.x}, y = {self.y}, z = {self.z}')

# Create objects a, b, c
a = Test()
b = Test()
c = Test()

print('First Object')
a.get()
print('Second Object')
b.get()
c.add(a, b)
print('Addition results')
c.disp()








# `Date` Class Output

class Date:
    pass

a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)

#Output: The `print(a)` statement prints the default object representation.






# `c1`, `c2`, `c3`, `c4` _str_ Output

Note: All methods should be `__str__`, not `_str_`.

- `print(a)` and `print(b)`: Calls `_str_` (incorrect spelling, so default object representation is printed).
- `print(c)`: Same, default object representation.
- `print(d)`: Same.
- `print(b._str_())`: Returns `35`.
- `print(c._str_())`: Prints 'Hyd' but returns None.
- `print(d._str_(50))`: Returns "50".








# Student Class: Total, Average, and Grade

class Student:
    def get(self):
        self.rno = int(input('Enter roll number: '))
        self.name = input('Enter name: ')
        self.gender = input('Enter gender: ')
        self.marks = [int(input('Enter mark: ')) for _ in range(3)]

    def compute(self):
        self.total = sum(self.marks)
        self.avg = self.total / 3.0
        if min(self.marks) < 40:
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
        print('Roll Number:', self.rno)
        print('Student Name:', self.name)
        print('Gender:', self.gender)
        print('Total Marks:', self.total)
        print('Average:', self.avg)
        print('Grade:', self.grade)

    def __str__(self):
        return f'{self.rno}, {self.name}, {self.gender}, {self.total}, {self.avg}, {self.grade}'

# Usage
s = Student()
s.get()
s.compute()
s.disp()            # Method call
print(str(s))       # __str__ method










# Example: Operations on Rational Numbers

import math

class Rat:
    def get(self):
        self.num = int(input('Enter numerator: '))
        self.den = int(input('Enter denominator: '))
        self.test()

    def test(self):
        while self.den == 0:
            self.den = int(input('Denominator zero! Reenter denominator: '))

    def __str__(self):
        return f'{self.num} / {self.den}'

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
        self.num = a.num * b.den
        self.den = a.den * b.num
        self.simplify()

    def simplify(self):
        if self.num != 0:
            g = math.gcd(abs(self.num), abs(self.den))
            self.num //= g
            self.den //= g

a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print('Enter first rational number')
a.get()
print('Enter second rational number')
b.get()
c.add(a, b)
d.sub(a, b)
e.mul(a, b)

if b.num != 0:
    f.div(a, b)
    print('Sum:', c)
    print('Difference:', d)
    print('Product:', e)
    print('Division:', f)
else:
    print('Sum:', c)
    print('Difference:', d)
    print('Product:', e)
    print('Division is not permitted')
