#TARUN BANALA   22-09-2-25    HOME WORK
'''cwd/
│
├── main.py   # (your test file)
└── p1/
    ├── __init__.py
    └── mod1.py'''

# Save in any file of cwd
import p1.mod1

# --- From mod1 ---
# How to print object 'x' of mod1 in package p1
print(p1.mod1.x)

# How to call function f1() of mod1 in package p1
p1.mod1.f1()

# How to call method m1() of class c1 in mod1 of package p1
obj1 = p1.mod1.c1()
obj1.m1()

print("---------------")

# --- From __init__.py ---
# How to print object 'x' of __init__ module in package p1
print(p1.x)

# How to call function f1() of __init__ module in package p1
p1.f1()

# How to call method m1() of class c1 in __init__ module of package p1
obj2 = p1.c1()
obj2.m1()

# Save in any file of cwd
from p1.mod1 import *
import p1   # to access __init__.py contents

# --- From mod1 ---
# How to print object 'x' of mod1 in package p1
print(x)

# How to call function f1() of mod1 in package p1
f1()

# How to call method m1() of class c1 in mod1 of package p1
c1().m1()

print("---------------")

# --- From __init__.py ---
# How to print object 'x' of __init__ module in package p1
print(p1.x)

# How to call function f1() of __init__ module in package p1
p1.f1()

# How to call method m1() of class c1 in __init__ module of package p1
p1.c1().m1()

# Save in any file of cwd
import p1

# --- From __init__.py ---
# How to print object 'x' of __init__.py in package p1
print(p1.x)

# How to call function f1() of __init__.py in package p1
p1.f1()

# How to call method m1() of class c1 in __init__.py in package p1
obj = p1.c1()
obj.m1()

print("---------------")

# --- Another way (import names directly) ---
from p1 import x, f1, c1

# print object 'x' from __init__.py
print(x)

# call function f1() from __init__.py
f1()

# call method m1() from class c1 in __init__.py
c1().m1()

print("---------------")

# From mod1 just for comparison
import p1.mod1
print(p1.mod1.x)
# Save in any file of cwd

# This loads __init__.py automatically
import p1

# This loads mod1 explicitly
import p1.mod1

# Another way to import mod1
from p1 import mod1

# Import everything from mod1 into current namespace
from p1.mod1 import *



