#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') # Hello
import mod2 #How  to  import  mod2
mod2.print(x) #(How  to  print   variable  'x'   of  mod2)
mod2.f1() #How  to  call  function  f1()  of  mod2
print('Bye') # Bye
import  mod4 # imports mod 4
print(x) # Error name 'x' is not defined
f1() # Error name 'f1' is not defined

#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') # Hello
import mod2 #How  to  import  mod2
mod2.print(x) #(How  to  print   variable  'x'   of  mod2)
mod2.f1() #How  to  call  function  f1()  of  mod2
print('Bye') # Bye
import  mod4 # imports mod 4
print(x) # Error name 'x' is not defined
f1() # Error name 'f1' is not defined

print('Before') # Before
import runpy
runpy.run_module('mod2') # How  to  run  mod2
print(mod2 . x) # error name 'mod2' is not defined
mod2 . f1() # error name 'mod2' is not defined
print('After') # After
run_module('mod2') # error name 'run_module' is not defined
runpy . run_module(mod2) # error name mod2 is not defined

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') # Begin
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # (How  to  print  variable  'x'  of  cal   module)
print(y) # (How  to  print  variable  'y'  of  cal   module)
print(cal . x) # Error name cal not defined
print(add(10,7)) # (How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7)) # (How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)) # (How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7)) # (How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) # Error name cal not defined
a=c1()
a.m1() #1How  to  call  m1()  method  of  class  c1  in  cal  module
b=cal.c1() # Error name cal not defined

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin') # Begin
from cal import x, add, mul, c1 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # error name y is not defined
print(cal . x) # error name call is not defined
print(add(10,7))# How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) # error name sub is not defined
print(mul(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) # error name div is not defined
a=c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module

# Module  alias
print('Begin')
import cal as c # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) # How  to  print  variable  'x'  of  cal   module)
print(c.y) # How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7)) # (How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7)) # (How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7)) # (How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7)) # (How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a= c.c1()
a.m1()#How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) # error name cal is not defined
from math as m import  * # module not found error

# Member  alias
from cal import x as x1, add as a,mul as m, c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(x1) # How  to  print  variable  'x'  of  cal   module)
print(x) # error name x is not defined
print(a(10,7)) #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7)) #(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
a = c()
a.m1() # How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10,7)) #error name add is not defined
b=c1()#error name c1 is not defined

# Find  outputs  (Home  work)
x = 30
def   disp():
    print('disp  function  of  same  module ')
class   c1:
    def   m1(self):
        print('m1  method of  class  c1  in  same  module')
from mod2 import *
from mod1 import *
print(x) # 10
disp() # disp  function  of  mod1
a=c1()
a.m1() # m1  method  of  class  c1  in  mod1

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
    print('disp  function  of  same  module ')
class   c1:
    def   m1(self):
	print('m1  method of  class  c1  in  same  module')
print(x) # 20
disp() # disp  function  of  mod2
a = c1()
a . m1() # m1  method of  class  c1  in  mod2

# How to use members of all the three modules with from statement ?
from mod1 import *   # How to import members of mod1
from mod2 import *   # How to import members of mod2
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(mod1.x)          # How to print variable 'x' of mod1
 mod1.disp()            # How to call disp() function of mod1
a = mod1.c1()
a.m1()            # How to call method m1() of class c1 in mod1
print()           # prints space
print(mod2.x)          # How to print variable 'x' of mod2
mod2.disp()            # How to call disp() function of mod2
b = mod2.c1()
b.m1()            # How to call method m1() of class c1 in mod2
print()           # prints space

print(x)          # How to print variable 'x' of current module
disp()            # How to call disp() function of current module
a = c1()
a.m1()            # How to call method m1() of class c1 in current module

# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One') # One
print('Two') # Two
print('Three') # Three
if __name__ == "__main__":
	print('Four')
print('Five')
print('Six')
print('Seven') # Seven
print('Eight') # Eight
print('Nine') # Nine

print('Begining of mod2')  # Begining of mod2
import mod1                 # In mod1 there are no print statements, so nothing is executed
print('End of mod2')        # End of mod2

from cal import *        # Only members in __all__ are imported: add, x, mul, c1, z
print(x)                  # 100
print(y)                  # Error: 'y' is not imported because it's not in __all__
print(add(10, 7))         # 17
print(sub(10, 7))         # Error: 'sub' is not imported because it's not in __all__
print(mul(10, 7))         # 70
print(div(10, 7))         # Error: 'div' is not imported because it's not in __all__
a = c1()
a.m1()                    # m1 method

import  cal
print(cal . x) # 100
print(cal . y) # error name y is not defined
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #error name sub is not defined
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # name div is not defined
a = cal . c1()
a . m1() # m1  method



from  cal  import   y , sub , mul
print(x) # error x sub is not defined
print(y) # 200
print(add(10 , 7)) # error name add is not defined
print(sub(10 , 7)) # 3
print(mul(10 , 7)) # 70
print(div(10 , 7)) #error name div is not defined
a = c1()

import  mod1 # imports mod1 for the first time and executes
print('Hyd')    # Hyd
print('Sec')    # Sec
print('Cyb')    # Cyb
# print('India') # This line is commented, so no output
# print('USA')   # This line is commented, so no output
import  mod1 # not imported
import  mod1 # not imported
import importlib         # imports importlib module, no output
import mod1               # executes mod1 top-level prints:
                         # Hyd
                         # Sec
                         # Cyb
print()                  # prints a blank line
importlib.reload(mod1)   # re-executes mod1 top-level prints:
                         # Hyd
                         # Sec
                         # Cyb
print()                  # prints a blank line
importlib.reload(mod1)   # re-executes mod1 again:
                         # Hyd
                         # Sec
                         # Cyb
importlib.reload('mod1') # Error: module argument must be a module, not str
reload(mod1)             # Error: name 'reload' is not defined
