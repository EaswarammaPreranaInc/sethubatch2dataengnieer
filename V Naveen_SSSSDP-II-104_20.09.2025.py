#1.  Save  in  any  file  of  cwd  (Homework)
from Prog1 import mod1, mod2 # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1() 
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = mod2.c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # Error
#print(x) # Error

#10
#p1  --->  mod1   --->  f1  function
#p1  ---> mod1  ---> c1  ---> m1 method


#20
#p1  ---> mod2  ---> f1
#p1  ---> mod2 ---> c1 ---> m1



#2.  Save  in  any  file  of  cwd
from Prog1.mod1 import * # How  to  import  members  of  mod1  in  package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1()  # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from Prog1.mod2 import * # How  to  import   members  of  mod2   in  package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # Error
#print(mod1 . x) # Error
#from  p1   import  mod1 . * # Error

#10
#p1  --->  mod1   --->  f1  function
#p1  ---> mod1  ---> c1  ---> m1 method


#20
#p1  ---> mod2  ---> f1
#p1  ---> mod2 ---> c1 ---> m1




#3. (Home  work)
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  Prog1 . mod1    import    *
from  Prog1 . mod2    import    *
print(x) # 20
f1() # p1  ---> mod2  ---> f1
a = c1()
a . m1() # p1  ---> mod2 ---> c1 ---> m1





#4.  (Home  work)
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  Prog1 . mod2    import   *
from  Prog1 . mod1    import   *
print(x) # 10
f1() # p1  --->  mod1   --->  f1  function
a = c1()
a . m1() # p1  ---> mod1  ---> c1  ---> m1 method






#5. (Home work)
from  Prog1 . mod1    import    *
from  Prog1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) # 30
f1() # Function  of  same  module
a = c1()
a . m1() # Method  of  class  c1  in same  module




#6. (Home  work)
# How  to  use  members  of  both  the  modules
from Prog1.mod1 import x as x1 ,f1 as f11 , c1 as c11 # How  to  import   members  of  mod1   in  package  p1  with  from  statement
from Prog1.mod2 import * # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x1) # How  to  print  object  'x'  of   mod1  in  package  p1
f11() # How  to  call  function  f1()  of   mod1  in  package  p1
a =  c11() 
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x) # How  to  print  object  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1() 
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

#10
#p1  --->  mod1   --->  f1  function
#p1  ---> mod1  ---> c1  ---> m1 method


#20
#p1  ---> mod2  ---> f1
#p1  ---> mod2 ---> c1 ---> m1




#7. Save  in  any  file  of  cwd
from Prog1 import mod1 # How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1() 
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
# print(p1 . mod1 . x) # Error
print()
print()
from Prog1.p2 import mod2 # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = mod2.c1() 
a.m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x) # Error
#from  p1  import   p2 . mod2 # Error
#from  p2  import  mod2 # Error
#10
#p1  --->  mod1   --->  f1  function
#p1  ---> mod1  ---> c1  ---> m1 method


#20
#p1  ---> mod2  ---> f1
#p1  ---> mod2 ---> c1 ---> m1



#8. Save  in  any  file  of  cwd
from Prog1.mod1 import * # How  to  import  members  of  mod1  in   package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1() 
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from Prog1.p2.mod2 import * # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = c1() 
a.m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * # Error
#10
#p1  --->  mod1   --->  f1  function
#p1  ---> mod1  ---> c1  ---> m1 method


#20
#p1  ---> mod2  ---> f1
#p1  ---> mod2 ---> c1 ---> m1



