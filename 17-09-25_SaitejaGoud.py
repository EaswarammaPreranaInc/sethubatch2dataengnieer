#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') #Hello
How  to  import  mod2 #import mod2
print(How  to  print   variable  'x'   of  mod2)
How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()


#  Find  outputs  (Home  work)
print('Before')   #Before
module (mod2) #How  to  run  mod2
print(mod2 . x) #error
mod2 . f1() #error member cannot accesed directly
print('After') #after
run_module('mod2') #error
runpy . run_module(mod2) error




# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')  #Begin
from cal import * #How  to  import  all  the  members  of  cal  module
print(X) #How  to  print  variable  'x'  of  cal   module)
print(y) #(How  to  print  variable  'y'  of  cal   module)
print(cal . x) #error
print(add(10,7))#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7))#(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7)) #(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) #error
b=c1() #How  to  call  m1()  method  of  class  c1  in  cal  module
b.m1()
b = cal . c1()  # error

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin') #Begin
from cal import x,add, mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #(How  to  print  variable  'x'  of  cal   module)
print(y) #error
print(cal . x) #error
print(add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) #error
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) #error
b=c1()
b.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module



# Module  alias
print('Begin') #Begin
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) #How  to  print  variable  'x'  of  cal   module)
print(c.y) #How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
obj=c.c1() 
obj.m1() #How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) #error
from  math  as   m  import  *  #error


# Member  alias
from cal import x as a, add as sum, mul as m ,c1 as cc #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)How  to  print  variable  'x'  of  cal   module)
print(x) #error
print(sum(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
obj= cc() 
obj.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) #error
b = c1() # error


# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) #10
disp()
a = c1()
a . m1()

'''
10
disp function of mod 1
m1 method of class c1 in mod 1
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
print(x) #30
disp()  # disp function of same module
a = c1()
a . m1() #m1 method of class c1 in same module


# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1, mod2 #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
obj= mod1.c1() 
obj.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) #How  to  print  variable  'x'  of  mod2
mod2.disp() #How  to  call  disp()  function  of  mod2
obj=mod2.c1() #
obj.m1() #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x) #How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
obj=c1() 
obj.m1() #How  to  call  method  m1()  of  class   c1  in  current  module


# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as a, disp as d, c1 as c
from mod2 import x as b, disp as d1, c1 as z
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(a)How  to  print  variable  'x'  of  mod1)
d() #How  to  call  disp()  function  of  mod1
obj =c()
obj.m1()
#How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(b)How  to  print  variable  'x'  of  mod2)
d1()#How  to  call  disp()  function  of  mod2
b= z()
b.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x) #How  to  print  variable  'x'  of  current  module)
disp()How  to  call  disp()  function  of current  module
p=c1()
p.m1() #How  to  call  method  m1()  of  class   c1  in  current  module


# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if(__name__) == ('__main__'):
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
print('Begining  of  mod2') # Begining of mod2
import   mod1
print('End  of  mod2')

'''
# Begining of mod2
# one
# two
# three
# seven
# Eight
# Nine
# End of mod2
# '''


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


'''
_all_
----------
1) What  is   _all_ ?  ---> List  of  members  of  the  module  which  are  to  be  imported  when  *  is  used

2) from  cal   import   *
    Which  members  are  imported ?  ---> Those  members  which  are  in  _all_  list  of  cal  module

3) What  happens  when  _all_  list  has  an  invalid  member ?  --->  from  module  import  *  throws  ImportError

4) Where  is  _all_  list  defined  ?  ---> Inside  the  module  i.e.  Any  where  in  the  module

5) from  cal   import   *
    Which  members  are  imported  when  _all_  list  is  not  defined  in  cal  module ?  --->
										All  the  members  are  imported  becoz  default  _all_  is   every  member  of  the  module

6) from  cal   import   *
    Which  members  are  imported  when  _all_  list  is  empty  in  cal  module ?  --->  No  member  is  imported

7) from  cal  import   y , sub , mul
    Which  members  are  imported ? ---> y , sub  and  mul  but  not  members  of  _all_  list

8) _all_  list  plays  a  key  role  only  when  *  is  used  in  import  clause  of  from  statement

9) import  module
    Which  members  are  imported ?  ---> No  member  is  imported  becoz  import  statement  imports  module  but  not  members
'''

#  Find  outputs
from  cal  import  *
print(x)
print(y)
print(add(10 , 7)) #17
print(sub(10 , 7)) #error
print(mul(10 , 7)) #70
print(div(10 , 7)) #eror
a = c1()
a . m1() # m1 method

#  Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.4
a = cal . c1()
a . m1()   #m1 method



#  Find  outputs
from  cal  import   y , sub , mul
print(x) #100
print(y) #200
print(add(10 , 7)) #error
print(sub(10 , 7)) #3
print(mul(10 , 7)) #70
print(div(10 , 7)) #error
a = c1() #error



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
'''Hyb
  Sec
  Cyb
'''

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')  #error
reload(mod1) #error
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




