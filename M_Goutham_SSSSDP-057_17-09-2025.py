#  How  to  reuse  mod2  ?  (Home  work)
print('Hello') #Prints Hello
import mod2 #How  to  import  mod2
print(mod2.x) #(How  to  print   variable  'x'   of  mod2)
mod2.f1() #How  to  call  function  f1()  of  mod2
print('Bye') #Prints Bye
import  mod4 #Here mod4 is imported
print(x)  # Error #'x' is not defined in the current namespace (must use mod4.x if defined in mod4)
f1()  #Error: 'f1' is not defined in the current namespace (must use mod4.f1() if defined in mod4)




#  Find  outputs  (Home  work)
print('Before') #Prints Before
import runpy
runpy.run_module('mod2') #How  to  run  mod2
print(mod2 . x) #Error #We have not imported mod2
mod2 . f1() #Error #We have not imported mod2
print('After') #Prints After
run_module('mod2') #Error #we have to run the module by runpy.run_module('mod2')
runpy . run_module(mod2) #Error #mod2 must be a string 



# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import *#How  to  import  all  the  members  of  cal  module
print(x) #(How  to  print  variable  'x'  of  cal   module)
print(y) #(How  to  print  variable  'y'  of  cal   module)
print(cal . x) #Error #as we have not imported the cal module
print(add(10,7)) #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10,7)) #(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(mul(10,7)) #(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10,7))#(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y)) #Error #as we have not imported the cal module we just imported the members of cal module
a = c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1() #Error #as we have not imported the cal module we just imported to members of cal module



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin') #prints Begin
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #(How  to  print  variable  'x'  of  cal   module)
print(y) #Error #we have not imported the y from cal module 
print(cal . x) #Error #we have not imported the cal module
print(add(10,7)) #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7)) #Error #we have not imported the sub from cal module
print(mul(10,7)) #(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7)) #Error #we have not imported the div function from the cal module
a = c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module



# Module  alias
print('Begin') #Prints Begin
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) 	#(How  to  print  variable  'x'  of  cal   module)
print(c.y)	#(How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))	#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(c.sub(10,7))	#(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(c.mul(10,7))	#(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(c.div(10,7))	#(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
a = c.c1()
a.m1() #How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)#Error #we have imported the cal module using memeber alias so error
from  math  as   m  import  * #Error – invalid syntax: `as` cannot be used with `from ... import *`



# Member  alias
from cal import x as y,add as a,mul as m,c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(y)	#(How  to  print  variable  'x'  of  cal   module)
print(x)#Error #we have imported the x with another name
print(a(10,7))	#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(m(10,7))	#(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
a = c()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) #Error #we have imported the add function with another name
b = c1() #Error #we have already imported the class c1 with name c 




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


x = 30  # Here ref x points to int obj 30 (local x)
def disp():
    print('disp  function  of  same  module ')  # Local disp() defined
class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')  # Local class c1
from mod2 import *  # All members of mod2 are imported
from mod1 import *  # All members of mod1 are imported; they overwrite those from mod2 if names match
print(x)  # Prints x from mod1 if present; else mod2 if present; else prints local x (30)
disp()  # Calls disp() from mod1 if defined; else mod2; else local version
a = c1()  # Creates object of class c1 from mod1 if present; else mod2; else local version
a.m1()  # Calls method m1() of whichever c1 class is in effect



# Find outputs  (Home  work)
from  mod1  import  * #Here all the members of mod1 are imported
from mod2 import *  # All members of mod2 are imported; they overwrite those from mod1 if names match
def   disp(): #Here disp function is defined
	print('disp  function  of  same  module ')
class   c1: #Here c1 class is created
	def   m1(self): #Here m1 method is defined
		print('m1  method of  class  c1  in  same  module')
print(x) #Prints the x from local if not their then mod2 if not their then mod1 
disp() #here disp() function is called from current program
a = c1() #Here current program c1 class obj is created
a . m1() #Here current program c1 class of m1 method is executed



# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2 #How  to  import  mod1  and  mod2
x = 30 #Here current program ref x points to int obj 30
def   disp(): #Here disp() function is defined
		print('disp  function  of  same  module')
