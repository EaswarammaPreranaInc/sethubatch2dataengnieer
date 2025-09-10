def toh(n, p1, p2, p3):
    if n > 0:
        toh(n-1, p1, p3, p2)
        print(p1, "--->", p3)   # Moves disk
        toh(n-1, p2, p1, p3)

# toh(3, 1, 2, 3)
n = int(input('How many disks ? :   '))
toh(n, 1, 2, 3)





def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)     # 10
        x = 20
        print(x)     # 20
        x += 5       # now x = 25
    print(x)         # 10
    x += 5           # x = 15
    inner()
    print(x)         # 25
outer()
print(x)             # Error





def outer():
    x = 10
    def inner():
        print(x)     # Error 'x' is used before nonlocal declared
        nonlocal x
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)
outer()





def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)     # 20
        x += 5       # x = 25
    print(x)         # 10
    x += 5           # x = 15
    inner()
    print(x)         # 15 (local x unaffected)
outer()
print(x)             # 25 (global x updated)






def outer():
    def inner():
        nonlocal x   # Error
        x = 20
        print(x)
    inner()
    print(x)
outer()
print(x)





def outer():
    def inner():
        global x
        x = 20
        print(x)     # 20
        x = x + 5    # x = 25
    inner()
    print(x)         # 25 (global x)
outer()
print(x)             # 25




def f1():
    nonlocal x   # Error




def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200   # local b
        print(a, b)   # 100 200
    print(a, b)       # 10 20
    inner()
    print(a, b)       # 100 20
outer()





def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    f2()
    return x
print(f1())   # Hello





def fun():
    x = 10
    def gun():
        x = x + 20    # Error
        print(x)
    gun()
fun()






x = 10
def outer():
    x = 20
    def inner():
        global x
        nonlocal x   # Error





def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)    # 10
        f3()
    f2()
f1()
