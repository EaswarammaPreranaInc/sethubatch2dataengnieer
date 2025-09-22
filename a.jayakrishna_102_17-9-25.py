#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
import mod2 # How  to  import  mod2
print(mod2.x) # How  to  print   variable  'x'   of  mod2)
mod2.f1() # How  to  call  function  f1()  of  mod2
print('Bye')
#import  mod4 # Error
#print(x) # Error
#f1() # Error
'''
10
f1 function mod2 modules
Bye
'''




#  Find  outputs  (Home  work)
print('Before')
import runpy  # How  to  run  mod2
runpy.run_module('mod2')
print(mod2 . x)
mod2 . f1()
print('After')
#run_module('mod2') # Error
#runpy . run_module(mod2) # error
'''
Before
10
f1 function mod2 modules
After
'''





# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # How  to  print  variable  'y'  of  cal   module)
#print(cal . x) # Error
print(add(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
#print(cal . add(x , y)) # Error
a = c1() # How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1() 
#b = cal.c1() #Error
'''
Begin
100
200
17
3
70
1.4285714285714286
m1  method
'''






# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1 # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y)
#print(cal . x) # Error
print(add(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
a = c1()
a.m1() # How  to  call  m1()  method  of  class  c1 in cal module
'''
Begin
100
200
17
3
70
1.4285714285714286
m1  method
'''    





# Module  alias
print('Begin')
import cal as jai # How  to  import  cal  module  with   another  name  using  import  statement
print(jai.x) # How  to  print  variable  'x'  of  cal   module)
print(jai.y) # How  to  print  variable  'y'  of  cal   module)
print(jai.add(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(jai.sub(10,7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(jai.mul(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(jai.div(10,7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a = jai.c1()
a.m1() # How  to  call  m1()  method  of  c1  class  in  cal  module
#print(cal . x) # Error
#from  math  as m import * # Error
'''
Begin
100
200
17
3
70
1.4285714285714286
m1  method
'''






# Member  alias
from cal import x as jai,add as rs,mul as jk,c1 as sp # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(jai)  # How  to  print  variable  'x'  of  cal   module)
#print(x) # Error
print(rs(10,7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(jk(10,7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
a = sp()
a.m1() # How  to  call  m1()  method  of  class  c1  in  cal  module
#print(add(10 , 7)) # Error
#b = c1()# Error
'''
100
17
70
m1  method
'''





# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod122  import   *
from  mod12  import   *
print(x)
disp()
a = c1()
a . m1()
'''
10
disp  function  of  mod12
m1  method  of  class  c1  in  mod12
'''




# Find outputs  (Home  work)
from  mod12  import  *
from  mod122 import  *
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
import mod12 , mod122 # How  to  import  mod12  and  mod122
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod12.x) # How  to  print  variable  'x'  of  mod12
mod12.disp() #How  to  call  disp()  function  of  mod12
a = mod12.c1()
a.m1() # How  to  call  method  m1()  of  class   c1  in  mod12
print()
print(mod122.x) # How  to  print  variable  'x'  of  mod122
mod122.disp() # How  to  call  disp()  function  of  mod122
b = mod122.c1()
b.m1()  # How  to  call  method  m1()  of  class   c1  in  mod122
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c = c1()
c.m1() # How  to  call  method  m1()  of  class   c1  in  current  module
'''
10
disp  function  of  mod12
m1  method  of  class  c1  in  mod12

20
disp  function  of  mod122
m1  method of  class  c1  in  mod122

30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''




# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod12 import * # How  to  import  members  of  mod12
from mod122 import * # How  to  import  members  of  mod122
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x) # How  to  print  variable  'x'  of  mod12)
disp() # How  to  call  disp()  function  of  mod12
a = c1() # How  to  call  method  m1()  of  class   c1  in  mod12
a.m1()
print()
print()
print(x) # How  to  print  variable  'x'  of  mod122)
disp() # How  to  call  disp()  function  of  mod122
b = c1()
b.m1() # How  to  call  method  m1()  of  class   c1  in  mod122
print()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
c = c1() 
c.m1() #How  to  call  method  m1()  of  class   c1  in  current  module
'''
30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module


30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module


30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module
'''




# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod11
print('End of mod2')
'''
Begining  of  mod2
One
Two
Three
Seven
Eight
Nine
End of mod2
'''







#  Find  outputs
from  cal1  import  *
print(x)
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()
a . m1()
'''
100
200
17
3
70
1.4285714285714286
m1  method
'''





#  Find  outputs
import  cal1
print(cal1 . x)
print(cal1 . y)
print(cal1 . add(10 , 7))
print(cal1 . sub(10 , 7))
print(cal1 . mul(10 , 7))
print(cal1 . div(10 , 7))
a = cal1 . c1()
a . m1()
'''
100
200
17
3
70
1.4285714285714286
m1  method
'''



#  Find  outputs
from  cal1  import   y , sub , mul
#print(x) # Error
print(y)
#print(add(10 , 7)) # Error
print(sub(10 , 7))
print(mul(10 , 7))
#print(div(10 , 7)) # Error
#a = c1() # Error
'''
200
3
70
'''






# Find  outputs  (Home  work)
import  mod01
import  mod01
import  mod01
'''
Hyd
Sec
Cyb
'''




# reload()  function  demo  program   (Home  work)
import    importlib
import  mod01
print()
importlib . reload(mod01)
print()
importlib . reload(mod01)
#importlib . reload('mod01') # Error
#reload(mod01) # Error
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