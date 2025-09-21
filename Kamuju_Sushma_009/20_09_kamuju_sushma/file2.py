#  Save  in  any  file  of  cwd
# How  to  import  members  of  mod1  in  package  p1
from p1.mod1 import *
# How  to  print  object  'x'  of   mod1  in  package  p1
print(x)
# How  to  call  function  f1()  of   mod1  in  package  p1
f1()
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a=c1()
a.m1()
print()
print()
# How  to  import   members  of  mod2   in  package  p1
from p1.mod1 import *
# How  to  print  object  'x'  of   mod2  in  package  p1
print(x)
# How  to  call  function  f1()  of   mod2  in  package  p1
f1()
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
a=c1()
a.m1()
# print(p1 . mod1 . x) # mod1 is not imported 
# print(mod1 . x) #mod1 is not imported
# from  p1   import  mod1 . * cannot use '.' in from clause 