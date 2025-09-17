#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') # print
import mod2 # How  to  import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye') # Bye
import  mod4 # importing mod4
print(x) # error
f1() # error


#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') # Hello
import mod2 # How  to  import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye') # Bye
import  mod4
print(x) # error
f1() # error


#  Find  outputs  (Home  work)
print('Before') # Before
py mod2.py # How  to  run  mod2
print(mod2 . x) # x value is printed
mod2 . f1() # f1 is called from mod2
print('After') # After
run_module('mod2') # imported and executed
runpy . run_module(mod2) # error


# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') # Begin
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # How  to  print  variable  'x'  of  cal   module
print(y) # How  to  print  variable  'y'  of  cal   module
print(cal . x) # error
print(add(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10, 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(mul(10, 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10, 7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7
print(add(x , y)) # call  add()  function  of  cal  module  by  passing  10  and  7
a = c1() # How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1() # error
a.m1() # m1() method


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')  #Begin
from cal import x , add , mul , c1 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) # How  to  print  variable  'x'  of  cal   module
print(y) # error
print(cal . x) # error
print(add(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10 , 7)) # error
print(mul(10, 7) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10 , 7)) # error
a = c1() # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()

# Module  alias
print('Begin') # Begin
impoert cal as ref # How  to  import  cal  module  with   another  name  using  import  statement
print(ref.x) # How  to  print  variable  'x'  of  cal   module
print(ref.y) # How  to  print  variable  'y'  of  cal   module
print(ref.add(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(ref.sub(10,7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(ref.mul(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(ref.div(10,7) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7
a = ref.c1()How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) # error
from  math  as   m  import  * # import  math  module  with   another  name  using  from  statemen


# Member  alias
from cal import x as x1, add as add1, mul as mul1, c1 as c11 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement

print(x1) # How  to  print  variable  'x'  of  cal   module
print(x) # error
print(add1(10, 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(mul1(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
a = c11() # How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) # error
b = c1() # error


# Find  outputs  (Home  work)
x = 30 # int obj
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) # error
disp() # disp  function  of  same  module
a = c1() # creates object of c1, unless overwritten by mod1/mod2
a . m1() # prints "m1 method..." unless c1 was overwritten


# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # prints 30
disp() # calls disp() of same module
a = c1() # creates object of class c1 defined in the same module
a . m1() # calls m1() method of class c1 → prints "m1 method of class c1 in same module"


# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1, mod2 # How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) # How  to  print  variable  'x'  of  mod1
mod1.disp() # How  to  call  disp()  function  of  mod1
a = mod1.c1()How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print() # next line
print(mod2.x) # How  to  print  variable  'x'  of  mod2
mod2.disp() # How  to  call  disp()  function  of  mod2
b = mod2.c1()How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
s = c1()How  to  call  method  m1()  of  class   c1  in  current  module
s.m1()

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as c11   # import members of mod1
from mod2 import x as x2, disp as disp2, c1 as c12   # import members of mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)         # print variable 'x' of mod1
disp1()           # call disp() function of mod1
a1 = c11()        # create object of class c1 from mod1
a1.m1()           # call m1() method of class c1 in mod1
print()
print()
print(x2)         # print variable 'x' of mod2
disp2()           # call disp() function of mod2
a2 = c12()        # create object of class c1 from mod2
a2.m1()           # call m1() method of class c1 in mod2
print()
print()
print(x)          # print variable 'x' of current module
disp()            # call disp() function of current module
a3 = c1()         # create object of class c1 from current module
a3.m1()           # call m1() method of class c1 in current module


# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
if __name__ == "__main__":     # runs only when mod1.py is executed directly
    print('Two')
    print('Three')
    print('Four')
print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
py  mod1.py
What  are  the  outputs ?  ---> One Five Six Seven Eight Nine
'''


# Find  outputs (Home  work)
print('Begining  of  mod2') # Begining  of  mod2
import   mod1
'''
Begining of mod2
One
Five
Six
Seven
Eight
Nine
End of mod2
'''
print('End  of  mod2')

#  Find  outputs
from  cal  import  * 
print(x) # prints x value
print(y) # prints y value if cal module contains
print(add(10 , 7)) # prints add(10,7)
print(sub(10 , 7)) # prints sub(10,7)
print(mul(10 , 7)) # prints mul(10,7)
print(div(10 , 7)) # prints div(10,7)
a = c1()# obj is created
a . m1() # call m1()


#  Find  outputs
import  cal
print(cal . x) # prints x value
print(cal . y) # prints y value
print(cal . add(10 , 7)) # prints add(10,7)
print(cal . sub(10 , 7)) # prints sub(10,7)
print(cal . mul(10 , 7)) # prints mul(10,7)
print(cal . div(10 , 7)) # prints div(10,7)
a = cal . c1() # creates obj
a . m1() # call m1()


#  Find  outputs
from  cal  import   y , sub , mul # 3 statements imported
print(x) # error
print(y) # prints y value
print(add(10 , 7)) # error
print(sub(10 , 7)) # prints sub(10,7)
print(mul(10 , 7)) # prints mul(10,7)
print(div(10 , 7)) # error
a = c1() # error


# Find  outputs  (Home  work)
import  mod1 
import  mod1
import  mod1 # mod1 imported only once


# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1) # executing mod1 
print()
importlib . reload(mod1) # executing mod1 again
importlib . reload('mod1') # error
reload(mod1) # error