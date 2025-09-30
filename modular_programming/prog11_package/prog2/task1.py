# # Save  in  any  file  of  cwd
# How  to  import  mod1  of  package  p1  with  from  statement
from p1 import mod1
# How  to  print  object  'x'  of   mod1  in  package  p1
print(mod1.x)
# How  to  call  function  f1()  of   mod1  in  package  p1
mod1.f1()
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
c = mod1.c1()
# print(p1 . mod1 . x)         #p1 is not defined
print()
print()
# How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
from p1.p2 import mod2
# How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
print(mod2.x)
# How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()
# How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
c = mod2.c1()
c.m1()
# print(p1 . p2 . mod2 . x)           #p1 is not defined
# from  p1  import   p2 . mod2        #no dot permitted in import clause of from statement
# from  p2 import mod2                #p2 is not defined