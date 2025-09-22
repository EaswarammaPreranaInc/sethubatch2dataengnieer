import  p1.mod_1
print(p1.mod_1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod_1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a=p1.mod_1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) # How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1() # How  to  call  function  f1()  of  _init_  module  in  package  p1
a=p1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1

from  p1 import mod_1
print(mod_1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod_1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a= mod_1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1.x) # error name p1 is not defined
print(p1.__init__.x) # error name p1 is not defined
print(__init__.x) # Error name __init__ is not defined

from  p1.mod_1 import *
print(x) # How  to  print  object  'x'  of  mod1  in  package  p1
f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1.x) # error name p1 is not defined
print(p1.__init__.x) # error name p1 is not defined
print(__init__ . x) # error name __init__ is not defined
from p1 import mod1.* # error invalid syntax

from p1 import *
import p1 # How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x) # How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.f1() # How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1() # How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(x) # How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
f1() #How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x) # error name p1 is not defined


import   p1 # imports sub-directory p1 of cwd 
import  p1 . mod1 # imports sub-directory p1.mod1 of cwd
from   p1   import  mod1 # imports mod 1 of sub-directory p1 of cwd
from   p1 . mod1  import   * # imports all the members of mod 1 of sub-directory p1 of cwd
import  p1 . _init_ # imports sub-directory p1.__init__  of cwd
