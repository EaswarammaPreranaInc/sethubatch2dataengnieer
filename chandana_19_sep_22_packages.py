# Save  in   cwd \ p1 \ _init_ . py
print('_init_   module  of  package ' , __name__ , ' is  executed')
x = 10
def   f1():
	print('package  p1 ---> _init_  module ---> f1  function')
class   c1:
	def  m1(self):
		print('package  p1 ---> _init_  module ---> class  c1  ---> m1  method')


# Save  in  cwd \  p1 \ mod1 . py
x = 20
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')


# Save in any file of cwd
import  p1.mod1
print(mod1.x) #  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1() #  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) #  print  object  'x'  of  _init_  module  in  package  p1
p1.f1() # call  function  f1()  of  _init_  module  in  package  p1
b=p1.c1() 
b.m1() # call  method  m1()  of  class  c1  in   init  module  of  package  p1



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) #  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1() 
a.m1() # call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # error : p1 is not imported
#print(p1 . _init_ . x) # error: invalid syntax 
#print(_init_ . x) # error : innalid


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) #  print  object  'x'  of  mod1  in  package  p1
f1() # call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1() # call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # error : p1 is not imported
#print(p1 . _init_ . x) # error : invalid
#print(_init_ . x) # error : invalid
#from  p1  import  mod1 . * # error: invalid synatx



# Save  in  any  file  of  cwd
import p1 # import  _init_  module  of  package  p1  with  import  statement
print(p1.x) #  print  object  'x'  of   _init_  module   in   package  p1
p1.f1() # call  function  f1()  of   init  module  in  package  p1
a=p1.c1() 
a.m1() # call method  m1()  of  class  c1  in   init  module  of  package  p1
from p1 import x,f1,c1
print(x) # print  object  'x'  of   _init_  module   in   package  p1  in  another  way
f1() # call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=c1() 
a.m1() # call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
#print(p1 . mod1 . x) # error : mod1 is not imported



# Save  in  any  file  of  cwd
import   p1 # import p1/__init__
import  p1 . mod1 # imports module mod1
from   p1   import  mod1 # imports module mod1
from   p1 . mod1  import   * # imports members of mod1
#import  p1 . _init_ # error