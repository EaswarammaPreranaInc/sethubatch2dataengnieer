
# Find outputs (Home work)
def f1():
    print('f1  function')
def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
# end of the function
print('Begin')# Begin
f2(f1)# f2  function \n f1  function \n Back  to  f2  function
print('End')# End


#  Find  outputs  (Home  work)
def f1():
    print('f1  function')
def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
# end of the function
print('Begin')# Begin
f2(f1())# f1  function \n f2  function \n Back  to  f2  function
print('End')# End


#  Find  outputs  (Home  work)
def outer():
    print('Outer  Function')
    def inner():
        print('Inner function')
    return inner
# End of the function
fun = outer()# Outer  Function
print('Hello')# Hello
fun()# Inner function
print('Bye')# Bye
inner()# error


#  Find  outputs  (Home  work)
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
f1 = outer(10)# Outer  Function
f2 = outer(20)# Outer  Function
f1()# 1st  inner  function
f2()# 2nd  inner  function


#  Find  outputs  (Home  work)
def outer(msg):
    def inner():
        print(msg)
    return inner
# End of the function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()# Hi
hello_fun()# Hello


#  Find  outputs  (Home  work)
def decor(fun):
    print(fun.__name__)# f1
    def inner():
        return fun() + 2
    return inner
@decor
def f1():
    return 10
# End of the function
print('End')# End


#  How  to  call  f1()  function  when  @decor  tag  is  missing  
def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner
def f1():
    return 10
# end of the function
f1 = decor(f1)
print(f1())# 12


# Find  outputs(Home  work)
def decor(fun):
    print(fun.__name__)# wish
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
wish('Python')# Hello Python
wish('Java')# Hi Java


# Find  outputs(Home  work)
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
# End of the function
print(div(10, 3))# 3.3333333333333335
print(div(10, 0))# Division   by  0  is  not  permitted
print(inner(10, 3))# error

# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def decor(fun):
    def inner(a, b):
        return 4.5
    return inner
@decor
def div(a, b):
    return a / b
print(div(9, 2))# 4.5
print(div(2, 9))# 4.5


#  Find  outputs (Home  work)
def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function')
        fun()
        print('Decoration  is  finished')
    return inner
@decor
def f1():
    print('Hello')
# End of the function
f1()
print('Bye')# Bye


#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def decor(fun):
    print(fun.__name__)# f1, f2, f3, f4 
    def inner(*x):
        print(x)
        fun(*x)
        print('End  of  decoration')
    return inner
@decor
def f1(x):
    print('f1  function  :  ', x)
@decor
def f2(x, y):
    print('f2  function  :  ', x, y)
@decor
def f3(x, y, z):
    print('f3 function : ', x, y, z)
@decor
def f4():
    print('f4 function')
# end of function
f1(10)# (10,) \n f1  function  :  10 \n End  of  decoration
f2(25, 10.8)# (25, 10.8) \n f2  function  :  25 10.8 \n End  of  decoration
f3('Hyd', True, 3 + 4j)# ('Hyd', True, (3+4j)) \n f3 function :  Hyd True (3+4j) \n End  of  decoration
f4()# () \n f4 function \n End  of  decoration
