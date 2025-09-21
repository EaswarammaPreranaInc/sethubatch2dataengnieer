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



#  Save  in  any  file  of  cwd  
from p1 import mod1, mod2  #  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) #   print  object  'x'  of   mod1  in  package  p1
mod1.f1() #  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1() 
a.m1() #  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()

print(mod2.x) #  print  object  'x'  of   mod2  in  package  p1
mod2.f1() #  call  function  f1()  of   mod2  in  package  p1
b=mod2.c1()
b.m1() #   call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # error: because p1 is not imported
#print(x) # error: searches in the current program


#  Save  in  any  file  of  cwd
from p1.mod1 import x,f1,c1 #   import  members  of  mod1  in  package  p1
print(x) #   print  object  'x'  of   mod1  in  package  p1
f1() #   call  function  f1()  of   mod1  in  package  p1
a=c1() 
a.m1() #   call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()

from p1.mod2 import x,f1,c1 #   import   members  of  mod2   in  package  p1
print(x) #   print  object  'x'  of   mod2  in  package  p1
f1() #  call  function  f1()  of   mod2  in  package  p1
b=c1() 
b.m1() # call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # Error: p1 is not imported
#print(mod1 . x) # # error : mod1 is not imported
#from  p1   import  mod1 . * # error



''' 
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



''' 
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



''' 
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



'''  
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1.mod1 import x as x1, f1 as f1_mod1, c1 as c1_mod1 # import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import x as x2, f1 as f1_mod2, c1 as c1_mod2 # import   members  of  mod2   in  package  p1  with  from  statement
print(x1)# print  object  'x'  of   mod1  in  package  p1
f1_mod1()#  call  function  f1()  of   mod1  in  package  p1
a=c1_mod1() 
a.m1() # call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x2) # print  object  'x'  of   mod2  in  package  p1
f1_mod2() # call  function  f1()  of   mod2  in  package  p1
b=c1_mod2() 
a.m1() # call  method  m1()  of   class  c1  in  mod2  of  package  p1



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



# Save  in  any  file  of  cwd
from p1 import mod1 # import  mod1  of  package  p1  with  from  statement
print(mod1.x) # print  object  'x'  of   mod1  in  package  p1
mod1.f1() # call  function  f1()  of   mod1  in  package  p1
a=mod1.c1() 
a.m1() # call  method  m1()  of   class  c1  in  mod1  of  package  p1
#print(p1 . mod1 . x) # error : p1 is not imported
print()
print()
from p1.p2 import mod2 # import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x) # print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() # call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b=mod2.c1() 
b.m1() # call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x) # error : p1 and p2 are not imported
#from  p1  import   p2 . mod2 # error : invalid syntax
#from  p2  import  mod2 # error : p2 is inside p1, not in current working directory



# Save  in  any  file  of  cwd
from p1.mod1 import x,f1,c1 # import  members  of  mod1  in   package  p1
print(x) # print  object  'x'  of   mod1  in  package  p1
f1() # call  function  f1()  of   mod1  in  package  p1
a=c1() 
a.m1() # call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import x,f1,c1 # import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) # print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b=c1() 
b.m1() #  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * # error : invalid syntax