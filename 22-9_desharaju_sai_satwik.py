import  p1.mod1
print(p1.mod1.x)        # print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()            # call  function  f1()  of  mod1  in  package  p1
obj1 = p1.mod1.c1()
obj1.m1()               # call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x)             # print  object  'x'  of  _init_  module  in  package  p1
p1.f1()                 # call  function  f1()  of  _init_  module  in  package  p1
obj2 = p1.c1()
obj2.m1()               #  call  method  m1()  of  class  c1  in   init  module  of  package  p1


'''
Output:

20
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

10
package p1 ---> __init__ module ---> f1 function
package p1 ---> __init__ module ---> class c1 ---> m1 method
'''


from p1 import mod1    
print(mod1.x)          # print object 'x' of mod1 in package p1
mod1.f1()              # call function f1() of mod1 in package p1
obj1 = mod1.c1()
obj1.m1()              #call method m1() of class c1 in mod1 of package p1
print(p1.x)            # Error 
print(p1._init_.x)     # Error 
print(_init_.x)        # Error 

'''
Output:


20
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

10
package p1 ---> __init__ module ---> f1 function
package p1 ---> __init__ module ---> class c1 ---> m1 method
'''

from p1.mod1 import *     
print(x)                  # How to print object 'x' of mod1 in package p1
f1()                      # How to call function f1() of mod1 in package p1
obj1 = c1()
obj1.m1()                 # How to call method m1() of class c1 in mod1 of package p1
print(p1.x)               # Error p1 is not imported
print(p1._init_.x)        # Error No module _init_
print(_init_.x)           # Error _init_ is not a module in the current working diretory
from p1 import mod1.*     # Error . can't be used in the import clause of the from statement

'''
Output:

20
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method
'''



import p1               # How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x)             # How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.f1()                 # How  to  call  function  f1()  of   init  module  in  package  p1
obj1 = p1.c1()
obj1.m1()               # How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
from p1 import *
print(x)                # How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
f1()                    # How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
obj2 = c1()
obj2.m1()               # How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1.mod1.x)        # Error mod1 is not imported

'''
Output:

10
package p1 ---> __init__ module ---> f1 function
package p1 ---> __init__ module ---> class c1 ---> m1 method

10
package p1 ---> __init__ module ---> f1 function
package p1 ---> __init__ module ---> class c1 ---> m1 method
'''



import p1                   # Imports the package p1 (executes __init__.py)
import p1.mod1              # Imports mod1.py inside package p1
from p1 import mod1         # Imports mod1 directly
from p1.mod1 import *       # Imports all members of mod1 directly
import p1._init_            # Error __init__.py is not imported by this statement. It automatically runs __init__.py when you import the package.

'''
Output:

__init__ module of package p1 is executed
'''
