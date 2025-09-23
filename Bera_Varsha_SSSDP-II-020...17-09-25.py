#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
# How  to  import  mod2
import  mod2
print(mod2.x)# print(How  to  print   variable  'x'   of  mod2)
# How  to  call  function  f1()  of  mod2
mod2.f1()
print('Bye')
import  mod4
print(x)
f1()



#  Find  outputs  (Home  work)
import runpy
print('Before')
runpy.run_module(mod2)# How  to  run  mod2
print(mod2 . x)#error mod2 can not be used as it is not imported
mod2 . f1()##error mod2 can not be used as it is not imported
print('After')
run_module('mod2')#error no run_module() fun in curr module
runpy . run_module(mod2)#error

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * # How  to  import  all  the  members  of  cal  module
print(x)# print(How  to  print  variable  'x'  of  cal   module)
print(y)# print(How  to  print  variable  'y'  of  cal   module)
# print(cal . x)#error module cal not be used as it is not imported
print(add(10,7))# print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))# print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))# print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))# print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
# print(cal . add(x , y))#error module cal not be used as it is not imported
# How  to  call  m1()  method  of  class  c1  in  cal  module
b=c1()
b.m1()
# b = cal . c1()#error module cal not be used as it is not imported
'''
Begin
100
200
17
3
70
1.42
m1 method
'''

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)# print(How  to  print  variable  'x'  of  cal   module)
# print(y)#error no object y in current module
# print(cal . x)#error module cal not be used as it is not imported
print(add(10,7))# print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7))# print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
# How  to  call  m1()  method  of  class  c1  in  cal  module
c=c1()
c.m1()
'''
Begin
100
17
70
m1 method
'''

# Module  alias
print('Begin')
import cal as m# How  to  import  cal  module  with   another  name  using  import  statement
print(m.x)# print(How  to  print  variable  'x'  of  cal   module)
print(m.y)# print(How  to  print  variable  'y'  of  cal   module)
print(m.add(10,7))# print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m.sub(10,7))# print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(m.mul(10,7))# print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(m.div(10,7))# print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
# How  to  call  m1()  method  of  c1  class  in  cal  module
a=c.c1()
a.m1()
# print(cal . x)#error cal module can not be used as it i not imported
# from  math  as   m  import  *#error: module alias is not permitted in from statement

# Member  alias
# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import x as x1, add as add1, mul as mul1, c1 as c1alias
print(x1)#print(How  to  print  variable  'x'  of  cal   module)
#print(x)#error x does not exist
print(add1(10,7))# print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(mul1(10,7))# print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
# How  to  call  m1()  method  of  class  c1  in  cal  module
a=c2()
a.m1()
print(add(10 , 7))
# b = c1()#no call c1 in current module


# mod1.py
x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')


'''
What  are  the  members  of  mod1 ?   ---> Object  'x' , function  disp()  and  class  c1
'''
#mod2.py
x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')


'''
What  are  the  members  of  mod2 ? --->  Object  'x' ,  function  disp()  and  class  c1
'''
# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)
disp()
a = c1()
a . m1()
'''
10
'disp  function  of  mod1'
'm1  method  of  class  c1  in  mod1'
'''

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)
disp()
a = c1()
a . m1()
'''
30
'disp  function  of  same module'
'm1  method of  class  c1  in  same module'
'''

import mod1,mod2# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
# How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)# print(How  to  print  variable  'x'  of  mod1)
mod1.disp()# How  to  call  disp()  function  of  mod1
b=mod1.c1()
# How  to  call  method  m1()  of  class   c1  in  mod1
b.m1()
print()
print(mod2.x)# print(How  to  print  variable  'x'  of  mod2)
mod2.disp()# How  to  call  disp()  function  of  mod2
obj2=mod2.c1()
b.m1()# How  to  call  method  m1()  of  class   c1  in  mod2
print()
# print(How  to  print  variable  'x'  of  current  module)
print(x)
disp()
obj3=c1()
obj3.m1()
# How  to  call  disp()  function  of current  module
disp()
# How  to  call  method  m1()  of  class   c1  in  current  module
b.m1()
'''
10
disp function of mod1
m1 method of class c1 in mod1
20
disp function of mod2
m1 method of class c1 in mod2
30
disp function of same module 
m1 method of class c1 in same module
'''


# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1,disp as disp1,c1 as c11 #How  to  import  members  of  mod1
from mod1 import x as x2,disp as disp2,c1 as c12#How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)# print(How  to  print  variable  'x'  of  mod1)
disp1()# How  to  call  disp()  function  of  mod1
c=c1()
c.m1()
print()# How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x2)# print(How  to  print  variable  'x'  of  mod2)
disp2()# How  to  call  disp()  function  of  mod2
# How  to  call  method  m1()  of  class   c1  in  mod2
a=c12()
a.m1()
print()
print()
# print(How  to  print  variable  'x'  of  current  module)
print(x)
# How  to  call  disp()  function  of current  module
disp()
# How  to  call  method  m1()  of  class   c1  in  current  module
a=c1()
a.m1()

# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
if __name__ == '__main__':
	print('Three')
	print('Four')
	print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')
# output:
'''
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


'''
py  mod1.py
What  are  the  outputs ?  --->
'''
# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
'''
Begining  of  mod2
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
End  of  mod2

'''
#  Find  outputs
from  cal  import  *
print(x)#100
print(y)#namerror
print(add(10 , 7))#17
print(sub(10 , 7))#nameerror
print(mul(10 , 7))#70
print(div(10 , 7))#nameerror
a = c1()
a . m1()#m1 method

#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.4285714285714286
a = cal . c1()
a . m1()#m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x)#name error
print(y)#200
print(add(10 , 7))#name error
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#name error
a = c1()#name error

# Find  outputs  (Home  work)
import  mod1#executes
import  mod1
import  mod1

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()#blank
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)
