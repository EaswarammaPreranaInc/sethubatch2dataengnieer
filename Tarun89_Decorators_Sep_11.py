#TARUN BANALA             11-09-2025
# Find outputs (Home work)
def f1():
    print('f1 function')  # Function definition
def f2(fun):
    print('f2 function')  # Function definition
    fun()
    print('Back to f2 function')  # Function definition
# end of the function
print('Begin')  # Output: Begin
f2(f1)  # Output: f2 function → f1 function → Back to f2 function
print('End')  # Output: End

# Find outputs (Home work)
def f1():
    print('f1 function')  # Function definition
def f2(fun):
    print('f2 function')  # Function definition
    fun()
    print('Back to f2 function')  # Function definition
# end of the function
print('Begin')  # Output: Begin
f2(f1())  # Output: f1 function → f2 function → TypeError: 'NoneType' object is not callable
print('End')  # This line won't execute due to error

# Find outputs (Home work)
def outer():
    print('Outer Function')  # Function definition
    def inner():
        print('Inner function')  # Function definition
    return inner  # Function definition
# End of the function
fun = outer()  # Output: Outer Function
print('Hello')  # Output: Hello
fun()  # Output: Inner function
print('Bye')  # Output: Bye
inner()  # Output: NameError: name 'inner' is not defined

# Find outputs (Home work)
def outer(x):
    print('Outer Function')  # Function definition
    def inner1():
        print('1st inner function')  # Function definition
    # End of inner1
    def inner2():
        print("2nd inner function")  # Function definition
    # End of inner2
    if x == 10:
        return inner1  # Function definition
    else:
        return inner2  # Function definition
#end of the function
f1 = outer(10)  # Output: Outer Function
f2 = outer(20)  # Output: Outer Function
f1()  # Output: 1st inner function
f2()  # Output: 2nd inner function

# Find outputs (Home work)
def outer(msg):
    def inner():
        print(msg)  # Function definition
    return inner  # Function definition
# End of the function
hi_fun = outer('Hi')  # Creates closure
hello_fun = outer('Hello')  # Creates closure
hi_fun()  # Output: Hi
hello_fun()  # Output: Hello

# Find outputs (Home work)
def decor(fun):
    print(fun . _name_)  # Should be __name__ → Output: f1
    def inner():
        return fun() + 2  # Function definition
    return inner  # Function definition
@decor
def f1():
    return 10  # Function definition
# End of the function
print('End')  # Output: End

# How to call f1() function when @decor tag is missing ?
def decor(fun):
    def inner():
        x = fun()  # Function definition
        return x + 2  # Function definition
    return inner  # Function definition
def f1():
    return 10  # Function definition
#end of the function
f1 = decor(f1)  # Manual decoration
print(f1())  # Output: 12

# Find outputs(Home work)
def decor(fun):
    print(fun . _name_)  # Should be __name__ → Output: wish
    def inner(name):
        if name == 'Python':  # Function definition
            print('Hello', name)  # Function definition
        else:  # Function definition
            fun(name)  # Function definition
    return inner  # Function definition
@decor
def wish(name):
    print('Hi', name)  # Function definition
# End of the function
wish('Python')  # Output: Hello Python
wish('Java')  # Output: Hi Java

# Find outputs(Home work)
def decor(fun):
    def inner(x, y):
        try:  # Function definition
            return fun(x, y)  # Function definition
        except:  # Function definition
            return 'Division by 0 is not permitted'  # Function definition
    return inner  # Function definition
@decor
def div(a, b):
    return a / b  # Function definition
# End of the function
print(div(10, 3))  # Output: 3.3333333333333335
print(div(10, 0))  # Output: Division by 0 is not permitted
print(inner(10, 3))  # Output: NameError: name 'inner' is not defined

# Modify following div function such that div(9, 2) and div(2, 9) should return 4.5 only
def decor(fun):
    def inner(a, b):  # Function definition
        return fun(max(a, b), min(a, b))  # Always divide larger by smaller
    return inner  # Function definition
@decor
def div(a, b):
    return a / b  # Function definition
print(div(9, 2))  # Output: 4.5
print(div(2, 9))  # Output: 4.5

# Find outputs (Home work)
def decor(fun):
    def inner():
        print(F'Decorating {fun . _name_} function')  # Should be __name__ → Output: Decorating f1 function
        fun()  # Function definition
        print('Decoration is finished')  # Function definition
    return inner  # Function definition
@decor
def f1():
    print('Hello')  # Function definition
# End of the function
f1()  # Output: Decorating f1 function → Hello → Decoration is finished
print('Bye')  # Output: Bye

# Most tricky program
# Same decorator to multiple functions with different signatures
def decor(fun):
    print(fun . _name_)  # Should be __name__ → Output: f1, f2, f3, f4 (during decoration)
    def inner(*x):  # * is var-arg parameter
        print(x)  # Prints tuple of arguments → Output: (10,), (25, 10.8), ('Hyd', True, (3+4j)), ()
        fun(*x)  # * unpacks object 'x' → Calls original functions
        print('End of decoration')  # Output: End of decoration (after each function call)
    return inner  # Function definition
@decor
def f1(x):
    print('f1 function : ', x)  # Output: f1 function : 10
@decor
def f2(x, y):
    print('f2 function : ', x, y)  # Output: f2 function : 25 10.8
@decor
def f3(x, y, z):
    print('f3 function : ', x, y, z)  # Output: f3 function : Hyd True (3+4j)
@decor
def f4():
    print('f4 function')  # Output: f4 function
# end of function
f1(10)  # Triggers decorated function call
f2(25, 10.8)  # Triggers decorated function call
f3('Hyd', True, 3 + 4j)  # Triggers decorated function call
f4()  # Triggers decorated function call
