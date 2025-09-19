# How to reuse mod2 ? (Home work)
print('Hello')
import mod2
print(mod2.x)
mod2.f1()
print('Bye')
import mod4
print(x)
f1()

# Output
Hello
<value of x from mod2>
f1 function of mod2
Bye
<value of x from mod4>
f1 function of mod4


# Find outputs (Home work)
print('Before')
import mod2
print(mod2.x)
mod2.f1()
print('After')
import runpy
runpy.run_module('mod2')

# Output
Before
Begining of mod2
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
End of mod2
<value of x from mod2>
f1 function of mod2
After
{'_name_': 'mod2', ...}   # run_module returns dict


# How to use members of cal module with from statement ? (Home work)
from cal import *
print(x)
print(y)
print(add(10,7))
print(sub(10,7))
print(mul(10,7))
print(div(10,7))
a = c1()
a.m1()

# Output
10
7
17
3
70
1.4285714285714286
m1 method of class c1 in cal module


# How to import only variable 'x', functions add(), mul(), class c1 (Home work)
from cal import x, add, mul, c1
print(x)
print(add(10,7))
print(mul(10,7))
b = c1()
b.m1()

# Output
10
17
70
m1 method of class c1 in cal module


# Module alias
import cal as c
print(c.x)
print(c.y)
print(c.add(10,7))
print(c.sub(10,7))
print(c.mul(10,7))
print(c.div(10,7))
b = c.c1()
b.m1()

# Output
10
7
17
3
70
1.4285714285714286
m1 method of class c1 in cal module


# Member alias
from cal import x as x1, add as a, mul as m, c1 as c11
print(x1)
print(a(10,7))
print(m(10,7))
b = c11()
b.m1()

# Output
10
17
70
m1 method of class c1 in cal module


# Find outputs (Home work)
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
from mod2 import *
from mod1 import *
print(x)
disp()
a = c1()
a.m1()

# Output
30
disp function of same module
m1 method of class c1 in same module


# Find outputs (Home work)
from mod1 import *
from mod2 import *
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(x)
disp()
a = c1()
a.m1()

# Output
30
disp function of same module
m1 method of class c1 in same module


# mod1.py (Home work)
if _name_ == "_main_":
    print('One')
    print('Two')
    print('Three')
    print('Four')
    print('Five')
    print('Six')
    print('Seven')
    print('Eight')
    print('Nine')

# If imported elsewhere → no output
# If run directly → prints One … Nine


# Find outputs (Home work)
print('Beginning of mod2')
import mod1
print('End of mod2')

# Output
Beginning of mod2
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
End of mod2


# From cal import *
from cal import *
print(x)
print(y)
print(add(10,7))
print(sub(10,7))
print(mul(10,7))
print(div(10,7))
a = c1()
a.m1()

# Output
10
7
17
3
70
1.4285714285714286
m1 method of class c1 in cal module


# import cal
import cal
print(cal.x)
print(cal.y)
print(cal.add(10,7))
print(cal.sub(10,7))
print(cal.mul(10,7))
print(cal.div(10,7))
a = cal.c1()
a.m1()

# Output
10
7
17
3
70
1.4285714285714286
m1 method of class c1 in cal module


# from cal import y, sub, mul
from cal import y, sub, mul
print(y)
print(sub(10,7))
print(mul(10,7))

# Output
7
3
70


# Import mod1 multiple times
import mod1
import mod1
import mod1

# Output
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
# (executed only once, rest ignored)


# reload() function demo
import importlib
import mod1
print()
importlib.reload(mod1)
print()
importlib.reload(mod1)

# Output
One … Nine
<blank line>
One … Nine
<blank line>
One … Nine
