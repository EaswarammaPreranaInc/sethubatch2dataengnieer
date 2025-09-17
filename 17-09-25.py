#1st program
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')#Hello
import mod2#How  to  import  mod2
print(mod2.x)#How  to  print   variable  'x'   of  mod2)
print(mod2.f1())#How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)#Error,x is not defined
f1()#Error, f1 is not defined in current module


#2nd program
#  Find  outputs  (Home  work)
print('Before')#Before
import runpy
runpy.run_module('mod2')#How  to  run  mod2
print(mod2 . x)#x value defined in mod2 is printed
mod2 . f1()#f1 function defined in mod2 is executed
print('After')#After
run_module('mod2')#error,there is no run_module in current module
runpy . run_module(mod2)#error,the argument should be a string module


#3rd program
# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')#Begin
from cal import * #How  to  import  all  the  members  of  cal  module
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#How  to  print  variable  'y'  of  cal   module)
print(cal . x)#error
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))#error
a=c1()
a.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()#error


#4th program
# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#y value of cal modue is printed
print(cal . x)#error
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
#How  to  call  m1()  method  of  class  c1  in  cal  module
a=c1()
a.m1()


#5th program
# Module  alias
print('Begin')
impoprt cal as c#How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(c.y)#How  to  print  variable  'y'  of  cal   module)
print(c.add())#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub())#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul())#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div())#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
#How  to  call  m1()  method  of  c1  class  in  cal  module
a=c.c1()
a.m1()
print(cal . x)#error,no module cal is found
from  math  as   m  import  * #syntax error


#6th program
# Member  alias
from cal import x as a, add as sum , mul as m ,c1 as cls#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)#How  to  print  variable  'x'  of  cal   module)
print(x)#error , x is not defined
print(sum(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
#How  to  call  m1()  method  of  class  c1  in  cal  module
c=cls()
c.m1()
print(add(10 , 7))#error ,add method not defined
b = c1()#error,c1 is not defined


#7th program
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
disp()#disp function of mod1 \n None
a = c1()#c1 class object of mod1 is crerated
a . m1()#m1 method of class c1 in mod1


#8th program
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
disp()#disp function of same module \n None
a = c1()#local class object is created
a . m1()#m1 method of class c1 in same module


#9th program
# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2#How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1
mod1.disp()#How  to  call  disp()  function  of  mod1
#How  to  call  method  m1()  of  class   c1  in  mod1
a=mod1.c1()
a.m1()
print()
print(mod2.x)#How  to  print  variable  'x'  of  mod2
mod2.disp()#How  to  call  disp()  function  of  mod2
#How  to  call  method  m1()  of  class   c1  in  mod2
b=mod2.c1()
b.m1()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
#How  to  call  method  m1()  of  class   c1  in  current  module
c=c1()
c.m1()


#10th program
# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as a, disp as fun1 ,m1 as met1,c1 as cls1 #How  to  import  members  of  mod1
from mod2 import x as b, disp as fun2 ,m1 as met2,c1 as cls2#How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(a)#How  to  print  variable  'x'  of  mod1)-->use alias to differentiate the members of each module 
fun1()#How  to  call  disp()  function  of  mod1
#How  to  call  method  m1()  of  class   c1  in  mod1
obj1=cls1()
obj1.met1()
print()
print()
print(b)#How  to  print  variable  'x'  of  mod2)
fun2()#How  to  call  disp()  function  of  mod2
#How  to  call  method  m1()  of  class   c1  in  mod2
obj2=cls2()
obj2.met2()
print()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
#How  to  call  method  m1()  of  class   c1  in  current  module
obj=c1()
obj.m1()


#11th program
# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')#One
print('Two')#Two
print('Three')#Three
print('Four')#Four
print('Five')#Five
print('Six')#Six
print('Seven')#Seven
print('Eight')#Eight
print('Nine')#Nine


#12th program
# Find  outputs (Home  work)
print('Begining  of  mod2')#Begining of mod2
import   mod1
print('End  of  mod2')#End of mod2


#13th program
#  Find  outputs
from  cal  import  * #error,z not exists
print(x)#100
print(y)#error, y is not defined in the current program
print(add(10 , 7))#17
print(sub(10 , 7))#error ,sub() is not defined
print(mul(10 , 7))#70
print(div(10 , 7))#error div() is not defined
a = c1()
a . m1()#m1 method


#14th program
#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.428
a = cal . c1()
a . m1()#m1 method


#15th program
#  Find  outputs
from  cal  import   y , sub , mul
print(x)#error x is not defined
print(y)#200
print(add(10 , 7))#error,add() not defined
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#error,add() not defined
a = c1()#error cannot call function before defination


#16th program
# Find  outputs  (Home  work)
import  mod1 #mod1 is imported
import  mod1 #discarded
import  mod1 #discarded


#17th program
# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1 # mod1 is imported for the first time
print()
importlib . reload(mod1) #mod1 is loaded into the memory for 2nd time and executed
print()
importlib . reload(mod1)#mod1 is loaded into the memory for 3rd time and executed
importlib . reload('mod1')#error, argument cannot be a string for reload function
reload(mod1)#error ,there is function reload()
