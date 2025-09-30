# Save  in  any  file  of  cwd
import  p1 . mod1 
print(p1.mod1.x)  #How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()      #How  to  call  function  f1()  of  mod1  in  package  p1
c = p1.mod1.c1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
c.m1()
print()
print()
print(p1.x)       #How  to  print  object  'x'  of  _init_  module  in  package  p1
print(p1.f1())    #How  to  call  function  f1()  of  _init_  module  in  package  p1
c = p1.c1()
c.m1()            #How  to  call  method  m1()  of  class  c1  in   init  module of package p1
'''
OUTPUT:
_init_   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


10
package  p1 ---> _init_  module ---> f1  function
None
package  p1 ---> _init_  module ---> class  c1  ---> m1  method
'''