#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')                                                     Hello
How  to  import  mod2                                              import mod2
print(How  to  print   variable  'x'   of  mod2)                   print(mod2.x)
How  to  call  function  f1()  of  mod2                            mod2.f1()
print('Bye')                                                       Bye
import  mod4
print(x)                                                           Error
f1()                                                               Error

#  Find  outputs  (Home  work)
print('Before')                                                Before
How  to  run  mod2                                             run_module('mod2')
print(mod2 . x)                                                Error
mod2 . f1()                                                    Error
print('After')                                                 After
run_module('mod2')                                             mod2 will execute
runpy . run_module(mod2)                                       Error

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')                                                                                    Begin
How  to  import  all  the  members  of  cal  module                                               from cal import *
print(How  to  print  variable  'x'  of  cal   module)                                            print(x)
print(How  to  print  variable  'y'  of  cal   module)                                            print(y)
print(cal . x)                                                                                    Error
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)                   print(add(10,7))
print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)                   print(sub(10,7))
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)                   print(mul(10,7))
print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)                   print(div(10,7))
print(cal . add(x , y))                                                                           Error
How  to  call  m1()  method  of  class  c1  in  cal  module                                       b=c1()
b = cal . c1()                                                                                    b.m1()

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')                                                                                                                   Begin
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle                                                        from cal import x,add,mul,c1
print(How  to  print  variable  'x'  of  cal   module)                                                                           print(x)
print(y)                                                                                                                         Error
print(cal . x)                                                                                                                   Error
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)                                                  print(add(10,7))
print(sub(10 , 7))                                                                                                               Error
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)                                                  print(mul(10,7))
print(div(10 , 7))                                                                                                               Error
How  to  call  m1()  method  of  class  c1  in  cal  module                                                                      obj=c1()
                                                                                                                                 obj.m1()

# Module  alias 
print('Begin')                                                                                Begin
How  to  import  cal  module  with   another  name  using  import  statement                  import cal as c
print(How  to  print  variable  'x'  of  cal   module)                                        print(c.x)
print(How  to  print  variable  'y'  of  cal   module)                                        print(c.y)
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)               print(c.add(10,7))
print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)               print(c.sub(10,7))
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)               print(c.mul(10,7))
print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)               print(c.div(10,7))
How  to  call  m1()  method  of  c1  class  in  cal  module                                   obj=c.c1()
                                                                                              obj.m1()
print(cal . x)                                                                                Error
from  math  as   m  import  *

# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement            from cal import x as X,add as addition,mul as multiplication,c1 as C1
print(How  to  print  variable  'x'  of  cal   module)                                                                               print(X)
print(x)                                                                                                                             Error
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)                                                      print(addition(10,7))
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)                                                      print(multiplication(10,7))
How  to  call  m1()  method  of  class  c1  in  cal  module                                                                          b=C1()
                                                                                                                                     b.m1()
print(add(10 , 7))                                                                                                                   Error
b = c1()                                                                                                                             Error

# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)                                                                  10
disp()                                                                    disp function of mod1
a = c1()
a . m1()                                                                  m1 method of class c1 in mod1

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)                                                               20
disp()                                                                 disp function of mod2
a = c1()
a . m1()                                                               m1 method of class c1 in mod2

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
How  to  import  mod1  and  mod2                                                                                             import mod1
                                                                                                                             import mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1                                                                                 print(mod1.x)
How  to  call  disp()  function  of  mod1                                                                                     mod1.disp()
How  to  call  method  m1()  of  class   c1  in  mod1                                                                         obj1 = mod1.c1()
                                                                                                                              obj1.m1()
print()
print(How  to  print  variable  'x'  of  mod2                                                                                 print(mod2.x)
How  to  call  disp()  function  of  mod2                                                                                     mod2.disp()
How  to  call  method  m1()  of  class   c1  in  mod2                                                                         obj2=mod2.c1()
                                                                                                                              obj2.m1()
print() 
print(How  to  print  variable  'x'  of  current  module)                                                                     print(x)
How  to  call  disp()  function  of current  module                                                                           disp()
How  to  call  method  m1()  of  class   c1  in  current  module                                                              obj3=c1()
                                                                                                                              obj3.m1()
# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1                                                                   from mod1 import x as x1,disp as disp1,c1 as c1_mod1
How  to  import  members  of  mod2                                                                   from mod1 import x as x2, disp as disp2, c1 as c1_mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)                                                      print(x1)
How  to  call  disp()  function  of  mod1                                                           disp1()
How  to  call  method  m1()  of  class   c1  in  mod1                                               obj1 = c1_mod1()
                                                                                                    obj1.m1()
print()
print()
print(How  to  print  variable  'x'  of  mod2)                                                     print(x2)
How  to  call  disp()  function  of  mod2                                                          disp2()
How  to  call  method  m1()  of  class   c1  in  mod2                                              obj2=c1_mod2()
                                                                                                   obj2.m1()
print()
print()
print(How  to  print  variable  'x'  of  current  module)                                         print(x)
How  to  call  disp()  function  of current  module                                               disp()
How  to  call  method  m1()  of  class   c1  in  current  module                                  obj3=c1()
                                                                                                  obj3.m1()

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

print('One')
print('Two')
if __name__ == "__main__":
    print('Three')
    print('Four')
    print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')

# Find  outputs (Home  work)
print('Begining  of  mod2')                              Begining of mod2
import   mod1                                            One
                                                         Two
                                                         Six
                                                         Seven
                                                         Eight
                                                         Nine
print('End  of  mod2')                                   End of mod2


#  Find  outputs
from  cal  import  *
print(x)                          100
print(y)                          Error
print(add(10 , 7))                17
print(sub(10 , 7))                Error
print(mul(10 , 7))                70
print(div(10 , 7))                Error
a = c1()
a . m1()                          m1 method


#  Find  outputs
import  cal
print(cal . x)                      100
print(cal . y)                      200
print(cal . add(10 , 7))            17
print(cal . sub(10 , 7))            3
print(cal . mul(10 , 7))            70
print(cal . div(10 , 7))            1.42
a = cal . c1()
a . m1()                            m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x)                                       Error
print(y)                                       200
print(add(10 , 7))                             Error
print(sub(10 , 7))                             3
print(mul(10 , 7))                             70
print(div(10 , 7))                             Error
a = c1()

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1                                  Hyd
                                              Sec
                                              Cyb

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)                                Hyd
                                                        Sec
                                                        Cyb
print()
importlib . reload(mod1)                                Hyd
                                                        Sec
                                                        Cyb
importlib . reload('mod1')                              Error
reload(mod1)                                            Error
