
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2 #How  to  import  mod2
print(mod2.x) #How  to  print   variable  'x'   of  mod2
mod2.f1() #How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()

#  Find  outputs  (Home  work)
print('Before')
runpy.run_module('mod2') #How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * #How  to  import  all  the  members  of  cal  module
print(x) #How  to  print  variable  'x'  of  cal   module)
print(y) #How  to  print  variable  'y'  of  cal   module)
print(cal . x) #Error
print(add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10,7)) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7
print(cal . add(x , y)) #error
a=c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1() #error


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #How  to  print  variable  'x'  of  cal   module
print(y)
print(cal . x) #error
print(add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) #error
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) #error
a=c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module

# Module  alias
print('Begin')
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) #How  to  print  variable  'x'  of  cal   module)
print(c.y) #How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7)) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a=c.c1()
a.m1() #How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) #error
#from  math  as   m  import  * #error

# Member  alias
from cal import x as x1,add as addition, mul as multiply,c1 as class_c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(x1) #How  to  print  variable  'x'  of  cal   module)
print(x) #Error
print(addition(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(multiply(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
a=class_1() 
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) #error
b = c1() #error

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

# Find  outputs  (Home  work)
x = 30
def   disp():
        print('disp  function  of  same  module ')
class   c1:
    def   m1(self):
        print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) #value of x in mod 2
disp() #function  of f1  in mod 2
a = c1() #class c1 in mod 2
a . m1() #method m1 in mod 2

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
    print('disp  function  of  same  module ')
class   c1:
    def   m1(self):
        print('m1  method of  class  c1  in  same  module')
print(x) #value of x in the current program
disp() #function display in the current program
a = c1() #class c1 in current program
a . m1() #method m1 in current program

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1
import mod2 #How  to  import  mod1  and  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class   c1:
    def   m1(self):
        print('m1  method of  class  c1  in  same  module')
print(mod1.x) #How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a=mod1.c1() 
a.m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) #How  to  print  variable  'x'  of  mod2
mod2.disp() #How  to  call  disp()  function  of  mod2
b=mod2.c1()
b.m1() #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c=c1()
c.m1() #How  to  call  method  m1()  of  class   c1  in  current  module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as c1_mod1 #How to import mod1
from mod2 import x as x2, disp as disp2, c1 as c1_mod2 #How to import mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
    def   m1(self):
        print('m1   method  of  class  c1  in  same  module')
print(x1) #How  to  print  variable  'x'  of  mod1)
disp1() #How  to  call  disp()  function  of  mod1
a=c1_mod1()
a.m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x2) #How  to  print  variable  'x'  of  mod2)
disp2() #How  to  call  disp()  function  of  mod2
b=c1_mod2() 
b.m1() #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x) #How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c=c1()
c.m1() #How  to  call  method  m1()  of  class   c1  in  current  module

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
What  are  the  outputs ?  --->  one Two Three Four 
                                 Five Six Seven Eight Nine
'''
# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
'''
Begining of mod2
one Two Three
Seven Eight Nine
End of mod 2'''

#  Find  outputs
from  cal  import  *
print(x) #value of x in cal module
print(y) #error
print(add(10 , 7)) #return value of add function in cal module
print(sub(10 , 7)) #error
print(mul(10 , 7))#return value of mul function in cal module
print(div(10 , 7)) #error
a = c1() # c1 class in cal module
a . m1() #m1 method in cal module

#  Find  outputs
import  cal
print(cal . x) #value of x in cal module
print(cal . y) #value of y in cal module
print(cal . add(10 , 7)) #return value of add function in cal module
print(cal . sub(10 , 7)) #return value of sub function in cal module
print(cal . mul(10 , 7)) #return value of mul function in cal module
print(cal . div(10 , 7)) #return value of div function in cal module
a = cal . c1() #class c1 in cal module
a . m1() #m1 in cal module

#  Find  outputs
from  cal  import   y , sub , mul
print(x) #error
print(y) #value of y in cal module
print(add(10 , 7)) #error
print(sub(10 , 7)) #return value of sub function in cal module
print(mul(10 , 7)) #return value of mul function in cal module
print(div(10 , 7)) #error
a = c1() #error

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
#If we write any times import statment of module it will import only once

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1) #reload mod1
print()
importlib . reload(mod1) #reloads again
importlib . reload('mod1') #error:args not be a string
reload(mod1) #error:reload function is not found in current program
