# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)       #30
disp()         #disp  function  of  same  module 
a = c1()
a.m1()         #m1  method of  class  c1  in  same  module