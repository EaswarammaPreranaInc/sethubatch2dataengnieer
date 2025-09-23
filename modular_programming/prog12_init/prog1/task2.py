# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)     #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()         #How  to  call  function  f1()  of  mod1  in  package  p1
c = mod1.c1()
c.m1()            #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
# print(p1 . x)              #error, p1 is not imported
# print(p1 . __init__ . x)     #error, p1 is not imported
# print(__init__.x)          #error, __init__ is not imported
'''
OUTPUT:
_init_   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''