class   c1: #Here c1 class is created
	def   m1(self): #Here method m1 of c1 class is defined
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)	#(How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a = mod1.c1()
a.m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print() #Prints nothing
print(mod2.x) #(How  to  print  variable  'x'  of  mod2
mod2.disp() #How  to  call  disp()  function  of  mod2
b = mod2.c1() #How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print() #Prints nothing
print(x)	#(How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c = c1() #How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()


# How to import members of mod1
from mod1 import x as x1, disp as disp1, c1 as c1_mod1  # Import x, disp(), c1 from mod1 with aliases

# How to import members of mod2
from mod2 import x as x2, disp as disp2, c1 as c1_mod2  # Import x, disp(), c1 from mod2 with aliases

x = 30  # Variable x in current module

def disp():
    print('disp function of same module')  # Function in current module

class c1:
    def m1(self):
        print('m1 method of class c1 in same module')  # Class in current module

# ----------------------------------------------------
# print(How to print variable 'x' of mod1)
print(x1)  # Prints variable 'x' of mod1

# How to call disp() function of mod1
disp1()  # Calls disp() function from mod1

# How to call method m1() of class c1 in mod1
a = c1_mod1()
a.m1()  # Calls m1() method from class c1 in mod1

print()
print()

# print(How to print variable 'x' of mod2)
print(x2)  # Prints variable 'x' of mod2

# How to call disp() function of mod2
disp2()  # Calls disp() function from mod2

# How to call method m1() of class c1 in mod2
b = c1_mod2()
b.m1()  # Calls m1() method from class c1 in mod2

print()
print()

# print(How to print variable 'x' of current module)
print(x)  # Prints variable 'x' of current module

# How to call disp() function of current module
disp()  # Calls disp() function from current module

# How to call method m1() of class c1 in current module
c = c1()
c.m1()  # Calls m1() method from class c1 in current module





# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__ != '__main__':
	print('Four')
	print('Five')
	print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
py  mod1.py
What  are  the  outputs ?  --->
One
Two
Three
Seven
Eight
Nine
'''


print('Begining of mod2')  # Prints the Beginning of mod2
import mod1  # Executes mod1.py as it is imported
print('End of mod2')  # Prints the End of mod2




#  Find  outputs
from  cal  import  * #Here we have imported all the members of cal module
print(x) #Prints the value of x of cal module
print(y) #Prints the value of y of cal module
print(add(10 , 7)) #add function of cal module is called 
print(sub(10 , 7)) #sub function of cal module is called
print(mul(10 , 7)) #mul function of cal module is called
print(div(10 , 7)) #div function of cal module is called
a = c1() #creates an empty obj of c1 class of cal module
a . m1() #m1 method of c1 class of cal module is called




#  Find  outputs
import  cal #Here cal module is imported and executed
print(cal . x) #prints the value of x of cal module
print(cal . y) #prints the value of y of cal module
print(cal . add(10 , 7)) #add function of cal module is called and printed
print(cal . sub(10 , 7)) #sub function of cal module is called and printed
print(cal . mul(10 , 7)) #mul function of cal module is called and printed
print(cal . div(10 , 7)) #div function of cal module is called and printed
a = cal . c1() #creates an empty object for class c1 of cal module
a . m1() #here m1 method of class c1 of cal module is called 



#  Find  outputs
from  cal  import   y , sub , mul #Here we have imported the memebrs y,sub,mul of cal module
print(x) #Error #we have not imported the x from cal module
print(y) #prints the value of y of cal module
print(add(10 , 7)) #Error #we have not imported the add function of cal module
print(sub(10 , 7)) #here sub function of cal module is called and printed
print(mul(10 , 7)) #Here mul function of cal module is called and printed
print(div(10 , 7)) #Error #we have not imported the div function of cal module
a = c1() #Error #we have not imported the class c1 from cal module	



# Find  outputs  (Home  work)
import mod1
import mod1
import mod1  #mod1 is imported 3 times, but executed only once (first time)



# reload()  function  demo  program   (Home  work)
import    importlib #Here we have imported the importlib module
import  mod1 #Here we have imported the mod1 module
print() #prints nothing
importlib . reload(mod1) #Here we are running the module mod1 using reload function
print() #Prints nothing
importlib . reload(mod1) #Here we are running the module mod1 using reload function
importlib . reload('mod1') #Error #we cannot give string as argument for reload function
reload(mod1) #Error #we have to use module name as prefix inorder to use reload function