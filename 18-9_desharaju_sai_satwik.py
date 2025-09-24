

print("\nQ1: dir() of sys, time, math")
import sys, time, math
print(dir(sys))   # list of sys attributes
print()
print(dir(time))  # list of time attributes
print()
print(dir(math))  # list of math attributes



print("\nQ2: dir(cal)")
import cal
print(dir(cal))   # lists add, sub, mul, div, c1, x, y, plus __builtins__, __name__, etc.

x = 25
def disp(): print("Hello")
class c1: 
    def m1(self): pass

print(dir())            # lists names in current namespace
print(type(dir()))      # <class 'list'>
print(type(dir))        # <class 'builtin_function_or_method'>


a = []
for name in dir(cal):
    if not (name.startswith("_") or name.endswith("_")):
        a.append(name)
print(a)   # ['add', 'sub', 'mul', 'div', 'c1', 'x', 'y']


print(dir())
print()
from cal import *
print(dir())   # now includes add, sub, mul, div, c1, x, y
print()
from cal import add, mul, x
print(dir())   # same but explicit import


import sys
print("Original sys.path:")
for p in sys.path:
    print(p)
print("Total dirs:", len(sys.path))



sys.path.append("c:\\sairam")
print("After append, total dirs:", len(sys.path))
#import sample
#print(sample.x)
#sample.f1()
#obj = sample.c1(); obj.m1()


from random import *
print(random())           # float in [0.0, 1.0)
print(randint(1,100))     # random int
print(uniform(1,100))     # float in [1,100]
print(randrange(10))      # 0–9
print(randrange(1,11))    # 1–10
print(randrange(1,11,2))  # odd numbers
lst = [10,20,15,12,18]
print(choice(lst))        # random element
print(choice("RAJESH"))   # random character
s = {10,20,30,40}
print(choice(list(s)))    # random choice from set (converted to list)

s = "Rama Rao"
from random import choice
for _ in range(10):
    print(choice(s))


import string
for _ in range(10):
    pwd = ""
    for pos in range(1,7):
        if pos % 2 == 1:
            pwd += choice(string.ascii_uppercase)  # alphabet
        else:
            pwd += str(randint(0,9))               # digit
    print(pwd)

# ----------------------------------------------------

print("\nQ11: Random element of list 10 times")
lst = [25,10.8,"Hyd",True,3+4j,None]
for _ in range(10):
    print(choice(lst))

# ----------------------------------------------------

print("\nQ12: Generate 10 six-digit OTPs")
for _ in range(10):
    print(randint(100000,999999))

# ----------------------------------------------------

print("\nQ13: Open websites with gap (demo)")
import webbrowser, time
sites = ["google.com","rediff.com","gmail.com","amazon.com","netflix.com"]
#for site in sites:
#    webbrowser.open("http://" + site)
#    time.sleep(randint(5,20))

# ----------------------------------------------------

moves = ["Rock","Paper","Scissors"]
while True:
    user = int(input("What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : "))
    comp = randint(0,2)
    print("User:", moves[user])
    print("Computer:", moves[comp])
    if user == comp:
        print("Draw")
    elif (user==0 and comp==2) or (user==1 and comp==0) or (user==2 and comp==1):
        print("User wins")
    else:
        print("Computer wins")
    cont = input("Continue (y/n)? ")
    if cont.lower() != "y":
        print("End of the game")
        break
