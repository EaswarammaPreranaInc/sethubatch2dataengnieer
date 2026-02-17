#TARUN BANALA   CONSTRUCTORS    29-09-2025
# Find outputs
class Rat:
    def _init_(self, nr1=22, dr1=7):  # Constructor with double underscore missing
        self.nr = nr1
        self.dr = dr1
    def _str_(self):  # String method with double underscore missing
        return F'{self.nr} / {self.dr}'
#end of the class

a = Rat()  # Error: _init_ not called, object created but attributes not set
b = Rat(9)  # Serror
c = Rat(5, 8)  #error
d = Rat(dr1=9)  # Same error
e = Rat(dr1=3, nr1=2)  # Same error
x = eval(input('Enter numerator: ')) # x=11
y = eval(input('Enter Denominator: '))  # y=15
f = Rat(x, y)  # Same error

print('a: ', a)  # Prints default object representation: <__main__.Rat object at 0x...>
print('b: ', b)  # Prints default object representation: <__main__.Rat object at 0x...>
print('c: ', c)  # Prints default object representation: <__main__.Rat object at 0x...>
print('d: ', d)  # Prints default object representation: <__main__.Rat object at 0x...>
print('e: ', e)  # Prints default object representation: <__main__.Rat object at 0x...>
print('f: ', f)  # Prints default object representation: <__main__.Rat object at 0x...>

c._init_()  # Manually calls _init_ method
print('c: ', c)  # Now prints: 22 / 7

a._init_(3.8, 4.6)  # Manually calls _init_ with floats
print('a: ', a)  # Prints: 3.8 / 4.6

g = Rat(nr1=9, 5)  # SyntaxError: positional argument follows keyword argument
h = Rat(nr=9, dr=5)  # TypeError: _init_ got unexpected keyword arguments

# Find outputs (Home work) - Date class
class Date:
    def _init_(self, dd1, mm1, yy1):  # Constructor missing double underscores
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1

a = Date(15, 8, 1947)  # Works: creates object with dd=15, mm=8, yy=1947
b = Date(yy1=1950, mm1=1, dd1=26)  # Works: creates object with dd=26, mm=1, yy=1950
c = Date(mm1=7, dd1=19, yy1=1985)  # Works: creates object with dd=19, mm=7, yy=1985

print('a: ', a._dict_)  # Prints: {'dd': 15, 'mm': 8, 'yy': 1947}
print('b: ', b._dict_)  # Prints: {'dd': 26, 'mm': 1, 'yy': 1950}
print('c: ', c._dict_)  # Prints: {'dd': 19, 'mm': 7, 'yy': 1985}

d = Date()  # TypeError: missing 3 required positional arguments
e = Date(dd=30, mm=4, yy=2022)  # TypeError: unexpected keyword arguments
f = Date(dd1=26, mm1=8, 2023)  # SyntaxError: positional argument follows keyword argument

# Find outputs (Home work) - Constructor return values
class c1:
    def _init_(self):  # Constructor cannot return non-None value
        print('c1 class constructor')
        return 25  # TypeError: __init__ should return None

class c2:
    def _init_(self):
        print('c2 class constructor')
        return None  # This works

class c3:
    def _init_(self):
        print('c3 class constructor')

a = c1()  # TypeError: __init__ should return None
b = c2()  # Prints: c2 class constructor
print(b)  # Prints: <__main__.c2 object at 0x...>
print(b._init_())  # Prints: c2 class constructor, then None
c = c3()  # Prints: c3 class constructor
print(c._init_())  # Prints: c3 class constructor, then None

# Find outputs (Home work) - Recursive constructor
class c1:
    def _init_(self):
        print('Constructor')
        b = c1()  # Infinite recursion

a = c1()  # RecursionError: maximum recursion depth exceeded

# Difference between init() and _init_() methods
class c1:
    def _init_(self):  # Constructor (but with wrong name)
        print('Constructor')
        self.x = 10
        self.y = 20

class c2:
    def init(self):  # Regular method
        print('Method')
        self.x = 30
        self.y = 40

a = c1()  # Prints: Constructor
print(a._dict_)  # Prints: {'x': 10, 'y': 20}
b = c2()  # No output
print(b._dict_)  # Prints: {} (empty dictionary)
b.init()  # Prints: Method
print(b._dict_)  # Prints: {'x': 30, 'y': 40}

# Find outputs (Home work) - Dynamic attribute creation
class c1:
    def _init_(self):
        self.a = 10
    def m1(self):
        self.b = 20

class c2:
    def m3(self):
        x.e = 50  # Adds attribute to global x object

def f1():
    x.c = 30  # Adds attribute to global x object

