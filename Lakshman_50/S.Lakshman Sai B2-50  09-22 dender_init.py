#================================================ # Save  in   cwd \ p1 \ _init_ . py
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
#================================================ # Save  in  cwd \  p1 \ mod1 . py
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
#================================================ The  above  two  are  not  home  works
#================================================ # Save  in  any  file  of  cwd

import p1.mod1
# How to print object 'x' of mod1 in package p1
print(p1.mod1.x)
# How to call function f1() of mod1 in package p1
p1.mod1.f1()
# How to call method m1() of class c1 in mod1 of package p1
a = p1.mod1.c1()
a.m1()
print()
print()
# How to print object 'x' of _init_ module in package p1
print(p1.x)
# How to call function f1() of _init_ module in package p1
p1.f1()
# How to call method m1() of class c1 in init module of package p1
b = p1.c1()
b.m1()

#================================================ # Save  in  any  file  of  cwd

from  p1   import  mod1
# How  to  print  object  'x'  of  mod1  in  package  p1
print(mod1.x)
# How  to  call  function  f1()  of  mod1  in  package  p1
mod1.f1()
# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a=mod1.c1()
a.m1()
print(p1 . x)  #Error becoz p1 is not imported
print(p1 . _init_ . x)  #Error p1.__init__ is n  imported
print(_init_ . x)   #dender init not in cwd


#================================================ # Save  in  any  file  of  cwd

from  p1 . mod1   import  *
# How  to  print  object  'x'  of  mod1  in  package  p1
print(x)
# How  to  call  function  f1()  of  mod1  in  package  p1
f1()
# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a=c1()
a.m1()
print(p1 . x)              #Error becoz p1 module is not imported
print(p1 . _init_ . x)     #Error becoz init is not imported
print(_init_ . x) #Error becoz init is not imported
from  p1  import  mod1 . *          #Error becoz'.' is not imported

#================================================ # Save  in  any  file  of  cwd

# How  to  import  _init_  module  of  package  p1  with  import  statement
import p1.__init__.
# How  to  print  object  'x'  of   _init_  module   in   package  p1
print(p1.x)
# How  to  call  function  f1()  of   init  module  in  package  p1
p1.f1()
# How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
a=p1.c1()
a.m1()
# How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
print(p1.__init__.x)
# How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
p1.__init__.f1()
# How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
a=p1.__init__.c1()
a.m1()
print(p1 . mod1 . x)   #Error mod1 is not imported

#================================================ # Save  in  any  file  of  cwd

import   p1  #import   p1 and excuted __init__ module
import  p1 . mod1       #imported p1.mod1 (__init__ is not excuted becoz already imported and excuteted)
from   p1   import  mod1  #import mod1
from   p1 . mod1  import   *   #import members of p1.mod1
import  p1 . _init_   #import members  of __init__     excutes stmts of dender init