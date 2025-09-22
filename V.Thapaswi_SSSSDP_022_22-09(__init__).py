# Save  in   cwd \ p1 \ _init_ . py
print('_init_   module  of  package ' , _name_ , ' is  executed')
x = 10
def   f1():
	print('package  p1 ---> _init_  module ---> f1  function')
class   c1:
	def  m1(self):
		print('package  p1 ---> _init_  module ---> class  c1  ---> m1  method')


'''
1) What  is  the  name  of  module ?  ---> p1 . _init_

2) What  are  the  members  of  the  p1 . _init_ ?   ---> Object  'x'  ,  function   f1()  and  class   c1

3) py  _init_ . py
    What  are  the  outputs  ?  --->  _init_   module  of  package  _main_  is  executed
'''


# Save  in  cwd \  p1 \ mod1 . py
x = 20
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')


'''
1) What  is  the  name  of  module  ?  --->  p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?   ---> Object  'x'  ,  function  f1()  and   class  c1
'''

# Save  in  any  file  of  cwd
import  p1 . mod1
print(mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
mod.f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
import p1#first import p1 and call the members of p1
p1.x#How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1()#How  to  call  function  f1()  of  _init_  module  in  package  p1
a=p1.c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1



# Save  in  any  file  of  cwd
from  p1   import  mod1
mod1.x#How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)#error bcz p1 is not imported
print(p1 . _init_ . x)#error bcz __init__ not imported
print(_init_ . x)#error


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)#How  to  print  object  'x'  of  mod1  in  package  p1
f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)#error bcz p1 is not imported
print(p1 . _init_ . x)#error __init__ is not imported
print(_init_ . x)#error
from  p1  import  mod1 . *#error '.' not use in import clause in from statement


# Save  in  any  file  of  cwd
import p1#How  to  import  _init_  module  of  package  p1  with  import  statement
p1.x#How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.f1()#How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1()#How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
from p1 import x#How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
f1()#How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x)#error mod1 is not imported


# Save  in  any  file  of  cwd
import   p1#import package p1 and __init__ module is automatically executed
import  p1 . mod1#module of p1 is imported
from   p1   import  mod1 #module is imported 
from   p1 . mod1  import   *#all members of modules is imported
import  p1 . _init_#__init__ is imported

