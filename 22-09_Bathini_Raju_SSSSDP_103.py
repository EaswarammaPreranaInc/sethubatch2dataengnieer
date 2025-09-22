# Save  in   cwd \ p1 \ __init__ . py
print('__init__   module  of  package ' , __name__ , ' is  executed')
x = 10
def   f1():
	print('package  p1 ---> __init__  module ---> f1  function')
class   c1:
	def  m1(self):
		print('package  p1 ---> __init__  module ---> class  c1  ---> m1  method')


'''
1) What  is  the  name  of  module ?  ---> p1 . __init__

2) What  are  the  members  of  the  p1 . __init__ ?   ---> Object  'x'  ,  function   f1()  and  class   c1

3) py  __init__ . py
    What  are  the  outputs  ?  --->  __init__   module  of  package  __main__  is  executed
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
print(mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1() 
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
import p1 #1st import p1 and  call the members of p1
print(p1.x) #How  to  print  object  'x'  of  __init__  module  in  package  p1
p1.f1() #How  to  call  function  f1()  of  __init__  module  in  package  p1
a=p1.c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error p1 is not imported 
print(p1 . __init__ . x) #Error
print(__init__ . x) #Error


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) #How  to  print  object  'x'  of  mod1  in  package  p1
f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) #Error
print(p1 . __init__  . x) #Error
print(__init__ . x) #Error
from  p1  import  mod1 . * # Error we cant use . after import 


# Save  in  any  file  of  cwd
import p1.__init__ #How  to  import  __init__  module  of  package  p1  with  import  statement
print(__init__.x) #How  to  print  object  'x'  of   __init__  module   in   package  p1
__init__.f1() #How  to  call  function  f1()  of   init  module  in  package  p1
a=__init__.c1()
a=m1() #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
import p1
print(p1.x) #How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
p1.f1() #How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
a= p1.c1() 
a.m1()#How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x) # Error


# Save  in  any  file  of  cwd
import   p1 # p1 package is imported and __init module is executed only one time __init executed
import  p1 . mod1  #module mod1 is imported and __init module is executed
from   p1   import  mod1 # mod1 is imported  and __init module is executed
from   p1 . mod1  import   * # members of mod1 imported  and __init module is executed
import  p1 . __init__ #init module is imported  and __init module is executed