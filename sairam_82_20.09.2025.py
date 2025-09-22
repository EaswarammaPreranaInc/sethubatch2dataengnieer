#  Save  in  any  file  of  cwd  (Homework)
from PYTHON import mod1
from PYTHON import mod2    #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
mod1.x  #How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()  ##How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1() #
a.m1() #    How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
mod2.x  #How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1()   #How  to  call  function  f1()  of   mod2  in  package  p1
b=mod2.c1()
b.m1()  #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)    # error as p1 is not imported 
print(x)    # eror as x is not there in current module

#  Save  in  any  file  of  cwd
from PYTHON.mod1 import *  #How  to  import  members  of  mod1  in  package  p1
print(x) ##How  to  print  object  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from PYTHON.mod2 import * #How  to  import   members  of  mod2   in  package  p1
print(x)  ##How  to  print  object  'x'  of   mod2  in  package  p1
f1()#How  to  call  function  f1()  of   mod2  in  package  p1
b=c1()
b.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x)    # error as package is not imported only members are imported
#print(mod1 . x)# error as module are not imported only members are imported
#from  p1   import  mod1 . *     # error as in from statement import clause . should not be there

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
from  PYTHON. mod1    import    *
from  PYTHON . mod2    import    *
print(x)    # imports and prints x of python.mod2 as it is latest one imported
f1()    # imports and prints f1 of python.mod2 as it is latest one imported
a = c1() # imports class c1 of mod2 of PYTHON package
a . m1()    # m1 of c1 class object a


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
from  PYTHON . mod2    import   *
from  PYTHON. mod1    import   *
print(x)    # imports and prints x of python.mod1 as it is laST imported
f1()    # imports and prints f1 of python.mod1 as it is last imported
a = c1() # imports class c1 of mod1 of PYTHON package
a . m1()    # m1 of c1 class object a


''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  PYTHON . mod1    import    *
from  PYTHON. mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)    # imports and prints x of current program as it is laST imported
f1()    # imports and prints f1 of current prgm as it is last imported
a = c1() # imports class c1 of current prgm
a . m1()    # m1 of c1 class object a


'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''

from PYTHON.mod1 import x as x1, f1 as f11, c1 as c11 #How  to  import  members  of  mod1  in  package  p1
from PYTHON.mod2 import x as x2, f1 as f12, c1 as c12    #How  to  import   members  of  mod2   in  package  p1
print(x1) ##How  to  print  object  'x'  of   mod1  in  package  p1
print(f11()) #How  to  call  function  f1()  of   mod1  in  package  p1
a=c11()
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x2) #How  to  print  object  'x'  of   mod2  in  package  p1
print(f12()) #How  to  call  function  f1()  of   mod2  in  package  p1
b=c12()
b.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1


# Save  in  any  file  of  cwd
from PYTHON import mod1     # How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)    # #How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()    # #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1()    # #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(  PYTHON . mod1 . x)    # error as Python is not imported
print()
print()
from  PYTHON.p2 import mod2 #How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)    # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()    # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=mod2.c1()
a.m1()    #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(PYTHON . p2 . mod2 . x)   #error as PYTHON.p2 is not imported
from  PYTHON  import   p2 . mod2   # error as in from statement import clause . should not be there  
from  PYTHON  import  mod2  # imports mod2 of current package

# Save  in  any  file  of  cwd
from PYTHON.mod1 import *   #How  to  import  members  of  mod1  in   package  p1
print(x)    ##How  to  print  object  'x'  of   mod1  in  package  p1
f1()    #How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()  #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from PYTHON.p2.mod2 import *    #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)    #How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()    #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1()  #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  PYTHON  import  mod1 . *  # error as in from statement import clause . should not be there 
