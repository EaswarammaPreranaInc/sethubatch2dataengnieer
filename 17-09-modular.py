
#  Reuse mod2
print('Hello')
import mod2
print(mod2.x)
mod2.f1()
print('Bye')
import mod4
print(x)
f1()

'''
Hello
20
f1 function of mod2
Bye
20
f1 function of mod2
'''


# run_module demo

print('Before')
import runpy
import mod2
print(mod2.x)
mod2.f1()
print('After')
runpy.run_module('mod2')

'''
Before
20
f1 function of mod2
After
Begining of mod2
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
End of mod2
'''


# from cal import *

print('Begin')
from cal import *
print(x)
print(y)
print(add(10, 7))
print(sub(10, 7))
print(mul(10, 7))
print(div(10, 7))
print(add(x, y))
b = c1()
b.m1()
print('End')

'''
Begin
100
200
17
3
70
1.4285714285714286
300
m1  method
End
'''


#Import selected members

print('Begin')
from cal import x, add, mul, c1
print(x)
print(add(10, 7))
print(mul(10, 7))
b = c1()
b.m1()
print('End')

'''
Begin
100
17
70
m1  method
End
'''


# Module alias

print('Begin')
import cal as c
print(c.x)
print(c.y)
print(c.add(10, 7))
print(c.sub(10, 7))
print(c.mul(10, 7))
print(c.div(10, 7))
b = c.c1()
b.m1()
print('End')

'''
Begin
100
200
17
3
70
1.4285714285714286
m1  method
End
'''

#  Member alias

from cal import x as a, add as plus, mul as times, c1 as cls
print(a)
print(plus(10, 7))
print(times(10, 7))
b = cls()
b.m1()

'''
100
17
70
m1  method
'''


# Import order effect

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
30
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
'''


# Import order effect (reversed)

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
30
disp  function  of  same  module 
m1  method of  class  c1  in  same  module
'''


# Prevent execution in import

if __name__ == "__main__":
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
py mod1.py
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
'''

# Import inside mod2

print('Begining  of  mod2')
import mod1
print('End  of  mod2')

'''
Begining  of  mod2
Four
Five
Six
Seven
Eight
Nine
End  of  mod2
'''

#  from cal import *

from cal import *
print(x)
print(y)
print(add(10, 7))
print(sub(10, 7))
print(mul(10, 7))
print(div(10, 7))
a = c1()
a.m1()

'''
100
200
17
3
70
1.4285714285714286
m1  method
'''


#  import cal

import cal
print(cal.x)
print(cal.y)
print(cal.add(10, 7))
print(cal.sub(10, 7))
print(cal.mul(10, 7))
print(cal.div(10, 7))
a = cal.c1()
a.m1()

'''
100
200
17
3
70
1.4285714285714286
m1  method
'''


#  Import selective members

from cal import y, sub, mul
print(y)
print(sub(10, 7))
print(mul(10, 7))

'''
200
3
70
'''


# mod1.py simple prints

print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

'''
Hyd
Sec
Cyb
'''


# Multiple imports

import mod1
import mod1
import mod1

'''
Hyd
Sec
Cyb
'''


# reload() demo

import importlib
import mod1
print()
importlib.reload(mod1)
print()
importlib.reload(mod1)

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
