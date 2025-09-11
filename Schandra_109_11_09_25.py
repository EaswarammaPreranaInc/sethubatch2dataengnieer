# ==========================================
# Program 1
# Q: Find outputs (Home work)
def f1():
    print('f1  function')

def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
# end of the function

print('Begin')
f2(f1)
print('End')

# Output:
# Begin
# f2  function
# f1  function
# Back  to  f2  function
# End
# ==========================================


# ==========================================
# Program 2
# Q: Find outputs (Home work)
def f1():
    print('f1  function')

def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
# end of the function

print('Begin')
f2(f1())
print('End')

# Output:
# Begin
# f1  function
# f2  function
# Traceback (most recent call last):
#   ...
# TypeError: 'NoneType' object is not callable
# ==========================================


# ==========================================
# Program 3
# Q: Find outputs (Home work)
def outer():
    print('Outer  Function')
    def inner():
        print('Inner function')
    return inner
# End of the function

fun = outer()
print('Hello')
fun()
print('Bye')
inner()

# Output:
# Outer  Function
# Hello
# Inner function
# Bye
# Traceback (most recent call last):
#   ...
# NameError: name 'inner' is not defined
# ==========================================


# ==========================================
# Program 4
# Q: Find outputs (Home work)
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
# end of the function

f1 = outer(10)
f2 = outer(20)
f1()
f2()

# Output:
# Outer  Function
# Outer  Function
# 1st  inner  function
# 2nd  inner  function
# ==========================================


# ==========================================
# Program 5
# Q: Find outputs (Home work)
def outer(msg):
    def inner():
        print(msg)
    return inner
# End of the function

hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

# Output:
# Hi
# Hello
# ==========================================


# ==========================================
# Program 6
# Q: Find outputs (Home work)
def decor(fun):
    print(fun._name_)
    def inner():
        return fun() + 2
    return inner

@decor
def f1():
    return 10
# End of the function

print('End')

# Output:
# f1
# End
# ==========================================


# ==========================================
# Program 7
# Q: How to call f1() function when @decor tag is missing?
def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner

def f1():
    return 10
# end of the function

f1 = decor(f1)
print(f1())

# Output:
# 12
# ==========================================


# ==========================================
# Program 8
# Q: Find outputs (Home work)
def decor(fun):
    def inner(name):
        if name == 'Python':
            print('Hello', name)
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print('Hi', name)
# End of the function

wish('Python')
wish('Java')

# Output:
# wish
# Hello Python
# Hi Java
# ==========================================


# ==========================================
# Program 9
# Q: Modify following div function such that div(9,2) and div(2,9) return 4.5 only
def decor(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)
    return inner

@decor
def div(a, b):
    return a / b

print(div(9, 2))
print(div(2, 9))

# Output:
# 4.5
# 4.5
# ==========================================


# ==========================================
# Program 10
# Q: Find outputs (Home work)
def decor(fun):
    def inner():
        print(f'Decorating {fun._name_} function')
        fun()
        print('Decoration is finished')
    return inner

@decor
def f1():
    print('Hello')
# End of the function

f1()
print('Bye')

# Output:
# Decorating f1 function
# Hello
# Decoration is finished
# Bye
# ==========================================


# ==========================================
# Program 11 (Most tricky)
# Q: Same decorator to multiple functions with different signatures
def decor(fun):
    print(fun._name_)
    def inner(*x):   # * packs arguments
        print(x)
        fun(*x)      # * unpacks arguments
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

# end of function
f1(10)
f2(25, 10.8)
f3('Hyd', True, 3 + 4j)
f4()

# Output:
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
