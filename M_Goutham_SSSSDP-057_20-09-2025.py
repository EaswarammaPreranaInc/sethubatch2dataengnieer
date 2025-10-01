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




#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1,mod2	#How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)	#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1() 	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print() #Prints nothing
print() #prints nothing
print(mod2.x)	#How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b = mod2.c1()
b.m1()	#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x) #Error #we are importing the mod1 and mod2 modules not p1 package
print(x) #Error #x is not defined in the current module




#  Save  in  any  file  of  cwd
from p1.mod1 import *	#How  to  import  members  of  mod1  in  package  p1
print(x)	#How  to  print  object  'x'  of   mod1  in  package  p1
f1()	#How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1() 	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print() #prints nothing
print() #prints nothing
from p1.mod2 import * #How  to  import   members  of  mod2   in  package  p1
print(x) #How  to  print  object  'x'  of   mod2  in  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b = c1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
b.m1()
print(p1 . mod1 . x) #Error #we have imported the members of mod1 and mod2 not p1 and mo1 mod2
print(mod1 . x) #Error #we have imported the members of mod1 and mod2 not mod1
from  p1   import  mod1 . * #Error #we cannot use '.' in from clause




'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30 #Ref x points to int obj 30
def   f1(): #f1 function is defined 
	print('Function  of  same  module')
class  c1: #c1 class is created
	def  m1(self): #m1 method of c1 class is defined
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    * #Here we have imported the members of mod1 from p1 package #ignored
from  p1 . mod2    import    * #Here we have imported the members of mod2 from p1 package #Recognized
print(x) #prints value of x from mod2 module
f1() #f1 function is called from mod2
a = c1() #c1 class obj of mod2 is created
a . m1() #m1 method of c1 class from mod2 is called





'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30 #Ref x points to int obj 30 
def   f1(): #f1 function is defined 
	print('Function  of  same  module')
class  c1: #c1 class is created
	def  m1(self): #m1 method of class c1
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   * #Here we are importing the members of mod2 of p1 package
from  p1 . mod1    import   * #Here we are importing the members of mod1 of p1 package
print(x) #Prints the value of x of mod1 module
f1() #f1 function is called from mod1 module
a = c1() #creates an empty object of c1 class of mod1 module
a . m1() #m1 method of c1 class of mod2 is called




''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1 import *	#Here we are importing the members of mod1 from p1 package 
from  p1 . mod2 import *  #Here we are importing the members of mod2 from p1 package
x = 30	#Ref x points to int obj 30
def   f1(): #Here f1 function is defined 
	print('Function  of  same  module')
class  c1: #Here c1 class is created 
	def  m1(self): #Here m1 method is defined in c1 class 
		print('Method  of  class  c1  in same  module')
print(x) #Prints the value of x in current program i.e 30
f1() #Here current program function f1 is called 
a = c1() #Here current program c1 class object is created
a . m1() #Here m1 method is called from current program c1 class




'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1 import mod1 #How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1 import mod2 #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(mod1.x)	#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1()
print() #Prints nothing
print() #Prints nothing
print(mod2.x) #How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b = mod2.c1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
b.m1()



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
from p1 import mod1	#How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)	#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()	#How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1()	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x) #Error #we are importing the mod1 from p1 not p1 directly
print() #Prints nothing
print() #Prints nothing
from p1.p2 import mod2 #How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)	#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b = mod2.c1()
b.m1()	 #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x) #Error #we are imported the mod2 of sub-package p2 of p1 package
from  p1  import   p2 . mod2 #Error #We cannot use '.' in from clause 
from  p2  import  mod2 #Error #We have p2 inside p1 so it should be p1.p2 




# Save  in  any  file  of  cwd
from p1.mod1 import * 	#How  to  import  members  of  mod1  in   package  p1
print(x) #How  to  print  object  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = c1() 
a.m1()	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print() #Prints nothing
print() #Prints nothing
from p1.p2.mod2 import * #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) #How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
b = c1() #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
b.m1()
from  p1  import  mod1 . * #Error #we cannot use '.' in from clause