def f1():
    a = 20
    print(a)              # 20
    dict = globals()
    print(dict['a'])      # 11
    a = 30
    dict['a'] = 40
# End of f1() function
a = 10
print(a)                  # 10
a += 1
f1()
print(a)                  # 40

x = 10
def f1():
    print(x)               # 10
    print(globals()['x'])  # 10
# End of the function
f1()

def f1():
    x = 20
    print(x)               # 20
    print(globals()['x'])  # Error: 'x' not defined in global scope
# End of the function
f1()

def f1():
    a = 40
    b = 50
    c = 60
    print(a, b, c)              # 40 50 60
    dict = globals()
    print(dict['a'], dict['b'], dict['c'])  # 10 20 30
    dict['a'] = 100
    dict['b'] = 200
    dict['c'] = 300
def f2():
    print(a, b, c)              # 100 200 300
# End of f2 function
a = 10
b = 20
c = 30
f1()
f2()

def f1():
    x = 20
    print(x)              # 20
def f2():
    global x
    x = 30
    print(x)              # 30
    x += 1                # x becomes 31 globally
def f3():
    global y
    y = 40
    print(y)              # 40
    y += 1                # y becomes 41 globally
def f4():
    x = 50
    global x              # Error: SyntaxError: name 'x' is declared global after assignment in function
# End of the functions
x = 10
print(x)                  # 10
x += 1                     # x becomes 11
f1()
print(x)                  # 11
f2()
print(x)                  # 31
x += 1                     # x becomes 32
f3()
print(y)                  # 41
f4()
print(x)                  # This line will not execute because f4() raises SyntaxError

def f1():
    global a
    a = 20
    print(a)               # 20
    print(globals()['a'])  # 20
    a = 30
# End of the function
a = 10
print(a)                   # 10
f1()
print(a)                   # 30
def f1():
    global a
    print(a)               # Error: 'a' is not defined
    a = 10
    print(globals()['a'])  # 10
    a = 20
    print(a)               # 20
    a = 30
def f2():
    print(a)               # 30
# End of f2 function
f1()
f2()
print(a)                   # 30

def f1():
    global a
    a = 10
    print(a)               # 10
    a = 20
def f2():
    global a
    print(a)               # 20
    a = 30
def f3():
    print(a)               # 30
    globals()['a'] = 40
# End of the functions
f1()
f2()
f3()
print(a)                   # 40

def f1():
    global a
    a = 10
    print(a)               # 10
    a = 20
def f2():
    print(a)               # Error: 'a' referenced before assignment
    a = 30
    print(a)               # not executed because of error
def f3():
    print(a)               # not executed because of error
    globals()['a'] = 40
# End of the functions
f1()
f2()                     # Error occurs here
f3()
print(a)  # not executed because of error

def f1():
    a = 10
    global a               # Error: SyntaxError – cannot declare 'a' global after assignment
    print(a)
    global b
    b = 20  # not executed because of error
# End of f1() function
f1()
print(a)  # not executed because of error
print(b)  # not executed because of error

def f1():
    global a
    print(a)               # 11
    a += 1                 # a becomes 12
def f2():
    global a
    print(a)               # 13
    a += 1                 # a becomes 14
# End of the functions
a = 10
print(a)                   # 10
a += 1                      # a becomes 11
f1()
print(a)                   # 12
a += 1                      # a becomes 13
f2()
print(a)                   # 14

def f1():
    a = 20
    print(a)               # 20
def f2():
    print(a)               # Error: 'a' referenced before assignment
    a += 1
# End of the functions

a = 10
print(a)                   # 10
f1()
a += 1                      # a becomes 11
f2()                        # Error occurs here
print(a)  # not executed because of error

def f1():
    a = 20 # Error: name 'a' is assigned before global declaration
    global a
    print(a)  # not executed because of error
    print(globals()['a']) # not executed because of error
    a = 30
    globals()['a'] = 40  # not executed because of error
# End of f1()
a = 10
print(a)   # 10
a += 1
f1()       
print(a)   # not executed because of error

def f1():
    x = x + 5
# End of f1 function

def f2():
    x = globals()['x'] + 5
    print(x)
# End of f2 function
x = 10
f1()        # Error: local variable 'x' used before assignment
f2()        # not executed because program stops at error
print(x)    # not executed because program stops at error


