# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)         #How  to  print  object  'x'  of  mod1  in  package  p1
f1()             #How  to  call  function  f1()  of  mod1  in  package  p1
c1().m1()        #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
# print(p1 . x)           #p1 is not defined nor imported
# print(p1 . __init__ . x)  #p1 is not defined nor imported
# print(__init__ . x)       #__init__ is not defined nor imported    
# from  p1  import mod1.*     #dot is not permitted in import clause of from statement
'''
OUTPUT:
_init_   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''