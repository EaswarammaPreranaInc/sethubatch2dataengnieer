#TARUN BANALA           09-09-2025
#Short and Tricky Programs:

# Program 1
def f1():
    global a
    if a:
        print(a)        # 3 (1st call), 2 (2nd call), 1 (3rd call)
        a = a - 1       # a=2, a=1, a=0
        f1()            # Recursive call, Recursive call, Base case (a=0)
        print('Hello')  # After return: Hello (3rd), Hello (2nd), Hello (1st)
        print('Hi')     # Hi (3rd), Hi (2nd), Hi (1st)
        print(a)        # 0 (3rd), 0 (2nd), 0 (1st)
    print('Bye')        # Bye (4th), Bye (3rd), Bye (2nd), Bye (1st)
a = 3
f1()                    # Initial call
print('End')            # End


# Program 2
def f1():
    a = 3               # Local variable (not global)
    if a:
        print(a)        # 3 (1st), 3 (2nd), 3 (3rd)
        a = a - 1       # a=2 (local), a=2 (local), a=2 (local)
        f1()            # Recursive call, Recursive call, Base case (a=3 truthy but local)
        print('Hello')  # Hello (3rd), Hello (2nd), Hello (1st)
        print('Hi')     # Hi (3rd), Hi (2nd), Hi (1st)
        print(a)        # 2 (3rd), 2 (2nd), 2 (1st)
    print('Bye')        # Bye (4th), Bye (3rd), Bye (2nd), Bye (1st)
a = 3                   # Global a (unused in recursion)
f1()                    # Initial call
print('End')            # End


# Program 3
def f1(x, y):
    if x > 40:          # Base case when x>40
        return
    x += y              # x = x + y
    f1(x, y)            # Recursive call
    print(x)            # Print after return (stack unwinding)
x = 10
f1(x, x := x + 1)       # x=10, y=11 (walrus operator)
print(x)                # x remains 10 (global unchanged)


# Program 4
def f1(x):
    print(x)            # 3, 2, 1, 0
    if x:               # If x not zero
        f1(x - 1)       # Recursive call: f1(2), f1(1), f1(0)
    print(x)            # 0, 1, 2, 3 (after returns)
f1(3)                   # Initial call


# Program 5
def f1():
    print('f1 function')    # f1 function (each call)
    f2()                    # Call f2
    print('End of f1 function') # Never reached due to infinite recursion
def f2():
    print('f2 function')    # f2 function (each call)
    f1()                    # Call f1 (mutual recursion)
    print('End of f2 function') # Never reached
f1()                        # Initial call


# Program 6
def f1():
    print('f1 function')    # f1 function
def f2():
    print('f2 function')    # f2 function
f1()                        # f1 function
f2()                        # f2 function
print(f1 is f2)             # False (different function objects)
f2 = f1                     # f2 now references f1
f2()                        # f1 function (called through f2)
print(f1 is f2)             # True (same object now)
f2 = f1()                   # f1() returns None, so f2 = None
print(f2)                   # None
# f2()                      # Error: None is not callable


# Program 7
p = print                   # p references points to print function
p('Hyderabad')              # Hyderabad (via p)
print = None                # Overwrite print with None
# print('Hello')            # Error: None is not callable
p('Hello')                  # Hello 


# Program 8
x = id                       # x references points to id
print(x(25))                 # Print id of object 25
p = len                      # p references built-in len
print(p('Hyd'))              # Print length of 'Hyd' -> 3
# Output: [id of 25] 3

# Program 9
def f1(a):
    def f2():
        return 10           # f2 always returns 10
    return f2() + 20 + a    # 10 + 20 + a
print(f1(30))               # 10 + 20 + 30 = 60
# Output: 60

# Program 10
def outer():
    print('Outer function')     # Outer function
    def inner1():
        print('1st inner function') # 1st inner function
    def inner2():
        print('2nd inner function') # 2nd inner function
    print('Hi')                 # Hi
    inner2()                    # Call inner2
    print('Hello')              # Hello
    inner1()                    # Call inner1
    print('Back to outer function') # Back to outer function
print('Begin')                  # Begin
outer()                         # Call outer
print('Bye')                    # Bye


# Program 11
x = 10                      # Global x = 10
def outer():
    x = 20                  # Outer local x = 20
    def inner():
        x = 30              # Inner local x = 30
        print(x)            # 30 (inner local)
        print(globals()['x']) # 10 (global x)
    inner()                 # Call inner
outer()                     # Call outer
print('Bye')                # Bye
# Output: 30 10 Bye

# Program 12
x = 10                      # Global x = 10
def outer():
    x = 20                  # Outer local x = 20
    def inner():
        print(x)            # 20 
        print(globals()['x']) # 10 
    inner()                 # Call inner
outer()                     # Call outer
# Output: 20 10

# Program 13
x = 10                      # Global x = 10
def outer():
    def inner():
        print(x)            # 10 
    inner()                 # Call inner
outer()                     # Call outer
# Output: 10
