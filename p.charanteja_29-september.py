# 1. Rat Class Example

class Rat:
    def _init_(self, nr1 = 22, dr1 = 7):
        self.nr = nr1
        self.dr = dr1
    def _str_(self):
        return F'{self.nr} / {self.dr}'
# end of the class

a = Rat()                    # No output (incorrect constructor name, so does not run 'self.nr = ...', instance has no attributes)
b = Rat(9)                   # No output (same issue, arguments ignored)
c = Rat(5, 8)                # No output
d = Rat(dr1=9)               # No output
e = Rat(dr1=3, nr1=2)        # No output

x = eval(input('Enter numerator  :  '))  # Assume input is 11
y = eval(input('Enter Denominator  :  '))    # Assume input is 15
f = Rat(x, y)                 # No output

print('a  :  ', a)            # a : <__main__.Rat object at 0x...>
print('b  :  ', b)            # b : <__main__.Rat object at 0x...>
print('c  :  ', c)            # c : <__main__.Rat object at 0x...>
print('d  :  ', d)            # d : <__main__.Rat object at 0x...>
print('e  :  ', e)            # e : <__main__.Rat object at 0x...>
print('f  :  ', f)            # f : <__main__.Rat object at 0x...>

c._init_()                    # No output
print('c  :  ', c)            # c : <__main__.Rat object at 0x...>

a._init_(3.8, 4.6)            # No output
print('a  :  ', a)            # a : <__main__.Rat object at 0x...>

# g = Rat(nr1=9, 5)           # Error: positional argument after keyword argument
# h = Rat(nr=9, dr=5)         # Error: unexpected keyword arguments







# 2. Date Class Example

class Date:
    def _init_(self, dd1, mm1, yy1):
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1
# End of class

a = Date(15, 8, 1947)           # No output
b = Date(yy1=1950, mm1=1, dd1=26)# No output
c = Date(mm1=7, dd1=19, yy1=1985)# No output

print('a  :  ', a._dict_)       # AttributeError: 'Date' object has no attribute '_dict_'
print('b  :  ', b._dict_)       # AttributeError
print('c  :  ', c._dict_)       # AttributeError

d = Date()                      # TypeError: missing 3 required positional arguments
e = Date(dd=30, mm=4, yy=2022)  # TypeError: unexpected keyword arguments
f = Date(dd1=26, mm1=8, 2023)   # SyntaxError: positional argument after keyword argument







# 3. Constructor Return Values

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

# End of class

a = c1()                        # No output
b = c2()                        # No output
print(b)                        # <__main__.c2 object at 0x...>
print(b._init_())               # c2 class constructor
                                # None
c = c3()                        # No output
print(c._init_())               # c3 class constructor
                                # None







# 4. Constructor Recursion

class c1:
    def _init_(self):
        print('Constructor')
        b = c1()
# End of class
a = c1()                        # No output: because _init_ is not __init__, so nothing prints.








# 5. Difference Between init() and _init_()

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
print(a._dict_)                 # AttributeError: 'c1' object has no attribute '_dict_'
b = c2()
print(b._dict_)                 # AttributeError
b.init()                        # Method
print(b._dict_)                 # AttributeError








# 6. Adding Attributes After Creation

class c1:
    def _init_(self):
        self.a = 10
    def m1(self):
        self.b = 20
# End of class c1

class c2:
    def m3(self):
        x.e = 50
# End of class c2

def f1():
    x.c = 30
# End of function f1

x = c1()
print(x._dict_)                 # AttributeError
x.m1()                          # No output
print(x._dict_)                 # AttributeError
f1()                            # No output
print(x._dict_)                 # AttributeError
x.d = 40
print(x._dict_)                 # AttributeError
y = c2()
y.m3()                          # No output
print(x._dict_)                 # AttributeError
z = c1()
print(z._dict_)                 # AttributeError







# 7. Deleting Attributes

class c1:
    def _init_(self):
        self.x = 10
        self.y = 20
        self.z = 30
# end of the class

a = c1()
b = c1()
print(a._dict_)                 # AttributeError
print(b._dict_)                 # AttributeError
del a.x                         # No output
del b.y                         # No output
print(a._dict_)                 # AttributeError
print(b._dict_)                 # AttributeError
print(a.x)                      # AttributeError
print(b.y)                      # AttributeError








# 8. Overloading Constructors

class c1:
    def _init_(self):
        print('1st constructor')
    def _init_(self):
        print('2nd constructor')
    def _init_(self):
        print('3rd constructor')
# End of the class

a = c1()                        # No output

# Only the last _init_ method exists (previous ones overwritten), but it never runs unless called explicitly.







# 9. Overloading by Arguments

class c1:
    def _init_(self):
        print('No argument constructor')
    def _init_(self, x):
        print('single argument constructor : ', x)
    def _init_(self, x, y):
        print('Two argument constructor : ', x, y)
# End of class

a = c1(10, 20)                  # Error: _init_ is not __init__, no output, no error unless called manually.
b = c1(30)                      # Error
c = c1()                        # Error







# 10. Default Arguments

class c1:
    def _init_(self):
        print('No argument constructor')
    def _init_(self, x):
        print('single argument constructor :', x)
    def _init_(self, x=100, y=200):
        print('Two argument constructor :', x, y)
# End of class

