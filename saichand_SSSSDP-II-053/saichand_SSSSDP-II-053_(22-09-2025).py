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






# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)		# How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()			# How  to  call  function  f1()  of  mod1  in  package  p1
a=p1.mod1.c1() 
a.m1()				# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x)			# How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1()				# How  to  call  function  f1()  of  _init_  module  in  package  p1
a=p1.c1()
a.m1()				# How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1





# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)			# How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()			# How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1()				# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)			# error
print(p1 . _init_ . x )		# error
print(_init_ . x)		# error





# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)			# How  to  print  object  'x'  of  mod1  in  package  p1
f1()				# How  to  call  function  f1()  of  mod1  in  package  p1
a=c1() 
a.m1()				# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)			# error
print(p1 . _init_ . x)		# error
print(_init_ . x)		# error
from  p1  import  mod1 . * 	# error





# Save  in  any  file  of  cwd
import p1.__init__ 		# How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x)			# How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.f1()				# How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1()				# How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1.__init__.x)		# How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
p1.__init__.f1()		# How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=p1.__init__.c1()
a.m1()				# How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x)		# error






# Save  in  any  file  of  cwd
import   p1 			# _init_   module  of  package  p1  is  executed
import  p1 . mod1 		# only mod1  module  of  package  p1  is  imported 
from   p1   import  mod1 	# only mod1  module  of  package  p1  is  imported 
from   p1 . mod1  import   * 	# only mod1  module  members of  package  p1  is  imported 
import  p1 . _init_ 		# error 

