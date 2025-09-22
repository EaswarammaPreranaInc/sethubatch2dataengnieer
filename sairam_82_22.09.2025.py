# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x )  #How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()    #.How  to  call  function  f1()  of  mod1  in  package  p1
a=p1.mod1.c1()  
a.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) #How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1() ##How  to  call  function  f1()  of  _init_  module  in  package  p1
a=p1.c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1

# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)   #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()   #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1()   #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)   # error as p1 is not imported
print(p1 . __init__ . x)  #error as __init__ is not imported
print(__init__ . x) #error as __init__ is not imported


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)    #How  to  print  object  'x'  of  mod1  in  package  p1
f1()    #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()    #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)   # error as p1 is not imported
print(p1 . _init_ . x)  # error as p1 and__init __ are not imported
print(_init_ . x)   # error as __init__ is not imported
from  p1  import  mod1 . *  # error as . cant be used in import clause of from statement

# Save  in  any  file  of  cwd
import p1.__init__   #How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.__init__.x)    ##How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.__init__.f1()    ##How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.__init__.c1()
a.m1()    ##How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1.x) #How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
p1.f1()    ##How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=p1.c1()
a.m1()  #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x)    # error as mod1 is not imported

# Save  in  any  file  of  cwd
import   p1     # package p1 is imported and its __init__.py is executed
import  p1 . mod1   # module mod1 of package p1 is imported
from   p1   import  mod1 # module mod1 of package p1 is imported
from   p1 . mod1  import   *    # all members of module mod1 of package p1 are imported
import  p1 . __init__   # module __init__ of package p1 is imported

