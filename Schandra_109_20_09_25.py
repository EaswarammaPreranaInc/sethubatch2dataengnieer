: # Save  in  cwd \  p1 \ mod1 . py
x = 10
def  f1():
	print('p1  --->  mod1   --->  f1  function')
class   c1:
	def  m1(self):
		print('p1  ---> mod1  ---> c1  ---> m1 method')



'''
1) What  is  the  name  of  module ?  --->  p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x' ,  Function   f1()  and  class  c1
'''
: # Save  in  cwd \ p1 \ mod2 . py
x = 20
def   f1():
	print('p1  ---> mod2  ---> f1')
class   c1:
	def  m1(self):
		print('p1  ---> mod2 ---> c1 ---> m1 ')



'''
1) What  is  the  name  of  module ?  --->  p1 . mod2

2) What  are  the  members  of  p1 . mod2 ?  --->  Object  'x' ,  Function   f1()  and  class  c1
'''

##############
Folder Structure

cwd/
│
└── p1/
    ├── mod1.py
    └── mod2.py


import p1.mod1
import p1.mod2

print(p1.mod1.x)   # 10
print(p1.mod2.x)   # 20

p1.mod1.f1()       # prints from mod1
p1.mod2.f1()       # prints from mod2

obj1 = p1.mod1.c1()
obj2 = p1.mod2.c1()

obj1.m1()          # p1 ---> mod1 ---> c1 ---> m1 method
obj2.m1()          # p1 ---> mod2 ---> c1 ---> m1 





: #  Save  in  any  file  of  cwd  (Homework)
How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1
How  to  call  function  f1()  of   mod2  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)
print(x)
##############

Folder structure

cwd/
│
├── test_pkg.py      # your test file
└── p1/
    ├── mod1.py
    └── mod2.py


 test_pkg.py
# Import modules with from statement
from p1 import mod1, mod2

# --- mod1 ---
# Print object 'x' of mod1
print(mod1.x)

# Call function f1() of mod1
mod1.f1()

# Call method m1() of class c1 in mod1
obj1 = mod1.c1()
obj1.m1()

print()  # blank line

# --- mod2 ---
# Print object 'x' of mod2
print(mod2.x)

# Call function f1() of mod2
mod2.f1()

# Call method m1() of class c1 in mod2
obj2 = mod2.c1()
obj2.m1()

print()
print("Direct access if imported members individually:")

# You *could also* import specific members directly
from p1.mod1 import x, f1, c1
print(x)      # x from mod1
f1()          # f1 from mod1
c1().m1()     # m1 from mod1

🔹 Expected Output
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 

Direct access if imported members individually:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


 Notice the difference:

from p1 import mod1 → use mod1.x, mod1.f1()

from p1.mod1 import x → use x directly





: #  Save  in  any  file  of  cwd
How  to  import  members  of  mod1  in  package  p1
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  import   members  of  mod2   in  package  p1
How  to  print  object  'x'  of   mod2  in  package  p1
How  to  call  function  f1()  of   mod2  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)
print(mod1 . x)
from  p1   import  mod1 . *
######################
Folder structure

cwd/
│
├── test_members.py   # your test file
└── p1/
    ├── mod1.py
    └── mod2.py

 test_members.py
# --- Import members of mod1 ---
from p1.mod1 import x, f1, c1

# Print object 'x' of mod1
print(x)

# Call function f1() of mod1
f1()

# Call method m1() of class c1 in mod1
obj1 = c1()
obj1.m1()

print()
print()

# --- Import members of mod2 ---
from p1.mod2 import x as x2, f1 as f12, c1 as c12
# (used alias names to avoid conflict with mod1 members)

# Print object 'x' of mod2
print(x2)

# Call function f1() of mod2
f12()

# Call method m1() of class c1 in mod2
obj2 = c12()
obj2.m1()

🔹 Expected Output
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 

 Important Notes

1. print(p1.mod1.x) → wrong, because you only imported members, not the full p1 package.
Use print(x) (after from p1.mod1 import x)

