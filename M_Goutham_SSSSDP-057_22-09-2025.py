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
    What  are  the  outputs  ?  --->  __init__   module  of  package  _main_  is  executed
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


#The  above  two  are  not  home  works




# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.mod1.c1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print() #Prints nothing
print() #Prints nothing
print(p1.x) #Prints the value of x in __init__ module
p1.f1() #f1 function from __init__ is execulted
b = p1.c1() #Here we are creating the object for __init__ c1 class
b.m1() #calling the m1 method of c1 class of __init__ module



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print(p1 . x) #Error #p1 is not imported
print(p1 . __init__ . x) #Error #it is not a submodule 
print(__init__ . x) #Error #same thing we cannot use __init__ as module name



# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) #How  to  print  object  'x'  of  mod1  in  package  p1
f2() #How  to  call  function  f1()  of  mod1  in  package  p1
a = c1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
a.m1()
print(p1 . x) #Error #we are importing the members of mod1
print(p1 . __init__ . x) #Error #__init__ cannot be a sub module
print(__init__ . x) #Error #we cannot use __init__ as module name
from  p1  import  mod1 . * #Error #we cannot use '.' in from clause



# Save  in  any  file  of  cwd
import p1 #How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.x) #How  to  print  object  'x'  of   __init__  module   in   package  p1
p1.f1() #How  to  call  function  f1()  of   init  module  in  package  p1
a = p1.c1() #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
a.m1() 
print(x) #How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
f1() #How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
b = c1()
b.m1() #How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x) #Error #we are not importing the mod1 we are importing the only p1



# Save  in  any  file  of  cwd
import   p1 #Here we are importing only p1 
import  p1 . mod1 #Here we are importing mod1 from p1 package
from   p1   import  mod1 #Here we are importing the mod1 from p1
from   p1 . mod1  import   * #Here we are importing the members of mod1 from p1 package
import  p1 . __init__ #Error #we no need to import __init__ it directly imported when p1 is imported It is executed **automatically** when you do `import p1