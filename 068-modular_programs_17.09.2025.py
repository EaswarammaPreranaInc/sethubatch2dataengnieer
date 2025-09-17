#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')  #  Hello
import mod2   #How  to  import  mod2
print(mod2.x)  #How  to  print   variable  'x'   of  mod2
mod2.f1()    #How  to  call  function  f1()  of  mod2
print('Bye')  #  Bye
import  mod4
print(x)  #  Error due to we cannot use directly x 
f1()  #  Error


#  Find  outputs  (Home  work)
print('Before')  #  before
import mod2   #How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')  #  After
run_module('mod2')  #  Error
runpy.run_module(mod2)  #  Error


# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')  #  Begin
from cal import *  #How  to  import  all  the  members  of  cal  module
print(x)   #  How  to  print  variable  'x'  of  cal   module
print(y)   #   How  to  print  variable  'y'  of  cal   module)
#print(cal . x)  #  Error due to without module name we can use with members
print(add(10,7))  #  How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10,7))   #  How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))   #  How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))   #  How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
#print(cal . add(x , y))  #  Error due to we can give variable values
c=c1()
c.m1()   # How  to  call  m1()  method  of  class  c1  in  cal  module
import cal
b = cal . c1()  



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')  #  Begin
from cal import x,add,mul,c1   #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)   #  How  to  print  variable  'x'  of  cal   module)
print(y)  #  Error due to y is not imported
print(cal . x)  #  Error due to we imported members not mudule
print(add(10,7))   #  How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))  #  Error due to sub not imported
print(mul(10,7))   #  How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))  #  Error due to div not imported
c=c1()  #How  to  call  m1()  method  of  class  c1  in  cal  module
c.m1()



# Module  alias
print('Begin')
import cal as pradeep  #  How  to  import  cal  module  with   another  name  using  import  statement
print(pradeep.x)   #  How  to  print  variable  'x'  of  cal   module
print(pradeep.y)   #  How  to  print  variable  'y'  of  cal   module)
print(pradeep.add(10,7))   #  How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(pradeep.sub(10,7))  #  How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(pradeep.mul(10,7))  #  How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(pradeep.div(10,7))  #  How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
c=pradeep.c1  #  How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)  #  Error due to we imported as pradeep
from  math  as   m  import  *  #  error due to syntax error


# Member  alias
from cal import x,add,mul,c1    #   How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(x)   #How  to  print  variable  'x'  of  cal   module)
print(x)
print(add(10,7))   #   How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))  #  How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
c1.m1()  #  How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()


# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')  
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)  #  10
disp()  #  disp()  function of mod1
a = c1()  
a . m1()  #  class c1, function m1 from mod1 



# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)  #  20
disp()  #  disp function od mod2
a = c1()
a . m1()  #  m1  method of  class  c1  in  mod2



# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2   #  How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)  #  How  to  print  variable  'x'  of  mod1
mod1.disp()  #  How  to  call  disp()  function  of  mod1
mod1.c1().m1()   #  How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x)  #  How  to  print  variable  'x'  of  mod2
mod2.disp()  #  How  to  call  disp()  function  of  mod2
mod2.c1().m1()  #  How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)  #  How  to  print  variable  'x'  of  current  module)
disp()  #  How  to  call  disp()  function  of current  module
c1().m1()  # How  to  call  method  m1()  of  class   c1  in  current  module



# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import *  #  How  to  import  members  of  mod1
from mod2 import *   #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
# we cannot print x from mod1 due to here we imported both mod1,2 x values
How  to  call  disp()  function  of  mod1
# we cannot call x from mod1 due to here we imported both mod1,2 members
How  to  call  method  m1()  of  class   c1  in  mod1
# we cannot call m1 from mod1 due to here we imported mod1,mod2 members
print()
print()
print(How  to  print  variable  'x'  of  mod2)
# we cannot print x from mod2 due to here we imported x value in both mod1,2
How  to  call  disp()  function  of  mod2
# we cannot call disp() from mod2 due to here we imported disp from mod1,2 at a time
How  to  call  method  m1()  of  class   c1  in  mod2
# we cannot call m1() from mod2 due to here we imported c1 from mod1,2 at a time
print()
print()
print(x)  #  How  to  print  variable  'x'  of  current  module)
disp()  #  How  to  call  disp()  function  of current  module
c1().m1()  #  How  to  call  method  m1()  of  class   c1  in  current  module



# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import *  #How  to  import  members  of  mod1
from mod2 import *  #  How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
#  We cannot print x due to mod1 x is negleted
How  to  call  disp()  function  of  mod1
#  We cannot print x due to mod1 disp() is negleted
How  to  call  method  m1()  of  class   c1  in  mod1
#  We cannot print x due to mod1 c1 is negleted
print()
print()
print(How  to  print  variable  'x'  of  mod2)
#  We cannot print x due to mod1 c1 is negleted
How  to  call  disp()  function  of  mod2
#  We cannot print disp due to mod1 c1 is negleted
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)  #  How  to  print  variable  'x'  of  current  module)
disp()  #  How  to  call  disp()  function  of current  module
c1().m1()  #  How  to  call  method  m1()  of  class   c1  in  current  module



# # mod1.py  (Home  work)
# #  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
# print('One')
# print('Two')
# print('Three')
# print('Four')
# print('Five')
# print('Six')
# print('Seven')
# print('Eight')
# print('Nine')


# '''
# py  mod1.py
# What  are  the  outputs ?  --->
# '''


# # Find  outputs (Home  work)
# print('Begining  of  mod2')  #  Beging of mod2
# import   mod1
# print('End  of  mod2')  #  End of mod2


# #  cal . py
# __all__ =  ['add' , 'x'  , 'mul' , 'c1' , 'z']
# x = 100
# y = 200
# def  add(a , b):
# 	return   a + b
# def	  sub(a , b):
# 	return   a - b
# def	  mul(a , b):
# 	return   a * b
# def	  div(a  ,  b):
# 	return  a / b
# class   c1:
# 	def  m1(self):
# 		print('m1  method')


'''
_all_
----------
1) What  is   _all_ ?  ---> List  of  members  of  the  module  which  are  to  be  imported  when  *  is  used

2) from  cal   import   *
    Which  members  are  imported ?  ---> Those  members  which  are  in  _all_  list  of  cal  module

3) What  happens  when  _all_  list  has  an  invalid  member ?  --->  from  module  import  *  throws  ImportError

4) Where  is  _all_  list  defined  ?  ---> Inside  the  module  i.e.  Any  where  in  the  module

5) from  cal   import   *
    Which  members  are  imported  when  _all_  list  is  not  defined  in  cal  module ?  --->
										All  the  members  are  imported  becoz  default  _all_  is   every  member  of  the  module

6) from  cal   import   *
    Which  members  are  imported  when  _all_  list  is  empty  in  cal  module ?  --->  No  member  is  imported

7) from  cal  import   y , sub , mul
    Which  members  are  imported ? ---> y , sub  and  mul  but  not  members  of  _all_  list

8) _all_  list  plays  a  key  role  only  when  *  is  used  in  import  clause  of  from  statement

9) import  module
    Which  members  are  imported ?  ---> No  member  is  imported  becoz  import  statement  imports  module  but  not  members
'''


#  Find  outputs
from  cal  import  *
print(x)  #  100
print(y)  #  200
print(add(10 , 7))  #  17
print(sub(10 , 7))  #  3
print(mul(10 , 7))  #  70
print(div(10 , 7))  #  1.42..
a = c1()
a . m1()  #  m1 method



#  Find  outputs
import  cal
print(cal . x)  #  100
print(cal . y)  #  200
print(cal . add(10 , 7))  #  17
print(cal . sub(10 , 7))  #  3
print(cal . mul(10 , 7))  #  70
print(cal . div(10 , 7))  #  1.42
a = cal . c1()
a . m1()  #  m1 method


#  Find  outputs
from  cal  import   y , sub , mul
print(x)  #  Error due to x is not defined
print(y)  #  200
print(add(10 , 7))  #  Error due to add method not defined
print(sub(10 , 7))  #  3
print(mul(10 , 7))  #  70
print(div(10 , 7))   #  Error due to div method nat defined
a = c1()  #  Error due to no class c1 in current module



# mod1.py  (Home  work)
print('Hyd')  #  Hyd
print('Sec')  #  Sec
print('Cyb')  #  Cyb
#print('India')
#print('USA')


# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)  
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)  #  Errror due to reload function is not defined
