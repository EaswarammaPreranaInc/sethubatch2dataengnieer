# home work on 17/09/2025 questions 

-------------------------------------------------------------------------------------------------------

#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
How  to  import  mod2
print(How  to  print   variable  'x'   of  mod2)
How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()

#outputs 
Hello
100
I am f1() of mod2
Bye
200
I am f1() of mod4
----------------------------------------------------------------------
#  How  to  reuse  mod2  ?  (Home  work)
print('Hello')
How  to  import  mod2
print(How  to  print   variable  'x'   of  mod2)
How  to  call  function  f1()  of  mod2
print('Bye')
import  mod4
print(x)
f1()

#output

Hello
10
This is f1() from mod2
Bye
20
This is f1() from mod4

----------------------------------------------------------------------------
#  Find  outputs  (Home  work)
print('Before')
How  to  run  mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)


#outputs

Before
mod2 executing...
50
This is f1() of mod2
After
mod2 executing...

-------------------------------------------------------------------------------------------

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
How  to  import  all  the  members  of  cal  module
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7)
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7)
print(cal . add(x , y))
How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()


#outputs

Begin
5
3
17
3
70
1.4285714285714286
8
m1() method of class c1 in cal module


-------------------------------------------------------------------------------------------------------------
# Module alias 
print('Begin')

import cal as c    # How to import cal module with another name using import statement

print(c.x)         # How to print variable 'x' of cal module
print(c.y)         # How to print variable 'y' of cal module
print(c.add(10, 7)) # How to call add() function of cal module by passing 10 and 7
print(c.sub(10, 7)) # How to call sub() function of cal module by passing 10 and 7
print(c.mul(10, 7)) # How to call mul() function of cal module by passing 10 and 7
print(c.div(10, 7)) # How to call div() function of cal module by passing 10 and 7

b = c.c1()         # How to call m1() method of c1 class in cal module
b.m1()

print(c.x)

--------------------------------------------------------------------------------------------------------------------
# Module alias 
print('Begin')

import cal as c    # importing cal module with another name

print(c.x)         # print variable 'x' of cal module
print(c.y)         # print variable 'y' of cal module
print(c.add(10, 7)) # call add() function of cal module
print(c.sub(10, 7)) # call sub() function of cal module
print(c.mul(10, 7)) # call mul() function of cal module
print(c.div(10, 7)) # call div() function of cal module

b = c.c1()         # create object of c1 class in cal module
b.m1()             # call m1() method of c1 class

print(c.x)
-------------------------------------------------------------------------------------------------------

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
a = c1()
a . m1()

#outputs

10
disp function of mod1
m1 method of class c1 in mod1


-------------------------------------------------------------------------------------------------------------
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
a = c1()
a . m1()
#outputs

30
disp function of same module
m1 method of class c1 in same module


---------------------------------------------------------------------------------------------------------------------

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(How  to  print  variable  'x'  of  mod2
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module

#outputs

import mod1
import mod2

x = 30
def disp():
    print("disp function of current module")
class c1:
    def m1(self):
        print("m1 method of class c1 in current module")


# --- Members of mod1 ---
print(mod1.x)       # variable x from mod1
mod1.disp()         # function disp() from mod1
obj1 = mod1.c1()    # object of class c1 in mod1
obj1.m1()

print()

# --- Members of mod2 ---
print(mod2.x)       # variable x from mod2
mod2.disp()         # function disp() from mod2
obj2 = mod2.c1()    # object of class c1 in mod2
obj2.m1()

print()

# --- Members of current module ---
print(x)            # variable x of current module
disp()              # function disp() of current module
obj3 = c1()         # object of class c1 in current module
obj3.m1()


----------------------------------------------------------------------------------------------------------------------------------------------

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module


#outputs

from mod1 import *   # import all members of mod1
from mod2 import *   # import all members of mod2

x = 30
def disp():
    print("disp function of current module")
class c1:
    def m1(self):
        print("m1 method of class c1 in current module")


# --- Members of mod1 ---
print(mod1.x)        # variable x from mod1
disp()               # disp() from mod1 is overwritten, so use alias if needed
obj1 = mod1.c1()
obj1.m1()

print()
print()

# --- Members of mod2 ---
print(mod2.x)        # variable x from mod2
mod2.disp()          # disp() from mod2
obj2 = mod2.c1()
obj2.m1()

print()
print()

# --- Members of current module ---
print(x)             # variable x of current module
disp()               # function disp() of current module
obj3 = c1()
obj3.m1()


---------------------------------------------------------------------------------------------------------------------------------------

# mod1.py  (Home  work)
#  How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
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
What  are  the  outputs ?  --->
'''

###############3#outputs

# mod1.py

# How to prevent execution of the middle 3 statements when mod1 is imported elsewhere
print("One")
print("Two")

if __name__ == "__main__":   #  prevents execution when imported
    print("Three")
    print("Four")
    print("Five")

print("Six")
print("Seven")
print("Eight")
print("Nine")


-------- case 1 : running directly -------------->>> python mod1.py
One
Two
Three
Four
Five
Six
Seven
Eight
Nine

-- import mode1 ---> from another module

One
Two
Six
Seven
Eight
Nine
----------------------------------------------------------------------------------------------

# mod2.py
print('Begining  of  mod2')
import mod1
print('End  of  mod2')

case 1 :Run python mod2.py

#outputs
Begining  of  mod2
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
End  of  mod2

------

Case 2 :If mod1.py has the if __name__ == "__main__":

Begining  of  mod2
One
Two
Six
Seven
Eight
Nine
End  of  mod2


----------------------------------------------------------------------------------------------------------

#  Find  outputs
from  cal  import  *
print(x)
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()
a . m1()

#outputs

5
10
17
3
70
1.4285714285714286
m1() method of class c1 in cal module


--------------------------------------------------------------

#  Find  outputs
import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))
print(cal . sub(10 , 7))
print(cal . mul(10 , 7))
print(cal . div(10 , 7))
a = cal . c1()
a . m1()

#outputs
5
10
17
3
70
1.4285714285714286
m1() method of class c1 in cal module

-------------------------------------------------------------------------

#  Find  outputs
from  cal  import   y , sub , mul
print(x)
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()


#outputs
NameError: name 'x' is not defined
10
NameError: name 'add' is not defined
3
70
NameError: name 'div' is not defined
NameError: name 'c1' is not defined

----------------------------------------------------------------------------------------------

# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

#outputs
Hyd
Sec
Cyb


-----------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

#outputs 
Hyd
Sec
Cyb

-----------------------------------------------------------------------------------------------------
import importlib
import mod1
print()
importlib.reload(mod1)
print()
importlib.reload(mod1)
importlib.reload('mod1')
reload(mod1)


#outputs

Hyd
Sec
Cyb

Hyd
Sec
Cyb

Hyd
Sec
Cyb


----- 

