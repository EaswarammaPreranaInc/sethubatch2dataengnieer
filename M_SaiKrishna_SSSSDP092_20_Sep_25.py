# Save  in  cwd \  p1 \ mod1 . py
x = 10
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')



'''
1) What  is  the  name  of  module ?  --->  p1 . mod1
2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x' ,  Function   f1()  and  class  c1
'''
# Save  in  cwd \ p1 \ mod2 . py
x = 20
def   f1():
	print('p1  ---> mod2  ---> f1')
class   c1:
	def  m1(self):
		print('p1  ---> mod2 ---> c1 ---> m1 ')



'''
1) What  is  the  name  of  module ?  --->  p1 . mod2

2) What  are  the  members  of  p1 . mod2 ?  --->  Object  'x' ,  Function   f1()  and  class  c1
'''


# Save in any file of cwd (Homework)
from p1 import mod1, mod2# How to import mod1 and mod2 of package p1 with from statement
print(mod1.x)# How to print object 'x' of mod1 in package p1
mod1.f1()# How to call function f1() of mod1 in package p1
a1 = mod1.c1()# How to call method m1() of class c1 in mod1 of package p1
a1.m1()
print()# blank line
print(mod2.x)# How to print object 'x' of mod2 in package p1
mod2.f1()# How to call function f1() of mod2 in package p1
a2 = mod2.c1()# How to call method m1() of class c1 in mod2 of package p1
a2.m1()


# How to import members of mod1 in package p1
from p1.mod1 import x, f1, c1
print(x)# How to print object 'x' of mod1 in package p1
f1()# How to call function f1() of mod1 in package p1
b1 = c1()# How to call method m1() of class c1 in mod1 of package p1
b1.m1()

print()# blank line

# How to import members of mod2 in package p1
from p1.mod2 import x as x2, f1 as f2, c1 as c2
print(x2)# How to print object 'x' of mod2 in package p1
f2()# How to call function f1() of mod2 in package p1
b2 = c2()# How to call method m1() of class c1 in mod2 of package p1
b2.m1()

# Only for reference (these may give error if not correct in Python):
print(p1.mod1.x)# error
print(mod1.x)# works only if mod1 imported
print(x)# works only if imported x from mod1
from  p1   import  mod1 . *# error


'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)# prints 30
f1()# call function of same module
a = c1()# create object of c1 of same module
a . m1()# call method of c1 of same module


''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)
f1()
a = c1()
a . m1()
'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1.mod1 import x as x1, f1 as f1_mod1, c1 as c1_mod1  # How to import members of mod1 in package p1 with from statement
from p1.mod2 import x as x2, f1 as f1_mod2, c1 as c1_mod2  # How to import members of mod2 in package p1 with from statement
print(x1)# How to print object 'x' of mod1 in package p1
f1_mod1()# How to call function f1() of mod1 in package p1
obj1 = c1_mod1()     
obj1.m1()# How to call method m1() of class c1 in mod1 of package p1
print()
print(x2)# How to print object 'x' of mod2 in package p1
f1_mod2()# How to call function f1() of mod2 in package p1
obj2 = c1_mod2()
obj2.m1()# How to call method m1() of class c1 in mod2 of package p1


# Save  in   cwd \ p1 \ mod1.py
x = 10
def   f1():
	print('p1  --->  mod1  --->  f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> mod1 ---> c1 ---> m1 method ')

'''
1) What  is  the  name  of  module ?  ---> p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
'''
# Save  in   cwd \ p1 \ p2 \ mod2.py
x = 20
def   f1():
	print('p1 ---> p2 ---> mod2 ---> f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')

'''
1) What  is  the  name  of  module  ?  --->  p1 . p2 . mod2

2) What  are  the  members  of  p1 . p2 . mod2 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
'''
# Save  in  any  file  of  cwd
from p1 import mod1# How to import mod1 of package p1 with from statement
print(mod1.x)# How to print object 'x' of mod1 in package p1
mod1.f1()# How to call function f1() of mod1 in package p1
obj1 = mod1.c1()# How to call method m1() of class c1 in mod1 of package p1
obj1.m1()
print()
print()
from p1.p2 import mod2# How to import mod2 of sub-package p2 in package p1 with from statement
print(mod2.x)# How to print object 'x' of mod2 in sub-package p2 of package p1
mod2.f1()# How to call function f1() of mod2 in sub-package p2 of package p1
obj2 = mod2.c1()# How to call method m1() of class c1 in mod2 of sub-package p2 in package p1
obj2.m1()
from p2 import mod2# Alternative import if p2 is top-level package (if installed separately)

# Save  in  any  file  of  cwd
from p1.mod1 import x, f1, c1  # How to import members of mod1 in package p1
print(x)# How to print object 'x' of mod1 in package p1
f1()# How to call function f1() of mod1 in package p1
obj1 = c1()
obj1.m1()# How to call method m1() of class c1 in mod1 of package p1
print()
print()
from p1.p2.mod2 import x, f1, c1  # How to import members of mod2 in sub-package p2 of package p1
print(x)# How to print object 'x' of mod2 in sub-package p2 of package p1
f1()# How to call function f1() of mod2 in sub-package p2 of package p1
obj2 = c1()
obj2.m1()# How to call method m1() of class c1 in mod2 of sub-package p2 of package p1
