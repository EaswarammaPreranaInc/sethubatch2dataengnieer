

def f1():
    print('f1  function')

def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')

print("=== Example 1 ===")
print('Begin')
f2(f1)
print('End')

# Begin
# f2  function
# f1  function
# Back  to  f2  function
# End



def f1():
    print('f1  function')

def f2(fun):
    print('f2  function')
    fun()   # error if fun is None
    print('Back  to  f2  function')

print("\n=== Example 2 ===")
print('Begin')
try:
    f2(f1())   # f1() runs, returns None, then None()
except Exception as e:
    print("Error:", e)
print('End')
# Output before error:
# Begin
# f1  function
# f2  function
# Error: 'NoneType' object is not callable
# End



def outer():
    print('Outer  Function')
    def inner():
        print('Inner function')
    return inner

print("\n=== Example 3 ===")
fun = outer()
print('Hello')
fun()
print('Bye')
try:
    inner()   # error
except Exception as e:
    print("Error:", e)

# Outer  Function
# Hello
# Inner function
# Bye
# Error: name 'inner' is not defined



def outer(x):
    print('Outer  Function')
    def inner1():
        print('1st  inner  function')
    def inner2():
        print("2nd  inner  function")
    if x == 10:
        return inner1
    else:
        return inner2

print("\n=== Example 4 ===")
f1 = outer(10)
f2 = outer(20)
f1()
f2()

# Outer  Function
# Outer  Function
# 1st  inner  function
# 2nd  inner  function



def outer(msg):
    def inner():
        print(msg)
    return inner

print("\n=== Example 5 ===")
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

# Hi
# Hello



def decor(fun):
    print(fun.__name__)
    def inner():
        return fun() + 2
    return inner

@decor
def f1():
    return 10

print("\n=== Example 6 ===")
print('End')

# f1
# End



def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner

def f1():
    return 10

print("\n=== Example 7 ===")
f1 = decor(f1)
print(f1())
 12



def decor(fun):
    print(fun.__name__)
    def inner(name):
        if name == 'Python':
            print('Hello', name)
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print('Hi', name)

print("\n=== Example 8 ===")
wish('Python')
wish('Java')

# wish
# Hello Python
# Hi Java



def decor(fun):
    def inner(x, y):
        try:
            return fun(x, y)
        except:
            return 'Division by 0 is not permitted'
    return inner

@decor
def div(a, b):
    return a / b

print("\n=== Example 9 ===")
print(div(10, 3))
print(div(10, 0))
try:
    print(inner(10, 3))  # error
except Exception as e:
    print("Error:", e)

# 3.3333333333333335
# Division by 0 is not permitted
# Error: name 'inner' is not defined



def decor(fun):
    def inner(a, b):
        if a < b:   # swap so larger first
            a, b = b, a
        return fun(a, b)
    return inner

@decor
def div(a, b):
    return a / b

print("\n=== Example 10 ===")
print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5



def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function')
        fun()
        print('Decoration is finished')
    return inner

@decor
def f1():
    print('Hello')

print("\n=== Example 11 ===")
f1()
print('Bye')

# Decorating f1 function
# Hello
# Decoration is finished
# Bye



def decor(fun):
    print(fun.__name__)
    def inner(*x):  # var-arg decorator
        print(x)
        fun(*x)
        print('End of decoration')
    return inner

@decor
def f1(x):
    print('f1 function :', x)

@decor
def f2(x, y):
    print('f2 function :', x, y)

@decor
def f3(x, y, z):
    print('f3 function :', x, y, z)

@decor
def f4():
    print('f4 function')

print("\n=== Example 12 ===")
f1(10)
f2(25, 10.8)
f3('Hyd', True, 3 + 4j)
f4()

# f1
# f2
# f3
# f4
# (10,)
# f1 function : 10
# End of decoration
# (25, 10.8)
# f2 function : 25 10.8
# End of decoration
# ('Hyd', True, (3+4j))
# f3 function : Hyd True (3+4j)
# End of decoration
# ()
# f4 function
# End of decoration
