# Find outputs
class Rat:
    def _init_(self , nr1 = 22, dr1 = 7):
        self.nr = nr1
        self.dr = dr1
    def _str_(self):
        return f'{self.nr} / {self.dr}'

a = Rat()
b = Rat(9)
c = Rat(5, 8)
d = Rat(dr1=9)
e = Rat(dr1=3, nr1=2)
x = 11   # input
y = 15   # input
f = Rat(x, y)
print('a : ', a)
print('b : ', b)
print('c : ', c)
print('d : ', d)
print('e : ', e)
print('f : ', f)
c._init_()
print('c : ', c)
a._init_(3.8, 4.6)
print('a : ', a)
g = Rat(nr1=9, 5)     # Error: positional arg follows keyword
h = Rat(nr=9, dr=5)   # Error: unexpected keyword 'nr'

Output:
a :  22 / 7
b :  9 / 7
c :  5 / 8
d :  22 / 9
e :  2 / 3
f :  11 / 15
c :  22 / 7
a :  3.8 / 4.6
Error at g (SyntaxError) and h (TypeError)

-------------------------------------------------------

# Find outputs (Home work)
class Date:
    def _init_(self, dd1, mm1, yy1):
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1

a = Date(15, 8, 1947)
b = Date(yy1=1950, mm1=1, dd1=26)
c = Date(mm1=7, dd1=19, yy1=1985)
print('a : ', a._dict_)
print('b : ', b._dict_)
print('c : ', c._dict_)
d = Date()                        # Error: missing args
e = Date(dd=30, mm=4, yy=2022)    # Error: unexpected keywords
f = Date(dd1=26, mm1=8, 2023)     # Error: positional arg follows keyword

Output:
a :  {'dd': 15, 'mm': 8, 'yy': 1947}
b :  {'dd': 26, 'mm': 1, 'yy': 1950}
c :  {'dd': 19, 'mm': 7, 'yy': 1985}
Then errors at d, e, f

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('c1 class constructor')
        return 25
class c2:
    def _init_(self):
        print('c2 class constructor')
        return None
class c3:
    def _init_(self):
        print('c3 class constructor')

a = c1()        # Error: cannot return in _init_
b = c2()        # Error: cannot return in _init_
print(b)
print(b._init_())
c = c3()
print(c._init_())

Output:
TypeError: _init_() should return None, not 'int'/'NoneType'

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('Constructor')
        b = c1()
a = c1()

Output:
Infinite recursion → RecursionError

-------------------------------------------------------

# Difference between init() and _init_() (Home work)
class c1:
    def _init_(self):
        print('Constructor')
        self.x = 10
        self.y = 20
class c2:
    def init(self):
        print('Method')
        self.x = 30
        self.y = 40

a = c1()
print(a._dict_)
b = c2()
print(b._dict_)
b.init()
print(b._dict_)

Output:
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        self.a = 10
    def m1(self):
        self.b = 20
class c2:
    def m3(self):
        x.e = 50
def f1():
    x.c = 30

x = c1()
print(x._dict_)
x.m1()
print(x._dict_)
f1()
print(x._dict_)
x.d = 40
print(x._dict_)
y = c2()
y.m3()
print(x._dict_)
z = c1()
print(z._dict_)

Output:
{'a': 10}
{'a': 10, 'b': 20}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
{'a': 10}

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        self.x = 10
        self.y = 20
        self.z = 30
a = c1()
b = c1()
print(a._dict_)
print(b._dict_)
del a.x
del b.y
print(a._dict_)
print(b._dict_)
print(a.x)   # Error
print(b.y)   # Error

Output:
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}
AttributeError on a.x and b.y

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('1st constructor')
    def _init_(self):
        print('2nd constructor')
    def _init_(self):
        print('3rd constructor')
a = c1()

Output:
3rd constructor

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('No argument constructor')
    def _init_(self, x):
        print('single argument constructor : ', x)
    def _init_(self, x, y):
        print('Two argument constructor : ', x, y)
a = c1(10, 20)
b = c1(30)    # Error
c = c1()      # Error

Output:
Two argument constructor : 10 20
TypeError at b, c

-------------------------------------------------------

# Find outputs
class c1:
    def _init_(self, x=100, y=200):
        print('Two argument constructor : ', x, y)
a = c1(10, 20)
b = c1(30)
c = c1()

Output:
Two argument constructor : 10 20
Two argument constructor : 30 200
Two argument constructor : 100 200

-------------------------------------------------------

# What happens when function and class have same name?
def f1():
    print('Function')
    return 25
class f1:
    def _init_(self):
        print('Constructor')
a = f1()
print(a)

Output:
Constructor
<_main_.f1 object at ...>

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('Constructor')
def c1():
    print('Function')
a = c1()
print(a)

Output:
Function
None

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('Constructor')
def c1(x):
    print('Function : ', x)
a = c1()
b = c1(25)
print(b)

Output:
TypeError: c1() missing 1 required positional arg

-------------------------------------------------------

# Find outputs (Home work)
from prog9a import c1
class c1:
    def _init_(self):
        print('c1 class of prog9b')
a = c1()

Output:
c1 class of prog9b

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('c1 class of prog9c')
from prog9a import c1
a = c1()

Output:
Depends on prog9a.c1 definition

-------------------------------------------------------

# Destructor tricky program
class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(f'Object at address {id(self)} is lost')

a = c1()
a = None
b = c1()
del b
c = c1()
c = c1()
d = c1()
e = c1()

Output:
Object created at addresses (1000..)
Object lost messages when reassigned/deleted

-------------------------------------------------------

# Identify Error (Home work)
class c1:
    def _del_(self, x):
        print('destructor : ', x)
a = c1()
a._del_(25)

Output:
TypeError: _del_() takes 2 positional arguments but 1 given

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _del_(self, x=35):
        print('destructor : ', x)
a = c1()
a._del_(25)

Output:
destructor : 25

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _del_(self):
        print('destructor')
        b = c1()
a = c1()

Output:
Destructor recursion until program ends

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('constructor')
        del self
    def _del_(self):
        print('destructor')
        b = c1()
a = c1()

Output:
constructor
destructor
constructor
... (infinite recursion)

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _del_(self):
        print('1st destructor')
    def _del_(self):
        print('2nd destructor')
    def _del_(self):
        print('3rd destructor')
a = c1()

Output:
3rd destructor (when deleted at end)

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(f'Object at address {id(self)} is lost ')
c = b = a = c1()
del a
print('Hello')
del b
print('Hi')
del c
print('Bye')
d = c1()
print('End')

Output:
Object created...
Hello
Hi
Object lost ...
Bye
Object created...
End
Object lost ... (for d at program end)

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(f'Object at address {id(self)} is lost ')
list = [c1(), c1(), c1()]
del list

Output:
Object created thrice
All destructors called

-------------------------------------------------------

# Find outputs (Home work)
class c1:
    def _del_(self):
        print('destructor')
        return 25
a = c1()
print(a._del_())
print('Hello')
del a

Output:
destructor
25
Hello
destructor
