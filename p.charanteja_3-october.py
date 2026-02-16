# 1. Reference Count Program

import sys
class c1:
    pass
# End of the class
a = b = c = d = c1()
print(sys.getrefcount(b))          # 5
print(sys.getrefcount(c1()))       # 1
print(sys.getrefcount(352))        # 3
print(sys.getrefcount([10, 20, 15, 18]))   # 1
print(sys.getrefcount(10.8))       # 3
print(sys.getrefcount({10, 20, 15, 18}))   # 1
print(sys.getrefcount('Hyd'))      # 3
print(sys.getrefcount({10: 20, 30: 40}))   # 1
print(sys.getrefcount((10, 20, 30, 40)))   # 2






# 2. Constructor and Destructor Output

import sys
class Test:
    def __init__(self):
        print('Constructor  :  ', id(self))    # Constructor  :  <id>
        return None
    def __del__(self):
        print('Destructor  :  ', id(self))     # Destructor  :  <id>
        return 25
# End of the class
t = Test()
print(t.__init__())                # None (since __init__ returns None)
print(sys.getrefcount(t))          # 2
print(t.__del__())                 # Destructor  :  <id> \n 25
print(sys.getrefcount(t))          # 2
print('Bye')                       # Bye







# 3. Tricky Program 1

class c1:
    def __init__(self):
        print('Object is created')            # Object is created
    def __del__(self):
        print('Object is lost')
# End of the class
def f1():
    print('Function Begin')                   # Function Begin
    a = c1()
    print(a)                                 # <__main__.c1 object at ...>
    print('Function end')                    # Function end
    return a

print('Program Begin')                       # Program Begin
b = f1()
print(b)                                    # <__main__.c1 object at ...>
print('Program End')                        # Program End









# 4. Tricky Program 2

class c1:
    def __init__(self):
        print('Object is created')            # Object is created
    def __del__(self):
        print('Object is lost')
# End of the class
def f1():
    print('Function begin')                   # Function begin
    a = c1()
    print('Function end')                     # Function end
    return a
print('Program Begin')                        # Program Begin
f1()
print('Program End')                          # Program End
# After "Program End", "Object is lost" is printed (a is unreferenced after function exits)







# 5. Tricky Program 3

class c1:
    def __init__(self):
        print('Object is created')            # Object is created
    def __del__(self):
        print('Object is lost')
# End of the class
def f1():
    print('Function begin')                   # Function begin
    a = c1()
    print('Function end')                     # Function end
print('Program Begin')                        # Program Begin
b = f1()
print(b)                                     # None
print('Program End')                         # Program End
# After "Program End", "Object is lost" is printed






# 6. Circular Reference

class c1:
    def __init__(self, k):
        print('c1 class object is created')   # c1 class object is created
        self.b = k
        print('End of c1 class constructor')  # End of c1 class constructor
    def __del__(self):
        print('c1 class object is lost')
# End of class c1
class c2:
    def __init__(self):
        print('c2 class object is created')   # c2 class object is created
        self.a = c1(self)
        print('End of c2 class constructor')  # End of c2 class constructor
    def __del__(self):
        print('c2 class object is lost')
# End of class c2
print('Program begin')                        # Program begin
x = c2()
print('program end')                          # program end
# Destructors may NOT be called immediately due to circular reference, depends on Python's GC







# 7. Lucky Object

class c1:
    def __del__(self):
        print('Destructor')                    # Destructor
        global b
        b = self
a = c1()
del a
print('Hello')                                # Hello
# Destructor executes before Hello, and global variable b now refers to the object
