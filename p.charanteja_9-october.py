# 1. Nested Classes — Method Calls

class outer:
    def __init__(self):
        print('Outer class constructor')
    def m1(self):
        print('Outer class method')
    class inner:
        def __init__(self):
            print('Inner class constructor')
        def m1(self):
'''            print('Inner class method')
output:
    Inner class constructor
    Inner class method
'''






# 2. Initializing and Printing Emp Class

class emp:
    def __init__(self):
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0
        self.d = emp.date()
    def disp(self):
        print(self.empno, self.ename, self.sal)
        self.d.disp()
    class date:
        def __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947
        def disp(self):
            print(self.dd, self.mm, self.yy)

    e = emp()
    e.disp()
    #Output:
    ```
    25 Rama Rao 10000.0
    15 8 1947
    ```





# 3. Nested Inner Classes with disp

class outer:
    def __init__(self):
        self.x = 25
        self.i1 = outer.inner1()
        self.i2 = outer.inner2()
    def disp(self):
        print(self.x)
    class inner1:
        def disp(self):
            print('1st inner class method')
    class inner2:
        def disp(self):
            print('2nd inner class method')
o = outer()
o.disp()         # 25
o.i1.disp()      # 1st inner class method
o.i2.disp()      # 2nd inner class method
'''
output:
25
1st inner class method
2nd inner class method
'''






# 4. Outer and Inner Class Instantiations

class c1:
    def __init__(self):
        print('outer class c1 constructor')
    class c2:
        def __init__(self):
            print('inner class c2 constructor')
class c2:
    def __init__(self):
        print('outer class c2 constructor')
# Create c1 object:
a = c1()                # outer class c1 constructor
# Create inner c2 object:
b = c1.c2()             # inner class c2 constructor
# Create outer c2 object:
c = c2()                # outer class c2 constructor
'''
output:
outer class c1 constructor
inner class c2 constructor
outer class c2 constructor
'''






# 5. Outer and Inner c2 in the same class

class c2:
    def __init__(self):
        print('outer class constructor')
    class c2:
        def __init__(self):
            print('inner class constructor')
a = c2()                # outer
b = c2.c2()             # inner
c2.c2()                 # inner
'''
output:
outer class constructor
inner class constructor
inner class constructor
'''







# 6. Class with Static and Instance Variables

class c1:
    x = 10
    def __init__(self):
        self.y = 20
a = c1()
b = c1()
a.x += 1       # changes class variable for the a instance only (makes a's x = 11, doesn't affect b.x or c1.x)
b.y += 1       # b.y becomes 21
print(a.x)     # 11 (shadowed from class variable on instance)
print(a.y)     # 20
print(b.x)     # 10 (class variable)
print(b.y)     # 21
print(c1.x)    # 10 (class variable)
print(a.__dict__)    # {'y': 20, 'x': 11}
print(b.__dict__)    # {'y': 21}
print(c1.__dict__)   # shows class attributes (including x)
'''
output:
11
20
10
21
10
{'y': 20, 'x': 11}
{'y': 21}
{'__module__': '__main__', 'x': 10, '__init__': <function>, ...}
'''






# 7. Class — Changing Variable via Method

class c1:
    x = 10
    def m1(self):
        self.x = 20
a = c1()
a.m1()
print(c1.x)   # 10
print(a.x)    # 20 (instance var created/overridden at obj level)
'''
output:
10
20
'''






# 8. Class with @classmethod, @staticmethod, and Variables

class c1:
    x = 10
    def __init__(self):
        self.y = 20
    @classmethod
    def m1(cls):
        cls.x = 30
        cls.y = 40
a = c1()
b = c1()
c1.m1()
print(a.x)          # 30
print(a.y)          # 20
print(b.x)          # 30
print(b.y)          # 20
print(c1.x, c1.y)   # 30 40 (c1.y was created in class)
# The next lines will produce errors unless in m1 the y was set on class
# print(cls.x, cls.y)      # Error, 'cls' not defined in this context
# print(self.x, self.y)    # Error, 'self' not defined in this context







# 9. Static Method with One Parameter

class c1:
    @staticmethod
    def m1(self):
        print(self)
c1.m1(25)           # 25
a = c1()
a.m1(35)            # 35









# 10. Instance Method Invoked as Class and Instance

class c1:
    def m1(self):
        print(self)
c1.m1(25)       # 25 printed as self 
a = c1()
a.m1()          # <__main__.c1 object at ...>
a.m1(35)        # Error: m1() takes 1 positional argument but 2 were given






# 11. Static/Instance Method Overlapping Names

