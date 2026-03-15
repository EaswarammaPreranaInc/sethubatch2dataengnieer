# How to reuse mod2? (Home work)
print('Hello')                  # Hello
import mod2                     # How to import mod2
print(mod2.x)                   # How to print variable 'x' of mod2
mod2.f1()                       # How to call function f1() of mod2
print('Bye')                    # Bye
import mod4
print(x)                        # error if x not in current module/mod4
f1()                            # error if f1 not in current module/mod4

# Find outputs (Home work)
print('Before')                 # Before
# python mod2.py                # How to run mod2
print(mod2.x)                   # prints value of x from mod2
mod2.f1()                       # calls f1 function from mod2
print('After')                  # After
# run_module('mod2')            # error (run_module not defined)
# runpy.run_module(mod2)        # error (runpy not imported, mod2 must be a string)

# cal.py module has:
# x = 100, y = 200
# add(), sub(), mul(), div(), c1 class

# How to use members of cal module with from statement?
print('Begin')                  # Begin
from cal import *               # imports all members in __all__ of cal
print(x)                        # 100
print(y)                        # 200
print(cal.x)                    # error, cal not imported as module with from ... import *
print(add(10, 7))               # 17
print(sub(10, 7))               # 3
print(mul(10, 7))               # 70
print(div(10, 7))               # 1.4285714285714286
print(add(x, y))                # 300
b = c1()
b.m1()                          # m1 method

# How to import only x, add, mul, and c1 from cal?
print('Begin')                  # Begin
from cal import x, add, mul, c1
print(x)                        # 100
print(y)                        # error
print(add(10, 7))               # 17
print(sub(10, 7))               # error
print(mul(10, 7))               # 70
print(div(10, 7))               # error
b = c1()
b.m1()                          # m1 method

# Module alias
print('Begin')                  # Begin
import cal as C                 # import cal module with alias C
print(C.x)                      # 100
print(C.y)                      # 200
print(C.add(10, 7))             # 17
print(C.sub(10, 7))             # 3
print(C.mul(10, 7))             # 70
print(C.div(10, 7))             # 1.4285714285714286
b = C.c1()
b.m1()                          # m1 method
from math import *              # correct import for math

# Member alias
from cal import x as x1, add as add1, mul as mul1, c1 as c1class
print(x1)                       # 100
print(add1(10, 7))              # 17
print(mul1(10, 7))              # 70
b = c1class()
b.m1()                          # m1 method

# mod1.py members: x, disp(), c1 class

# mod2.py members: x, disp(), c1 class

# Find outputs (Home work)
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
from mod2 import *
from mod1 import *
print(x)                        # 10 (from mod1) or 20 (from mod2), as last imported overwrites
disp()                          # disp function of same module
a = c1()
a.m1()                          # m1 method of class c1 in same module

# Find outputs (Home work)
from mod1 import *
from mod2 import *
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(x)                        # 30
disp()                          # disp function of same module
a = c1()
a.m1()                          # m1 method of class c1 in same module

# How to use members of all three modules with import statement?
import mod1
import mod2
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(mod1.x)                   # x from mod1
mod1.disp()                     # disp from mod1
b = mod1.c1(); b.m1()           # m1 from mod1.c1
print()
print(mod2.x)                   # x from mod2
mod2.disp()                     # disp from mod2
b = mod2.c1(); b.m1()           # m1 from mod2.c1
print()
print(x)                        # 30 (current module)
disp()                          # disp from current module
c = c1(); c.m1()                # m1 from current module

# How to use members of all the three modules with from statement?
from mod1 import *
from mod2 import *
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(x)                        # 30 or overwritten (last imported x)
disp()                          # disp function of same module
a = c1(); a.m1()                # m1 from current module

# mod1.py (Home work)
if __name__ == "__main__":
    print('One')
    print('Two')
    print('Three')
    print('Four')
    print('Five')
    print('Six')
    print('Seven')
    print('Eight')
    print('Nine')
# py mod1.py runs all above prints
# When imported, none printed.

# Find outputs (Home work)
print('Begining of mod2')        # Begining of mod2
import mod1                     # prints as above if run as script
print('End of mod2')            # End of mod2

# _all_ in cal.py controls imported members for from cal import *

# Find outputs
from cal import *
print(x)                        # 100
print(y)                        # 200
print(add(10, 7))               # 17
print(sub(10, 7))               # 3
print(mul(10, 7))               # 70
print(div(10, 7))               # 1.4285714285714286
a = c1()
a.m1()                          # m1 method

# Find outputs
import cal
print(cal.x)                    # 100
print(cal.y)                    # 200
print(cal.add(10, 7))           # 17
print(cal.sub(10, 7))           # 3
print(cal.mul(10, 7))           # 70
print(cal.div(10, 7))           # 1.4285714285714286
a = cal.c1()
a.m1()                          # m1 method

# Find outputs
from cal import y, sub, mul
print(x)                        # error
print(y)                        # 200
print(add(10, 7))               # error
print(sub(10, 7))               # 3
print(mul(10, 7))               # 70
print(div(10, 7))               # error
a = c1()
# error if c1 not imported

# mod1.py (Home work)
print('Hyd')# Hyd
print('Sec')# Sec
print('Cyb')# Cyb
print('India')
print('USA')

# Find outputs (Home work)
import mod1
import mod1
import mod1
# Hyd \n Sec \n Cyb

# reload() function demo program (Home work)
import importlib
import mod1
print()# (prints blank line)
importlib.reload(mod1)
print()# blank line
importlib.reload(mod1)
importlib.reload('mod1')# error
reload(mod1)# error 
