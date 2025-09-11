def  f1():
    print('f1  function')  # f1  function
def   f2(fun):
    print('f2  function')  # f2  function
    fun()
    print('Back  to  f2  function')  # Back  to  f2  function
# end of the function
print('Begin')  # Begin
f2(f1)
print('End')  # End

def  f1():
    print('f1  function')  # f1  function
def   f2(fun):
    print('f2  function')  # f2  function
    fun()               # Error line commented: 'NoneType' object is not callable
    print('Back  to  f2  function')  # Back  to  f2  function
# end of the function
print('Begin')  # Begin
f2(f1())  # f1() prints its output first
print('End')  # End

def   outer():
    print('Outer  Function')  # Outer  Function
    def  inner():
        print('Inner function')  # Inner function (will only run if inner() is called)
    return   inner
# End  of  the  function
fun = outer()  
print('Hello')  # Hello
fun() 
print('Bye')  # Bye
inner()  # Error: 'inner' is not defined in global scope

def  outer(x):
    print('Outer  Function')  # Outer  Function  # Outer  Function
    def  inner1():
        print('1st  inner  function')  # 1st  inner  function
    # End  of  inner1
    def  inner2():
        print("2nd  inner  function")  # 2nd  inner  function
    # End  of  inner2
    if   x == 10:
        return  inner1
    else:
        return  inner2
#end of the function
f1 = outer(10)  
f2 = outer(20)  
f1()  
f2()  

def   outer(msg):
    def  inner():
        print(msg)  # Hi  # Hello (depends on which function is called)
    return  inner
# End  of the function
hi_fun = outer('Hi')  
hello_fun = outer('Hello')  
hi_fun()  
hello_fun()  

def   decor(fun):
    print(fun._name_)  # f1
    def   inner():
        return   fun() +  2
    return  inner
@decor
def   f1():
    return  10
# End of the function
print('End')  # End

def   decor(fun):
    def   inner():
        x = fun()
        return   x + 2
    return  inner
def  f1():
    return  10
#end  of  the  function
f1 = decor(f1)  
print(f1())  # 12

def   decor(fun):
    print(fun._name_)  # wish
    def    inner(name):
        if   name  == 'Python':
            print('Hello', name)  # Hello Python (for name == 'Python')
        else:
            fun(name)  # Hi Java (for other names)
    return  inner
@decor
def    wish(name):
    print('Hi', name)
# End  of  the  function
wish('Python')  # Hello Python
wish('Java')    # Hi Java

def   decor(fun):
    def  inner(x, y):
        try:
            return fun(x, y)
        except:
            return 'Division by 0 is not permitted'
    return inner
@decor
def  div(a, b):
    return a / b
# End  of  the  function
print(div(10, 3))  # 3.3333333333333335
print(div(10, 0))  # Division by 0 is not permitted
# print(inner(10, 3))  # Error: 'inner' is not defined in global scope

# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def decor(fun):
    def inner(a, b):
        if a>b:
            return float(a) / float(b)  
        else:
            return float(b) / float(a)
    return inner
@decor
def div(a, b):
    return a / b
print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5

def   decor(fun):
    def   inner():
        print(f'Decorating {fun._name_} function')  # Decorating f1 function
        fun()                                       # Hello
        print('Decoration is finished')            # Decoration is finished
    return  inner
@decor
def   f1():
    print('Hello')  # Hello
# End  of  the  function
f1()  
print('Bye')  # Bye

def   decor(fun):
    print(fun._name_)  # prints function name at decoration time
    def   inner(*x):  # * is var-arg parameter
        print(x)      # prints the arguments as tuple
        fun(*x)       # * unpacks object 'x' to call original function
        print('End of decoration')  # End of decoration
    return  inner
@decor
def   f1(x):
    print('f1 function :', x)  # f1 function : 10
@decor
def   f2(x, y):
    print('f2 function :', x, y)  # f2 function : 25 10.8
@decor
def  f3(x, y, z):
    print('f3 function :', x, y, z)  # f3 function : Hyd True (3+4j)
@decor
def   f4():
    print('f4 function')  # f4 function
# end of function
f1(10)  
# (10,)
# f1 function : 10
# End of decoration
f2(25, 10.8)  
# (25, 10.8)
# f2 function : 25 10.8
# End of decoration
f3('Hyd', True, 3 + 4j)  
# ('Hyd', True, (3+4j))
# f3 function : Hyd True (3+4j)
# End of decoration
f4()  
# ()
# f4 function   
# End of decoration
