
# mod2.py

x = 20
def f1():
    print("f1() function of mod2")
    


# 1) How  to  reuse  mod2  ?  (Home  work)

print('Hello')
import mod2     # How  to  import  mod2
print(mod2.x)   # How  to  print   variable  'x'   of  mod2
mod2.f1()       # How  to  call  function  f1()  of  mod2
print('Bye')    # bye
import  mod4    # Error as mod4 is not defined
print(x)        # Error as there is no 'x' in the current program
f1()            # Error as there is no 'f1()' in the current program

'''
output:
Hello
20
f1() function of mod2
Bye
'''




# 2) Find  outputs  (Home  work)

import runpy
import mod2
print('Before')         # Before
runpy . run_module('mod2')      # How  to  run  mod2
print(mod2 . x)         # print obeject x of mod2
mod2 . f1()             # executes the f1() of mod2
print('After')          # After
run_module('mod2')      # Erron as run_module() is not defined in the current program
runpy . run_module(mod2)# Error as 'mod2' argument must be a str, not module

'''
output:
Before
20
f1() function of mod2
After
'''




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




# 3) How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)

print('Begin')
from cal import *       # How  to  import  all  the  members  of  cal  module
print(x)                # How  to  print  variable  'x'  of  cal   module
print(y)                # How  to  print  variable  'y'  of  cal   module
print(cal . x)          # Error as cal module is not imported
print(add(10,7))        # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10,7))        # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(mul(10,7))        # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10,7))        # How  to  call  div()  function  of  cal  module  by  passing  10  and  7
print(cal . add(x , y)) # Error as cal module is not imported
a=c1()                  # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()
b = cal . c1()          # Error as cal module is not imported

'''
output:
Begin
100
200
17
3
70
1.4285714285714286
m1  method
'''



# 4) How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)

print('Begin')
from cal import x,add,mul,c1    # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)                        # How  to  print  variable  'x'  of  cal   module
print(y)                        # Error as 'y' is not defined in current program
print(cal . x)                  # Error as cal module is not imported
print(add(10,7))                # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10 , 7))              # Error as 'sub' is not defined in current program
print(mul(10,7))                # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10 , 7))              # Error as 'div' is not defined in current program
a=c1()                          # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()

'''
output:
Begin
100
17
70
m1  method
'''




# 5) Module  alias

print('Begin')
import cal as c     # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)          # How  to  print  variable  'x'  of  cal   module)
print(c.y)          # How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))  # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7))  # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7))  # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7))  # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a=c.c1()            # How  to  call  m1()  method  of  c1  class  in  cal  module
a.m1()
print(cal . x)      # Error as cal module is not imported
from  math  as   m  import  * # Error as math module is not imported we cannot alias the math as m
'''
output:
Begin
100
200
17
3
70
1.4285714285714286
m1  method
'''



# 6) Member  alias

from cal import x as obj1,add as a, sub as s, mul as m, c1 as cls # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(obj1)     # How  to  print  variable  'x'  of  cal   module)
print(x)        # Error as x is not defined in current program
print(a(10,7))  # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7))  # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
a=cls()         # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()
print(add(10 , 7))  # Error as add is not defined in current program
b = c1()            # Error as c1() is not defined in current program
'''
output:
100
17
70
m1  method
'''



# mod1.py

x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')


#mod2.py

x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')





# 7) Find  outputs  (Home  work)

x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)    # x from mod2 will be printed as it is lastest
disp()      # disp() from mod2 will be executed as it is lastest
a = c1()    # object a is created for c1() from mod2 as it is lastest
a . m1()    # m1() of c1() from mod2 will be executed as it is lastest

'''
output:
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
'''




# 8) Find outputs  (Home  work)

from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)    # object x in the current program will be printed as it is lastest
disp()      # disp() in the current program will be executed as it is lastest
a = c1()    # object a is created for c1() in the current program as it is lastest
a . m1()    # m1() in the current program will be executed as it is lastest

'''
output:
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''



# 9) How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?

import mod1,mod2    # How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)       # How  to  print  variable  'x'  of  mod1
mod1.disp()         # How  to  call  disp()  function  of  mod1
a=mod1.c1()         # How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print(mod2.x)       # How  to  print  variable  'x'  of  mod2
mod2.disp()         # How  to  call  disp()  function  of  mod2
b=mod2.c1()         # How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print(x)            # How  to  print  variable  'x'  of  current  module)
disp()              # How  to  call  disp()  function  of current  module
c=c1()              # How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()

'''
output:
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1

20
disp  function  of  mod2
m1  method of  class  c1  in  mod2

30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''




# 10) How  to  use  members  of  all  the  three  modules  with  from  statement ?

from mod1 import x as x1, disp as disp1, c1 as cls1  # How  to  import  members  of  mod1
from mod2 import x as x2, disp as disp2, c1 as cls2  # How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)   # How  to  print  variable  'x'  of  mod1)
disp1()     # How  to  call  disp()  function  of  mod1
a=cls1()    # How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print()
print(x2)   # How  to  print  variable  'x'  of  mod2)
disp1()     # How  to  call  disp()  function  of  mod2
b=cls2()    # How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print()
print(x)    #How  to  print  variable  'x'  of  current  module)
disp()      # How  to  call  disp()  function  of current  module
c=c1()      # How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()

'''
output:
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1


20
disp  function  of  mod1
m1  method of  class  c1  in  mod2


30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module
'''




# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere

print('One')
print('Two')
print('Three')
if __name__=='__main__':  # if only we run this directly these statements will be executed otherwise not
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')




# 11) Find  outputs (Home  work)

print('Begining  of  mod2')
import   mod1
print('End  of  mod2')

'''
output:
Begining  of  mod2
One
Two
Three
Seven
Eight
Nine
End  of  mod2
'''




#  cal . py
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




# 12) Find  outputs

from  cal  import  *
print(x)
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()
a . m1()

'''
output:
100
200
17
3
70
1.4285714285714286
m1  method
'''




# 13) Find  outputs

import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))
print(cal . sub(10 , 7))
print(cal . mul(10 , 7))
print(cal . div(10 , 7))
a = cal . c1()
a . m1()

'''
output:
100
200
17
3
70
1.4285714285714286
m1  method    
'''    




# 14) Find  outputs

from  cal  import   y , sub , mul
print(x)            # Error as 'x' is not defined in current program
print(y)
print(add(10 , 7))  # Error as add is not defined in current program
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))  # Error as div is not defined in current program
a = c1()            # Error as c1 is not defined in current program

'''
output:
200
3
70    
'''    





# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')




# 15) Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

'''
output:
Hyd
Sec
Cyb
'''



# 16) reload()  function  demo  program   (Home  work)

import  importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')  # Error as reload argument should be only module 
reload(mod1)                # Error as reload() function is not defined in the current program

'''
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
'''