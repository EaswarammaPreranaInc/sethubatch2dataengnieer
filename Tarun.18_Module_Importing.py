#1
# How to reuse mod2 ? (Home work)
print('Hello')
import mod2       #How to import mod2
print(mod2.x)      #(How to print variable 'x' of mod2)
print(mod2.f1())  #How to call function f1() of mod2
print('Bye')
import mod4
print(x)         #Error
f1()              #Error



#2
# How to reuse mod2 ? (Home work)
print('Hello')
import mod2                     #How to import mod2
print(mod2.x)                   #How to print variable 'x' of mod2)
print(mod2.f1())                #How to call function f1() of mod2
print('Bye')
import mod4
print(x)                             #Error
f1()                                   #Error


#3
 # Find outputs (Home work)
print('Before')
run_module('mod2')              #How to run mod2
print(mod2 . x)
mod2 . f1()
print('After')
run_module('mod2')
runpy . run_module(mod2)      #Error



#cal . py
x = 100
y = 200
def add(a , b):
 return a + b
def sub(a , b):
 return a - b
def mul(a , b):
 return a * b
def div(a , b):
 return a / b
class c1:
 def m1(self):
  print('m1 method')

cal.py is not a ho,me work


 #4
# How to use members of cal module with from statement ? (Home work)
print('Begin')
import cal                                    #How to import all the members of cal module
print(cal.x)                                  #How to print variable 'x' of cal module)
print(cal.y)                                  #How to print variable 'y' of cal module)
print(cal . x)                  
print(cal.add(10,7))                  #How to call add() function of cal module by passing 10 and 7)
print(cal.sub(10,7) )                 #How to call sub() function of cal module by passing 10 and 7)
print(cal.mul(10,7) )                 #How to call mul() function of cal module by passing 10 and 7)
print(cal.div(10,7) )                 #How to call div() function of cal module by passing 10 and 7)
print(cal . add(x , y))               #Error
a=cal.c1()
a.m1()                              #How to call m1() method of class c1 in cal module
b = cal . c1()                    #Error


#5
# How to import only variable 'x' , functions add() and mul() and class c1 of cal module ? (Home work)
print('Begin')
#_all_ = ['x', 'add', 'mul', 'c1']
from cal import x,add,mul,c1                #How to import members x , add , mul and class c1 of cal moudle
print(x)                                                  #How to print variable 'x' of cal module)
print(y)
print(cal . x)                                           #Error
print(add(10,7))                                     #How to call add() function of cal module by passing 10 and 7)
print(sub(10 , 7))
print(mul(10,7))                                    #How to call mul() function of cal module by passing 10 and 7)
print(div(10 , 7))
a=c1()
a.m1()                                                   #How to call m1() method of class c1 in cal module


#6 # Module alias
print('Begin')
import cal as c           #How to import cal module with another name using import statement
print(c.x)                   #How to print variable 'x' of cal module)
print(c.y)                   #How to print variable 'y' of cal module)
print(c.add(10,7))     #How to call add() function of cal module by passing 10 and 7)
print(c.sub(10,7))     #How to call sub() function of cal module by passing 10 and 7)
print(c.mul(10,7))           #How to call mul() function of cal module by passing 10 and 7)
print(c.div(10,7))            #How to call div() function of cal module by passing 10 and 7)
a=c.c1()
a.m1()                                 #How to call m1() method of c1 class in cal module
print(cal . x)                        #Error
from math as m import *   #Error


#7
# Member alias
from cal import x,add as a,mul as m,c1 as c   #How to import members x , add , mul and class c1 of cal moudle with another name using from statement
print(x)        #How to print variable 'x' of cal module)
print(x)
print(a(1,7))                  #How to call add() function of cal module by passing 10 and 7)
print(m(10,7))                #How to call mul() function of cal module by passing 10 and 7)
d=c()                            
d.m1()                              #How to call m1() method of class c1 in cal module
print(add(10 , 7))            #Error
b = c1()                           #Error


#8
# mod1.py
x = 10
def disp():
 print('disp function of mod1')
class c1:
 def m1(self):
  print('m1 method of class c1 in mod1')



#mod2.py
x = 20
def disp():
 print('disp function of mod2')
class c1:
 def m1(self):
  print('m1 method of class c1 in mod2')

 mod1 and mod2 are not homeworks




#10 # Find outputs (Home work)
x = 30
def disp():
  print('disp function of same module ')
class c1:
 def m1(self):
  print('m1 method of class c1 in same module')
from mod2 import *
from mod1 import *
print(x)                            #10
disp()                               #disp function of mod1
a = c1()
a . m1()                              #m1 method of class c1 in mod1

#11
 # Find outputs (Home work)
from mod1 import *
from mod2 import *
x = 30
def disp():
 print('disp function of same module ')
class c1:
 def m1(self):
  print('m1 method of class c1 in same module')
print(x)                #30
disp()                   #disp function of same module 
a = c1()
a . m1()               #m1 method of class c1 in same module


