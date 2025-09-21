# Save  in  any  file  of  cwd
# How  to  import  mod1  of  package  p1  with  from  statement
from p1 import mod1
# How  to  print  object  'x'  of   mod1  in  package  p1
print(mod1.x)
# How  to  call  function  f1()  of   mod1  in  package  p1
print(mod1.f1())
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a=mod1.c1()
a.m1()
# print(p1 . mod1 . x)  #not imported mod1 with packagr
print()
print()
# How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
from p1 import mod2
# How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
print(mod2.x)
# How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
print(mod2.f1())
# How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
a=mod2.c1()
print(a.m1())
# print(p1 . p2 . mod2 . x) cannot use through package
# from  p1  import   p2 . mod2 cannot use '.' in from clause
# from  p2  import  mod2 p2 is not in current module
