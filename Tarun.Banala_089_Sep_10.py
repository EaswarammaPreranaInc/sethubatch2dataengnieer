#TARUN BANALA    10-09-2025
# Towers of Hanoi Implementation
def toh(n, p1, p2, p3):
    if n >= 1:
        toh(n-1, p1, p3, p2)  # Move n-1 disks from p1 to p2 using p3
        print(f"{p1} ---> {p3}")  # Move nth disk from p1 to p3
        toh(n-1, p2, p1, p3)  # Move n-1 disks from p2 to p3 using p1

print("Towers of Hanoi with 3 disks:")
toh(3, 1, 2, 3)
"""
Output:
1 ---> 3
1 ---> 2
3 ---> 2
1 ---> 3
2 ---> 1
2 ---> 3
1 ---> 3
"""

# Nested Function with nonlocal
def outer1():
    x = 10
    def inner():
        nonlocal x
        print(x)  # Output: 15
        x = 20
        print(x)  # Output: 20
        x += 5
    print(x)  # Output: 10
    x += 5
    inner()
    print(x)  # Output: 25

print("\nNested Function with nonlocal:")
outer1()
"""
Output:
10
15
20
25
"""

# Nested Function with nonlocal (different order)
def outer2():
    x = 10
    def inner():
        print(x)  # Output: 15
        nonlocal x
        x = 20
        print(x)  # Output: 20
        x += 5
    print(x)  # Output: 10
    x += 5
    inner()
    print(x)  # Output: 25

print("\nNested Function with nonlocal (different order):")
outer2()
"""
Output:
10
15
20
25
"""

# Nested Function with global
def outer3():
    x = 10
    def inner():
        global x
        x = 20
        print(x)  # Output: 20
        x += 5
    print(x)  # Output: 10
    x += 5
    inner()
    print(x)  # Output: 15

print("\nNested Function with global:")
outer3()
print(x)  # Output: 25 (global x)
"""
Output:
10
15
20
15
25
"""

# Error: nonlocal without binding
try:
    def outer4():
        def inner():
            nonlocal x  # Error: no binding for nonlocal 'x' found
            x = 20
            print(x)
        inner()
        print(x)
    outer4()
    print(x)
except Exception as e:
    print(f"\nError case: {e}")

# Nested Function with global (error case)
x = 0  # Define global x first
def outer5():
    def inner():
        global x
        x = 20
        print(x)  # Output: 20
        x = x + 5
    inner()
    try:
        print(x)  # Error: x is not defined in outer scope
    except Exception as e:
        print(f"Error: {e}")

print("\nNested Function with global (error case):")
outer5()
print(x)  # Output: 25 (global x)
"""
Output:
20
Error: name 'x' is not defined
25
"""

# Error: nonlocal not in nested function
try:
    def f1_error():
        nonlocal x  # Error: nonlocal used not in nested function
except Exception as e:
    print(f"\nError case: {e}")

# nonlocal and local variable
def outer6():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200  # This creates a new local variable b
        print(a, b)  # Output: 100 200
    print(a, b)  # Output: 10 20
    inner()
    print(a, b)  # Output: 100 20

print("\nnonlocal and local variable:")
outer6()
"""
Output:
10 20
100 200
100 20
"""

# nonlocal in returned function
def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    f2()
    return x

print("\nnonlocal in returned function:")
print(f1())  # Output: Hello

# Uninitialized variable in inner scope
def fun():
    x = 10
    def gun():
        try:
            x = x + 20  # Error: local variable 'x' referenced before assignment
            print(x)
        except Exception as e:
            print(f"Error: {e}")
    gun()

print("\nUninitialized variable in inner scope:")
fun()
"""
Output:
Error: local variable 'x' referenced before assignment
"""

# global and nonlocal conflict
x = 10
def outer7():
    x = 20
    def inner():
        try:
            global x
            nonlocal x  # Error: cannot be both nonlocal and global
        except Exception as e:
            print(f"Error: {e}")

print("\nglobal and nonlocal conflict:")
outer7()
"""
Output:
Error: name 'x' is nonlocal and global
"""

# Double nonlocal in nested functions
def f1_double():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)  # Output: 10
        f3()
    f2()

print("\nDouble nonlocal in nested functions:")
f1_double()
"""
Output:
10
"""
