'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
# How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod1 import x as x1, f1 as f11, c1 as c11
# How  to  import   members  of  mod2   in  package  p1  with  from  statement
from p1.mod2 import x as x2, f1 as f12, c1 as c12
# How  to  print  object  'x'  of   mod1  in  package  p1
print(x1)
# How  to  call  function  f1()  of   mod1  in  package  p1
f11()
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
c = c11()
c.m1()
print()
print()
# How  to  print  object  'x'  of   mod2  in  package  p1
print(x2)
# How  to  call  function  f1()  of   mod2  in  package  p1
f12()
# How  to  call  method  m1()  of   class  c1  in  mod2 of package p1
c = c12()
c.m1()