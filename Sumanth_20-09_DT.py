from p1 import mod1, mod2 # How to import mod1 and mod2 of package p1 with from statement
print(mod1.x) # How to print object 'x' of mod1 in package p1
mod1.f1() # How to call function f1() of mod1 in package p1
a = mod1.c1() # How to call method m1() of class c1 in mod1 of package p1
a.m1() # Calling the method on the instance 'a'
print() # print()
print() # print()
print(mod2.x) # How to print object 'x' of mod2 in package p1
mod2.f1() # How to call function f1() of mod2 in package p1
b = mod2.c1() # Creating an instance of c1 from mod2
b.m1() # How to call method m1() of class c1 in mod2 of package p1
print(mod1.x) # print(mod1.x) - This will work because mod1 is imported.
print(x) # print(x) - This will fail with a NameError because 'x' is not directly imported.



from p1 import mod1                      # How to import members of mod1 in package p1
print(mod1.x)                            # How to print object 'x' of mod1 in package p1
mod1.f1()                                # How to call function f1() of mod1 in package p1
obj_c1_mod1 = mod1.c1()                  # How to call method m1() of class c1 in mod1 of package p1
obj_c1_mod1.m1()                         # Continuation of the previous action
print()                                  # print()
print()                                  # print()
from p1.p2 import mod2                   # How to import members of mod2 in sub-package p2 of package p1
print(mod2.x)                            # How to print object 'x' of mod2 in sub-package p2 of package p1
mod2.f1()                                # How to call function f1() of mod2 in sub-package p2 of package p1
obj_c1_mod2 = mod2.c1()                  # How to call method m1() of class c1 in mod2 of sub-package p2 of package p1
obj_c1_mod2.m1()                         # Continuation of the previous action




from p1 import mod1                      # How to import members of mod1 in package p1 with from statement
from p1 import mod2                      # How to import members of mod2 in package p1 with from statement
print(mod1.x)                            # How to print object 'x' of mod1 in package p1
mod1.f1()                                # How to call function f1() of mod1 in package p1
a = mod1.c1()                            # How to call method m1() of class c1 in mod1 of package p1
a.m1()                                   # Calling the method on the instance
print()                                  # print()
print()                                  # print()
print(mod2.x)                            # How to print object 'x' of mod2 in package p1
mod2.f1()                                # How to call function f1() of mod2 in package p1
b = mod2.c1()                            # Creating an instance of c1 from mod2
b.m1()                                   # How to call method m1() of class c1 in mod2 of package p1




from p1 import mod1#How to import members of mod1 in package p1
print(mod1.x)#How to print object 'x' of mod1 in package p1
mod1.f1()#How to call function f1() of mod1 in package p1
mod1.c1().m1()#How to call method m1() of class c1 in mod1 of package p1
print()
print()
from p1 import mod2#How to import members of mod2 in package p1
print(mod2.x)#How to print object 'x' of mod2 in package p1
mod2.f1()#How to call function f1() of mod2 in package p1
mod2.c1().m1()#How to call method m1() of class c1 in mod2 of package p
print(p1.mod1.x)
print(mod1.x)
from p1.p2 import mod2#How to import mod2 of sub-package p2 in package p1 with from statement
print(mod2.x)#How to print object 'x' of mod2 in sub-package p2 of package p1
mod2.f1()#How to call function f1() of mod2 in sub-package p2 of package p1
mod2.c1().m1()#How to call method m1() of class c1 in mod2 of sub-package p2 in package p1
