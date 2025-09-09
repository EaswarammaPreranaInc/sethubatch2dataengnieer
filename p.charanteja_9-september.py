# Fibonacci Series: Recursive Function
#Python Recursive Function

def fib(i):  # 'i' is the term number (0-based)
    if i == 0:
        return 0  # 0th term
    if i == 1:
        return 1  # 1st term
    return fib(i-1) + fib(i-2)  # Recursive step

n = int(input('How many terms? : '))
print('Fibonacci series')
for idx in range(n):
    print(fib(idx), end=' ')







# Recursive Power Function
# Python Recursive Function

def power(a, b):
    if b == 0:
        return 1  # base case: anything^0 is 1
    if b > 0:
        return a * power(a, b-1)  # power for positive
    return (1/a) * power(a, b+1)  # power for negative exponent


a = float(input("Enter base: "))
b = int(input("Enter power: "))
print(f"{a}^{b} = {power(a, b)}")







# Recursive Function to Reverse a Number
# Python Recursive Function

from math import log10

def rev(n):
    if n == 0:
        return 0
    length = int(log10(n)) + 1  # length of n
    return (n % 10) * (10 ** (length - 1)) + rev(n // 10)

n = int(input('Enter any number: '))
print('Reverse Number:', rev(n))






# Trace Outputs for Tricky Programs
# Global vs Local Variables with Recursion

#### Program 1

def f1():
    global a
    if a:
        print(a)
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')
a = 3
f1()
print('End')

'''
Output Trace:

3          # a=3
2          # a=2
1          # a=1
0          # a=0
Hello
Hi
0
Bye
Hello
Hi
1
Bye
Hello
Hi
2
Bye
End
'''


#### Program 2

def f1():
    a = 3
    if a:
        print(a)
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')
a = 3
f1()
print('End')
'''
Output:  
Recursion never ends because 'a' is reset to 3 in each call. The function will repeatedly print 3 until maximum recursion depth is exceeded (infinite recursion).
'''





# Tricky Parameter Modifications
## Walrus Operator (:=) in Parameters

def f1(x, y):
    if x > 40:
        return
    x += y
    f1(x, y)
    print(x)
x = 10
f1(x, x := x + 1)
print(x)
'''
- x := x+1` updates x to 11; function call is 'f1(10, 11)'.  
- Recursion: x increases by y (11) in each call until x > 40. Prints in reverse as the stack unwinds: 21, 32, 43  
- Final x outside function is 11.
'''

## Printing at Recursion Entry and Exit

def f1(x):
    print(x)
    if x:
        f1(x-1)
    print(x)
f1(3)
'''
Output:

3
2
1
0
0
1
2
3
'''






## Mutually Recursive Functions

def f1():
    print('f1 function')
    f2()
    print('End of f1 function')
def f2():
    print('f2 function')
    f1()
    print('End of f2 function')
f1()
'''
- Infinite mutual recursion; prints "f1 function", "f2 function", then repeats until maximum recursion depth is reached.
'''

## Function References and Assignments

def f1():
    print('f1 function')
def f2():
    print('f2 function')
f1()
f2()
print(f1 is f2)
f2 = f1
f2()
print(f1 is f2)
f2 = f1()
print(f2)
f2()
'''
Output:

f1 function
f2 function
False
f1 function
True
f1 function
None
'''





## Function References for print, id, len
'''
- Assign `p = print` and call as `p('Hyderabad')`
- If `print = None`, restore by using another reference:  
'''  
p = print
print = None
p('Hello')

'''
- Assign `x = id`; call with `x(25)`  
- Assign `p = len`; call with `p('Hyd')` to get length.
'''





## Function Nesting and Execution Trace

def f1(a):
    def f2():
        return 10
    return f2() + 20 + a
print(f1(30))
'''
Output: 60.

'''

## Inner Functions and Variable Scope

def outer():
    x = 20
    def inner():
        x = 30
        print(x)               # 30 (local x)
        print(globals()['x'])  # 10 (global x)
    inner()
outer()
print('Bye')
'''
Output:  
30  
10  
Bye  
'''

