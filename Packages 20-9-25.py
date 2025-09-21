# Save  in  any  file  of  cwd
# How  to  import  members  of  mod1  in   package  p1
from p1.mod1 import *
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
# How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
from p1.p2.mod2 import *
print(x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b = c1()
b . m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from p1 import mod1 . * # error as there should be no . in import clause

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''


#  Save  in  any  file  of  cwd
from p1 import mod1 # How  to  import  members  of  mod1  in  package  p1
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1() 
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2 import mod2 # How  to  import   members  of  mod2   in  package  p1
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  package  p1
b = mod2.c1() 
b . m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x) # error as p1 is not imported
print(mod1 . x)
from p1 import mod1 . * # error as there should be no . in import clause

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
10
'''


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
a = c1()
a . m1()

'''
20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''


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
a = c1()
a . m1()

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

'''


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
a = c1()
a . m1()

'''
30
Function  of  same  module
Method  of  class  c1  in same  module
'''



'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
# How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod1 import x as x1 , f1 as f11 , c1 as c11
# How  to  import   members  of  mod2   in  package  p1  with  from  statement
from p1.mod2 import x as x2 , f1 as f12 , c1 as c12
# How  to  print  object  'x'  of   mod1  in  package  p1
print(x1)
# How  to  call  function  f1()  of   mod1  in  package  p1
f11()
a = c11()
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x2) # How  to  print  object  'x'  of   mod2  in  package  p1
f12() # How  to  call  function  f1()  of   mod2  in  package  p1
b = c12()
b . m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1

'''


# Save  in  any  file  of  cwd
# Save  in  any  file  of  cwd
# How  to  import  mod1  of  package  p1  with  from  statement
from p1 import mod1
# How  to  print  object  'x'  of   mod1  in  package  p1
print(mod1.x)
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x) # Error as p1 is not imported
print()
print()
from p1.p2 import mod2 # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b = mod2.c1() 
b . m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x) # Error as p1.p2 is not imported
from  p1  import   p2 . mod2 # error aas in import clause we cannot use .
from  p2  import  mod2 # error as there is no p2 in cwd

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method

'''


# Save  in  any  file  of  cwd
# How  to  import  members  of  mod1  in   package  p1
from p1.mod1 import x as x1 , f1 as f11 , c1 as c11
print(x1) # How  to  print  object  'x'  of   mod1  in  package  p1
f11() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c11()
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import x as x2 , f1 as f12 , c1 as c12 # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x2) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f12() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = c12()
a . m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . *  # error as in import clause we cannot use .


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method

'''

