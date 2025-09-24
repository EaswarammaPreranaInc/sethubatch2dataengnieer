


print("Hello")
import mod2
print(mod2.x)          # prints variable x of mod2
mod2.disp()            # calling function of mod2
a = mod2.c1(); a.m1()  # calling class method of mod2
print("Bye")
import mod2 as mod4     # reuse with alias
print(mod4.x)
mod4.disp()
b = mod4.c1(); b.m1()

"""

Hello
20
disp function of mod2
m1 method of class c1 in mod2
Bye
20
disp function of mod2
m1 method of class c1 in mod2
"""



import runpy
print("Before")
runpy.run_module("mod2")
print("After")

"""
Before
# (contents of mod2 executed, nothing printed unless mod2 has prints)
After
"""


import cal
print(cal.x)   # 100
print(cal.y)   # 200
print(cal.add(10,7))  # 17
print(cal.sub(10,7))  # 3
print(cal.mul(10,7))  # 70
print(cal.div(10,7))  # 1.428...
c = cal.c1(); c.m1()

"""
100
200
17
3
70
1.4285714285714286
m1 method
"""



from cal import *
print(x)            # 100
print(y)            # 200
print(add(10,7))    # 17
print(sub(10,7))    # 3
print(mul(10,7))    # 70
print(div(10,7))    # 1.428...
a = c1(); a.m1()



from cal import x, add, mul, c1
print(x)            # 100
print(add(10,7))    # 17
print(mul(10,7))    # 70
b = c1(); b.m1()


print("\nQ6: Module alias")
import cal as mycal
print(mycal.x)         # 100
print(mycal.y)         # 200
print(mycal.add(10,7)) # 17
print(mycal.sub(10,7)) # 3
print(mycal.mul(10,7)) # 70
print(mycal.div(10,7)) # 1.428...
obj = mycal.c1(); obj.m1()


from cal import x as x1, add as plus, mul as times, c1 as myc1
print(x1)          # 100
print(plus(10,7))  # 17
print(times(10,7)) # 70
b = myc1(); b.m1()


x = 30
def disp(): print("disp function of same module")
class c1:
    def m1(self): print("m1 method of class c1 in same module")

from mod2 import *
from mod1 import *

print(x)  # 30 (local variable overrides)
disp()    # disp of same module
a = c1(); a.m1()  # same module class



print("\nQ9: Use all 3 modules with import")
import mod1, mod2
x = 30
def disp(): print("disp function of same module")
class c1:
    def m1(self): print("m1 method of class c1 in same module")

print(mod1.x)     # 10
mod1.disp()
c = mod1.c1(); c.m1()
print(mod2.x)     # 20
mod2.disp()
d = mod2.c1(); d.m1()
print(x)          # 30
disp()
e = c1(); e.m1()


import importlib
import mod1
importlib.reload(mod1)   # reloads the module
importlib.reload(mod1)
