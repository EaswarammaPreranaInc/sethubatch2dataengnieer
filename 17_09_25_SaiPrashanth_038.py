#!/usr/bin/env python
# coding: utf-8
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2#How  to  import  mod2
print(mod2.x) #How  to  print   variable  'x'   of  mod2)
mod2.f1() #How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') #hello
from mod2 import * #How  to  import  mod2
print(x) #How  to  print   variable  'x'   of  mod2)
f1() #How  to  call  function  f1()  of  mod2
print('Bye') #Bye
import  mod4
print(x) #x of mod4
f1() #f1 function of mod4#  Find  outputs  (Home  work)
print('Before') #Before
import mod2 #How  to  run  mod2
print(mod2 . x) #x of mod2
mod2 . f1() #f1 function of mod2
print('After') #After
run_module('mod2')  #error
runpy . run_module(mod2) #error mod2 should be string # How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') #Begin
from cal import * #How  to  import  all  the  members  of  cal  module
print(x) #How  to  print  variable  'x'  of  cal   module)
print(y) #How  to  print  variable  'y'  of  cal   module)
print(cal . x) #error  cal is not define
print(add(10,7))#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) #error
a=c1()#How  to  call  m1()  method  of  class  c1  in  cal  module
print(a.m1())
b = cal . c1() #error cal is not define# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin') #Begin
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #How  to  print  variable  'x'  of  cal   module)
print(y)#error
print(cal . x) #error
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) #error
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) #error
a=c1()#How  to  call  m1()  method  of  class  c1  in  cal  module
print(a.m1())# Module  alias
print('Begin') #Begin
import cal as c#How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(c.y)#How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7)) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a=c.c1() #How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) #error
from  math  as   m  import  * #error# Member  alias
from cal import x as X , add as a, mul as m ,c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(X)#How  to  print  variable  'x'  of  cal   module)
print(x) #error
print(a(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
met=c() #How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) #error
b = c1() #error# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) #10
disp() #disp  function  of  mod1
a = c1()
a . m1() #m1  method  of  class  c1  in  mod1# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) #30
disp() #disp  function  of  same  module
a = c1()
a . m1() #m1  method of  class  c1  in  same  module# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2 #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) #How  to  print  variable  'x'  of  mod2
mod2.disp()How  to  call  disp()  function  of  mod2
b=mod2.c1()
b.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c=c1()
c.m1()#How  to  call  method  m1()  of  class   c1  in  current  module# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as d1, c1 as c1_mod1 #How  to  import  members  of  mod1
from mod2 import x as x2, disp as d2, c1 as c1_mod2 #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1) #How  to  print  variable  'x'  of  mod1)
d1() #How  to  call  disp()  function  of  mod1
a = c1_mod1() #How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print()
print(x2) #How  to  print  variable  'x'  of  mod2)
d2() #How  to  call  disp()  function  of  mod2
b=c1_mod2() #How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print()
print(x) #How  to  print  variable  'x'  of  current  module)
c=c1() #How  to  call  disp()  function  of current  module
c.m1() #How  to  call  method  m1()  of  class   c1  in  current  module# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__='__main__':
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
py  mod1.py
What  are  the  outputs ?  ---> 
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
'''# Find  outputs (Home  work)
print('Begining  of  mod2') #Begining  of  mod2
import   mod1
'''
outputs of mod1
One
Two
Three
Seven
Eight
Nine'''

print('End  of  mod2') #End  of  mod2#  Find  outputs
from  cal  import  *
print(x) #100
print(y) #error
print(add(10 , 7)) #70
print(sub(10 , 7)) #error
print(mul(10 , 7)) #70
print(div(10 , 7)) #error
a = c1()
a . m1() #m1  method#  Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.4
a = cal . c1()
a . m1() #m1  method#  Find  outputs
from  cal  import   y , sub , mul
print(x) #error
print(y) #200
print(add(10 , 7)) #error
print(sub(10 , 7)) #3
print(mul(10 , 7)) #70
print(div(10 , 7)) #error
a = c1() #error# Find  outputs  (Home  work)
import  mod1
Hyd
Sec
Cyb
import  mod1 #ignored
import  mod1 #ignored
# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1 
'''output
Hyd
Sec
Cyb'''
print()
importlib . reload(mod1)
'''output
Hyd
Sec
Cyb'''
print()
importlib . reload(mod1)
'''output
Hyd
Sec
Cyb'''
importlib . reload('mod1') #error
reload(mod1) #error