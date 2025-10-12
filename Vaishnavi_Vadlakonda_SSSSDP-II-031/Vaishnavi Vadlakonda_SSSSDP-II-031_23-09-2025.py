# Save  in  any  file  of  cwd
import  p1 . mod1
print(mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) #How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1() # How  to  call  function  f1()  of  _init_  module  in  package  p1
a = p1.c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1
'''
Outputs
_init_   module  of  package ' , p1.mod1, ' is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


10
package  p1 ---> _init_  module ---> f1  function
package  p1 ---> _init_  module ---> class  c1  ---> m1  method
'''









# Save  in  any  file  of  cwd
from p1 import mod1
print(mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error because cannot use p1 package without importing
print(p1 . _init_ . x) # Error because cannot use p1 package without importing
print(_init_. x) # Error because cannot use __init__ module without importing
'''
Outputs
_init_   module  of  package ' , mod1 , ' is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''









# Save  in  any  file  of  cwd
from p1.mod1 import  *
print(x) # How  to  print  object  'x'  of  mod1  in  package  p1
f1()  #ow  to  call  function  f1()  of  mod1  in  package  p1
a = c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error because cannot use p1 package without importing
print(p1 . _init_ . x) # Error because cannot use p1 package without importing
print(_init_ . x) # Error because cannot use __init__ module without importing
from p1 import mod1.* # Error because cannot use '.' operator in import clause of from statement
'''
Outputs
_init_   module  of  package ' , p1.mod1 , ' is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''









# Save  in  any  file  of  cwd
import p1.__init__ #How  to  import  _init_  module  of  package  p1  with  import  statement
print(__init__.x) # How  to  print  object  'x'  of   _init_  module   in   package  p1
__init__.f1() # How  to  call  function  f1()  of   init  module  in  package  p1
a = __init__.c1() 
a.m1() # How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
import(x) # How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
f1() # How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a = c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1.mod1.x) # Error, cannot use mod1 without importing
'''
Outputs
_init_   module  of  package ' , p1.__init__, ' is  executed
10
package  p1 ---> _init_  module ---> f1  function
package  p1 ---> _init_  module ---> class  c1  ---> m1  method
10
package  p1 ---> _init_  module ---> f1  function
package  p1 ---> _init_  module ---> class  c1  ---> m1  method
'''









# Save  in  any  file  of  cwd
import p1
import p1 . mod1
from p1 import mod1
from p1.mod1 import   *
import p1.__init__
'''
__init__ module is executed only once
'''