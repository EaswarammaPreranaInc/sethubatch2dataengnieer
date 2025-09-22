# Save  in  any  file  of  cwd
# How  to  import  __init__  module  of  package  p1  with  import  statement
import p1.__init__  
# How  to  print  object  'x'  of   __init__  module   in   package  p1
print(p1.x)
# How  to  call  function  f1()  of   init  module  in  package  p1
p1.f1()
# How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
a=p1.c1()
a.m1()
# How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
from p1 import __init__
print(__init__.x)
# How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
__init__.f1()
# How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
a=__init__.c1()
a.m1()
# print(p1 . mod1 . x) error package is not imported