#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2    #How  to  import  mod2
print(mod2.x)   #How  to  print   variable  'x'   of  mod2)
mod2.f1()   #How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)    # error as x is not defined in current module
f1()    # error as there is no f1 in current module

#  Find  outputs  (Home  work)
import runpy
print('Before')
runpy.run_module('mod2')  #How  to  run  mod2
print(mod2 . x) # error as mod2 is not imported
mod2 . f1() # error as mod2 is not imported
print('After')  # prints after
run_module('mod2')  # module name should be there as prefix
runpy . run_module(mod2)    # arg should be string mod

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import *   #How  to  import  all  the  members  of  cal  module
print(x)    #How  to  print  variable  'x'  of  cal   module)
print(y)    #How  to  print  variable  'y'  of  cal   module)
print(cal . x)  # cal mod is not importd so error
print(add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))    #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))    #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))    #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) # x,y are not defined in current module
b=c1()
b.m1()  #How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()  # cal module is not imported so error


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1   #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)    #How  to  print  variable  'x'  of  cal   module)
print(y)    # error as y is not there in current module
print(cal . x)  # here error as cal mod is not imported
print(add(10,7))    #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))   # error as sub is not there in current module
print(mul(10,7))    #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))   # error as div is not there in current module
a=c1()
a.m1()  ##How  to  call  m1()  method  of  class  c1  in  cal  module

# Module  alias
print('Begin')
import cal as c  #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)  #How  to  print  variable  'x'  of  cal   module)
print(c.y)  #How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))  #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7))  #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7))  #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7))  #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a=c.c1()
a.m1()  ##How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)  # error as cal mod is not imported
from  math  as   m  import  *   # error in from stat we cant use module alias

# Member  alias
from cal import x as y,add as a,mul as m,c1 as c3   #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(y)    ##How  to  print  variable  'x'  of  cal   module)
print(x)    # error as x is niether imported nor defined in current prgm
print(a(10,7))  #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7))  #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
k=c3()
k.m1()  #How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) # error as add is niether imported not defined
b = c1()    # errror

# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)    # prints x of mod1
disp()  # prints disp of mod 1
a = c1()
a . m1()    # prints m1 of c1 of mod1

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)    # prints 30
disp()  # prints dip func of current prgm
a = c1()    
a . m1()    # executes m1 of c1 in current prgm

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2    #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)   #How  to  print  variable  'x'  of  mod1
mod1.disp()     #How  to  call  disp()  function  of  mod1
a=mod1.c1()
a.m1()          #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x)   #How  to  print  variable  'x'  of  mod2
mod2.disp()     #How  to  call  disp()  function  of  mod2
b=mod2.c1()
b.m1()          #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)        #How  to  print  variable  'x'  of  current  module)
disp()          #How  to  call  disp()  function  of current  module
c=c1()
c.m1()          #How  to  call  method  m1()  of  class   c1  in  current  module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as d1 #How  to  import  members  of  mod1
from mod2 import x as x2, disp as disp2, c1 as d2   #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)   #How  to  print  variable  'x'  of  mod1)
disp1()   #How  to  call  disp()  function  of  mod1   
a1=d1()
a1.m1()   ##How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x2)   ##How  to  print  variable  'x'  of  mod2)
disp2()   ##How  to  call  disp()  function  of  mod2
a2=d2()
a2.m1()   ##How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)    #How  to  print  variable  'x'  of  current  module)
disp()    #How  to  call  disp()  function  of current  module
a3=c1()
a3.m1()   ##How  to  call  method  m1()  of  class   c1  in  current  module

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
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
'''
Begining  of  mod2
One
Two
Three
Seven
Eight
Nine
End  of  mod2
'''

#  Find  outputs
from  cal  import  *
print(x)    # 100
print(y)    # error as y is not there in __all__
print(add(10 , 7))  # 17
print(sub(10 , 7))  # error as sub is not there in __all__
print(mul(10 , 7))  # 70
print(div(10 , 7))  # error as div is not there in __all__
a = c1()
a . m1()  # m1  method

#  Find  outputs
import  cal
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) # 1.42
a = cal . c1()
a . m1() # m1  method

#  Find  outputs
from  cal  import   y , sub , mul
print(x) # error as x is not there in curretn prgm
print(y) # 200
print(add(10 , 7)) # error as add is not there in current prgm
print(sub(10 , 7)) # 30
print(mul(10 , 7)) # 70
print(div(10 , 7)) # error as div is not there in current prgm
a = c1() # error as c1 is not there in current prgm


# Find  outputs  (Home  work)
import  mod1    # 1st statemnt is executed
import  mod1    # remaining are skipped
import  mod1
'''
Hyd
Sec
Cyb
'''

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1    # mod 1 is imported and statements of mod1 are executed
print()
importlib . reload(mod1) # mod 1 is loaded to memory and executed
print()
importlib . reload(mod1) # mod 1 is loaded to memory and executed
importlib . reload('mod1')  # arg should be non string so error
reload(mod1)    # relaod function is not there in current prgm so error

'''
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