#12
 # How to use members of all the 3 modules(mod1 , mod2 and current module) with import statement ?
import mod1 as a
import mod2  as b                 #How to import mod1 and mod2
x = 30
def disp():
  print('disp function of same module')
class c1:
 def m1(self):
  print('m1 method of class c1 in same module')
print(a.x)                         #How to print variable 'x' of mod1
a.disp()               #How to call disp() function of mod1
d=a.c1()
d.m1()                            #How to call method m1() of class c1 in mod1
print()
print(b.x)                          #How to print variable 'x' of mod2
b.disp()                  #How to call disp() function of mod2
e=b.c1()
e.m1()                             #How to call method m1() of class c1 in mod2
print()
print(x)                         #How to print variable 'x' of current module)
disp()                            #How to call disp() function of current module
f=c1()
f.m1()                            #How to call method m1() of class c1 in current module


#13 # How to use members of all the three modules with from statement ?
import mod1 as a             #How to import members of mod1
import mod2 as b               #How to import members of mod2
x = 30
def disp():
        print('disp function of same module')
class c1:
 def m1(self):
  print('m1 method of class c1 in same module')
print(a.x)               #How to print variable 'x' of mod1)
a.disp()                  #How to call disp() function of mod1
d=a.c1()
d.m1()                 #How to call method m1() of class c1 in mod1
print()
print()
print(b.x)            #How to print variable 'x' of mod2)
b.disp()               #How to call disp() function of mod2
e=b.c1()              
e.m1()                    #How to call method m1() of class c1 in mod2
print()
print()
print(x)                     #How to print variable 'x' of current module)
disp()                      #How to call disp() function of current module
f=c1()
f.m1()                       #How to call method m1() of class c1 in current module

#14
 # mod1.py (Home work)
# How to prevent execution the middle 3 statements when mod1 is imported elsewhere
py mod1.py
print('One')
print('Two')
print('Three')
if  _name=="main_":
      print('Four')
      print('Five')
        print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
py mod1.py
What are the outputs ? --->
'''


#15
# Find outputs (Home work)
print('Begining of mod2')
import mod1
print('End of mod2')

"""
Begining of mod2
One
Two
Three
Seven
Eight
Nine
End of mod2
"""



 # cal . py
_all_ = ['add' , 'x' , 'mul' , 'c1' , 'z']
x = 100
y = 200
def add(a , b):
 return a + b
def sub(a , b):
 return a - b
def mul(a , b):
 return a * b
def div(a , b):
 return a / b
class c1:
 def m1(self):
  print('m1 method')


'''
_all_
----------
1) What is _all_ ? ---> List of members of the module which are to be imported when * is used

2) from cal import *
    Which members are imported ? ---> Those members which are in _all_ list of cal module

3) What happens when _all_ list has an invalid member ? ---> from module import * throws ImportError

4) Where is _all_ list defined ? ---> Inside the module i.e. Any where in the module

5) from cal import *
    Which members are imported when _all_ list is not defined in cal module ? --->
          All the members are imported becoz default _all_ is every member of the module

6) from cal import *
    Which members are imported when _all_ list is empty in cal module ? ---> No member is imported

7) from cal import y , sub , mul
    Which members are imported ? ---> y , sub and mul but not members of _all_ list

8) _all_ list plays a key role only when * is used in import clause of from statement

9) import module
    Which members are imported ? ---> No member is imported becoz import statement imports module but not members
'''
 cal.py is not a homework



#16 # Find outputs
from cal import *
print(x)                                    #100
print(y)                                    #Error
print(add(10 , 7))                   #17
print(sub(10 , 7))                  #Error
print(mul(10 , 7))                   #70
print(div(10 , 7))                      #Error
a = c1()
a . m1()                                        #m1method


#17 # Find outputs
import cal
print(cal . x)                               #100
print(cal . y)                                #200
print(cal . add(10 , 7))               #17
print(cal . sub(10 , 7))                 #3
print(cal . mul(10 , 7))                 #70
print(cal . div(10 , 7))                 #1.3
a = cal . c1()
a . m1()                                        ##m1method




#18 # Find outputs
from cal import y , sub , mul
print(x)                                 #Error
print(y)                                 #200
print(add(10 , 7))                  #Error
print(sub(10 , 7))                   #3
print(mul(10 , 7))                 #70       
print(div(10 , 7))                 #Error
a = c1()                               #Error



 # mod1.py (Home work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')
 mod1.py is not a home work


#19# Find outputs (Home work)
import mod1
import mod1
import mod1                

"""
Hyd
Sec
Cyb
"""



#20
 # reload() function demo program (Home work)
import importlib
import mod1
print()
importlib . reload(mod1)            #Hyd    Sec      Cyb
print()
importlib . reload(mod1)           ##Hyd    Sec      Cyb
importlib . reload('mod1')          #Error
reload(mod1)                           #Error
