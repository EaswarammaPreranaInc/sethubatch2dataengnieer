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
		pass
#End  of  the  class
x = 100
y = 200
if  __name__ ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')



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
print('Begin')#Begin
import cal#How  to  import  all  the  members  of  cal  module
print(cal.x)#100
print(cal.y)#200
#print(x)#Error
print(cal.add(10,7))#17
print(cal.sub(10,7))#3
print(cal.mul(10,7))#70
print(cal.div(10,7))#1.4285714285714286
#print(add(x , y))#Error
#How  to  call  m1()  method  of  class  c1  in  cal  module
b =cal.c1()#m1  method
b.m1()
# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)#100
print(y)#Error
print(cal . x)#NameError: name 'cal' is not defined
print(add(10,7))#17
print(sub(10 , 7))#sub is not defined
print(mul(10,7))#70
print(div(10 , 7))#div is not defined
#How  to  call  m1()  method  of  class  c1  in  cal  module
b=c1()
b.m1()#m1 method


# Module  alias
How  to  import  cal  module  with   another  name  using  import  statement
print('Begin')
import cal as c#How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)#100
print(c.y)#200
print(c.add(10,7))#17
print(c.sub(10,7))#3
print(c.mul(10,7))#70
print(c.div(10,7))#1.42
#How  to  call  m1()  method  of  c1  class  in  cal  module
b=c.c1()
b.m1#m1 method
print(cal . x)#Error
#from  math  as   m  import  *#Error

# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import x as x1 , add as add1,mul as mul1,c1 as c11
print(x1)#100
print(x)#Error
print(add1(10,7))#17
print(mul1(10,7))#70
a=c11()
a.m1()#m1 method
print(add(10,7))#No add() function
b=c1()#no class c1 in current module

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
disp()#disp  function  of  mod1
a = c1()
a . m1()#m1  method  of  class  c1  in  mod1

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
a . m1()#m1  method of  class  c1  in  same  module

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2#How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#10
mod1.disp()#disp function of mod1 #How  to  call  disp()  function  of  mod1
b=mod1.c1()#How  to  call  method  m1()  of  class   c1  in  mod1
b.m1()#m1 method of calss c1 in mod1
print()
print(mod2.x)#20 (How  to  print  variable  'x'  of  mod2
mod2.disp()#disp function of mod2  How  to  call  disp()  function  of  mod2
b1=mod2.c1()#How  to  call  method  m1()  of  class   c1  in  mod2
b1.m1()#m1 method of calss c1 in mod1
print()
print(x)#30
disp()#disp  function  of  same  module How  to  call  disp()  function  of current  module
b2=c1()#How  to  call  method  m1()  of  class   c1  in  current  module
b2.m1()#'m1  method of  class  c1  in  same  module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as c1_mod1
from mod2 import x as x2, disp as disp2, c1 as c1_mod2
# ---- mod1 ----
print("x of mod1 =", x1)#10
disp1()#disp function of mod1
obj1 = c1_mod1()
obj1.m1()#m1  method of  class  c1  in  mod1

print()
print()

# ---- mod2 ----
print("x of mod2 =", x2)#20
disp2()#disp function of mod2
obj2 = c1_mod2()
obj2.m1()#m1  method of  class  c1  in  mod2

print()
print()

# ---- current module ----
print("x of current module =", x)
disp()#disp function of current module
obj3 = c1()
obj3.m1()#m1  method of  class  c1  in  current module

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
'''#output:
30
One
Two
Three
Four
Five
Six
Seven
Eight
Nine'''

# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
#output:
#Begining  of  mod2
#End  of  mod2



#  Find  outputs
from  cal  import  *
print(x)#100
print(y)#200
print(add(10 , 7))#17
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#1.42
a = c1()
a . m1()#m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x)#Error
print(y)#200
print(add(10 , 7))#Error
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#Error
a = c1()

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
#empty'''

#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.42
a = cal . c1()
a . m1()#m1 method of cal

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)















