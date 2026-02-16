# Exploring locals and globals
def f1():
    a = 20
    print(a)
    dict = globals()
    print(dict['a'])
    a = 30
    dict['a'] = 40
a = 10
print(a)
a += 1
f1()
print(a)

Output:

10
20
11
40







# Accessing global variable inside function
x = 10
def f1():
    print(x)
    print(globals()['x'])
f1()
Output:

10
10









# Local and global variable access
x = 10
def f1():
    x = 20
    print(x)
    print(globals()['x'])
f1()

Output:

20
10







# Local, global update and function access
def f1():
    a = 40
    b = 50
    c = 60
    print(a, b, c)
    dict = globals()
    print(dict['a'], dict['b'], dict['c'])
    dict['a'] = 100
    dict['b'] = 200
    dict['c'] = 300
def f2():
    print(a, b, c)
a = 10
b = 20
c = 30
f1()
f2()

Output:

40 50 60
10 20 30
100 200 300





# global keyword demo program
def f1():
    x = 20
    print(x)
def f2():
    global x
    x = 30
    print(x)
    x += 1
def f3():
    global y
    y = 40
    print(y)
    y += 1
x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1
f3()
print(y)

Output:

10
11
20
11
30
31
41






# global and function update sequence
def f1():
    global a
    a = 20
    print(a)
    print(globals()['a'])
    a = 30
a = 10
print(a)
f1()
print(a)

Output:

10
20
20
30





# complex global/local mix and sequencing
def f1():
    global a
    print(a)
    a = 10
    print(globals()['a'])
    a = 20
    print(a)
    a = 30
def f2():
    print(a)
f1()
f2()
print(a)

Output:

NameError






# sequence of global changes and globals update
def f1():
    global a
    a = 10
    print(a)
    a = 20
def f2():
    global a
    print(a)
    a = 30
def f3():
    print(a)
    globals()['a'] = 40
f1()
f2()
f3()
print(a)

Output:

10
20
30
40







# local/global, print, assignment
def f1():
    global a
    a = 10
    print(a)
    a = 20
def f2():
    print(a)
    a = 30
    print(a)
def f3():
    print(a)
    globals()['a'] = 40
f1()
f2()
f3()
print(a)

Output:

10
UnboundLocalError







# invalid use of global with local assignment
def f1():
    a = 10
    global a
    print(a)
    global b
    b = 20
f1()
print(a)
print(b)

Output:

SyntaxError







# globals and in-function increment
def f1():
    global a
    print(a)
    a += 1
def f2():
    global a
    print(a)
    a += 1
a = 10
print(a)
a += 1
f1()
print(a)
a += 1
f2()
print(a)

Output:

10
11
12
13
14