2. from p1 import mod1.* → invalid syntax in Python.
 Correct is:

from p1.mod1 import *


Then you can use x, f1(), c1() directly.





: '''  (Home  work)
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
print(x)
f1()
a = c1()
a . m1()

####################
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 








: '''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x)
f1()
a = c1()
a . m1()
#######################
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method




: ''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)
f1()
a = c1()
a . m1()
#################
30
Function  of  same  module
Method  of  class  c1  in same  module


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 Summary Table


| Order of Definitions & Imports | Final owner of `x`, `f1`, `c1` | Output source     |
| ------------------------------ | ------------------------------ | ----------------- |
| Local → mod1 → mod2            | **mod2** wins                  | Output from mod2  |
| Local → mod2 → mod1            | **mod1** wins                  | Output from mod1  |
| mod1 → mod2 → Local            | **Local** wins                 | Output from local |

compare_cases.py

# --- Case 1: Local → mod1 → mod2 ---
def case1():
    x = 30
    def f1():
        print("Function  of  same  module")
    class c1:
        def m1(self):
            print("Method  of  class  c1  in same  module")

    from p1.mod1 import *
    from p1.mod2 import *

    print("=== Case 1: Local → mod1 → mod2 ===")
    print(x)
    f1()
    a = c1()
    a.m1()
    print()

# --- Case 2: Local → mod2 → mod1 ---
def case2():
    x = 30
    def f1():
        print("Function  of  same  module")
    class c1:
        def m1(self):
            print("Method  of  class  c1  in same  module")

    from p1.mod2 import *
    from p1.mod1 import *

    print("=== Case 2: Local → mod2 → mod1 ===")
    print(x)
    f1()
    a = c1()
    a.m1()
    print()

# --- Case 3: mod1 → mod2 → Local ---
def case3():
    from p1.mod1 import *
    from p1.mod2 import *

    x = 30
    def f1():
        print("Function  of  same  module")
    class c1:
        def m1(self):
            print("Method  of  class  c1  in same  module")

    print("=== Case 3: mod1 → mod2 → Local ===")
    print(x)
    f1()
    a = c1()
    a.m1()
    print()


# --- Run all cases ---
if __name__ == "__main__":
    case1()
    case2()
    case3()


###When you run:
python compare_cases.py

Output:
=== Case 1: Local → mod1 → mod2 ===
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 

=== Case 2: Local → mod2 → mod1 ===
10
p1  --->  mod1   ---> f1  function
p1  ---> mod1  ---> c1  ---> m1 method

=== Case 3: mod1 → mod2 → Local ===
30
Function  of  same  module
Method  of  class  c1  in same  module
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



: '''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
How  to  import   members  of  mod1   in  package  p1  with  from  statement
How  to  import   members  of  mod2   in  package  p1  with  from  statement
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1
How  to  call  function  f1()  of   mod2  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
##############################
from p1.mod1 import *
from p1.mod2 import *

# Import members of mod1 with alias
from p1.mod1 import x as x1, f1 as f1_mod1, c1 as c1_mod1

# Import members of mod2 with alias
from p1.mod2 import x as x2, f1 as f1_mod2, c1 as c1_mod2

# --- Using members of mod1 ---
print("Members of mod1:")
print(x1)          # object x of mod1
f1_mod1()          # function f1 of mod1
obj1 = c1_mod1()   # class c1 of mod1
obj1.m1()          # method m1 of class c1 in mod1

print()
print()

# --- Using members of mod2 ---
print("Members of mod2:")
print(x2)          # object x of mod2
f1_mod2()          # function f1 of mod2
obj2 = c1_mod2()   # class c1 of mod2
obj2.m1()          # method m1 of class c1 in mod2

## expected output

Members of mod1:
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method

Members of mod2:
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1 




: # Save  in   cwd \ p1 \ mod1.py
x = 10
def   f1():
	print('p1  --->  mod1  --->  f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> mod1 ---> c1 ---> m1 method ')



'''
1) What  is  the  name  of  module ?  ---> p1 . mod1

