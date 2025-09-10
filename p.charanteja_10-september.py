#1. Towers of Hanoi – Generalized Steps


def toh(n, p1, p2, p3):
    if n > 0:
        toh(n-1, p1, p3, p2) 
        print(f"{p1} ---> {p3}")
        toh(n-1, p2, p1, p3) 

'''
output:
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3
'''






#2. Homework – Find Outputs and Identify Errors

#(a) Nonlocal variable used before assignment

def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)
outer()
print(x)

'''
Output:
Prints 10 (before increment)

Error occurs in inner() at print(x) since nonlocal x + assigning to x means x is considered uninitialized in the function scope before assignment.

Error: UnboundLocalError: local variable 'x' referenced before assignment.
'''



#(b) Nonlocal after variable reference

def outer():
    x = 10
    def inner():
        print(x)
        nonlocal x
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)
outer()

'''
Output
Error: SyntaxError: name 'x' is used prior to nonlocal declaration

nonlocal must be declared before any usage.
'''




#(c) Use global inside nested function

def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)
outer()
print(x)


'''
Output:

10
20
15
25
'''



#(d) Nonlocal to undefined variable

def outer():
    def inner():
        nonlocal x
        x = 20
        print(x)
    inner()
    print(x)
outer()
print(x)

'''
Output
Error: SyntaxError: no binding for nonlocal 'x' found in enclosing scopes
'''




#(e) Only using global, not defined before main

def outer():
    def inner():
        global x
        x = 20
        print(x)
        x = x + 5
    inner()
    print(x)
outer()
print(x)

'''
Output:

20
25
25
'''



#(f) Error: nonlocal outside any enclosing function

def f1():
    nonlocal x

'''
Output
Error: SyntaxError: no binding for nonlocal 'x' found in enclosing scopes
'''



#(g) Nonlocal for one variable, assignment inside

def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200
        print(a, b)
    print(a, b)
    inner()
    print(a, b)
outer()
'''
Output:

10 20
100 200
100 20
'''



#(h) Nonlocal in nested, assignment, return

def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    f2()
    return x
print(f1())

'''
Output:

text
Hello
'''



#(i) Assignment using local variable before initialization

def fun():
    x = 10
    def gun():
        x = x + 20
        print(x)
    gun()
fun()

'''
Output
Error: UnboundLocalError: local variable 'x' referenced before assignment
'''



#(j) Both global and nonlocal for same variable

x = 10
def outer():
    x = 20
    def inner():
        global x
        nonlocal x

'''
Output
Error: SyntaxError: name 'x' is nonlocal and global
'''



#(k) Nested functions with repeated nonlocal

def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)
        f3()
    f2()
f1()

'''
Output:

10
'''

