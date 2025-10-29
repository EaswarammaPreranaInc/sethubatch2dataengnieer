# Clean, runnable examples for nested/inner classes and related OOP concepts

# Example 1: outer class with nested inner class
class Outer:
    def __init__(self):
        print('Outer class constructor')
        self.x = 25

    def m1(self):
        print('Outer class method, x =', self.x)

    class Inner:
        def __init__(self):
            print('Inner class constructor')

        def m1(self):
            print('Inner class method')


print('--- Example 1: nested class usage ---')
# create an Outer object
a = Outer()
a.m1()
# 1) Create inner using outer instance
i = a.Inner()
i.m1()
# 2) Create inner directly from class
j = Outer.Inner()
j.m1()
# 3) One-line call
Outer.Inner().m1()


# Example 2: emp with nested date class
class Emp:
    def __init__(self, empno=25, ename='Rama Rao', sal=10000.0):
        self.empno = empno
        self.ename = ename
        self.sal = sal
        self.hire_date = Emp.Date(15, 8, 1947)

    def disp(self):
        print(f'Empno: {self.empno}, Name: {self.ename}, Salary: {self.sal}')
        print('Hire date:', end=' ')
        self.hire_date.disp()

    class Date:
        def __init__(self, dd=1, mm=1, yy=2000):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def disp(self):
            print(f'{self.dd:02d}-{self.mm:02d}-{self.yy}')


print('\n--- Example 2: Emp and nested Date ---')
e = Emp()
e.disp()

# Example 3: class (static) vs instance variables
class C1:
    x = 10  # class variable

    def __init__(self):
        self.y = 20  # instance variable

    def m1(self):
        # setting instance attribute x will shadow class attribute for this instance
        self.x = 20

print('\n--- Example 3: class vs instance variables ---')
a = C1()
b = C1()
a.x += 1  # modifies class variable because attribute lookup finds class attr and assignment to a.x creates instance attr? careful
# actually a.x += 1 will create instance attribute 'x' with value 11 in Python
b.y += 1
print('a.x =', getattr(a, 'x'))
print('a.y =', getattr(a, 'y'))
print('b.x =', getattr(b, 'x'))
print('b.y =', getattr(b, 'y'))
print('C1.x =', C1.x)

# Example 4: classmethod and staticmethod
class C2:
    x = 10

    @classmethod
    def set_x(cls, value):
        cls.x = value

    @staticmethod
    def static_print(msg):
        print('static_print:', msg)

print('\n--- Example 4: classmethod and staticmethod ---')
C2.static_print('hello')
C2.set_x(30)
print('C2.x =', C2.x)

print('\nAll examples finished.')
