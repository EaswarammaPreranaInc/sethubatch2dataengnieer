#  Save  in  any  file  of  cwd  (Homework)
How  to  import  mod1   and  mod2  of  package  p1  with  from  statement             from p1 import mod1,mod2                   
How  to  print  object  'x'  of   mod1  in  package  p1                               print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1                             mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1                a=mod1.c1()
                                                                                      a.m1()
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1                               print(mod2.x)
How  to  call  function  f1()  of   mod2  in  package  p1                             mod2.f1()
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1                a=mod2.c1()
                                                                                      a.m1()
print(p1 . mod1 . x)                                                                  Error
print(x)                                                                              Error

#  Save  in  any  file  of  cwd
How  to  import  members  of  mod1  in  package  p1                                   from p1.mod1 import *
How  to  print  object  'x'  of   mod1  in  package  p1                               print(x)
How  to  call  function  f1()  of   mod1  in  package  p1                             f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1                a=c1()
                                                                                      a.m1()
print()
print()
How  to  import   members  of  mod2   in  package  p1                                 from p1.mod2 import *
How  to  print  object  'x'  of   mod2  in  package  p1                               print(x)
How  to  call  function  f1()  of   mod2  in  package  p1                             f1()
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1                a=c1()
                                                                                      a.m1()
print(p1 . mod1 . x)                                                                  Error
print(mod1 . x)                                                                       Error
from  p1   import  mod1 . *                                                           Error

'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)                                                             20
f1()                                                                 p1  ---> mod2  ---> f1
a = c1()
a . m1()                                                             p1  ---> mod2 ---> c1 ---> m1

'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x)                                                         10
f1()                                                             p1  ---> mod1  --->f1
a = c1()
a . m1()                                                         p1  ---> mod1  --->f1

''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)                                                      30
f1()                                                          Function  of  same  module
a = c1()
a . m1()                                                      Method  of  class  c1  in same  module

'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
How  to  import   members  of  mod1   in  package  p1  with  from  statement                           from p1 import mod1
How  to  import   members  of  mod2   in  package  p1  with  from  statement                           from p1 import mod2
How  to  print  object  'x'  of   mod1  in  package  p1                                                print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1                                              mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1                                 a=mod1.c1()
                                                                                                       a.m1()
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1                                                print(mod2.x)
How  to  call  function  f1()  of   mod2  in  package  p1                                              mod2.f1()
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1                                 a=mod2.c1()
                                                                                                       a.m1()

# Save  in  any  file  of  cwd
How  to  import  mod1  of  package  p1  with  from  statement                                          from p1 import mod1
How  to  print  object  'x'  of   mod1  in  package  p1                                                print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1                                              mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1                                 a=mod1.c1()
                                                                                                       a.m1()
print(p1 . mod1 . x)                                                                                   Error
print()
print()
How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement                    from p1.p2 import mod2
How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1                          print(mod2.x)
How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1                        mod2.f1()
How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1          a=mod2.c1()
                                                                                                      a.m1()
print(p1 . p2 . mod2 . x)                                                                             Error
from  p1  import   p2 . mod2                                                                          Error
from  p2  import  mod2                                                                                Error

# Save  in  any  file  of  cwd
How  to  import  members  of  mod1  in   package  p1                                                 from p1.mod1 import *
How  to  print  object  'x'  of   mod1  in  package  p1                                              print(x)
How  to  call  function  f1()  of   mod1  in  package  p1                                            f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1                               a=c1()
                                                                                                     a.m1()
print()
print()
How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1                            from p1.p2.mod2 import *
How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1                         print(x)
How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1                       f1()
How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1         a=c1()
                                                                                                     a.m1()
from  p1  import  mod1 . *                                                                           Error