x = c1()
print(x._dict_)  # Prints: {'a': 10}
x.m1()
print(x._dict_)  # Prints: {'a': 10, 'b': 20}
f1()
print(x._dict_)  # Prints: {'a': 10, 'b': 20, 'c': 30}
x.d = 40
print(x._dict_)  # Prints: {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y.m3()  # Adds attribute e to x object
print(x._dict_)  # Prints: {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z._dict_)  # Prints: {'a': 10}

# Find outputs (Home work) - Attribute deletion
class c1:
    def _init_(self):
        self.x = 10
        self.y = 20
        self.z = 30

a = c1()
b = c1()
print(a._dict_)  # Prints: {'x': 10, 'y': 20, 'z': 30}
print(b._dict_)  # Prints: {'x': 10, 'y': 20, 'z': 30}
del a.x  # Deletes x from a
del b.y  # Deletes y from b
print(a._dict_)  # Prints: {'y': 20, 'z': 30}
print(b._dict_)  # Prints: {'x': 10, 'z': 30}
print(a.x)  # AttributeError: 'c1' object has no attribute 'x'
print(b.y)  # AttributeError: 'c1' object has no attribute 'y'

# Find outputs (Home work) - Multiple constructors (last one wins)
class c1:
    def _init_(self):  # This gets overridden
        print('1st constructor')
    def _init_(self):  # This gets overridden
        print('2nd constructor')
    def _init_(self):  # Only this remains
        print('3rd constructor')

a = c1()  # Prints: 3rd constructor

# Find outputs (Home work) - Multiple constructors with different parameters
class c1:
    def _init_(self):  # Overridden
        print('No argument constructor')
    def _init_(self, x):  # Overridden
        print('single argument constructor : ', x)
    def _init_(self, x, y):  # Only this remains
        print('Two argument constructor : ', x, y)

a = c1(10, 20)  # Prints: Two argument constructor : 10 20
b = c1(30)  # TypeError: missing 1 required positional argument
c = c1()  # TypeError: missing 2 required positional arguments

# Find outputs - Multiple constructors with default parameters
class c1:
    def _init_(self):  # Overridden
        print('No argument constructor')
    def _init_(self, x):  # Overridden
        print('single argument constructor : ', x)
    def _init_(self, x=100, y=200):  # Only this remains
        print('Two argument constructor : ', x, y)

a = c1(10, 20)  # Prints: Two argument constructor : 10 20
b = c1(30)  # Prints: Two argument constructor : 30 200
c = c1()  # Prints: Two argument constructor : 100 200

# What happens when function and class have same name?
def f1():  # This gets overridden by class
    print('Function')
    return 25

class f1:  # Overrides the function
    def _init_(self):
        print('Constructor')

a = f1()  # Prints: Constructor
print(a)  # Prints: <__main__.f1 object at 0x...>

# Find outputs (Home work) - Function vs Class name conflict
class c1:
    def _init_(self):
        print('Constructor')

def c1():  # This overrides the class
    print('Function')

a = c1()  # TypeError: 'function' object is not callable (as constructor)
print(a)  # Not reached

# Find outputs (Home work) - Function with parameters vs Class
class c1:
    def _init_(self):
        print('Constructor')

def c1(x):  # This overrides the class
    print('Function : ', x)

a = c1()  # TypeError: c1() missing 1 required positional argument
b = c1(25)  # Prints: Function : 25
print(b)  # Prints: None

# Import related examples would require separate files
# Public and Private members demo program
class Test:
    def _init_(self):
        self.x = 10  # Public variable
        self.__y = 20  # Private variable (name mangled to _Test__y)
    
    def m1(self):
        print('m1 method')
        print(self.x)  # Prints: 10
        print(self.__y)  # Prints: 20 (accessible within class)
        self.__m2()  # Calls private method
        print('Back to m1 method')
    
    def __m2(self):  # Private method
        print('__m2 method')
        print(self.x)  # Prints: 10
        print(self.__y)  # Prints: 20

t = Test()
print('Outside')
print(t.x)  # Prints: 10
# print(t.y)  # AttributeError: 'Test' object has no attribute 'y'
# print(t.__y)  # AttributeError: 'Test' object has no attribute '__y'
print(t._dict_)  # Prints: {'x': 10, '_Test__y': 20}
t.m1()  # Calls public method
# t.__m2()  # AttributeError: 'Test' object has no attribute '__m2'

# Find outputs - Name conflicts with public/private
class c1:
    def _init_(self):
        self.x = 10  # Public
        self.__x = 20  # Private (becomes _c1__x)
        self._x_ = 30  # Public dunder
    
    def m1(self):
        print('public method')
    
    def __m1(self):
        print('private method')
    
    def _m1_(self):
        print('public Dunder method')

a = c1()
print(a.x)  # Prints: 10
print(a._x_)  # Prints: 30
# print(a.__x)  # AttributeError: 'c1' object has no attribute '__x'
a.m1()  # Prints: public method
a._m1_()  # Prints: public Dunder method
# a.__m1()  # AttributeError: 'c1' object has no attribute '__m1'

