#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2 #How  to  import  mod2
print(mod2.x)#How  to  print   variable  'x'   of  mod2)
mod2.f1()#How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()

#  Find  outputs  (Home  work)
import runpy
print('Before')
runpy.run_module('mod2')#How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)


#cal . py
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
'''

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * #How  to  import  all  the  members  of  cal  module
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))
#How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()
b.m1()

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x)#error
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
obj = c.c1#How  to  call  m1()  method  of  class  c1  in  cal  module
obj.m1()


# Module  alias
print('Begin')
import cal as c#How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(c.y)#How  to  print  variable  'y'  of  cal   module)
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
obj = c.c1#How  to  call  m1()  method  of  c1  class  in  cal  module
obj.m1()
print(cal . x)#error
from  math  as   m  import  *#error

# Member  alias
from cal import x as x1 , add as a , mul as m , c1 as c#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(x1)#How  to  print  variable  'x'  of  cal   module)
print(x)
print(a(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10 , 7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
obj = cal.c#How  to  call  m1()  method  of  class  c1  in  cal  module
obj.m1()
print(add(10 , 7))
b = c1()

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
print(x)#10
disp()#disp function of mod1
a = c1()
a . m1()#m1 method of class c1 in mod1

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)#30
disp()#disp function of same module
a = c1()
a . m1()#m1 method of class c1 in same module

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1#How  to  import  mod1  and  mod2
import mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1
mod1.disp()#How  to  call  disp()  function  of  mod1
a = mod1.c1#How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print(mod2.x)#How  to  print  variable  'x'  of  mod2
mod2.disp()#How  to  call  disp()  function  of  mod2
b =mod2.c1 #How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
c = c1#How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as c2 #How  to  import  members  of  mod1
from mod2 import x as x2, disp as disp2 , c1 as c3#How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1.x1)#How  to  print  variable  'x'  of  mod1)
mod1.disp1#How  to  call  disp()  function  of  mod1
a = mod1.c2#How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print()
print(mod2.x2)#How  to  print  variable  'x'  of  mod2)
mod2.disp2()#How  to  call  disp()  function  of  mod2
b = mod2.c3#How  to  call  method  m1()  of  class   c1  in  mod2
b.c3
print()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
c=c1#How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()


# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
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

'''

# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')

output:
Hyd
Sec 
Cyb

#  cal . py
__all__ =  ['add' , 'x'  , 'mul' , 'c1' , 'z']
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
__all__
----------
1) What  is   __all__ ?  ---> List  of  members  of  the  module  which  are  to  be  imported  when  *  is  used

2) from  cal   import   *
    Which  members  are  imported ?  ---> Those  members  which  are  in  __all__  list  of  cal  module

3) What  happens  when  __all__  list  has  an  invalid  member ?  --->  from  module  import  *  throws  ImportError

4) Where  is  __all__  list  defined  ?  ---> Inside  the  module  i.e.  Any  where  in  the  module

5) from  cal   import   *
    Which  members  are  imported  when  __all__  list  is  not  defined  in  cal  module ?  --->
										All  the  members  are  imported  becoz  default  __all__  is   every  member  of  the  module

6) from  cal   import   *
    Which  members  are  imported  when  __all__  list  is  empty  in  cal  module ?  --->  No  member  is  imported

7) from  cal  import   y , sub , mul
    Which  members  are  imported ? ---> y , sub  and  mul  but  not  members  of  __all__  list

8) __all__  list  plays  a  key  role  only  when  *  is  used  in  import  clause  of  from  statement

9) import  module
    Which  members  are  imported ?  ---> No  member  is  imported  becoz  import  statement  imports  module  but  not  members
'''
cal.py  is  not  a  homework

#  Find  outputs
from  cal  import  *
print(x)
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()
a . m1()#m1 method

#  Find  outputs
import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.4
a = cal . c1()
a . m1()#m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x)
print(y)
print(add(10 , 7))#error
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#error
a = c1()#error

# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')
mod1.py is  not  a  home  work

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

output:
Hyd
Sec 
Cyb 

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
Hyd
Sec 
Cyb

Hyd
Sec 
Cyb 

Hyd
Sec 
Cyb

