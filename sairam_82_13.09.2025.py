#Find Output
import time
def f1():
    print('One')
    yield 25
    print('Two')
    yield 10.8
    print('Three')
    yield 'Hyd'
    print('Four')
# End of generator

g = f1()

for x in g:
    print(x)
    time.sleep(1)
    print('Hello')
# End of for loop

print('End')
print(g)
print(next(g))   #cause error because it is fully exhausted
g = f1()
print(next(g))

'''
Output:
One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
<generator object f1 at 0x000001...>
Traceback (most recent call last):
  ...
StopIteration
'''

#Find output
import time
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator

g = f1()
print(next(g))
for x in g:
    print(x)
print()
for x in f1():
    print(x)
print()
gen = f1()
print(next(gen))
for x in f1():
    print(x)
print(next(gen))

'''
Output:
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8
'''
#Find Output
import time
g = (x * x for x in range(5))
for y in g:
    print(y)
    time.sleep(2)
    print('Hello')

for y in g:
    print(y)

'''
Output:
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello
'''

#Find Output
import time
for y in (x * x for x in range(5)):
    print(y)
    time.sleep(2)

for y in (x * x for x in range(5)):
    print(y)
    time.sleep(2)

'''
Output:
0
1
4
9
16
0
1
4
9
16
'''

#Find Output
import time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)
    time.sleep(2)
for y in g2:
    print(y)
print(g1 is g2)

'''
Output:
0
1
4
9
16
True
'''
#Find Output
l = [x * x for x in range(5)]
print(l)          # [0, 1, 4, 9, 16]
print(type(l))    # <class 'list'>

s = {x * x for x in range(5)}
print(s)          # {0, 1, 4, 9, 16}
print(type(s))    # <class 'set'>

d = {x : x * x for x in range(5)}
print(d)          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d))    # <class 'dict'>

g = (x * x for x in range(5))
print(g)          # <generator object <genexpr> at 0x...>
print(type(g))    # <class 'generator'>


#Find Output

def f1():
    return 10
    return 20
    return 30

def f2():
    yield 10
    yield 20
    yield 30

# End of the function
print(f1())   # 10   (function stops at first return)
print(f1())   # 10
print(f1())   # 10
print()

g = f2()
print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30
print(next(g))  # StopIteration (error, generator exhausted)

#Find Output
from timeit import timeit

print(timeit('[x * x for x in range(500)]'))
print(timeit('(x * x for x in range(500))'))

'''
Output:
20.0...   # list comprehension takes more time (it builds 500 elements)
0.0...    # generator is instant (just builds generator object, no iteration)
'''

import sys

list = [x * x for x in range(10000)]
gen = (x * x for x in range(100000000000000000000000000000000000000000000000))

print(sys.getsizeof(list))  # ~87,000 bytes (depends, but large memory)
print(sys.getsizeof(gen))   # ~112 bytes (very small)


#Program to find sum , difference , product , Division (generator)
def operations(a, b):
    yield f"Sum : {a + b}"
    yield f"Differnece :  {a - b}"
    yield f"Product :  {a * b}"
    if b == 0:
        yield "Division  by zero  is  not  permitted"
    else:
        yield f"Division : {a / b}"

# Driver code
x = int(input("Enter   first  number  :   "))
y = int(input("Enter   second  number  :   "))

for result in operations(x, y):
    print(result)


#Program yield numbers from x to y
def generate_numbers(x, y):
    while x <= y:
        yield x
        x += 1

# Driver code
start = int(input("Enter  start  value :  "))
end = int(input("Enter  end  value :  "))

for num in generate_numbers(start, end):
    print(num)


#Program to write fibnocci series (generator)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Driver code
last = int(input("Enter the last value of fibonacci series:"))
for num in fibonacci(last):
    print(num)
print("End")
