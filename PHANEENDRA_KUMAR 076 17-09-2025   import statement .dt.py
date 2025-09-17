 #  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
How  to  import  mod2
print(How  to  print   variable  'x'   of  mod2)
How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()
output:
Hello
import mod2
mod2.x
mod2.f1()
bye
error
error



#  Find  outputs  (Home  work)
print('Before')
How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)
 
output:
before
runpy.run_mod('mod2')
20
disp function of mod2
after
error
error




# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
from cal import*
print('Begin')---->begin
How  to  import  all  the  members  of  cal  module
from cal import*

print(How  to  print  variable  'x'  of  cal   module)->print(x)
print(How  to  print  variable  'y'  of  cal   module)-->print(y)
print(cal . x)----->error
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)--->add(10,7)
print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)--->sub(10,7)
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)---->mul(10,7)
print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)---->div(10,7)
print(cal . add(x , y))---->error

How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()---->error


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
from cal import x, add,mul,c1
print('Begin')---->begin

How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle---->from cal import x, add,mul,c1
print(How  to  print  variable  'x'  of  cal   module)---->print(x)
print(y)----->error
print(cal . x)---->error
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)---->add(10,7)
print(sub(10 , 7))---->error
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)--->mul(10,7)
print(div(10 , 7))----->error
How  to  call  m1()  method  of  class  c1  in  cal  module---->b=c1()b.m1()


 # Module  alias
print('Begin')----> begin
How  to  import  cal  module  with   another  name  using  import  statement
import cal as c
print(How  to  print  variable  'x'  of  cal   module)----->print(c.x)
print(How  to  print  variable  'y'  of  cal   module)----->print(c.y)
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)----->c.add(10,7)
print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)----->c.sub(10,7)
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)---->c.mul(10,7)
print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)----->c.div(10,7)
How  to  call  m1()  method  of  c1  class  in  cal  module--->b=c.c1()b.m1()
print(cal . x)----->error
from  math  as   m  import  *------> error



# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import x  as p,add as A, mul as M,c1 as c
print(How  to  print  variable  'x'  of  cal   module)------>print(p)
print(x)---->error
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)------>A(10,7)
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)------>M(10,7)
How  to  call  m1()  method  of  class  c1  in  cal  module----->b=c()b.m1()
print(add(10 , 7))---->error
b = c1()----->error



 # Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)---->10
disp()------>'disp  function  of  mod1'
a = c1()
a . m1()------>m1  method  of  class  c1  in  mod1



 # Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)---->30
disp()------>disp  function  of  same  module
a = c1()
a . m1()---->'m1  method of  class  c1  in  same  module


 # How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1
import mod2
How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1---------->print(mod1.x)
How  to  call  disp()  function  of  mod1------>>print(mod1.disp())
How  to  call  method  m1()  of  class   c1  in  mod1----->b=mod1.c1()
print()
print(How  to  print  variable  'x'  of  mod2----->print(mod2.x)
How  to  call  disp()  function  of  mod2---------. print(mod2.disp())
How  to  call  method  m1()  of  class   c1  in  mod2----->c.m1()
print()
print(How  to  print  variable  'x'  of  current  module)---->print(x)
How  to  call  disp()  function  of current  module----->print(disp())
How  to  call  method  m1()  of  class   c1  in  current  module--------->d=c1()
                                                                          d.m1()



# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
from mod1 import*

print(How  to  print  variable  'x'  of  mod1)--------->print(x)
How  to  call  disp()  function  of  mod1---------->disp()
How  to  call  method  m1()  of  class   c1  in  mod1
b=c1()
b.m1()
print()
print()
from mod2 import*
print(How  to  print  variable  'x'  of  mod2)---------> print(x)
How  to  call  disp()  function  of  mod2------>disp()
How  to  call  method  m1()  of  class   c1  in  mod2
c=c1()
c.m1()
print()
print()
print(How  to  print  variable  'x'  of  current  module)---------> print(x)
How  to  call  disp()  function  of current  module----->disp()
How  to  call  method  m1()  of  class   c1  in  current  module---->> z=c1()
                                                                       z.m1()




# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if_name_='_main_':
print('Four')
print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
py  mod1.py
What  are  the  outputs ?  --->
one
two
three
four
five
six
seven
eight
nine
'''




# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')


output:
begining of mod2
one
two
three
seven
eight
nine
end of mod2




 #  Find  outputs
from  cal  import  *---------> z attribute not threre in cal
print(x)---->100
print(y)--->error
print(add(10 , 7))---->17
print(sub(10 , 7))---->error
print(mul(10 , 7))----->70
print(div(10 , 7))-----> error
a = c1()
a . m1()----> m1 method



#  Find  outputs
import  cal
print(cal . x)---->100
print(cal . y)-------.>200
print(cal . add(10 , 7))----->17
print(cal . sub(10 , 7))---->3
print(cal . mul(10 , 7))---->70
print(cal . div(10 , 7))---->1.4
a = cal . c1()
a . m1()



 #  Find  outputs
from  cal  import   y , sub , mul
print(x)---->error
print(y)----->200
print(add(10 , 7))----. error
print(sub(10 , 7))----->3
print(mul(10 , 7))------->70
print(div(10 , 7))-----> error
a = c1()



 # Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
output;
hyd
sec
cyb



 # reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)


output:
hyd
sec
cyb 


hyd 
sec 
cyb

error
error
