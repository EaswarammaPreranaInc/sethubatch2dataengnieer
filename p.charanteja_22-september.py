# Using `import p1.mod1`

import p1.mod1

# To print object 'x' of mod1
print(p1.mod1.x)

# To call function f1() of mod1
p1.mod1.f1()

# To call method m1() of class c1 in mod1
obj = p1.mod1.c1()
obj.m1()

#To access items defined in `p1/__init__.py` (the “init module”):

import p1

# To print object 'x' from __init__.py
print(p1.x)

# To call function f1() from __init__.py
p1.f1()

# To call method m1() of class c1 in __init__.py
obj = p1.c1()
obj.m1()








# Using `from p1 import mod1`

from p1 import mod1

# Print object 'x' of mod1
print(mod1.x)

# Call function f1() of mod1
mod1.f1()

# Call method m1() of class c1 in mod1
obj = mod1.c1()
obj.m1()

#Accessing `__init__.py` members remains the same:

from p1 import x, f1, c1

print(x)
f1()
obj = c1()
obj.m1()







# Using `from p1.mod1 import *`

from p1.mod1 import *

# Print object 'x' (directly imported into namespace)
print(x)

# Call function f1()
f1()

# Call method m1() of class c1
obj = c1()
obj.m1()

#To import everything from `p1/__init__.py`:

from p1 import *  # Imports all symbols defined in p1/__init__.py






# To import the `__init__.py` module directly

- The `__init__` module of a package is referenced as the package itself.








