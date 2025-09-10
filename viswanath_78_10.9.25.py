q)def  toh(n , p1 , p2 , p3):
if  at  least  one  disk:
How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
How  to  move  disk  from  pole1  to  pole3
How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate
Ans)   # Towers of Hanoi
def toh(n, p1, p2, p3):
    if n > 0:
        toh(n-1, p1, p3, p2) 
        print(f"Move disk {n} from pole {p1} to pole {p3}")
        toh(n-1, p2, p1, p3)
n = int(input("How many disks ? : "))
toh(n, 1, 2, 3)

def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)  # 15
        x = 20
        print(x)  # 20
        x += 5
    print(x)  # 10
    x += 5
    inner()
    print(x)  # 25
outer()
print(x)  # Error: x is not defined outside the function

def outer():
    x = 10
    def inner():
         print(x)  # Error: nonlocal x declared after using x
        nonlocal x
        x = 20
        print(x)  # 20
        x += 5
    print(x)  # 10
    x += 5
    inner()
    print(x)  # 25
# End of outer function
outer()  
 
def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)  # 20
        x += 5
    print(x)  # 10
    x += 5
    inner()
    print(x)  # 15
outer()
print(x)  # 25

def outer():
    def inner():
        nonlocal x
        x = 20
        print(x)  # Error: no variable 'x' in outer scope for nonlocal
    inner()
    print(x)
outer()
print(x)

def outer():
    def inner():
        global x
        x = 20
        print(x)  # 20
        x = x + 5
    # End of inner function
    inner()
    print(x)  # 25
# End of the function
outer()
print(x)  # 25

# Identify Error
def f1():
    nonlocal x  # Error: no variable 'x' in outer scope for nonlocal

def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200
        print(a, b)  # 100 200
    # End of inner function
    print(a, b)  # 10 20
    inner()
    print(a, b)  # 100 20
# end of outer function
outer()

def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    # end of inner function
    f2()
    return x
# End of f1() function
print(f1())  # Hello

def fun():
    x = 10
    def gun():
        x = x + 20
        print(x)  # Error: local variable 'x' referenced before assignment
    # end of inner function
    gun()
# end of outer function
fun()

x = 10
def outer():
    x = 20
    def inner():
        global x
        nonlocal x  # Error: cannot use both global and nonlocal for same variable


def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)  # 10
        f3()
    f2()
f1()


