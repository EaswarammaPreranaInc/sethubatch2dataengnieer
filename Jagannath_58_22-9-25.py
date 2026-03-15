# Save  in  any  file  of  cwd
import  p1 . mod1
How  to  print  object  'x'  of  mod1  in  package  p1                                         print(p1.mod1.x)
How  to  call  function  f1()  of  mod1  in  package  p1                                       p1.mod1.f1()
How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1                          a=p1.mod1.c1()
                                                                                               a.m1()
print()
print()
How  to  print  object  'x'  of  _init_  module  in  package  p1                               import p1
                                                                                               print(p1.x)
How  to  call  function  f1()  of  _init_  module  in  package  p1                             p1.f1()
How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1                 a=p1.c1()
                                                                                               a.m1()

# Save  in  any  file  of  cwd
from  p1   import  mod1
How  to  print  object  'x'  of  mod1  in  package  p1                                         print(mod1.x)
How  to  call  function  f1()  of  mod1  in  package  p1                                       mod1.f1()
How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1                          a=mod1.c1()
                                                                                               a.m1()
print(p1 . x)                                                                                  Error
print(p1 . _init_ . x)                                                                         Error
print(_init_ . x)                                                                              Error


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
How  to  print  object  'x'  of  mod1  in  package  p1                                         print(x)
How  to  call  function  f1()  of  mod1  in  package  p1                                       f1()
How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1                          a=c1()
                                                                                               a.m1()
print(p1 . x)                                                                                  Error
print(p1 . _init_ . x)                                                                         Error
print(_init_ . x)                                                                              Error
from  p1  import  mod1 . *                                                                     Error


# Save  in  any  file  of  cwd
How  to  import  _init_  module  of  package  p1  with  import  statement                                      import p1
How  to  print  object  'x'  of   _init_  module   in   package  p1                                            print(p1.x)
How  to  call  function  f1()  of   init  module  in  package  p1                                              p1.f1()                                                
How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1                                  a=p1.c1()
                                                                                                               a.m1()
How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way                          from p1 import *
                                                                                                               print(x)
How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way                          f1()
How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way             a=c1()
                                                                                                               a.m1()
print(p1 . mod1 . x)                                                                                           Error


# Save  in  any  file  of  cwd
import   p1                                  imports package p1
import  p1 . mod1                            imports submodule m1 inside p1
from   p1   import  mod1                     imports module m1
from   p1 . mod1  import   *                 imports members of mod1 from p1
import  p1 . _init_                          imports package p1 automatically
