# How  to  use  members  of  all  the  three  modules  with  from  statement ?
#How  to  import  members  of  mod1
from mod1 import *
#How  to  import  members  of  mod2
from mod2 import *

x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
# print(How  to  print  variable  'x'  of  mod1)         #not possible becase it is imported before local
# How  to  call  disp()  function  of  mod1              #not possible becase it is imported before local
# How  to  call  method  m1()  of  class   c1  in  mod1  #not possible becase it is imported before local
# print()
# print()
# print(How  to  print  variable  'x'  of  mod2)          #not possible becase it is imported before local
# How  to  call  disp()  function  of  mod2               #not possible becase it is imported before local
# How  to  call  method  m1()  of  class   c1  in  mod2   #not possible becase it is imported before local
print()
print()
print(x)        #How  to  print  variable  'x'  of  current  module)
disp()          #How  to  call  disp()  function  of current  module
#How  to  call  method  m1()  of  class   c1  in  current  module
c = c1() 
c.m1()