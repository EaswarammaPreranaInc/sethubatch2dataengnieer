'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)                           #20
f1()                               #p1  ---> mod2  ---> f1
a = c1()
a.m1()                             #p1  ---> mod2 ---> c1 ---> m1