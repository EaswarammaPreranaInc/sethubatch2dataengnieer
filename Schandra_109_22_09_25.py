 : # Save  in   cwd \ p1 \ _init_ . py
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
:: # Save  in  cwd \  p1 \ mod1 . py
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





: # Save  in  any  file  of  cwd
import  p1 . mod1
How  to  print  object  'x'  of  mod1  in  package  p1
How  to  call  function  f1()  of  mod1  in  package  p1
How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
How  to  print  object  'x'  of  _init_  module  in  package  p1
How  to  call  function  f1()  of  _init_  module  in  package  p1
How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1

####################
import p1.mod1

print(p1.mod1.x)          # object 'x' from mod1
p1.mod1.f1()              # function f1() from mod1
obj = p1.mod1.c1()
obj.m1()                  # method m1() from mod1

print(p1.x)               # object 'x' from __init__.py
p1.f1()                   # function f1() from __init__.py
obj2 = p1.c1()
obj2.m1()                 # method m1() from __init__.py





: # Save  in  any  file  of  cwd
from  p1   import  mod1
How  to  print  object  'x'  of  mod1  in  package  p1
How  to  call  function  f1()  of  mod1  in  package  p1
How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)
print(p1 . _init_ . x)##is wrong, because _init_ is not a submodule.
print(_init_ . x)###Python runs __init__.py automatically.

#########################
from p1 import mod1

print(mod1.x)             # object 'x' from mod1
mod1.f1()                 # function f1() from mod1
obj = mod1.c1()
obj.m1()                  # method m1() from mod1

import p1                 # to access __init__.py members
print(p1.x)               # object 'x' from __init__.py
p1.f1()                   # function f1() from __init__.py
obj2 = p1.c1()
obj2.m1()                 # method m1() from __init__.py






: # Save  in  any  file  of  cwd
from  p1 . mod1   import  *
How  to  print  object  'x'  of  mod1  in  package  p1
How  to  call  function  f1()  of  mod1  in  package  p1
How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)
print(p1 . _init_ . x)
print(_init_ . x)
from  p1  import  mod1 . *
##################################
from p1.mod1 import *

print(x)       # object 'x' from mod1
f1()           # function f1() from mod1
obj = c1()
obj.m1()       # method m1() from mod1





: # Save  in  any  file  of  cwd
How  to  import  _init_  module  of  package  p1  with  import  statement
How  to  print  object  'x'  of   _init_  module   in   package  p1
How  to  call  function  f1()  of   init  module  in  package  p1
How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x)



: # Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . _init_

#####################
import p1

print(p1.x)      # object 'x' from __init__.py
p1.f1()          # function f1() from __init__.py
obj = p1.c1()
obj.m1()         # method m1() from __init__.py

$$Another way:

from p1 import x, f1, c1

print(x)
f1()
obj = c1()
obj.m1()