2) What  are  the  members  of  p1 . mod1 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
'''
: # Save  in   cwd \ p1 \ p2 \ mod2.py
x = 20
def   f1():
	print('p1 ---> p2 ---> mod2 ---> f1 function')
class   c1:
	def  m1(self):
		print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')



'''
1) What  is  the  name  of  module  ?  --->  p1 . p2 . mod2

2) What  are  the  members  of  p1 . p2 . mod2 ?  --->  Object  'x'  ,  Function   f1()  and  class  c1
'''
################
Folder structure

cwd/
└── p1/
    ├── mod1.py
    └── p2/
        └── mod2.py

🔹 Example: Using both modules in a script (cwd/test_both_modules.py)
# Import mod1 and mod2 with aliases
from p1 import mod1
from p1.p2 import mod2

# Access members of mod1
print(mod1.x)
mod1.f1()
obj1 = mod1.c1()
obj1.m1()

print()

# Access members of mod2
print(mod2.x)
mod2.f1()
obj2 = mod2.c1()
obj2.m1()


Expected Output:

10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method 

20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method




: # Save  in  any  file  of  cwd
How  to  import  mod1  of  package  p1  with  from  statement
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x)
print()
print()
How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x)
from  p1  import   p2 . mod2
from  p2  import  mod2
####################################

Script: use_package_modules.py (save in cwd)

# --- Import mod1 of package p1 using from statement ---
from p1 import mod1

# Access members of mod1
print("Members of mod1:")
print(mod1.x)    # object x of mod1
mod1.f1()        # function f1 of mod1
obj1 = mod1.c1() # class c1 of mod1
obj1.m1()        # method m1 of class c1 in mod1

print()
print()

# --- Import mod2 of sub-package p2 using from statement ---
from p1.p2 import mod2

# Access members of mod2
print("Members of mod2:")
print(mod2.x)    # object x of mod2
mod2.f1()        # function f1 of mod2
obj2 = mod2.c1() # class c1 of mod2
obj2.m1()        # method m1 of class c1 in mod2

print()
print()

# --- Notes on import statements ---
# print(p1.mod1.x)   #  won't work unless you 'import p1' first
# print(p1.p2.mod2.x) #  won't work unless you 'import p1.p2' first

# Correct ways to import:
# from p1 import mod1
# from p1.p2 import mod2


Expected Output

Members of mod1:
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method 


Members of mod2:
20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method 




: # Save  in  any  file  of  cwd
How  to  import  members  of  mod1  in   package  p1
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . *

######################
 use_members_directly.py (save in cwd)

# --- Import all members of mod1 from package p1 ---
from p1.mod1 import *

# Access members of mod1
print("Members of mod1:")
print(x)      # object x of mod1
f1()          # function f1 of mod1
obj1 = c1()   # class c1 of mod1
obj1.m1()     # method m1 of class c1 in mod1

print()
print()

# --- Import all members of mod2 from sub-package p2 of package p1 ---
from p1.p2.mod2 import *

# Access members of mod2
print("Members of mod2:")
print(x)      # object x of mod2
f1()          # function f1 of mod2
obj2 = c1()   # class c1 of mod2
obj2.m1()     # method m1 of class c1 in mod2


$$$  Important Notes

1.from p1.mod1 import * → brings all members (x, f1, c1) into the current namespace.

2.from p1.p2.mod2 import * → overwrites all members from mod1 if names are the same!

  .So after this, x, f1(), c1 will refer to mod2’s members, not mod1’s.

3.If you want to use both without overwriting, you need aliases like:

from p1.mod1 import x as x1, f1 as f1_mod1, c1 as c1_mod1
from p1.p2.mod2 import x as x2, f1 as f1_mod2, c1 as c2_mod2


Expected Output (without aliases, mod2 overwrites mod1)
Members of mod1:
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method 


Members of mod2:
20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method






