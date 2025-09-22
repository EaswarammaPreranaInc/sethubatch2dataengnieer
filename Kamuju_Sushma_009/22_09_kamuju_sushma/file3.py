# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
# How  to  print  object  'x'  of  mod1  in  package  p1
print(x)
f1()# How  to  call  function  f1()  of  mod1  in  package  p1
a=c1() #
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
# print(p1 . x) package not imported
# print(p1 . __init__ . x) #no need to use __init__ again
# print(__init__ . x) # __init__ not imported
# from  p1  import  mod1 . *  cannot use '.' in import clause of where statement