from p1 import mod1, mod2 # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a=mod2.c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(mod1.x)
print(x) # error name x is not defined

from p1.mod1 import * # How  to  import  members  of  mod1  in  package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import * # How  to  import   members  of  mod2   in  package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a=c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x) # error name p1 is not defined
print(mod1 . x) # error name mod1 is not defined
from p1 import mod1.* # syntax error

x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from p1.mod1 import *
from p1.mod2 import *
print(x)  # 20
f1()  # p1  ---> mod2  ---> f1
a=c1()
a.m1()  # p1  ---> mod2 ---> c1 ---> m1


x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1.mod2 import   *
from  p1.mod1 import   *
print(x)  # 10
f1()  # p1  --->  mod1   --->  f1  function
a=c1()
a.m1()  # p1  ---> mod1  ---> c1  ---> m1 method

from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)  # 30
f1()  # Function  of  same  module
a = c1()
a . m1()  # Method  of  class  c1  in same  module

from p1.mod1 import x as x11,f1 as f11,c1 as c11 # How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import x as x22,f1 as f22,c1 as c22 # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x11)# How  to  print  object  'x'  of   mod1  in  package  p1
f11() # How  to  call  function  f1()  of   mod1  in  package  p1
a=c11()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x22) # How  to  print  object  'x'  of   mod2  in  package  p1
f22() # How  to  call  function  f1()  of   mod2  in  package  p1
a=c22()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

from p1 import mod1 # How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x) # error name p1 not defined
print()
print()
from p1.p2 import mod2 # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a= mod2.c1()
a.m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x) # error name p1 not defined
from p1 import p2.mod2 # error invalid synta
from p2 import mod2 # module not found error

from p1.mod1 import * # How  to  import  members  of  mod1  in   package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import * # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)# How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from p1 import mod1.* # error invalid syntax
