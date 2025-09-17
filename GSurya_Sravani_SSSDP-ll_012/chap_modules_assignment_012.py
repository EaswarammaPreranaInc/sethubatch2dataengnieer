#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
# import mod2 How  to  import  mod2
print( mod2.x) (How  to  print   variable  'x'   of  mod2)
How  to  call  function  f1()  of  mod2# mod2.f1()
print('Bye')
import  mod4
print(x)error
f1()# error




#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
#import mod2 How  to  import  mod2
print(x.mod2)(How  to  print   variable  'x'   of  mod2)
How  to  call  function  f1()  of  mod2#mod2.f1()
print('Bye')
import  mod4
print(x)#x is checked for current module 
f1()# f1() is checked for current module 



#  Find  outputs  (Home  work)
print('Before')
run_module('mod2')How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)#error



# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
#From cal import*
How  to  import  all  the  members  of  cal  module
print(x)(How  to  print  variable  'x'  of  cal   module)
print(y)(How  to  print  variable  'y'  of  cal   module)
print(cal . x)#error
print(add(10,7)(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7)(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7)(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))# error
How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()
b.m1()



# Module  alias
print('Begin')
How  to  import  cal  module  with   another  name  using  import  statement
Import cal as c
print(c.x)(How  to  print  variable  'x'  of  cal   module)
print(c.y)(How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7)(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7)(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7)(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7)(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
How  to  call  m1()  method  of  c1  class  in  cal  module#error
print(cal . x)# error
from  math  as   m  import  *
Math module is imported as m




# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
From cal import x as x1,add as a, mul as m
print(x)(How  to  print  variable  'x'  of  cal   module)
print(x)#prints x value
print(add(10,7)(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
How  to  call  m1()  method  of  class  c1  in  cal  module
b.m1()
print(add(10 , 7))#17
b = c1()
b.m1()




# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)# m1 module x is printed
disp()# display function of mod1 is printed 
a = c1()
a . m1()
Method of m1 of class c1 of module 1 is printed 




# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)# x of module 2 is printed 
disp()# function of mod2 is printed
a = c1()
a . m1()
# m1 of mod2 is printed 




# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
from mod1 import *
from mod2 import *

How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x.mod1)How  to  print  variable  'x'  of  mod1
Mod1.disp()(How  to  call  disp()  function  of  mod1
a=c1()
a.m1()
How  to  call  method  m1()  of  class   c1  in  mod1
print(m1())
print(x.mod2)(How  to  print  variable  'x'  of  mod2
mod2.disp()
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print(c1.m1())
print(x)(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module#disp()
How  to  call  method  m1()  of  class   c1  in  current  module
a=c1()
a.m1()




# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module




# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
#begining of mod2
End of mod2



#  Find  outputs
from  cal  import  *
print(x) value of x is imported and printed from cal
print(y)value of x is imported and printed from cal
print(add(10 , 7))#17
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#1.4
a = c1()
a . m1()
m1 method 



#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))₹1.4
a = cal . c1()
a . m1()# m1 method 




#  Find  outputs
from  cal  import   y , sub , mul
print(x)#100
print(y)#200
print(add(10 , 7))#17
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#error
a = c1()

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1


# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

#hyd
Sec
Cyd
India
Usa

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
Hyd
Sec
Cyb
India 
Usa
importlib . reload(mod1)#error
importlib . reload('mod1')
#hyd
Sec
Cyd
India
Usa
reload(mod1)#error