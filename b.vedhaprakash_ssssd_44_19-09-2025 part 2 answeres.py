

# Homework Outputs (19/09/2025)

```python
# Save in cwd \ p1 \ mod1.py
x = 10
def f1():
    print('p1 ---> mod1 ---> f1 function')
class c1:
    def m1(self):
        print('p1 ---> mod1 ---> c1 ---> m1 method')

'''
1) What is the name of module ?  --->  p1.mod1
2) What are the members of p1.mod1 ?  --->  Object 'x', Function f1(), Class c1
'''
```

```python
# Save in cwd \ p1 \ mod2.py
x = 20
def f1():
    print('p1 ---> mod2 ---> f1')
class c1:
    def m1(self):
        print('p1 ---> mod2 ---> c1 ---> m1 ')

'''
1) What is the name of module ?  --->  p1.mod2
2) What are the members of p1.mod2 ?  --->  Object 'x', Function f1(), Class c1
'''
```

---

## Q1) Import `mod1` and `mod2` of package `p1` with `from` statement

```python
from p1 import mod1, mod2

print(mod1.x)         
mod1.f1()             
obj1 = mod1.c1()
obj1.m1()             

print()
print(mod2.x)         
mod2.f1()             
obj2 = mod2.c1()
obj2.m1()
```

Expected Output:

```
10
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

20
p1 ---> mod2 ---> f1
p1 ---> mod2 ---> c1 ---> m1 
```

---

## Q2) Import members of `mod1` and `mod2` directly

```python
from p1.mod1 import x, f1, c1
print(x)          
f1()              
obj1 = c1()
obj1.m1()         

print()

from p1.mod2 import x, f1, c1
print(x)          
f1()              
obj2 = c1()
obj2.m1()         
```

Expected Output:

```
10
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

20
p1 ---> mod2 ---> f1
p1 ---> mod2 ---> c1 ---> m1 
```

---

## Q3) Conflicts when importing with `*`

```python
x = 30
def f1():
    print('Function of same module')
class c1:
    def m1(self):
        print('Method of class c1 in same module')

from p1.mod1 import *
from p1.mod2 import *

print(x)     
f1()         
a = c1()      
a.m1()        
```

Expected Output:

```
30
Function of same module
Method of class c1 in same module
```

---

## Q4) Reverse order import

```python
x = 30
def f1():
    print('Function of same module')
class c1:
    def m1(self):
        print('Method of class c1 in same module')

from p1.mod2 import *
from p1.mod1 import *

print(x)      
f1()          
a = c1()
a.m1()
```

Expected Output:

```
30
Function of same module
Method of class c1 in same module
```

---

## Q5) Define after imports

```python
from p1.mod1 import *
from p1.mod2 import *

x = 30
def f1():
    print('Function of same module')
class c1:
    def m1(self):
        print('Method of class c1 in same module')

print(x)      
f1()          
a = c1()
a.m1()
```

Expected Output:

```
30
Function of same module
Method of class c1 in same module
```

---

## Q6) Use members of both modules

```python
from p1.mod1 import x as x1, f1 as f1_mod1, c1 as c1_mod1
from p1.mod2 import x as x2, f1 as f1_mod2, c1 as c1_mod2

print(x1)            
f1_mod1()            
obj1 = c1_mod1()
obj1.m1()            

print()

print(x2)            
f1_mod2()            
obj2 = c1_mod2()
obj2.m1()            
```

Expected Output:

```
10
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

20
p1 ---> mod2 ---> f1
p1 ---> mod2 ---> c1 ---> m1 
```

---

## Q7) Nested package example (`p1.p2.mod2`)

```python
# Save in cwd \ p1 \ mod1.py
x = 10
def f1():
    print('p1 ---> mod1 ---> f1 function')
class c1:
    def m1(self):
        print('p1 ---> mod1 ---> c1 ---> m1 method')

# Save in cwd \ p1 \ p2 \ mod2.py
x = 20
def f1():
    print('p1 ---> p2 ---> mod2 ---> f1 function')
class c1:
    def m1(self):
        print('p1 ---> p2 ---> mod2 ---> c1 ---> m1 method')
```

---

### Importing from nested package

```python
from p1 import mod1
from p1.p2 import mod2

print(mod1.x)        
mod1.f1()
obj1 = mod1.c1()
obj1.m1()

print()

print(mod2.x)        
mod2.f1()
obj2 = mod2.c1()
obj2.m1()
```

Expected Output:

```
10
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
```

---

### Importing members directly

```python
from p1.mod1 import x, f1, c1
print(x)       
f1()
obj1 = c1()
obj1.m1()

print()

from p1.p2.mod2 import x, f1, c1
print(x)       
f1()
obj2 = c1()
obj2.m1()
```

Expected Output:

```
10
p1 ---> mod1 ---> f1 function
p1 ---> mod1 ---> c1 ---> m1 method

20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
```

---


