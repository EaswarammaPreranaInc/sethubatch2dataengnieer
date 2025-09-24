from p1 import mod1, mod2

print(mod1.x)          # 10
mod1.f1()              # p1 ---> mod1 ---> f1 function
a = mod1.c1()
a.m1()                 # p1 ---> mod1 ---> c1 ---> m1 method

print()

print(mod2.x)          # 20
mod2.f1()              # p1 ---> mod2 ---> f1
b = mod2.c1()
b.m1()                 # p1 ---> mod2 ---> c1 ---> m1


from p1.mod1 import *

print(x)        # 10
f1()            # p1 ---> mod1 ---> f1 function
a = c1()
a.m1()          # p1 ---> mod1 ---> c1 ---> m1 method

print()

from p1.mod2 import *

print(x)        # 20   (overwrites mod1.x)
f1()            # p1 ---> mod2 ---> f1
b = c1()
b.m1()          # p1 ---> mod2 ---> c1 ---> m1



from p1 import mod1
print(mod1.x)      # 10
mod1.f1()
a = mod1.c1()
a.m1()

print()

from p1.p2 import mod2
print(mod2.x)      # 20
mod2.f1()
b = mod2.c1()
b.m1()

