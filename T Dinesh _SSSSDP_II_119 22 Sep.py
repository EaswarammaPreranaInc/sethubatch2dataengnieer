 Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
obj1 = p1.mod1.c1()
obj1.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) #How  to  print  object  'x'  of  __init__  module  in  package  p1
p1.f1() #How  to  call  function  f1()  of  __init__  module  in  package  p1
obj2 = p1.c1()
obj2.m1() #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1


     

# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
obj1 = mod1.c1()
obj1.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)   # error
print(p1 . __init__ . x)    # error
print(__init__ . x) # error




 
# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) #How  to  print  object  'x'  of  mod1  in  package  p1
f1() #How  to  call  function  f1()  of  mod1  in  package  p1
obj = c1()
obj.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)   # error
print(p1 . __init__ . x)    # error
print(__init__ . x) # error
from  p1  import  mod1 . *  # error




# Save  in  any  file  of  cwd
import p1   #How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.x)#How  to  print  object  'x'  of   __init__  module   in   package  p1
p1.f1() #How  to  call  function  f1()  of   init  module  in  package  p1
obj = p1.c1()
obj.m1() #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
from p1 import * 
print(x) #How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
f1() #How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
obj = c1()
obj.m1() #How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x)    