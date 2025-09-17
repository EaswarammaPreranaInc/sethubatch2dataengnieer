#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') # Hello
import mod2 # How  to  import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2)
mod2 . f1() # How  to  call  function  f1()  of  mod2
print('Bye') # Bye
import  mod4 # ModuleNotFound Error 
print(x) # error as there is no x in current program
f1() # error as there is no f11 function in current program

#  Find  outputs  (Home  work)
import runpy
print('Before') # Before
rumpy.run_module('mod2') # How  to  run  mod2
print(mod2 . x) # 25
mod2 . f1() # Function
print('After') # After
run_module('mod2') # Error as member of runpy module is not imported
runpy . run_module(mod2) # error as argument should be sting


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



# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # How  to  print  variable  'y'  of  cal   module)
print(cal . x) # Error as cal module is not imported
print(add(10 , 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10 , 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) # Error as cal module is not imported
# How  to  call  m1()  method  of  class  c1  in  cal  module
a = c1()
a . m1()
b = cal . c1() # error as cal module is not imported


'''
Begin
100
200
17
3
70
1.4
m1 method
'''


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
# How  to  import  members   x , add , mul  and  class  c1  of  cal  module
feom cal import x , add , mul , c1
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # Error as y is not imported
print(cal . x) # error as cal module is not imported 
print(add(10 , 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) # Error as sub function is not imported
print(mul(10 , 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) # Error as div function is not imported
# How  to  call  m1()  method  of  class  c1  in  cal  module
a = c1()
a . m1()

'''
Begin
100
17
70
m1 method
'''



# Module  alias
print('Begin')
import cal as c # How  to  import  cal  module  with   another  name  using  import  statement
print(c . x) # How  to  print  variable  'x'  of  cal   module)
print(c . y) # How  to  print  variable  'y'  of  cal   module)
print(c . add(10 , 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c . sub(10 , 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c . mul(10 , 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c . div(10 , 7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a = c . c1() # How  to  call  m1()  method  of  c1  class  in  cal  module
a . m1()
print(cal . x) # # error as cal is not imported

'''
Begin
100
200
17
3
70
1.4
m1 method
'''



# Member  alias
# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import add as a , x as z , mul as m , c1 as c
print(z) # How  to  print  variable  'x'  of  cal   module)
print(x) # Error as x is not imported
print(a(10 , 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10 , 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
# How  to  call  m1()  method  of  class  c1  in  cal  module
a = c()
a . m1()
print(add(10 , 7)) # error as add is not imported
b = c1() # error as c1() is not imported

'''
100
17
70
m1 method
'''


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
a = c1()
a . m1()



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
a = c1()
a . m1()



# How  to  import  mod1  and  mod2
import mod1 , mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1 . x) # How  to  print  variable  'x'  of  mod1
# How  to  call  disp()  function  of  mod1
mod1 . disp()
# How  to  call  method  m1()  of  class   c1  in  mod1
a = c1()
a . m1()
print()
print(mod2 . x) # How  to  print  variable  'x'  of  mod2
# How  to  call  disp()  function  of  mod2
mod2 . disp()
# How  to  call  method  m1()  of  class   c1  in  mod2
b = c1()
b  .m1()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
# How  to  call  method  m1()  of  class   c1  in  current  module
c = c1()
c . m1()

'''
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
20
disp  function  of  mod2
m1  method  of  class  c1  in  mod2
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''



# How  to  use  members  of  all  the  three  modules  with  from  statement ?
# How  to  import  members  of  mod1
from mod1 import x as x1 , disp as disp1 , c1 as c2
# How  to  import  members  of  mod2
from mod2 import x as x2 , disp as disp2 , c1 as c3
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1) # How  to  print  variable  'x'  of  mod1)
disp1() # How  to  call  disp()  function  of  mod1
e = c2() # How  to  call  method  m1()  of  class   c1  in  mod1
e . m1()
print()
print()
print(x2) # How  to  print  variable  'x'  of  mod2)
disp2() # How  to  call  disp()  function  of  mod2
d = c2() # How  to  call  method  m1()  of  class   c1  in  mod2
d . m1()
print()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp()# How  to  call  disp()  function  of current  module
# How  to  call  method  m1()  of  class   c1  in  current  module
f = c1()
f.m1()


'''
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
20
disp  function  of  mod2
m1  method  of  class  c1  in  mod2
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''



# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__ == '__name__':
	print('Four')
	print('Five')
	print('Six')
print('Seven')
print('Eight')
print('Nine')



# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')

'''
Begining of mod 2
One
Two
Three
Seven
Eight
Nine
End of Mod2
'''


#  cal . py
_all_ =  ['add' , 'x'  , 'mul' , 'c1']
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
from  cal  import  *
print(x)
print(y) # Error as y is not imported
print(add(10 , 7))
print(sub(10 , 7))  # Error as sub() is not imported
print(mul(10 , 7))
print(div(10 , 7)) # Error as div() is not imported
a = c1()
a . m1()

'''
100
17
70
m1 method
'''


#  Find  outputs
import  cal
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.4
a = cal . c1()
a . m1() # m1 method



#  Find  outputs
from  cal  import   y , sub , mul
print(x) #  # Error as x is not imported
print(y) # 200
print(add(10 , 7)) # Error as add() is not imported
print(sub(10 , 7)) # 3
print(mul(10 , 7))  # Error as mul() is not imported
print(div(10 , 7)) # 1.4
a = c1()  # Error as c1 class is not imported


# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')


# Find  outputs  (Home  work)
import  mod1 # statement of mod1 is imported 
import  mod1 # nothing is imported
import  mod1 # nothing is imported

'''
Hyd
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
importlib . reload('mod1') # Error becoz argument is string
reload(mod1) #  Error  becoz  reload()  is  not  imported  from  importlib  module
 
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
