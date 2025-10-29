
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')  # Hello
import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye') # Bye
import  mod4
print(x)    # Error x is not there in current module
f1()


#  Find  outputs  (Home  work)
print('Before') # Before
import mod2
print(mod2 . x) # x value in mod2
mod2 . f1()
print('After')  # After
run_module('mod2')  # Error run_module  is not there in current module
runpy . run_module(mod2) # Error argument of run_module should be string module

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') # Begin
from cal import *  #How  to  import  all  the  members  of  cal  module
print(x) # 100
print(y) # 200
print(cal . x) # Error since we are using cal module without importing
print(add(10,7)) # 17
print(sub(10,7)) # 3
print(mul(10,7)) # 70
print(div(10,7)) # 1.42
print(cal . add(x , y)) # Error since we are using cal module without importing
a=c1() 
a.m1() # m1 method
b = cal . c1() # Error since we are using cal module without importing

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')  # Begin
from cal import x,add,mul,c1 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) # 100
print(y) # Error y is not there in current module
print(cal . x) # Error since we are using cal module without importing
print(add(10,7)) # 17
print(sub(10 , 7)) # Error as function sub is not there in current module
print(mul(10,7)) # 70
print(div(10 , 7)) #  Error as function div is not there in current module
a=c1() 
a.m1()  # m1 method


# Module  alias
print('Begin')
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) # 100
print(c.y) # 200
print(c.add(10,7)) # 17
print(c.sub(10,7)) # 3
print(c.mul(10,7)) # 70
print(c.div(10,7)) # 1.42
a=c.c1() 
a.m1()  # m1 method
print(cal . x) # Error module name is changed to c
from  math  as   m  import  *  # Error Here module is not imported members of the module is imported 

# Member  alias
from cal import x as object , add as fun1 , mul as fun2 , c1 as class #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(object) # 100
print(x) # Error x is modified to new name as object
print(fun1) # 17
print(fun2) # 70
a=class()
a.m1() # m1 method
print(add(10 , 7)) # Error add function name is modified to fun1
b = c1() #Error  class c1 name is modified to class 


# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)    #  10
disp()  # disp function of mod1
a = c1()    
a . m1()    # m1 method  of class c1 in mod1


# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)    # 30
disp()  # disp function of same module
a = c1()
a . m1()    # m1  method of  class  c1  in  same  module

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
#How  to  import  mod1  and  mod2
import mod1 , mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #10
mod1.disp() #disp function of mod1
a=mod1.c1() 
a.m1()  # m1 methhod of class c1 in mod1
print()
print(mod2.x) #20
mod2.disp() # disp function of mod2
b=mod2.c1() 
b.m1()  # m1 method of class c1 in mod2
print()
print(x) # 30 
disp() # disp function of same module
c=c1() 
c.m1() # m1 method of class c1 in same module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as obj , disp as fun1 , c1 as class1 #How  to  import  members  of  mod1
from mod2 import x as obj2 , disp as fun2 , c1 as class2 #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  class1  in  same  module')
print(obj) # 10
fun1() # disp function of mod1
a=class1()
a.m1() # m1 method of class c1 in mod1
print()
print()
print(obj2) # 20
fun2() # disp function of mod2
b=class2() 
b.m1() # m1 method of class class2 in mod2
print()
print()
print(x) # 30
disp() # disp function of same module
c=c1()
c.m1() # m1 method of class c1 in same module

# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__ == '__main__':
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')



What  are  the  outputs ?  --->

# Find  outputs (Home  work)
print('Begining  of  mod2') # Begining of mod2
import   mod1   # One <nextline> Two <nextline> Three <nextline> Seven <nextline> Eight <nextline> Nine
print('End  of  mod2')  # End of mod2

#  Find  outputs
from  cal  import  *
print(x)    # 100
print(y)    # 200
print(add(10 , 7))  # 17
print(sub(10 , 7))  # 3
print(mul(10 , 7))  # 70
print(div(10 , 7))  # 1.42
a = c1()
a . m1()    # m1 method

#  Find  outputs
import  cal
print(cal . x)  # 100
print(cal . y)  # 200
print(cal . add(10 , 7))    # 17
print(cal . sub(10 , 7))    # 3
print(cal . mul(10 , 7))    # 70
print(cal . div(10 , 7))    # 1.42
a = cal . c1()
a . m1()    # m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x)    # Error x is not defined in current module
print(y)    # y is executed through module cal
print(add(10 , 7))  # Error add function is not there in current module
print(sub(10 , 7))  # 3
print(mul(10 , 7))  # 70
print(div(10 , 7))  # Error div function is not there in current module
a = c1()    # class c1 is not there in current module

# Find  outputs  (Home  work)
import  mod1
import  mod1    # Does nothing mod1 is already imported
import  mod1  # Same like second import it is also neglected


# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print() # nothing
importlib . reload(mod1) # Hyd <nextline> Sec <nextline> Cyb
print() # nothing
importlib . reload(mod1)    # Hyd <nextline> Sec <nextline> Cyb
importlib . reload('mod1')  # Error argument of reload function should be module not string module
reload(mod1)    # Error reload function is not there in current module
'''