class c1:
    @staticmethod
    def m1(self):
        print('static method')
        print(self)
    def m1(self):
        print('static / instance method')
        print(self)
# The instance method m1 overrides the static one.
c1.m1(25)   # static / instance method, prints 25
a = c1()
a.m1()      # static / instance method, prints <__main__.c1 object at ...>







# 12. Ways to Access and Add Static Variables

class c1:
    x = 25
    def __init__(self):
        print(c1.x)
        print(self.x)
    def m1(self):
        print(c1.x)
        print(self.x)
    @classmethod
    def m2(cls):
        print(c1.x)
        print(cls.x)
    @staticmethod
    def m3():
        print(c1.x)
c1.x                   # 25
self.x, cls.x          
# Method calls:
o = c1()
o.m1()
c1.m2()
c1.m3()
'''
output:
All print `25`.
'''


# 13. Adding Static/Instance Variables at Different Locations

class c1:
    a = 10  # at class level
    def __init__(self):
        c1.b = 20                # at constructor
        self.c = 30              # instance var
        c1.k = 25
    def m1(self):
        c1.d = 40                # static in instance method
        self.e = 50              # instance var
    @classmethod
    def m2(cls):
        cls.f = 60
        c1.g = 70                # another way
    @staticmethod
    def m3():
        c1.h = 80
print('Begin')
print(c1.__dict__)
x = c1()
print('Constructor')
print(c1.__dict__)
x.m1()
print('Instance method m1')
print(c1.__dict__)
c1.m2()
print('class method m2')
print(c1.__dict__)
c1.m3()
print('static method m3')
print(c1.__dict__)
c1.i = 90
x.j = 100
print('Outside the class')
print(c1.__dict__)
print("Object  'x' ")
print(x.__dict__)
'''
output:

- Static variables added: `a, b, k, d, f, g, h, i`
- Instance variables: `c, e, j`
'''






# 14. Class Unpacking Assignment

class c1:
    a, b, c = range(1, 4)
print(c1.a)    # 1
print(c1.b)    # 2
print(c1.c)    # 3
'''
output:
1
2
3
'''






# 15. Tricky Program — Test Class (Inputs: 10, 20, 30, 40, 50, 60, 70)

class Test:
    @classmethod
    def get1(cls):
        cls.x = int(input('Enter any number : '))
    def get2(self):
        self.y = int(input('Enter any number : '))
        self.z = int(input('Enter any number : '))
    def compute(self):
        Test.x += 1
        self.y += 1
        self.z += 1
        self.x = Test.x + 1
    def disp(self):
        print(Test.x, self.y, self.z, self.x, sep='\t')

# Execution part:
Test.get1()
a = Test()
b = Test()
c = Test()
a.get2()
b.get2()
c.get2()
a.compute()
b.compute()
c.compute()
a.disp()
b.disp()
c.disp()
```

## Inputs to give (in order):

```
10    # for Test.x via get1
20    # for a.y via a.get2
30    # for a.z via a.get2
40    # for b.y via b.get2
50    # for b.z via b.get2
60    # for c.y via c.get2
70    # for c.z via c.get2
```
## Final Outputs (from disp):

```
13    21    31    12
13    41    51    13
13    61    71    14
```







# 16. Adding Vectors

class vector:
    @staticmethod
    def get1():
        vector.n = int(input())
    def get2(self):
        self.a = [int(x) for x in input().split()]
    def add(self, x, y):
        self.a = [x.a[i] + y.a[i] for i in range(vector.n)]

vector.get1()     # input n
x = vector()
x.get2()          # input list
y = vector()
y.get2()          # input list
z = vector()
z.add(x, y)
print(z.a)


#Output: Sums elementwise lists of `x.a` and `y.a`.







# 17. Print Static variables from __dict__

class c1:
    x = 1
    y = 2
    z = 3
vars = {k:v for k, v in c1.__dict__.items() if not k.startswith('__') and not k.endswith('__')}
print(vars)
'''
Output:
{'x': 1, 'y': 2, 'z': 3}
'''







# 18. Variable Classifications

class c1:
    x = 10              # static   (class variable)
    def m1(self):
        self.y = 20     # instance var
        z = 30          # local variable
        c1.m = 40       # static var
def f1():
    a = c1()
    a.p = 50            # instance var
    c1.q = 60           # static var
    s = 70              # local variable
k = 80                  # global variable
c1.l = 90               # static var
b = c1()
b.n = 100               # instance var
'''
- k = global
- l, m, q = static (class)
- x = static (class)
- y, p, n = instance
- z, s = local
'''







