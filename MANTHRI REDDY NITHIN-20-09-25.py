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

# Save  in  cwd \ p1 \ mod2 . py
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
import p1.mod1,p1.mod2  # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(p1.mod1.x)  # How  to  print  object  'x'  of   mod1  in  package  p1
p1.mod1.f1()  # How  to  call  function  f1()  of   mod1  in  package  p1
a=p1.mod1.c1()  # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(p1.mod2.x)  # How  to  print  object  'x'  of   mod2  in  package  p1
p1.mod2.f1()  # How  to  call  function  f1()  of   mod2  in  package  p1
a=p1.mod2.c1()  # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
a.m1()  # 
print(p1 . mod1 . x) # 'x' value of a mod1 module 
print(x) # Error

#  Save  in  any  file  of  cwd
from p1.mod1 import *   # How  to  import  members  of  mod1  in  package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1()  # How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()   #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1()
print()
print()
from p1.mod2 imort *  # How  to  import   members  of  mod2   in  package  p1
print(x)  # How  to  print  object  'x'  of   mod2  in  package  p1
f1()   # How  to  call  function  f1()  of   mod2  in  package  p1
a=c1()  # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
a.m1()
print(p1 . mod1 . x) # Error 
print(mod1 . x) # Error 
from  p1   import  mod1 . * # Error


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
print(x) 
f1() 
a = c1()
a . m1()

# Output:
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1


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
print(x)
f1()
a = c1()
a . m1()

# Output :
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


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
print(x)
f1()
a = c1()
a . m1()

# Output :
30
Function  of  same  module
Method  of  class  c1  in same  module

'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1.mod1 import x as x1,f1 as f2,c1 as c2  # How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import *  # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x1)  # How  to  print  object  'x'  of   mod1  in  package  p1
f2()  # How  to  call  function  f1()  of   mod1  in  package  p1
a=c2()  # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1()
print()
print()
print(x)  # How  to  print  object  'x'  of   mod2  in  package  p1
f1()  # How  to  call  function  f1()  of   mod2  in  package  p1
a=c1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
a.m1()


# Save  in   cwd \ p1 \ mod1.py
x = 10
def   f1():
	print('p1  --->  mod1  --->  f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> mod1 ---> c1 ---> m1 method ')



'''
1) What  is  the  name  of  module ?  ---> p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
'''


# Save  in   cwd \ p1 \ p2 \ mod2.py
x = 20
def   f1():
	print('p1 ---> p2 ---> mod2 ---> f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')



'''
1) What  is  the  name  of  module  ?  --->  p1 . p2 . mod2

2) What  are  the  members  of  p1 . p2 . mod2 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
'''


# Save  in  any  file  of  cwd
import p1.mod1  # How  to  import  mod1  of  package  p1  with  from  statement
print(p1.mod1.x)  # How  to  print  object  'x'  of   mod1  in  package  p1
p1.mod1.f1()  # How  to  call  function  f1()  of   mod1  in  package  p1
a=p1.mod1.c1()  # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1() 
print(p1 . mod1 . x) # 10
print()
print()
import p1.p2.mod2  # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(p1.p2.mod2.x)  # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
p1.p2.mod2.f1()   # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=p1.p2.mod2.c1()    # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
a.m1()
print(p1 . p2 . mod2 . x) # 20
from  p1  import   p2 . mod2 # error
from  p2  import  mod2 # Error due to not found


# Save  in  any  file  of  cwd
from p1.mod1 import *  # How  to  import  members  of  mod1  in   package  p1
print(x)  # How  to  print  object  'x'  of   mod1  in  package  p1
f1()  # How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()  # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1()
print()
print()
from p1.p2.mod2 import *  # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)  # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()  # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()  # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
a.m1() 
from  p1  import  mod1 . * # Error
