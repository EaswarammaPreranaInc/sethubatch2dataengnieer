# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
#How  to  import  mod1  and  mod2
import mod1, mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)       #How  to  print  variable  'x'  of  mod1
mod1.disp()         #How  to  call  disp()  function  of  mod1
#How  to  call  method  m1()  of  class   c1  in  mod1
c = mod1.c1()
c.m1()

print()
print(mod2.x)         #How  to  print  variable  'x'  of  mod2
mod2.disp()           #How  to  call  disp()  function  of  mod2
#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)              #How  to  print  variable  'x'  of  current  module)
disp()                #How  to  call  disp()  function  of current  module
c = c1()              #How  to  call  method  m1()  of  class   c1  in current module
c.m1()