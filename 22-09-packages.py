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



import p1
import p1.mod1
from p1 import mod1
from p1.mod1 import *

print("---- From mod1 ----")
print(p1.mod1.x)         # 20
p1.mod1.f1()             # p1 ---> mod1 ---> f1 function
p1.mod1.c1().m1()        # p1 ---> mod1 ---> c1 ---> m1 method

print("---- From __init__ ----")
print(p1.x)              # 10
p1.f1()                  # package p1 ---> __init__ module ---> f1 function
p1.c1().m1()             # package p1 ---> __init__ module ---> class c1 ---> m1 method

print("---- Using from p1.mod1 import * ----")
print(x)                 # 20
f1()                     # p1 ---> mod1 ---> f1 function
c1().m1()                # p1 ---> mod1 ---> c1 ---> m1 method

print("---- Alternative import of __init__ members ----")
from p1 import x as x_init, f1 as f1_init, c1 as c1_init
print(x_init)            # 10
f1_init()                # package p1 ---> __init__ module ---> f1 function
c1_init().m1()           # package p1 ---> __init__ module ---> class c1 ---> m1 method







