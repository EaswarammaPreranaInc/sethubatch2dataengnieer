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


