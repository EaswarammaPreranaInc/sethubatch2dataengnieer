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
print(p1.mod1.x)  #  How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()  #  How  to  call  function  f1()  of  mod1  in  package  p1
a=p1.mod1.c1()
a.m1()  #  How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x)  #  How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1()  #  How  to  call  function  f1()  of  _init_  module  in  package  p1
b=p1.c1()  
b.m1()  #  How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)   #   How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()  #  How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1()   #   How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error due to p1 is not imported
print(p1 . __init__ . x)  #  Error due to p1 is not imported
print(__init__ . x)    #  Error due to __init__ is not imported


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)  #  How  to  print  object  'x'  of  mod1  in  package  p1
f1()  #  How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()   #  How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error due to 1 is not imported
print(p1 . __init__ . x)  #   Error due to p1 is not imported
print(__init__ . x)  #  Errorr due to __init__ is not imported
from  p1  import  mod1 . *  #  Error


# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__
