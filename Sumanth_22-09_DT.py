 #Save  in   cwd \ p1 \ _init_ . py
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
print(p1 . mod1 . x)#How  to  print  object  'x'  of  mod1  in  package  p1
print(p1 . mod1 . f1())#How  to  call  function  f1()  of  mod1  in  package  p1
print(p1 . mod1 . c1().m1())#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(x)#How  to  print  object  'x'  of  _init_  module  in  package  p1
f1()#How  to  call  function  f1()  of  _init_  module  in  package  p1
c1().m1()#How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1




# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
print(mod1.f1())#How  to  call  function  f1()  of  mod1  in  package  p1
print(mod1.c1().m1())#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)
print(p1 . _init_ . x)
print(_init_ . x)


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)#How  to  print  object  'x'  of  mod1  in  package  p1
print(f1())#How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print(p1 . x)#error
print(p1 . _init_ . x)#error
print(_init_ . x)#error
from  p1  import  mod1 . * #error




# Save  in  any  file  of  cwd
import p1 #How  to  import  _init_  module  of  package  p1  with  import  statement
print(x)#How  to  print  object  'x'  of   _init_  module   in   package  p1
f1()#How  to  call  function  f1()  of   init  module  in  package  p1
a=c1()#How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
a.m1()#How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
print(p1._init_.x)#How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=p1._init_.c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x)



# Save  in  any  file  of  cwd
import   p1#imports and executes  _init_  module  of  package  p1
import  p1 . mod1#imports and executes  mod1  module  of  package  p1
from   p1   import  mod1#imports  mod1  module  of  package  p1
from   p1 . mod1  import   *#imports  all  members  of  mod1  module  of  package  p1
import  p1 . _init_#imports and executes  _init_  module  of  package  p1
