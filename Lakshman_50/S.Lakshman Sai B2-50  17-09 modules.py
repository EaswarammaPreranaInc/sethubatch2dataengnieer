


#*********************************** #  How  to  reuse  mod2  ?  (Home  work)

print('Hello')
# How  to  import  mod2
import mod2
print(mod2.x)#(How  to  print   variable  'x'   of  mod2)
#How  to  call  function  f1()  of  mod2
mod2.f1()
print('Bye')
import  mod4   #Error becoz there is no mod4
print(x) # there is no x variable in current module
f1()   #there is f1() in current module

#*********************************** #  Find  outputs  (Home  work)
import runpy
print('Before')
#How  to  run  mod2
runpy.run_module('mod2')
print(mod2 . x) #Error becoz mod2 not imported
mod2 . f1() #Error
print('After')
run_module('mod2') #Error  becoz run_module is not imported
runpy . run_module(mod2) #Error becoz mod2 is not imported

#*********************************** #cal . py

x = 100
y = 200
def  add(a , b):
	return  a + b
def	 sub(a , b):
	return  a - b
def	 mul(a , b):
	return  a * b
def	 div(a , b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')


'''
1) What  is  the  module  name ?  ---> cal

2) What  are  the  members  of  cal  module ?  --->  Two  objects  x  and  y ,
																			      Four  functions  add() , sub() , mul()  and  div()  and
																				  class  c1

3) Is  m1()  a  member  of  cal  module ?  ---> No  becoz  it  is  a  method  of  class

4) How  many  statements  are  in  cal  module ?  --->  Two
																				     i.e.  x =  100   and  y = 200

5) py  cal . py
    What  are  the  outputs ?  ---> Nothing  becoz  there  are  no  print  statements  in  cal  module


cal.py  is  not  a  home  work
'''

#*********************************** # How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)

print('Begin')
#How  to  import  all  the  members  of  cal  module
from cal import *
print(x)#(How  to  print  variable  'x'  of  cal   module)
print(y)#How  to  print  variable  'y'  of  cal   module)
print(cal . x) #Error becoz cal module is not imported but members are imported
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))#Error becoz cal module is not imported but members are imported
#How  to  call  m1()  method  of  class  c1  in  cal  module
a=c1()
a.m1()
b = cal . c1()#Error becoz cal module is not imported but members are imported

#*********************************** # How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)

print('Begin')
# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
from cal import x,add,mul,c1
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y) #Error
print(cal . x) #Error becoz cal module is not imported but specify members are imported
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) #Error
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) #Error
#How  to  call  m1()  method  of  class  c1  in  cal  module
a=c1()
a.m1()

#*********************************** # Module  alias

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
a=c.c1()
a.m1()
print(cal . x) #Error becoz module is import as alis
from  math  as   m  import  *  #Error becoz alis is not premitted here becoz members are imported not module


#*********************************** # Member  alias

# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import x as x1, add as summ,mul as prod,c1 as c
print(x1)#How  to  print  variable  'x'  of  cal   module)
print(x)#Error becoz there is  no x in current module
print(summ(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(prod(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
# How  to  call  m1()  method  of  class  c1  in  cal  module
a=c1()
a.m1()
print(add(10 , 7))#Error becoz not defined add in current module
b = c1() #Error becoz not defined c1 in current module

#*********************************** # mod1.py

x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')


'''
What  are  the  members  of  mod1 ?   ---> Object  'x' , function  disp()  and  class  c1
'''

#*********************************** #mod2.py

x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')


'''
What  are  the  members  of  mod2 ? --->  Object  'x' ,  function  disp()  and  class  c1
'''

#*********************************** mod1  and  mod2  are  not  homeworks


#*********************************** # Find  outputs  (Home  work)

x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)
'''
'x' is 10 becoz 'x' is import from latest module
'''
disp()  #disp function of mod1
a = c1() #c1() of mod1
a . m1()#m1 from mod1

#*********************************** # Find outputs  (Home  work)

from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) #30
disp()  #current module function
a = c1() #current module of class 'c1'
a . m1() #current module method of class cl

#*********************************** # How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?

# How  to  import  mod1  and  mod2
import mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1
#How  to  call  disp()  function  of  mod1
mod1.disp()
#How  to  call  method  m1()  of  class   c1  in  mod1
a=mod1.c1()
a.m1
print()
print()#How  to  print  variable  'x'  of  mod2
#How  to  call  disp()  function  of  mod2
mod2.disp()
#How  to  call  method  m1()  of  class   c1  in  mod2
b=mod2.c1()
b.m1()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
# How  to  call  disp()  function  of current  module
disp()
# How  to  call  method  m1()  of  class   c1  in  current  module
c=c1()
c.m1()
#*********************************** # How  to  use  members  of  all  the  three  modules  with  from  statement ?

# How  to  import  members  of  mod1
from mod1 import x as x1, disp as disp1, c1 as c11# from mod1 import *
# How  to  import  members  of  mod2
from mod2 import x as x2, disp as disp2,c1 as c22# from mod2 import *
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print() #alis is must required       #How  to  print  variable  'x'  of  mod1)
# How  to  call  disp()  function  of  mod1
disp1()#alis is must required
# How  to  call  method  m1()  of  class   c1  in  mod1
a=c11() #alis is must required
a.m1()#alis is must required
print()
print()
print(x2)#How  to  print  variable  'x'  of  mod2)
# How  to  call  disp()  function  of  mod2
disp2()#alis is must required
# How  to  call  method  m1()  of  class   c1  in  mod2
b=c22()#alis is must required
b.m1()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
# How  to  call  disp()  function  of current  module
disp()
# How  to  call  method  m1()  of  class   c1  in  current  module
c=c1()
c.m1()
#*********************************** # mod1.py  (Home  work)

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

#*********************************** # Find  outputs (Home  work)

print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
'''
Begining of mod2
One
Two
Three
Seven
Eight
Nine
End of mod2
'''

#*********************************** #  cal . py

_all_ =  ['add' , 'x'  , 'mul' , 'c1' , 'z']
x = 100
y = 200
def  add(a , b):
	return   a + b
def	  sub(a , b):
	return   a - b
def	  mul(a , b):
	return   a * b
def	  div(a  ,  b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')


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
#*********************************** cal.py  is  not  a  homework
#*********************************** #  Find  outputs

# _all_ =  ['add' , 'x'  , 'mul' , 'c1' , 'z']  just to watch i written here
from  cal  import  *
print(x) #100
print(y)#Error
print(add(10 , 7))#17
print(sub(10 , 7))#Error
print(mul(10 , 7))#70
print(div(10 , 7))#Error
a = c1()
a . m1() # m1 method

#*********************************** #  Find  outputs
# _all_ =  ['add' , 'x'  , 'mul' , 'c1' , 'z']  just to watch i written here
import  cal  #
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.42
a = cal . c1()
a . m1()

#*********************************** #  Find  outputs

from  cal  import   y , sub , mul
print(x) #Error
print(y) #200
print(add(10 , 7))# Error
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#Error
a = c1()

#*********************************** # mod1.py  (Home  work)

print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

#*********************************** mod1.py is  not  a  home  work


#*********************************** # Find  outputs  (Home  work)

import  mod1
import  mod1
import  mod1
'''
Hyd
Sec
Cyd
'''
#*********************************** # reload()  function  demo  program   (Home  work)

import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)
'''
Hyd
Sec
Cyd

Hyd
Sec
Cyd

Hyd
Sec
Cyd
'''