# Find outputs

def outer():
    print('outer function')  # Prints outer function when outer() is called
    def inner():
        return 10            # Returns 10 to the inner()
    return inner             # Returns the inner function itself to the outer()
# End of the function
x = outer()                  # Executes outer(), prints outer function and assigns inner function to x
print(x())                   # Executes inner() through x, returns 10 and prints 10
# print(inner())             # Error inner() is not accessible outside outer()

'''
Outputs:
10
'''


# Find  outputs  (Home  work)

def bold(fun):
    def inner1():
        return '<b>' + fun() + '</b>'  # Adds bold tags to the result from fun()
    return inner1                      # Returns the function inner1

def italic(fun):
    def inner2():
        return '<i>' + fun() + '</i>'  # Adds italic tags to the result from fun()
    return inner2                      # Returns the function inner2

def underline(fun):
    def inner3():
        return '<u>' + fun() + '</u>'  # Adds underline tags to the result from fun()
    return inner3                      # Returns the function inner3

@bold
@italic
@underline
def f1():
    return 'Hello World'               # returns the text

print(f1())                            # Executes the decorated of f1, and prints "<b><i><u>Hello World</u></i></b>"

'''
Outputs:
<b><i><u>Hello World</u></i></b>
'''

'''
 Execution process:
1. underline decorates f1 by adding underline tags "<u>Hello World</u>"
2. italic decorates the result by adding italic tags "<i><u>Hello World</u></i>"
3. bold decorates the result by adding bold tags "<b><i><u>Hello World</u></i></b>"
'''

