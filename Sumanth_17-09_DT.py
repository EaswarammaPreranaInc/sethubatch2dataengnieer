#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
Import mod2 #How  to  import  mod2
print(mod2.x)#print(How  to  print   variable  'x'   of  mod2)
mod2.f1#How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()





#  Find  outputs  (Home  work)
print('Before')
run.module('mod2')#How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)



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
print('Begin')
from cal import *#How  to  import  all  the  members  of  cal  module 
print(cal.x)#(How  to  print  variable  'x'  of  cal   module)
print(cal.y)#(How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(cal.add(10,7))#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(cal.sub(10,7))#(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(cal.mul(10,7))#(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(cal.div(10,7))#(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))
c1.m1#How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()


#Homework
print('Begin')

from cal import x, add, mul, c1 #Import only x, add, mul, and class c1

print(x) #print variable 'x' of cal module
# print(y)#Error (y not imported)
# print(cal.x)#Error (cal not imported directly)

print(add(10, 7))#call add() function of cal module
# print(sub(10, 7)) #Error (sub not imported)
print(mul(10, 7)) #call mul() function of cal module
# print(div(10, 7))#Error (div not imported)

obj = c1()#Create object of class c1
obj.m1() #Call m1() method of class c1

#Homework
print('Begin')

import cal as c #import cal module with alias 'c'

print(c.x) #print variable 'x' of cal module
print(c.y) #print variable 'y' of cal module

print(c.add(10, 7)) #call add() function
print(c.sub(10, 7)) #call sub() function
print(c.mul(10, 7)) #call mul() function
print(c.div(10, 7)) #call div() function

obj = c.c1() #create object of class c1
obj.m1()   #call m1() method of class c1

#Homework
from cal import x as x1, add as add_func, mul as multiply, c1 as MyClass
#  Imported members with alias names

print(x1)  # print variable 'x' (aliased as x1)
print(add_func(10, 7)) # call add() (aliased as add_func)
print(multiply(10, 7)) # call mul() (aliased as multiply)

obj = MyClass() # create object of class c1 (aliased as MyClass)
obj.m1()   #call m1() method

#Program to conclude as function
x = 10
def disp():
    print('disp  function  of  mod1')
class c1:
    def m1(self):
        print('m1  method  of  class  c1  in  mod1')

#programs to conclude as function
x = 20
def disp():
    print('disp  function  of  mod2')
class c1:
    def m1(self):
        print('m1  method of  class  c1  in  mod2')

x = 30
def disp():
    print('disp  function  of  same  module ')
class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')


from mod2 import *
from mod1 import *

print(x)
disp()
a = c1()
a.m1()
'''
Ouput:
30
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
'''

#Homework
from mod1 import *
from mod2 import *
x = 30
def disp():
    print('disp  function  of  same  module ')
class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')

print(x)
disp()
a = c1()
a.m1()
'''
Output:
30
disp  function  of  same  module 
m1  method of  class  c1  in  same  module
'''
#Homework Import
import mod1
import mod2

x = 30
def disp():
    print('disp  function  of  same  module')
class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')

print(mod1.x)
mod1.disp()
obj1 = mod1.c1()
obj1.m1()

print()
print(mod2.x)
mod2.disp()
obj2 = mod2.c1()
obj2.m1()

print()
print(x)
disp()
obj3 = c1()
obj3.m1()

'''
Output:
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1

20
disp  function  of  mod2
m1  method of  class  c1  in  mod2

30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''

#Homework Using From 
from mod1 import x as x1, disp as d1, c1 as c1_mod1
from mod2 import x as x2, disp as d2, c1 as c1_mod2

x = 30
def disp():
    print('disp  function  of  same  module')
class c1:
    def m1(self):
        print('m1   method  of  class  c1  in  same  module')

print(x1)
d1()
obj1 = c1_mod1()
obj1.m1()

print()
print(x2)
d2()
obj2 = c1_mod2()
obj2.m1()

print()
print(x)
disp()
obj3 = c1()
obj3.m1()

'''
Output:
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1

20
disp  function  of  mod2
m1  method of  class  c1  in  mod2

30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module
'''

#Homework to print only 1st 3 statements
# mod1.py
print('One')
print('Two')
print('Three')

if __name__ == "__main__":  
    print('Four')
    print('Five')
    print('Six')
    print('Seven')
    print('Eight')
    print('Nine')

 # Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
'''
Output:
Beginning of mod2
One 
Two
Three
End of mod2'''


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


#Find  outputs
from  cal  import  *
print(x) #100
print(y)#Error (because y not imported)
print(add(10,7))#17
print(sub(10,7))#Error (sub not imported)
print(mul(10,7))#70
print(div(10,7))#Error (div not imported)
a = c1() #creates object of class c1
a.m1()  #prints "m1 method"



#  Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.4
a = cal . c1() #creates object of class c1
a . m1() #prints 'm1 method



 #  Find  outputs
from  cal  import   y , sub , mul
print(x)#error not imported and could'nt find obj in current program
print(y) #200
print(add(10 , 7))#no add func in current and also not imported
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))##no div func in current and also not imported
a = c1() #creates a class b=object


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
#error cannot be imported multiple times



# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1) #Error: reload() argument must be a module
print()
importlib . reload(mod1)
importlib . reload('mod1') #Must not be string type error
reload(mod1) #Error: name 'reload' is not defined
