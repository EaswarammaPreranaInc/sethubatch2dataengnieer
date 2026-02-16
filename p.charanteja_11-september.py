# f2(f1) vs f2(f1())

def f1():
    print('f1  function')
def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
print('Begin')
f2(f1)
print('End')
'''
# Output:

Begin
f2  function
f1  function
Back  to  f2  function
End
-f2(f1) passes the function itself (not its result), which is called inside `f2`.

'''







def f1():
    print('f1  function')
def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
print('Begin')
f2(f1())
print('End')
'''
# Output:

Begin
f1  function
f2  function
TypeError: 'NoneType' object is not callable
-f1() is called immediately, prints 'f1 function'. Its return value (None) is passed to 'f2', so 'fun()' (i.e., 'None()') raises a 'TypeError'.
'''








# Decorator with Nested Functions and Function Variables

def outer():
    print('Outer  Function')
    def inner():
        print('Inner function')
    return inner
fun = outer()
print('Hello')
fun()
print('Bye')
inner()
'''
# Output:

Outer  Function
Hello
Inner function
Bye
Traceback (most recent call last):
NameError: name 'inner' is not defined
'''







# Factory Pattern Based on Arguments

def outer(x):
    print('Outer  Function')
    def inner1():
        print('1st  inner  function')
    def inner2():
        print('2nd  inner  function')
    if x == 10:
        return inner1
    else:
        return inner2
f1 = outer(10)
f2 = outer(20)
f1()
f2()
'''
# Output:

Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
'''







# Returning Functions with Arguments

def outer(msg):
    def inner():
        print(msg)
    return inner
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
'''
# Output:

Hi
Hello
'''







# Decorator That Prints the Function Name and Returns Modified Value

def decor(fun):
    print(fun.__name__)
    def inner():
        return fun() + 2
    return inner
@decor
def f1():
    return 10
print('End')
'''
# Output:

f1
End
'''







# Manual Decorator Application Without `@`

def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner
def f1():
    return 10
f1 = decor(f1)
print(f1())
'''
# Output:

12
'''






# Decorator Controlling Print Output Based on Argument

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
wish('Python')
wish('Java')
'''
# Output:

wish
Hello Python
Hi Java
'''







# Decorator for Safe Division

def decor(fun):
    def inner(x, y):
        try:
            return fun(x, y)
        except:
            return 'Division   by  0  is  not  permitted'
    return inner
@decor
def div(a, b):
    return a / b
print(div(10, 3))
print(div(10, 0))
print(inner(10, 3))
'''
# Output:
3.3333333333333335
'''







# Decorator Forces Specific Output

def decor(fun):
    def inner(a, b):
        return 4.5
    return inner
@decor
def div(a, b):
    return a / b
print(div(9 , 2))
print(div(2 , 9))
'''
# Output:

4.5
4.5
'''








# Decorator that Announces Decoration Start and Stop

def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function')
        fun()
        print('Decoration is finished')
    return inner
@decor
def f1():
    print('Hello')
f1()
print('Bye')
'''
# Output:

Decorating f1 function
Hello
Decoration is finished
Bye
'''








# Single Decorator for Multiple Function Signatures (Var-Arg)

def decor(fun):
    print(fun.__name__)
    def inner(*x):
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
f1(10)
f2(25, 10.8)
f3('Hyd', True, 3 + 4j)
f4()
'''
# Output:

f1
f2
f3
f4
(10,)
f1 function : 10
End of decoration
(25, 10.8)
f2 function : 25 10.8
End of decoration
('Hyd', True, (3+4j))
f3 function : Hyd True (3+4j)
End of decoration
()
f4 function
End of decoration
'''

