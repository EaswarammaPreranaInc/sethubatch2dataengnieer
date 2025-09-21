#To import both modules (`mod1`, `mod2`) from the package `p1`:

from p1 import mod1
from p1 import mod2

# Accessing 'x' from mod1
print(mod1.x)             # Output: 10

# Calling f1() from mod1
mod1.f1()                 # Output: p1  --->  mod1   --->  f1  function

# Creating c1 object and calling m1() from mod1
a = mod1.c1()
a.m1()                    # Output: p1  ---> mod1  ---> c1  ---> m1 method

print()  # for separation

# Accessing 'x' from mod2
print(mod2.x)             # Output: 20

# Calling f1() from mod2
mod2.f1()                 # Output: p1  ---> mod2  ---> f1

# Creating c1 object and calling m1() from mod2
b = mod2.c1()
b.m1()                    # Output: p1  ---> mod2 ---> c1 ---> m1







# Importing Members Directly From mod1 and mod2

from p1.mod1 import *
print(x)         # 10
f1()             # p1  --->  mod1   --->  f1  function
a = c1()
a.m1()           # p1  ---> mod1  ---> c1  ---> m1 method


#To import all members of mod2:
from p1.mod2 import *
print(x)         # 20
f1()             # p1  ---> mod2  ---> f1
b = c1()
b.m1()           # p1  ---> mod2 ---> c1 ---> m1






# Using a Sub-Package (mod2 inside p2)

If you have:
- `p1/mod1.py`
- `p1/p2/mod2.py`

Import like this:

from p1 import mod1           # For mod1 in p1
from p1.p2 import mod2        # For mod2 in p2


#Usage:

print(mod1.x)
mod1.f1()
a = mod1.c1()
a.m1()

print()

print(mod2.x)
mod2.f1()
b = mod2.c1()
b.m1()








# Output of Example Homework Codes

x = 30
def f1():
    print('Function  of  same  module')
class c1:
    def m1(self):
        print('Method  of  class  c1  in same  module')
from p1.mod1 import *
from p1.mod2 import *
print(x)           # 30 (local value, masks imported 'x')
f1()               # Function  of  same  module (local function masks imported)
a = c1()
a.m1()             # Method  of  class  c1  in same  module (local class masks imported)

