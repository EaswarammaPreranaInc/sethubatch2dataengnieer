# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=p1.mod1.c1() 
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) #How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1() #How  to  call  function  f1()  of  _init_  module  in  package  p1'''


# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1() 
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error because p1 is not imported
print(p1 . __init__ . x) # Error because p1 is not imported
print(__init__.x) # Error because p1 is not imported'''

# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)#How  to  print  object  'x'  of  mod1  in  package  p1
f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error
print(p1 . __init__ . x) # Error
print(__init__ . x) # Error
from  p1  import mod1.* # (.) is not used in import clause in from statement'''

# Save  in  any  file  of  cwd
import p1 #How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x) #How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.f1() #How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1() #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
if __name__=='__main__':
    from p1 import *
    print(p1.x)#How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
    p1.f1() #How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
    a=p1.c1()
    a.m1() #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way'''

# Save  in  any  file  of  cwd
import   p1  # _init_   module  of  package  p1  is  executed
import  p1 . mod1 # _init_   module  of  package  p1  is  executed
from   p1   import  mod1 # _init_   module  of  package  p1  is  executed
from   p1 . mod1  import * # _init_   module  of  package  p1  is  executed
import p1.__init__ #__init__   module  of  package  p1  is  executed
                    #__init__   module  of  package  p1.__init__  is  executed
