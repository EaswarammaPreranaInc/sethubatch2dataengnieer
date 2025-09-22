# Save  in  any  file  of  cwd
from  p1   import  mod1
# How  to  print  object  'x'  of  mod1  in  package  p1
print(mod1.x)
# How  to  call  function  f1()  of  mod1  in  package  p1
mod1.f1()
# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a=mod1.c1()
a.m1()
# print(p1 . x) package is not imported
# print(p1 . __init__ . x) package is not imported
# print(__init__ . x) __init__ module is not imported
