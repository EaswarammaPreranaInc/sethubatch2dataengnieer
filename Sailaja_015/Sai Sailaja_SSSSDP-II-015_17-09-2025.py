
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') # prints Hello
import mod2 # How to import mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye') # prints Bye
import mod4 # module not found error
print(x) # Error because it searches object 'x' in current program but there is no 'x' in current program and there is no prefix
f1() # Error because it searches function 'f1' in current program but there is no f1() function in current program and there is no prefix









#  Find  outputs  (Home  work)
print('Before') # prints Before
run_module('mod2') # How  to  run  mod2
print(mod2 . x) # prints value of object 'x' from module mod2
mod2 . f1() # calls f1() function of module mod2
print('After') # prints After
run_module('mod2') # it executes module mod2
runpy . run_module(mod2) # Error because argument of run_module should be string mod2 not just mod2









# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') # prints Begin
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # +How  to  print  variable  'y'  of  cal   module)
print(cal . x) # Error because objects of module cal are imported but not module cal
print(add(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10, 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10, 7)) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) # Error because functions of module cal are imported but not module
a = c1() # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()
b = cal.c1() # Error because module cal is not imported but members of module cal imported









# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin') # prints Begin
from cal import x, add, mul, c1 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # prints value of object 'y' from module cal
print(cal . x) # Error because objects of module cal are imported but not module cal
print(add(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) # Error because we are not imporetd sub() function from cal module
print(mul(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) # Error because we are not imporetd div() function from cal module
a = c1() #How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()
	








# Module  alias
print('Begin') # prints Begin
import cal as c # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) # How  to  print  variable  'x'  of  cal   module)
print(c.y) # How  to  print  variable  'y'  of  cal   module)
print(c.add()) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub()) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul()) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div()) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a = c.c1()# How  to  call  m1()  method  of  c1  class  in  cal  module
a.m1()
print(cal . x) # Error because we are imported cal module as c but not cal
from math as m import * # Error because from statement cannot permit module alias









# Member  alias
from cal import x as x, add as a, mul as m, c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(x) # How  to  print  variable  'x'  of  cal   module)
print(x)
print(a(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
b = c() # How  to  call  m1()  method  of  class  c1  in  cal  module
b.m1()
print(add(10, 7)) # Error because we imported add function as 'a' but not add
b = c1() # Error because we imported c1 class as 'c' but not add









# Find  outputs  (Home  work)
x = 30 # Ref x points to object 30
def disp():
	print('disp  function  of  same  module ')
class c1:
	def m1(self):
	    print('m1  method of  class  c1  in  same  module')
from mod2 import  * # imports all the members of mod2 module
from mod1 import  * # imports all the members of mod2 module
print(x) # prints 20, value of 'x' of module mod2 because latest got higher priority
disp() # call disp functions of mod2 and prints disp  function  of  mod2
a = c1() # creates class object of mod2 ,ref a points to c1 class object
a . m1() # calls method of c1 class of mod2 module i.e., m1  method of  class  c1  in  mod2









# Find outputs  (Home  work)
from  mod1  import  * # imports all the members of mod1
from  mod2  import  * # imports all the members of mod2
x = 30 # Ref x points to object 30
def disp():
	print('disp  function  of  same  module ')
class c1:
	def m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # prints 30, value of 'x' from current module because it is the latest
disp() # calls disp function of current module and prints disp  function  of  same  module
a = c1() # Creates c1 class object of current module
a . m1() # calls m1 method of c1 class of mod2









# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1, mod2 #How  to  import  mod1  and  mod2
x = 30 # Ref 'x' points to object 30
def disp():
	print('disp  function  of  same  module')
class c1:
	def m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) # How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a = mod1.c1() #How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print() # prints nothing
print(mod2.x) #How  to  print  variable  'x'  of  mod2
mod2.disp() #How  to  call  disp()  function  of  mod2
a = mod2.c1() #How  to  call  method  m1()  of  class   c1  in  mod2
a.m1()
print() # prints nothing
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
a = c1() # How  to  call  method  m1()  of  class   c1  in  current  module
a.m1()









# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import * # How  to  import  members  of  mod1
from mod2 import * # How  to  import  members  of  mod2
x = 30 # Ref 'x' pointsto object 30
def disp():
    print('disp  function  of  same  module')
class c1:
	def  m1(self):
	print('m1   method  of  class  c1  in  same  module')
print(x) # How  to  print  variable  'x'  of  mod1)
disp() # How  to  call  disp()  function  of  mod1
a = c1() # How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print() # prints nothing
print() # prints nothing
print(x) # How  to  print  variable  'x'  of  mod2)
disp() # How  to  call  disp()  function  of  mod2
a = c1() #How  to  call  method  m1()  of  class   c1  in  mod2
a.m1()
print() # prints nothing
print() # prints nothing
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
a = c1() # How  to  call  method  m1()  of  class   c1  in  current  module
a.m1()









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
'''
py  mod1.py
What are the outputs?--->
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
'''









# Find  outputs (Home  work)
print('Begining  of  mod2')
import mod1
print('End of mod2')
'''
Beggining of mod2
One
Two
Three
Seven
Eight
Nine
End of mod2
'''









#  Find  outputs
from  cal  import  *
print(x) # prints value of 'x'  i.e., 100
print(y) # prints value of 'y' i.e., 200
print(add(10 , 7)) # prints 17
print(sub(10 , 7)) # prints 3
print(mul(10 , 7)) # prints 70
print(div(10 , 7)) # prints 1.42
a = c1() # creates c1 class object and assigned to reference 'a'
a . m1() # calls method m1 of class c1 and prints 'm1  method'









#  Find  outputs
import cal # imports module cal
print(cal . x) # prints value of object 'x' of module cal i.e., 100
print(cal . y) # prints value of object 'y' of module cal i.e., 200
print(cal . add(10 , 7)) # prints 17
print(cal . sub(10 , 7)) # prints 3
print(cal . mul(10 , 7)) # prints 70
print(cal . div(10 , 7)) # prints 1.42
a = cal . c1() # creates c1 class object of module cal and assigned to a
a . m1() # calls m1 method of c1 class and prints 'm1 method'









#  Find  outputs
from cal import y , sub , mul # imports memebers, y , sub, mul of module cal
print(x) # Error because x is not imported
print(y) # prints 200
print(add(10 , 7)) # Error because add() function is not imported
print(sub(10 , 7)) # prints 3
print(mul(10 , 7)) # prints 70
print(div(10, 7)) # Error because div() function is not imported
a = c1() # Error because c1 class is not imported









# Find  outputs  (Home  work)
import mod1
import mod1
import mod1
'''
Hyd
Sec
Cyb
'''






# reload()  function  demo  program   (Home  work)
import importlib # imports importlib
import mod1 # imports mod1
print() # prints nothing
importlib . reload(mod1) # prints Hyd<nextline>Sec<nextline>Cyb<nextline>
print() # prints nothing
importlib . reload(mod1) # prints Hyd<nextline>Sec<nextline>Cyb<nextline>
importlib . reload('mod1') # Error because argument of reload must be just mod1 but not string mod1
reload(mod1) # prints Hyd<nextline>Sec<nextline>Cyb<nextline>
