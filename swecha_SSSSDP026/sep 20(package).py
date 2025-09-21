# Save  in  cwd \  p1 \ mod1 . py
x = 10
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')



'''
1) What  is  the  name  of  module ?  --->  p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x' ,  Function   f1()  and  class  c1
'''

#Save  in  cwd \ p1 \ mod2 . py
x = 20
def   f1():
	print('p1  ---> mod2  ---> f1')
class   c1:
	def  m1(self):
		print('p1  ---> mod2 ---> c1 ---> m1 ')



 '''
1) What  is  the  name  of  module ?  --->  p1 . mod2

2) What  are  the  members  of  p1 . mod2 ?  --->  Object  'x' ,  Function   f1()  and  class  c1
'''

#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1,mod2# How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)# How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1# How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x)# How  to  print  object  'x'  of   mod2  in  package  p1
mod1.f1# How  to  call  function  f1()  of   mod2  in  package  p1
a = mod2.c1()
a.c1()# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)#error we are not imported pacakage p1
print(x)#we have imported modules not members of module

#  Save  in  any  file  of  cwd
from p1.mod1 import *# How  to  import  members  of  mod1  in  package  p1
print(x)# How  to  print  object  'x'  of   mod1  in  package  p1
f1()# How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p2.mod2 import *# How  to  import   members  of  mod2   in  package  p1
print(x)# How  to  print  object  'x'  of   mod2  in  package  p1
f1()# How  to  call  function  f1()  of   mod2  in  package  p1
b = c1()
b.m1()# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)#error
print(mod1 . x)#error
from  p1   import  mod1 . *#error

'''  (Home  work)
# Save  the  following  code  in    any  file  of  cwd
# Find  outputs
# '''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)
f1()
a = c1()
a . m1()

# outputs:
10
p1 ---> mod2 ---> f1
p1 ---> mod2 ---> c1 ---> m1


# ''' (Home work)
# Save  the  following  code  in    any  file  of  cwd
# Find  outputs
# '''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)#30
f1()# function of same module
a = c1()
a . m1()#method of class c1 in same module

# '''  (Home  work)
# Save  the  following  code  in  any  file  of  cwd
# How  to  use  members  of  both  the  modules
# '''
from p1.mod1 import x as x1,f1 as f11,c1 as c11# How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import x as x2, f1 as f22,c2 as c22# How  to  import   members  of  mod2   in  package  p1  with  from  statement
x1# How  to  print  object  'x'  of   mod1  in  package  p1
f11# How  to  call  function  f1()  of   mod1  in  package  p1
a = c11()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
# print()
# print()
x2# How  to  print  object  'x'  of   mod2  in  package  p1
f22# How  to  call  function  f1()  of   mod2  in  package  p1
b = c22()
b.m1()# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1


# Save  in   cwd \ p1 \ mod1.py
x = 10
def   f1():
	print('p1  --->  mod1  --->  f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> mod1 ---> c1 ---> m1 method ')



# '''
# 1) What  is  the  name  of  module ?  ---> p1 . mod1

# 2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
# '''

# Save  in   cwd \ p1 \ p2 \ mod2.py
x = 20
def   f1():
	print('p1 ---> p2 ---> mod2 ---> f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')



# '''
# 1) What  is  the  name  of  module  ?  --->  p1 . p2 . mod2

# 2) What  are  the  members  of  p1 . p2 . mod2 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
# '''

# Save  in  any  file  of  cwd
from p1 import m1# How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)# How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()# How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x)#error
print()
print()
from p1 import p2.mod2# How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(p2.mod2.x)# How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
p2.mod2.f1()# How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = p2.mod2.c1()
a.m1()# How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x)#error
from  p1  import   p2 . mod2#error
from  p2  import  mod2#error

# Save  in  any  file  of  cwd
from p1.mod1 import# How  to  import  members  of  mod1  in   package  p1
print(x)# How  to  print  object  'x'  of   mod1  in  package  p1
f1()# How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import# How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)# How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()# How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b = c1()
b.m1()# How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . *#error