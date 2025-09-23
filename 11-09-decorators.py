# Find outputs (Home Work)
# ================================

def f1():
    print('f1  function')

def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')

print('Begin')                               #Begin
f2(f1)                                       #f2 function #f1 function #back to f2 function   
print('End')                                 #End

# --------------------------------

def f1():
    print('f1  function')

def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')

print('Begin')                            #Begin
#f2(f1())                                  #f1 function #f2 function #error
print('End')                              #End
 
# --------------------------------

def outer():
    print('Outer  Function')
    def inner():
        print('Inner function')
    return inner

fun = outer()                                     #Outer function   
print('Hello')                                    #hello
fun()                                             #Inner function
print('Bye')                                      #Bye
inner()                                           #Error

# --------------------------------

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

f1 = outer(10)                                 #Outer function
f2 = outer(20)                                 #outer function
f1()                                           #1st inner function
f2()                                           #2nd inner function

# --------------------------------

def outer(msg):
    def inner():
        print(msg)
    return inner

hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()                                     #Hii
hello_fun()                                  #Hello

# --------------------------------

def decor(fun):
    print(fun.__name__)                         #f1
    def inner(): 
        return fun() + 2
    return inner

@decor
def f1():
    return 10         

print('End')                                  #End

# --------------------------------

def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner

def f1():
    return 10

f1 = decor(f1)
print(f1())                                #12

# --------------------------------

def decor(fun):
    print(fun.__name__)                           #Wish
    def inner(name): 
        if name == 'Python':
            print('Hello', name)                  #Hello python
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print('Hi', name)                             #Hi java

wish('Python')
wish('Java')

# --------------------------------

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

print(div(10, 3))                 #3.33333333
print(div(10, 0))                 #Division by 0 is not permitted
print(inner(10, 3))               #error

# --------------------------------

# Modify following div function such that div(9,2) and div(2,9) should return 4.5 only
def decor(fun):
    def inner(a, b):
        return 4.5
    return inner

@decor
def div(a, b):
    return a / b

print(div(9, 2))                            #4.5
print(div(2, 9))                            #4.5

# --------------------------------

def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function')             #Decorating f1 function
        fun()                                                    #hello
        print('Decoration is finished')                          #decoration is finished
    return inner

@decor
def f1():
    print('Hello')

f1()
print('Bye')                                                    #bye

# --------------------------------

def decor(fun):
    print(fun.__name__)
    def inner(*x):   # var-arg parameter
        print(x)
        fun(*x)      # unpack tuple x
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
