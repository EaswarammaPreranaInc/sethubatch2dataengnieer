#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2                                 # How  to  import  mod2
print(mod2.x)                               # print(How  to  print   variable  'x'   of  mod2)
mod2.f1()                                   # How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)                                    # Error x is not in current module
f1()




#  Find  outputs  (Home  work)
print('Before')
import mod2                                 # How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')                          # error
runpy . run_module(mod2)                    # error




# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import                       # How  to  import  all  the  members  of  cal  module
print(x)                              # print(How  to  print  variable  'x'  of  cal   module)
print(y)                              # print(How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(add(10,7))                     # print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))                     # print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))                     # print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))                     # print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))
a=c1()
a.m1()                               # How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1         # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)                             # print(How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x)
print(add(10,7))                     # print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7))                     # print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
a=c1()
a.m1()                               # How  to  call  m1()  method  of  class  c1  in  cal  module




# Module  alias
print('Begin')
import cal as c                      # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)                           # print(How  to  print  variable  'x'  of  cal   module)
print(c.y)                           # print(How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))                   # print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7))                   # print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7))                   # print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7))                   # print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a=c.c1()        
a.m1()                               # How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)
from  math  as   m  import  *





# Member  alias
from cal import x as object,add as y1,mul as y2,c1 as class # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(object)                         # print(How  to  print  variable  'x'  of  cal   module)
print(x)                              # error x is modified to new name as object
print(y1)                             # print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(y2)                             # print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
a=class()
a.m1()                                # How  to  call  m1()  method  of  class  c1  in  cal  module
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
print(x)
disp()                  # disp function of mod1
a = c1()
a . m1()                # m1 method of class c1 in mod1




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
disp()                  # disp of the same module
a = c1()
a . m1()                # m1 method of class c1 in same module




# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
#How  to  import  mod1  and  mod2
import mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)               # print(How  to  print  variable  'x'  of  mod1
mod1.disp()                 # How  to  call  disp()  function  of  mod1
a=mod1.c1()
a.m1()                      # How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x)               # print(How  to  print  variable  'x'  of  mod2
mod2.disp()                 # How  to  call  disp()  function  of  mod2
b=mod2.c1()
b.m1()                      # How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)                    # print(How  to  print  variable  'x'  of  current  module)
disp()                      # How  to  call  disp()  function  of current  module
c=c1()
c.m1()                      # How  to  call  method  m1()  of  class   c1  in  current  module




# How  to  use  members  of  all  the  three  modules  with  from  statement ?
#How  to  import  members  of  mod1
#How  to  import  members  of  mod2
from mod1 import x as object1,disp as x1,c1 as class1
from mod2 import x as object2,disp as x2,c1 as class2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(object1)          # print(How  to  print  variable  'x'  of  mod1)
x1()                    # How  to  call  disp()  function  of  mod1
a=class1()              #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(obj2)             # print(How  to  print  variable  'x'  of  mod2)
x2()                    # How  to  call  disp()  function  of  mod2
b=class2()      
b.m1()                  # How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)                # print(How  to  print  variable  'x'  of  current  module)
disp()                  # How  to  call  disp()  function  of current  module
c=c1()
c.m1()                  # How  to  call  method  m1()  of  class   c1  in  current  module





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




# Find  outputs (Home  work)
print('Begining  of  mod2')     # Begining of mod2
import   mod1                   # One <next line> Two <next line> Three <next line> Seven <next line> Eight <next line> Nine 
print('End  of  mod2')          # End of mod 2





#  Find  outputs
from  cal  import  *
print(x)                        # 100
print(y)                        # 200
print(add(10 , 7))              # 17
print(sub(10 , 7))              # 3
print(mul(10 , 7))              # 70
print(div(10 , 7))              # 1.42
a = c1()
a . m1()                        # m1 method



#  Find  outputs
import  cal
print(cal . x)                      # 100
print(cal . y)                      # 200
print(cal . add(10 , 7))            # 17
print(cal . sub(10 , 7))            # 3
print(cal . mul(10 , 7))            # 70
print(cal . div(10 , 7))            # 1.42
a = cal . c1()
a . m1()                            # m1 method




#  Find  outputs
from  cal  import   y , sub , mul
print(x)                            # Error x is not defined in current mod
print(y)                            # y is executed through mod cal
print(add(10 , 7))                  # Error add function is not in current mod
print(sub(10 , 7))                  # 3
print(mul(10 , 7))                  # 70
print(div(10 , 7))                  # Error div function is not in current mod
a = c1()                            # Error class c1 i not in current mod



# Find  outputs  (Home  work)
import  mod1
import  mod1                        # Error mod1 is already imported
import  mod1                        # Error mod1 is already imported



# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()                         
importlib . reload(mod1)                        # Hyd <next line> Sec <next line> Cyb
print()
importlib . reload(mod1)                        # Hyd <next line> Sec <next line> Cyb
importlib . reload('mod1')                      # Error
reload(mod1)                                    # Error