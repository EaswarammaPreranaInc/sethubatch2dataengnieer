# Find outputs (Home work)
def f1():
    a = 20
    print(a)# 20
    dict = globals()
    print(dict['a'])# 11
    a = 30
    dict['a'] = 40
# End of f1() function
a = 10
print(a)# 10
a += 1# a = 11
f1()
print(a)# 40

# Find outputs (Home work)
x = 10
def f1():
    print(x)# 10
    print(globals()['x'])# 10
# End of the function
f1()

# Find outputs (Home work)
def f1():
    x = 20
    print(x)# 20
    print(globals()['x'])   # 10
# End of the function
f1()

# Find outputs (Home work)
def f1():
    a = 40
    b = 50
    c = 60
    print(a, b, c)# 40 50 60
    dict = globals()
    print(dict['a'], dict['b'], dict['c'])   # 10 20 30
    dict['a'] = 100
    dict['b'] = 200
    dict['c'] = 300
def f2():
    print(a, b, c)# 100 200 300
# End of f2 function
a = 10
b = 20
c = 30
f1()
f2()

# global keyword demo program (Home work)
def f1():
    x = 20
    print(x)# 20
def f2():
    global x
    x = 30
    print(x)# 30
    x += 1
def f3():
    global y
    y = 40
    print(y)# 40
    y += 1
def f4():
    x = 50
    global x# error
# End of the functions
x = 10
print(x)# 10
x += 1# x = 11
f1()
print(x)# 11
f2()
print(x)# 31
x += 1# x = 32
f3()
print(y)# 41
f4()# error
print(x)# 32

# Find outputs (Home work)
def f1():
    global a
    a = 20
    print(a)# 20
    print(globals()['a'])# 20
    a = 30
# End of the function
a = 10
print(a)# 10
f1()
print(a)# 30

# Find outputs(Home work)
def f1():
    global a
    print(a)# 10
    a = 10
    print(globals()['a'])# 10
    a = 20
    print(a)# 20
    a = 30
def f2():
    print(a)# 30
# End of f2 function
a = 10
f1()
f2()
print(a)# 30

# Find outputs (Home work)
def f1():
    global a
    a = 10
    print(a)# 10
    a = 20
def f2():
    global a
    print(a)# 20
    a = 30
def f3():
    print(a)# 30
    globals()['a'] = 40
# End of the function
f1()
f2()
f3()
print(a)# 40

# Find outputs (Home work)
def f1():
    global a
    a = 10
    print(a)# 10
    a = 20
def f2():
    print(a)# 20
    a = 30
    print(a)# 30
def f3():
    print(a)# 30
    globals()['a'] = 40
# End of the function
f1()
f2()
f3()
print(a)# 40

# Find outputs (Home work)
def f1():
    a = 10
    global a# error
    print(a)
    global b
    b = 20
# End of f1() function
f1()# error
print(a)# error
print(b)# error

# Find outputs (Home work)
def f1():
    global a
    print(a)# 11
    a += 1
def f2():
    global a
    print(a)# 12
    a += 1
# End of the function
a = 10
print(a)# 10
a += 1# a = 11
f1()
print(a)# 12
a += 1# a = 13
f2()
print(a)# 14

# Find outputs (Home work)
def f1():
    a = 20
    print(a)# 20
def f2():
    print(a)# 10
    a += 1# error
# End of the function
a = 10
print(a)# 10
f1()
a += 1# a = 11
f2()# error
print(a)# 11

# Find outputs (Home work)
def f1():
    a = 20
    global a# error
    print(a)
    print(globals()['a'])
    a = 30
    globals()['a'] = 40
# End of f1() function
a = 10
print(a)# 10
a += 1# a = 11
f1()# error
print(a)# 11

# Find outputs
def f1():
    x = x + 5# error
# End of f1 function
def f2():
    x = globals()['x'] + 5
    print(x)# 15
# End of f2 function
x = 10
f1()# error
f2()
print(x)# 10
