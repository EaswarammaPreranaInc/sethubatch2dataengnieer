# Save  in   cwd \ p1 \ _init_ . py
print('_init_   module  of  package ' , _name_ , ' is  executed')
x = 10
def   f1():
	print('package  p1 ---> _init_  module ---> f1  function')
class   c1:
	def  m1(self):
		print('package  p1 ---> _init_  module ---> class  c1  ---> m1  method')


'''
1) What  is  the  name  of  module ?  ---> p1 . _init_

2) What  are  the  members  of  the  p1 . _init_ ?   ---> Object  'x'  ,  function   f1()  and  class   c1

3) py  _init_ . py
    What  are  the  outputs  ?  --->  _init_   module  of  package  _main_  is  executed
'''
# Save  in  cwd \  p1 \ mod1 . py
x = 20
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')


'''
1) What  is  the  name  of  module  ?  --->  p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?   ---> Object  'x'  ,  function  f1()  and   class  c1
'''
# Save  in  any  file  of  cwd
import p1.mod1# How to import mod1 of package p1
print(p1.mod1.x)# How to print object 'x' of mod1 in package p1
p1.mod1.f1()# How to call function f1() of mod1 in package p1
obj1 = p1.mod1.c1()
obj1.m1()# How to call method m1() of class c1 in mod1 of package p1
print()
print()
print(p1.x)# How to print object 'x' of _init_ module in package p1
p1.f1()# How to call function f1() of _init_ module in package p1
c = p1.c1()
c.m1()# How to call method m1() of class c1 in _ini


# Save  in  any  file  of  cwd

from p1 import mod1# importing mod1 with from statement
print(mod1.x)# How to print object 'x' of mod1 in package p1
mod1.f1()# How to call function f1() of mod1 in package p1
obj1 = mod1.c1()
obj1.m1()# How to call method m1() of class c1 in mod1 of package p1

print(p1.x)# How to print object 'x' of _init_ module in package p1
print(p1._init_.x)# error (_init_ isn't a module attribute)
print(_init_.x)# error


# Save  in  any  file  of  cwd
from p1.mod1 import *# How to import members of mod1 directly
print(x)# How to print object 'x' of mod1 in package p1
f1()# How to call function f1() of mod1 in package p1
obj = c1()
obj.m1()# How to call method m1() of class c1 in mod1 of package p1
print(p1.x)# How to print object 'x' of _init_ module in package p1 (if imported)
print(p1._init_.x)# error
print(_init_.x)# error
from p1 import mod1.*# error, invalid syntax


# Save  in  any  file  of  cwd
import p1# How to import _init_ module of package p1 with import statement
print(p1.x)# How to print object 'x' of _init_ module in package p1
p1.f1()# How to call function f1() of _init_ module in package p1
ci = p1.c1()
ci.m1()# How to call method m1() of class c1 in _init_ module of package p1
# Another way (in a module inside package p1)
from . import x, f1, c1# How to use relative import inside package p1 file
print(p1 . mod1 . x)


# Save  in  any  file  of  cwd
import p1# Import package (runs __init__.py)
import p1.mod1# Import module mod1 in package p1
from p1 import mod1# from-import style
from p1.mod1 import *# star import (x, f1, c1 into namespace)
import p1._init_# error, __init__ is not directly importable as module