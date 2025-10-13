# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)		#How  to  print  object  'x'  of  mod1  in  package  p1#
print(p1.mod1.f1())		#How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.c1()		#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print()
print(p1.x)			#How  to  print  object  'x'  of  init  module  in  package  p1
p1.f1()				#How  to  call  function  f1()  of  init  module  in  package  p1
b = p1.c1()		#How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1
b.m1()





# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)			#How  to  print  object  'x'  of  mod1  in  package  p1
print(mod1.f1())		#How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()		#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print(p1 . x)			#Throws error as we are not importing p1
print(p1 ._init_. x)		#Throws error as we are not importing p1
print(_init_. x)		#Throws error as we are not importing dunder init module





# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)			#How  to  print  object  'x'  of  mod1  in  package  p1
f1()				#How  to  call  function  f1()  of  mod1  in  package  p1
a = c1()			#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print(p1 . x)			#Throws error as package p1 is not imported	
print(p1._init_.x)		#Throws error as package p1 is not imported
print(_init_.x)		#Throws error as dunder init module is not imported
from  p1  import  mod1 . *	#Syntax error





# Save  in  any  file  of  cwd
import p1				#How  to  import  init  module  of  package  p1  with  import  statement
print(p1.x)				#How  to  print  object  'x'  of   init  module   in   package  p1
print(p1.f1())				#How  to  call  function  f1()  of   init  module  in  package  p1
a = p1.c1()				#How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
c.m1()
from p1 import x			#How  to  print  object  'x'  of   init  module   in   package  p1  in  another  way
print(x)
from p1 import f1			#How  to  call  function  f1()  of   init  module  in  package  p1  in  another  way
f1()
from p1 import c1			#How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1  in  another  way
a = c1()
a.m1()
print(p1 . mod1 . x)			#Throws error as mod1 is not imported






# Save  in  any  file  of  cwd
import   p1			#imports package p1 and automatically executes _init_
import  p1 . mod1		#imports mod1 module of p1 package
from p1 import mod1		#imports module mod1 of package p1
from p1.mod1 import *		#imports all the members of module mod1 of package p1
import  p1._init_		#Throws error as dunder init can'be be imported in such manner
