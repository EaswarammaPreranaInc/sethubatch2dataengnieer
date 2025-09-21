
# Save  in  cwd \  p1 \ mod1 . py

x = 10
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')




# Save  in  cwd \ p1 \ mod2 . py

x = 20
def   f1():
	print('p1  ---> mod2  ---> f1')
class   c1:
	def  m1(self):
		print('p1  ---> mod2 ---> c1 ---> m1 ')




# 1) Save  in  any  file  of  cwd  (Homework)

from p1 import mod1, mod2       # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)                   # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()                       # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1()                          # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x)                   # How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1()                       # How  to  call  function  f1()  of   mod2  in  package  p1
a = mod2.c1()
a.m1()                          # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)            # Error as p1 is not imported 
print(x)                        # Error as x is not defined in the current module
'''
output:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1

'''





#  Save  in  any  file  of  cwd

from p1.mod1 import *           # How  to  import  members  of  mod1  in  package  p1
print(x)                        # How  to  print  object  'x'  of   mod1  in  package  p1
f1()                            # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1()                          # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import *           # How  to  import   members  of  mod2   in  package  p1
print(x)                        # How  to  print  object  'x'  of   mod2  in  package  p1
f1()                            # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1()
a.m1()                          # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)           	# Error as p1 is not imported 
print(mod1 . x)                	# Error as mod1 is not imported 
from  p1   import  mod1 . *    	# Error  as mod1.* is invalid 
'''
output:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1

'''







# 2) (Home  work) Save  the  following  code  in    any  file  of  cwd, Find  outputs

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

'''
Output:
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''




# 3) (Home  work) Save  the  following  code  in  any  file  of  cwd, Find  outputs

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

'''
Output:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''






# 4) (Home work) Save  the  following  code  in    any  file  of  cwd, Find  outputs

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

'''
Output:
30
Function  of  same  module
Method  of  class  c1  in same  module
'''





# 5) (Home  work) Save  the  following  code  in  any  file  of  cwd, How  to  use  members  of  both  the  modules

from p1.mod1 import x as x1, f1 as fun1, c1 as cls1   # How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import x as x2, f1 as fun2, c1 as cls2   # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x1)       # How  to  print  object  'x'  of   mod1  in  package  p1
fun1()          # How  to  call  function  f1()  of   mod1  in  package  p1
a = cls1()
a.m1()          # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x2)       # How  to  print  object  'x'  of   mod2  in  package  p1
fun2()          # How  to  call  function  f1()  of   mod2  in  package  p1
a = cls2()
a.m1()          # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
'''
output:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1

'''







# Save  in   cwd \ p1 \ mod1.py

x = 10
def   f1():
	print('p1  --->  mod1  --->  f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> mod1 ---> c1 ---> m1 method ')




# Save  in   cwd \ p1 \ p2 \ mod2.py

x = 20
def   f1():
	print('p1 ---> p2 ---> mod2 ---> f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')





# 6) Save  in  any  file  of  cwd

from p1 import mod1             # How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)                   # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()                       # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1()                          # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x)           	# Error p1 is not imported
print()
print()
from p1.p2 import mod2          # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)                   # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()                       # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = mod2.c1()
a.m1()                          # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x)      	# Error as it is invalid syntax
from  p1  import   p2 . mod2   	# Error as p2 . mod2 is not allowed in import path in from statement 
from  p2  import  mod2          # Error as p2 is not main package it only exists in p1
'''
output:
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method 

20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method

'''






# 7) Save  in  any  file  of  cwd

from p1.mod1 import *           # How  to  import  members  of  mod1  in   package  p1
print(x)                        # How  to  print  object  'x'  of   mod1  in  package  p1
f1()                            # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1()                          # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import *        # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)                        # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()                            # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = c1()
a.m1()                          # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . *     	# Error as cannot do mod1.* in an import statement
'''
output:
10
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method 

20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method

'''