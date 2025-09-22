# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.mod1.c1() 
a . m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) # How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1() # How  to  call  function  f1()  of  _init_  module  in  package  p1
b = p1.c1()
b . m1() # How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1

'''
__init__   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


10
package  p1 ---> _init_  module ---> f1  function
package  p1 ---> _init_  module ---> class  c1  ---> m1  method

'''

# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1() 
a . m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error as p1 is not imported
print(p1 . __init__ . x) # error as p1 is not imported
print(__init__ . x)  # error as there is no __init__ in current module

'''
__init__   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''

# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) # How  to  print  object  'x'  of  mod1  in  package  p1
f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = c1()
a . m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error as p1 is not imported
print(p1 . __init__ . x) # Error as p1 is not imported
print(__init__ . x) # Error as there is no __init__ in current program
from  p1  import  mod1 . * # Error as . cannot be used in import clause

'''
__init__   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

'''

# Save  in  any  file  of  cwd
import p1.__init__ # How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.__init__.x) # How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.__init__.f1() # How  to  call  function  f1()  of   init  module  in  package  p1
a = p1.__init__ .c1() # How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
a . m1() # How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
from p1 import f1 , c1
f1() # How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
b = c1()
b . m1()# How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x) # Error as p1.mod1 is not imported

'''
__init__   module  of  package  p1  is  executed
__init__   module  of  package  p1.__init__  is  executed
10
package  p1 ---> _init_  module ---> f1  function
package  p1 ---> _init_  module ---> class  c1  ---> m1  method
package  p1 ---> _init_  module ---> f1  function
package  p1 ---> _init_  module ---> class  c1  ---> m1  method
'''

# Save  in  any  file  of  cwd
import   p1 # package p1 is imported and __init__ is executed
import  p1 . mod1 # p1.mod1 is imported and __init__ is executed
from   p1   import  mod1 # mod1 is imported from p1
from   p1 . mod1  import   * # members of p1.mod1 is imported
import  p1 . __init__ # p1.__init__ is imported and executed