a = c1(10, 20)                  # No output
b = c1(30)                      # No output
c = c1()                        # No output









# 11. Function vs Class Name

def f1():
    print('Function')
    return 25

class f1:
    def _init_(self):
        print('Constructor')
# end of class

a = f1()                        # <__main__.f1 object at 0x...>
print(a)                        # <__main__.f1 object at 0x...>








# 12. Class and Function Same Name

class c1:
    def _init_(self):
        print('Constructor')
def c1():
    print('Function')
# end of class

a = c1()                        # Function
print(a)                        # None







# 13. Class and Function with Argument

class c1:
    def _init_(self):
        print('Constructor')
def c1(x):
    print('Function :', x)
# End of class c1

a = c1()                        # TypeError: c1() missing 1 required positional argument: 'x'
b = c1(25)                      # Function : 25
print(b)                        # None







# 14. prog9a.py Example

class c1:
    def _init_(self):
        print('c1 class of prog9a')
# Save in prog9a.py

# Output:
# No output produced until you manually call c1._init_()







# 15. prog9b Example

from prog9a import c1
class c1:
    def _init_(self):
        print('c1 class of prog9b')
a = c1()
# Output:
# No output. When you create 'a', only the base object is constructed, as _init_ is not called automatically.







# 16. prog9c Example

class c1:
    def _init_(self):
        print('c1 class of prog9c')
from prog9a import c1
a = c1()
# Output:
# No output. The imported c1 from prog9a has the same _init_ error, so nothing prints on object creation.







# 17. prog9d Dual Class

from prog9a import c1
class c1:
    def _init_(self):
        print('c1 class of prog9d')
# To use object of current:
a = c1()                        # No output

# To use object from prog9a:
b = prog9a.c1()                 # No output
'''
Output:  
No output from either `a` or `b`. Both use a class with wrong constructor name.

'''






# 18. prog9e Dual Class

import prog9a
class c1:
    def _init_(self):
        print('c1 class of prog9e')
# Current:
a = c1()                        # No output

# prog9a import:
b = prog9a.c1()                 # No output
'''
Output: 
No output again. Object construction does not trigger print statements.
'''








# 19. Public vs Private Members Example

class Test:
    def _init_(self):
        # self.x = 10   # public
        # self.__y = 20 # private
    def m1(self):
        print('m1 method')
        # print(self.x)
        # print(self.__y)
        # self.__m2()
        print('Back to m1 method')
    def __m2(self):
        print('__m2 method')
        # print(self.x)
        # print(self.__y)
# End of class

t = Test()
print('Outside')
# print(t.x)
# print(t.__y)
print(t._dict_)                 # AttributeError
# t.m1()
# t.__m2()                      # AttributeError; private method
print('End')







# 20. Demo of Private/Public Variables and Methods

class c1:
    def _init_(self):
        # self.x = 10         # public
        # self.__x = 20       # private
        # self._x_ = 30       # dunder

    def m1(self):
        print('public method')

    def __m1(self):
        print('private method')

    def _m1_(self):
        print('public Dunder method')

# End of class

a = c1()
# print(a.x)
# print(a._x_)
# print(a.__x)
print(a.__x)                   # AttributeError
# a.m1()
# a._m1_()
# a.__m1()                      # AttributeError; private
a.__m1()                        # AttributeError







# 21. Tricky Destructor Program

class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(F'Object at address {id(self)} is lost')

a = c1()                        # No output
a = None                        # No output
b = c1()                        # No output
del b                           # No output
c = c1()                        # No output
c = c1()                        # No output
d = c1()                        # No output
e = c1()                        # No output
# Since _init_ and _del_ are not __init__ and __del__, nothing prints.






# 22. Destructor with Argument (Error)

class c1:
    def _del_(self, x):
        print('destructor :', x)

a = c1()
a._del_(25)                     # destructor : 25






# 23. Destructor with Optional Argument

class c1:
    def _del_(self, x=35):
        print('destructor :', x)

a = c1()
a._del_(25)                     # destructor : 25






# 24. Destructor Calling Constructor

class c1:
    def _del_(self):
        print('destructor')
        b = c1()
a = c1()                        # No output






# 25. Constructor Calls Destructor and Self Deletion

class c1:
    def _init_(self):
        print('constructor')
        del self
    def _del_(self):
        print('destructor')
        b = c1()
a = c1()                        # No output







# 26. Multiple Destructors

class c1:
    def _del_(self):
        print('1st destructor')
    def _del_(self):
        print('2nd destructor')
    def _del_(self):
        print('3rd destructor')
# End of class

a = c1()                        # No output







# 27. All References to Same Object (destruction order)

class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(F'Object at address {id(self)} is lost')
# End of class

c = b = a = c1()                # No output
del a
print('Hello')                  # Hello
del b
print('Hi')                     # Hi
del c
print('Bye')                    # Bye
d = c1()                        # No output
print('End')                    # End








# 28. List of c1 Objects

class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(F'Object at address {id(self)} is lost')
# End of class

list = [c1(), c1(), c1()]       # No output
del list                        # No output







# 29. Destructor Returns Value

class c1:
    def _del_(self):
        print('destructor')
        return 25

a = c1()
print(a._del_())                # destructor
                                # 25
print('Hello')                  # Hello
del a                           # No output



