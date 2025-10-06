Dabbiru Sai Harsha Vardhn
# Save in any file of cwd
import p1.mod1
# object 'x' of mod1 in package p1
print(p1.mod1.x)
# function f1() of mod1 in package p1
print(p1.mod1.f1())
# method m1() of class c1 in mod1 of package p1
obj = p1.mod1.c1()
obj.m1()
print()
print()
# object 'x' of init module in package p1
print(p1.x)
# function f1() of init module in package p1
print(p1.f1())
# method m1() of class c1 in init module of package p1
obj2 = p1.c1()
obj2.m1()


# Save in any file of cwd
from p1 import mod1
# object 'x' of mod1 in package p1
print(mod1.x)
# function f1() of mod1 in package p1
print(mod1.f1())
# method m1() of class c1 in mod1 of package p1
obj = mod1.c1()
obj.m1()
print(p1.x)            # error, p1 not imported
print(p1.init.x)       # error, init is not a submodule name
print(init.x)          # error, init not defined
# ^ AttributeError / NameError


# Save in any file of cwd
from p1.mod1 import *
# object 'x' of mod1 in package p1
print(x)
# function f1() of mod1 in package p1
print(f1())
# method m1() of class c1 in mod1 of package p1
obj = c1()
obj.m1()
print(p1.x)            # error, p1 not imported
print(p1.init.x)       # error
print(init.x)          # error
from p1 import mod1.*  # SyntaxError



# Save in any file of cwd
import p1        # imports init.py of package p1
# object 'x' of init module in package p1
print(p1.x)
# function f1() of init module in package p1
print(p1.f1())
# method m1() of class c1 in init module of package p1
obj = p1.c1()
obj.m1()
# another way
from p1 import *
print(x)
print(f1())
obj = c1()
obj.m1()
print(p1.mod1.x)


# Save in any file of cwd
import p1
import p1.mod1
from p1 import mod1
from p1.mod1 import *
import p1.init     # error, init is not imported this way
