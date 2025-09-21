#1st program
#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1
from p1 import mod2 #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x)#How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1()#How  to  call  function  f1()  of   mod2  in  package  p1
b=mod2.c1()
b.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x)#error members cannot be called through packages
#print(x)#error x is not defined


#2nd program
#  Save  in  any  file  of  cwd  (Homework)
from p1.mod1 import * #How  to  import  members  of  mod1  in  package  p1
print(x)#How  to  print  object  'x'  of   mod1  in  package  p1
f1()#How  to  call  function  f1()  of   mod1  in  package  p1
p=c1()
p.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import * #How  to  import   members  of  mod2   in  package  p1
print(x)#How  to  print  object  'x'  of   mod2  in  package  p1
f1()#How  to  call  function  f1()  of   mod2  in  package  p1
q=c1()
q.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x)#error , as here module is not imported
#print(mod1 . x) #error, mod1 is not defined as it is not imported
#from  p1   import  mod1 . * #error cannot import module and members in the same import clause of from statement


#3rd program
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)#20
f1()#p1  ---> mod2  ---> f1
a = c1()
a . m1()#p1  ---> mod2 ---> c1 ---> m1


#4th program
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x)#10
f1() #p1  --->  mod1   --->  f1  function
a = c1()
a . m1()#p1  ---> mod1  ---> c1  ---> m1 method


#5th program
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)#30
f1()#Function of same module
a = c1()
a . m1()#Method of class c1 in same module


#6th program
from p1.mod1 import x as a ,f1 as fa ,c1 as ca #How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import x as b ,f1 as fb ,c1 as cb #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(a)#How  to  print  object  'x'  of   mod1  in  package  p1
fa()#How  to  call  function  f1()  of   mod1  in  package  p1
p=ca()
p.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(b)#How  to  print  object  'x'  of   mod2  in  package  p1
fb()#How  to  call  function  f1()  of   mod2  in  package  p1
q=cb()
q.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1


#7th program
# Save  in  any  file  of  cwd
from p1 import mod1 #How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
#print(p1 . mod1 . x) #error incorrect syntax to call members of imported module
print()
print()
from p1.p2 import mod2#How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=mod2.c1()
a.m1()#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x)#error,incorrect syntax to call the mod2 osbject
#from  p1  import   p2 . mod2 #error . operator cannot be used in import clause
#from  p2  import  mod2 #module not found found error


#8th program
# Save  in  any  file  of  cwd
from p1.mod1 import * #How  to  import  members  of  mod1  in   package  p1
print(x)#How  to  print  object  'x'  of   mod1  in  package  p1
f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import * #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * #error, invalid syntax
