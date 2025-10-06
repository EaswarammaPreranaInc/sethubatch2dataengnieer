
# Q1: Save in cwd \ p1 \ mod1.py
x = 10
def f1():
    print('p1  --->  mod1   --->  f1  function')
class c1:
    def m1(self):
        print('p1  ---> mod1  ---> c1  ---> m1 method')

'''
Output:
Module Name: p1.mod1
Members: Object x, Function f1(), Class c1
'''


# Q2: Save in cwd \ p1 \ mod2.py
x = 20
def f1():
    print('p1  ---> mod2  ---> f1')
class c1:
    def m1(self):
        print('p1  ---> mod2 ---> c1 ---> m1 ')

'''
Output:
Module Name: p1.mod2
Members: Object x, Function f1(), Class c1
'''


# Q3: Save in any file of cwd
from p1 import mod1, mod2

print(mod1.x)              # object x of mod1
mod1.f1()                  # function f1 of mod1
obj1 = mod1.c1()
obj1.m1()                  # method m1 of class c1 in mod1
print()
print(mod2.x)              # object x of mod2
mod2.f1()                  # function f1 of mod2
obj2 = mod2.c1()
obj2.m1()                  # method m1 of class c1 in mod2

'''
Output:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 
'''


# Q4: Save in any file of cwd
from p1.mod1 import *
from p1.mod2 import *

print(x)       # x of mod2 overwrites mod1
f1()           # f1 of mod2 overwrites mod1
a = c1()       # c1 of mod2 overwrites mod1
a.m1()

'''
Output:
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 
'''


# Q5: Save in any file of cwd
x = 30
def f1():
    print('Function  of  same  module')
class c1:
    def m1(self):
        print('Method  of  class  c1  in same  module')

from p1.mod1 import *
from p1.mod2 import *

print(x)
f1()
a = c1()
a.m1()

'''
Output:
30
Function  of  same  module
Method  of  class  c1  in same  module
'''


# Q6: Save in any file of cwd
x = 30
def f1():
    print('Function  of  same  module')
class c1:
    def m1(self):
        print('Method  of  class  c1  in same  module')

from p1.mod2 import *
from p1.mod1 import *

print(x)
f1()
a = c1()
a.m1()

'''
Output:
30
Function  of  same  module
Method  of  class  c1  in same  module
'''


# Q7: Save in any file of cwd
from p1.mod1 import *
from p1.mod2 import *

x = 30
def f1():
    print('Function  of  same  module')
class c1:
    def m1(self):
        print('Method  of  class  c1  in same  module')

print(x)
f1()
a = c1()
a.m1()

'''
Output:
30
Function  of  same  module
Method  of  class  c1  in same  module
'''


# Q8: Save in any file of cwd
from p1.mod1 import *
from p1.mod2 import *

print(mod1.x)       # using mod1.x explicitly not possible here because imported *
print(x)            # prints 20 because mod2 overwrites mod1
f1()                # from mod2
obj1 = c1()         # from mod2
obj1.m1()

'''
Output:
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 
'''
# Q9: Save in cwd \ p1 \ mod1.py
x = 10
def f1():
    print('p1  --->  mod1  --->  f1 function')
class c1:
    def m1(self):
        print('p1 ---> mod1 ---> c1 ---> m1 method ')

'''
Output:
1) What is the name of module? ---> p1.mod1
2) What are the members of p1.mod1? ---> Object 'x', Function f1(), Class c1
'''


# Q10: Save in cwd \ p1 \ p2 \ mod2.py
x = 20
def f1():
    print('p1 ---> p2 ---> mod2 ---> f1 function')
class c1:
    def m1(self):
        print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')

'''
Output:
1) What is the name of module? ---> p1.p2.mod2
2) What are the members of p1.p2.mod2? ---> Object 'x', Function f1(), Class c1
'''


# Q11: Save in any file of cwd
from p1 import mod1
from p1.p2 import mod2

print(mod1.x)         # object x of mod1
mod1.f1()             # function f1 of mod1
obj1 = mod1.c1()
obj1.m1()             # method m1 of c1 in mod1

print()
print(mod2.x)         # object x of mod2
mod2.f1()             # function f1 of mod2
obj2 = mod2.c1()
obj2.m1()             # method m1 of c1 in mod2

'''
Output:
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method 

20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''


# Q12: Save in any file of cwd
from p1.mod1 import *
from p1.p2.mod2 import *

print(x)     # object x of mod2 overwrites mod1
f1()         # f1 of mod2 overwrites mod1
a = c1()     # c1 of mod2 overwrites mod1
a.m1()

'''
Output:
20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''
