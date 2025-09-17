#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') #Hello
# How  to  import  mod2
import mod2
print(mod2.x)#How  to  print   variable  'x'   of  mod2)
print(mod2.f1())#How  to  call  function  f1()  of  mod2
print('Bye')
# import  mod4
# print(x) # no 'x' in the current module
# f1() #no 'x' in the current module

#  Find  outputs  (Home  work)
from runpy import run_module
print('Before') #Before
# How  to  run  mod2
run_module('mod2')
print(mod2 . x) #20
mod2 . f1()
print('After') #After 
run_module('mod2')
import runpy
runpy . run_module(mod2)

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
# How  to  import  all  the  members  of  cal  module
from cal import *
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#How  to  print  variable  'y'  of  cal   module)
# print(cal . x) error, module is not imported
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
# print(cal . add(x , y)) error, module is not imported
# How  to  call  m1()  method  of  class  c1  in  cal  module
import cal
b = cal . c1()

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
from cal import x,add,mul,c1
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x) #error, module is not imported
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
# How  to  call  m1()  method  of  class  c1  in  cal  module
obj=c1()
obj.m1()

# Module  alias
print('Begin')
# How  to  import  cal  module  with   another  name  using  import  statement
import cal as c
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(c.y)#How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
# How  to  call  m1()  method  of  c1  class  in  cal  module
obj=c.c1()
obj.m1()
print(cal . x)
# from  math  as   m  import  *, cannot do module alias when members are imported

# Member  alias
# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import x as l, add as a, mul as m, c1 as c
print(l)#How  to  print  variable  'x'  of  cal   module)
# print(x) error, x is not imported
print(a(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
# How  to  call  m1()  method  of  class  c1  in  cal  module
obj=c()
obj.m1()
print(add(10 , 7)) #error, add is not imported
b = c1() #c1 is not imported

# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
# from  mod1  import   *
print(x) #20
disp()#disp  function  of  mod2
a = c1() 
a . m1() #m1  method of  class  c1  in  mod2

# Find outputs  (Home  work)
# from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) #30
disp()
a = c1() 
a . m1() #m1  method of  class  c1  in  same  module

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
# How  to  import  mod1  and  mod2
import mod1
import mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(30)#How  to  print  variable  'x'  of  mod1
print(mod1.disp())#How  to  call  disp()  function  of  mod1
# How  to  call  method  m1()  of  class   c1  in  mod1
obj=mod1.c1()
obj.m1()
print()
print(mod2.x)#How  to  print  variable  'x'  of  mod2
# How  to  call  disp()  function  of  mod2
print(mod2.disp())
# How  to  call  method  m1()  of  class   c1  in  mod2
obj=mod2.c1()
obj.m1()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
# How  to  call  disp()  function  of current  module
disp()
# How  to  call  method  m1()  of  class   c1  in  current  module
obj2=c1()
obj2.m1()

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
# How  to  import  members  of  mod1
from mod1 import *
# How  to  import  members  of  mod2
from mod2 import *
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1)
# How  to  call  disp()  function  of  mod1
mod1.disp()
# How  to  call  method  m1()  of  class   c1  in  mod1
obj=mod1.c1()
obj.m1()
print()
print()
print(mod2.x)#How  to  print  variable  'x'  of  mod2)
# How  to  call  disp()  function  of  mod2
mod2.disp()
# How  to  call  method  m1()  of  class   c1  in  mod2
obj2=mod2.c1()
obj2.m1()
print()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
# How  to  call  disp()  function  of current  module
disp()
# How  to  call  method  m1()  of  class   c1  in  current  module
obj3=c1()
obj3.m1()

# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__=='__main__':
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
py  mod1.py
What  are  the  outputs ?  --->
'''

# Find  outputs (Home  work)
print('Begining  of  mod2') #begining of mod2
import   mod1 #One two three seven eight nine 
print('End  of  mod2') #end of mod2


#  Find  outputs
# from  cal  import  *  error z is invalid member
print(x) # 100
print(y) #200
print(add(10 , 7)) #17
# print(sub(10 , 7))  not imported
print(mul(10 , 7)) #70
# print(div(10 , 7)) #not imported
a = c1() 
a . m1() #m1  method

#  Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.42
a = cal . c1()
a . m1() #m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x) #error not imported
print(y) #200
print(add(10 , 7)) #not imported
print(sub(10 , 7)) #3
print(mul(10 , 7)) #70
print(div(10 , 7)) #not imported
a = c1() 

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

#Hyd Sec Cyb

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1 #Hyd Sec Cyb
print() 
importlib . reload(mod1) #Hyd Sec Cyb
print()
importlib . reload(mod1) #Hyd Sec Cyb
importlib . reload('mod1') #error
reload(mod1) #error not imported
