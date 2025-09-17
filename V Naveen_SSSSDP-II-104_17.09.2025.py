'''#1.  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2 # How  to  import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2)
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye')
#import  mod4 # Error due there is no mod4 module
#print(x) # Error due to there no object 'x' in current module
#f1() # Error due there is f1 function in current module




#2.  Find  outputs  (Home  work)
print('Before')
import runpy
runpy.run_module('mod2') # How  to  run  mod2
#print(mod2 . x) # Error due to we did not imported mod2 module
#mod2 . f1() # Error due to we did not imported mod2 module
print('After')
#run_module('mod2') # Error due to there is no run_module function in current module
#runpy . run_module(mod2) # Error due to arg should be string not just mod2




#3. How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # How  to  print  variable  'y'  of  cal   module)
#print(cal . x) # Error due module is not imported,members of the module is imported
print(add(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10, 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10, 7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
#print(cal . add(x , y)) # Error due module is not imported,members of the module is imported
a = c1 # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1(a)
#b = cal . c1() # Error due module is not imported,members of the module is imported



#4. How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x, add, mul, c1 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) # How  to  print  variable  'x'  of  cal   module)
#print(y) # Error due object y is not imported
#print(cal . x) # Error due to prefix is not neccessary
print(add(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
#print(sub(10 , 7)) # Error due to sub function is not imported
print(mul(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
#print(div(10 , 7)) # Error due to div function is not imported
a = c1() # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()




#5. Module  alias
print('Begin')
import cal as c # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) # How  to  print  variable  'x'  of  cal   module)
print(c.y) # How  to  print  variable  'y'  of  cal   module)
print(c.add(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10, 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10, 7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a = c.c1() # How  to  call  m1()  method  of  c1  class  in  cal  module
a.m1()
# print(cal . x) # Error due to cal is not imported as cal 
# from  math  as   m  import  * # here module is not permitted




#6. Member  alias
from cal import x as ex, add as a, mul as m, c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(ex) # How  to  print  variable  'x'  of  cal   module)
#print(x) # Error due to x is named as ex
print(a(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
v = c() # How  to  call  m1()  method  of  class  c1  in  cal  module
v.m1()
#print(add(10 , 7)) # Error due to add is named as a
#b = c1() # Error due to c1 is named as c





#7. Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) # 10
disp() # disp  function  of  mod1
a = c1()
a . m1() # m1  method  of  class  c1  in  mod1





#8. Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # 30
disp() # disp  function  of  same  module
a = c1()
a . m1() # m1  method of  class  c1  in  same  




#9. How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1 , mod2 # How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) # How  to  print  variable  'x'  of  mod1
mod1.disp() # How  to  call  disp()  function  of  mod1
a = mod1.c1() # How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print(mod2.x) # How  to  print  variable  'x'  of  mod2
mod2.disp() # How  to  call  disp()  function  of  mod2
b = mod2.c1() # How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
c = c1() # How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()




#10. How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import * # How  to  import  members  of  mod1
from mod2 import * # How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x) # How  to  print  variable  'x'  of  mod1)
disp() # How  to  call  disp()  function  of  mod1
a = c1() # How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print()
print(x) # How  to  print  variable  'x'  of  mod2)
disp() # How  to  call  disp()  function  of  mod2
b = c1()  # How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
c = c1() # How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()
#30
#disp  function  of  same  module
#m1   method  of  class  c1  in  same  module


#30
#disp  function  of  same  module
#m1   method  of  class  c1  in  same  module


#30
#disp  function  of  same  module
#m1   method  of  class  c1  in  same  module



#11. mod11.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod11  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__ != "__main__":
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')


#py  mod11.py
#What  are  the  outputs ?  --->#Begining  of  mod2
# One
#Two
#Three
#Seven
#Eight
#Nine
#End  of  mod2




#12. Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod11
print('End  of  mod2')
#Begining  of  mod2
#One
#Two
#Three
#Seven
#Eight
#Nine
#End  of  mod2




#13.  Find  outputs
from  call  import  *
print(x) # 100
print(y) # Error due to object 'y' is not imported
print(add(10 , 7)) # 17
print(sub(10 , 7)) # Error
print(mul(10 , 7)) # 70
print(div(10 , 7)) # Error
a = c1()
a . m1() # m1  method






#14.  Find  outputs
import  call
print(call . x) # 100 
print(call . y) # 200
print(call . add(10 , 7)) # 17
print(call . sub(10 , 7)) # 3
print(call . mul(10 , 7)) # 70
print(call . div(10 , 7)) # 1.42
a = call . c1()
a . m1() # m1 method






#15.  Find  outputs
from  call  import   y , sub , mul
#print(x) # Error due to object 'x' is not imported
print(y) # 200
#print(add(10 , 7)) # Error
print(sub(10 , 7)) # 3
print(mul(10 , 7)) # 70
#print(div(10 , 7)) # Error
#a = c1() # Error



#16. Find  outputs  (Home  work)
import  mod111
import  mod111
import  mod111
# Hyd
# Sec
# Cyb

'''

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod111
print()
importlib . reload(mod111)
print()
importlib . reload(mod111)
importlib . reload('mod111')
#reload(mod111)