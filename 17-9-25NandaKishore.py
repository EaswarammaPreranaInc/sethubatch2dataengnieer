#Nanda Kishore Vemula
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') #Hello
import mod2 #How  to  import  mod2
print(mod2.x)#How  to  print   variable  'x'   of  mod2)
mod2.f1()#How  to  call  function  f1()  of  mod2
print('Bye') #Bye
import  mod4
print(x) #Error
f1() #Error

#  Find  outputs  (Home  work)
import runpy #To run mod2
print('Before') #Before
runpy.run_module('mod2')#How  to  run  mod2
print(mod2 . x) #Error
mod2 . f1()#Error
print('After') #After
run_module('mod2')#Error
runpy . run_module(mod2)#Error


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
print('Begin') #Begin
from cal import* #How  to  import  all  the  members  of  cal  module
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#How  to  print  variable  'y'  of  cal   module)
print(cal . x) #Error
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7)#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) #Error
b=c1()#create object
b.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1() #Error


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#Error
print(cal . x)#Error
print(add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))#Error
print(mul())#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))#Error
b=c1()#create object
b.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module

# Module  alias
print('Begin')
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(c.y)#How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7))#How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
b=c.c1()#create object
b.m1()#How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) #Error
from  math  as   m  import  * #Error


# Member  alias
from cal import x as num,add as a,mul as m,c1 as cls #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(num)#How  to  print  variable  'x'  of  cal   module)
print(x) #Error
print(a(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
b=cls()#create object
b.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) #Error
b = c1() #Error


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
print(x)
disp()
a = c1()
a . m1()
'''
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
'''

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
disp()
a = c1()
a . m1()
'''
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1
import mod2
How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1
mod1.disp()#How  to  call  disp()  function  of  mod1
b=mod1.c1()#Create object
b.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x)#How  to  print  variable  'x'  of  mod2
mod2.disp()#How  to  call  disp()  function  of  mod2
obj=mod2.c1()
obj.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
b1=c1()
b1.m1()#How  to  call  method  m1()  of  class   c1  in  current  module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as num1, disp as disp1, c1 as c1s1
from mod2 import x as num2, disp as disp2, c1 as c1s2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
from mod1 import * #How  to  import  members  of  mod1
print(num1)#How  to  print  variable  'x'  of  mod1)
disp1()#How  to  call  disp()  function  of  mod1
b=cls1()
b.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(num2)#How  to  print  variable  'x'  of  mod2)
disp2()#How  to  call  disp()  function  of  mod2
obj=cls2()
obj.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
b1=c1()
b1.m1()#How  to  call  method  m1()  of  class   c1  in  current  module

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
What  are  the  outputs ?  --->One Two Three Four Five Six Seven Eight Nine
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


#  Find  outputs
from  cal  import  * #Error: as 'Z' as not present in cal but listed in __all__
print(x) #100
print(y) #Error
print(add(10 , 7)) #17
print(sub(10 , 7)) #Error
print(mul(10 , 7)) #70
print(div(10 , 7)) #Error
a = c1()
a . m1()# m1 method

#  Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.4
a = cal . c1()
a . m1() #m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x) #Error
print(y) #200
print(add(10 , 7)) #Error
print(sub(10 , 7)) #3
print(mul(10 , 7)) #70
print(div(10 , 7)) #Error
a = c1() #Error

# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
'''
Hyd
Sec
Cyb
'''

# reload()  function  demo  program   (Home  work)
import  importlib
import  mod1
print()
importlib . reload(mod1) #Reloads the mod1 and executes it
print()
importlib . reload(mod1) #Reloads the mod1 and executes it
importlib . reload('mod1') #Error
reload(mod1) #Error
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