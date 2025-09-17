#  How  to  reuse  mod2  ?  
print('Hello')
import mod2 # How  to  import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x) # pvm searches for object 'x' in current module
f1() # searches for function f1 in current module



#  Find  outputs 
print('Before')
import runpy
runpy.run_module('mod2') #  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
#runpy . run_module(mod2) # error: mod2 should be in quotes as it is a string not module object



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



# How  to  use  members  of  cal  module  with  from  statement ?  
print('Begin')
from cal import *  #   import  all  the  members  of  cal  module
print(x) #  print  variable  'x'  of  cal   module . No prefix is needed because of *
print(y) #   print  variable  'y'  of  cal   module
print(cal . x) 
print(add(10,7)) # call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10,7)) #   call  sub()  function  of  cal  module  by  passing  10  and  7
print(mul(10,7)) #   call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10,7)) #   call  div()  function  of  cal  module  by  passing  10  and  7
print(cal . add(x , y))
b = cal . c1() # create an object of class c1
b.m1() #   call  m1()  method  of  class  c1  in  cal  module



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1  #  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #   print  variable  'x'  of  cal   module
print(y)
#print(cal . x) # error : cal module is not imported fully
print(add(10,7)) #  call  add()  function  of  cal  module  by  passing  10  and  7
#print(sub(10 , 7)) # error : sub not imported
print(mul(10,7)) #  call  mul()  function  of  cal  module  by  passing  10  and  7
#print(div(10 , 7)) # error : div not imported
a=c1()
a.c1() #  call  m1()  method  of  class  c1  in  cal  module


# Module  alias
print('Begin')
import cal as c #   import  cal  module  with   another  name 'c'  using  import  statement
print(c.x) #   print  variable  'x'  of  cal   module
print(c.y) #   print  variable  'y'  of  cal   module
print(c.add(10,7)) #   call  add()  function  of  cal  module  by  passing  10  and  7
print(c.sub(10,7)) #   call  sub()  function  of  cal  module  by  passing  10  and  7
print(c.mul(10,7)) #   call  mul()  function  of  cal  module  by  passing  10  and  7
print(c.div(10,7)) #   call  div()  function  of  cal  module  by  passing  10  and  7
a=c.c1()
a.m1() #   call  m1()  method  of  c1  class  in  cal  module
#print(cal . x) # error : cal is not imported
from  math  as   m  import  *



# Member  alias
from cal import x as a , add as b, mul as c , c1 as d #  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)#   print  variable  'x'  of  cal   module
#print(x) # error
print(b(10,7)) #   call  add()  function  of  cal  module  by  passing  10  and  7
print(c(10,7)) #   call  mul()  function  of  cal  module  by  passing  10  and  7
obj=d() #   call  m1()  method  of  class  c1  in  cal  module
#print(add(10 , 7)) # error
#b = c1() # error : c1 is not imported



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




# Find  outputs 
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   * # import x, disp, c1 from mod2
from  mod1  import   * # import x, disp, c1 from mod1
print(x) # 10 : from mod1
disp() # disp function of mod1
a = c1() 
a . m1() # m1 method of class c1 in mod1



# Find outputs  
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # 30
disp()
a = c1() # disp function of same module
a . m1() # m1 method of class c1 in same module



# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1
import mod2 #  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) # How  to  print  variable  'x'  of  mod1
mod1.disp() #   call  disp()  function  of  mod1
a=mod1.c1() 
a.m1() #   call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) #  print  variable  'x'  of  mod2
mod2.disp() #   call  disp()  function  of  mod2
b=mod2.c1()
b.m1() #   call  method  m1()  of  class   c1  in  mod2
print()
print(x) #   print  variable  'x'  of  current  module
disp() #   call  disp()  function  of current  module
c=c1()
c.m1() # call  method  m1()  of  class   c1  in  current  module




# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x,disp,c1 #   import  members  of  mod1
from mod2 import x,disp,c1 #   import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1.x) #   print  variable  'x'  of  mod1)
mod1.disp() #   call  disp()  function  of  mod1
a=mod1.c1()
a.m1() #   call  method  m1()  of  class   c1  in  mod1
print()
print()
print(mod2.x) #   print  variable  'x'  of  mod2
mod2.disp() #   call  disp()  function  of  mod2
b=mod2.c1()
b.m1() #   call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x) #   print  variable  'x'  of  current  module
disp() #   call  disp()  function  of current  module
c=c1()
c.m1() #   call  method  m1()  of  class   c1  in  current  module



# mod1.py  
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__=="__main__":
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



# Find  outputs 
print('Begining  of  mod2')
import   mod1 # module m1 and statements of module1 are imported but not members
print('End  of  mod2')

'''
o/p:
Begining of mod2
One
Two
Three
Seven
Eight
Nine
End of mod2
'''


#  cal . py
_all_ =  ['add' , 'x'  , 'mul' , 'c1' , 'z'] # list of members of the module which are to be imported when * is used
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



#  Find  outputs
from  cal  import  * # error because of 'z' in cal.py
print(x) 
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()
a . m1()


#  Find  outputs
import  cal # import module cal and statements of module cal
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.42
a = cal . c1()
a . m1() # m1 method



#  Find  outputs
from  cal  import   y , sub , mul
print(x) # error : 'x' is not defined
print(y) # 200
print(add(10 , 7)) # error
print(sub(10 , 7)) # 3
print(mul(10 , 7)) # 70
print(div(10 , 7)) # error
a = c1() # error



# mod1.py  
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')


# Find  outputs  
import  mod1 
import  mod1
import  mod1 # only once mod1 is imported



# reload()  function  
import    importlib
import  mod1 
print()
importlib . reload(mod1) # re-executes the module
print()
importlib . reload(mod1)
#importlib . reload('mod1') # error mod1 is not string
#reload(mod1) # error

'''
o/p:
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