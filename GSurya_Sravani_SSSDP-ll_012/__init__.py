# Save  in  any  file  of  cwd
import  p1 . mod1
Print(p1.mode1.x)How  to  print  object  'x'  of  mod1  in  package  p1
Print(p1.mod1.f1())How  to  call  function  f1()  of  mod1  in  package  p1
A=p1.mod1.c1()
A.m1()How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
Print(x)How  to  print  object  'x'  of  __init__  module  in  package  p1
Print(f1())How  to  call  function  f1()  of  __init__  module  in  package  p1
a=C1()
a.m1()How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1




# Save  in  any  file  of  cwd
from  p1   import  mod1
Print(mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
Print(mod1.f1())#How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
mod1.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)#error
print(p1 . __init__ . x)#error
print(__init__ . x)#error




# Save  in  any  file  of  cwd
How  to  import  __init__  module  of  package  p1  with  import  statement#import p1
How  to  print  object  'x'  of   __init__  module   in   package  p1#print(x)
How  to  call  function  f1()  of   init  module  in  package  p1#
Print(f1())
How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1#a=c1()
a.m1()

How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way#from p1.mod1 import x
Print(x)
How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
#print(F1())
How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way#a=C1()
a.m1()
print(p1 . mod1 . x)#error




# Save  in  any  file  of  cwd
import   p1# p1 is imported and __init__module is imported and executed 
import  p1 . mod1#p1 package of module mod1 is imported 
from   p1   import  mod1#mod1 of package p1 is imported 
from   p1 . mod1  import   *# all members of package p1 and mod1 are imported 
import  p1 . __init__# init module is imported .