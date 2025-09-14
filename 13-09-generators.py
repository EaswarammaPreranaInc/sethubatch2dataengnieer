# How to iterate generator with for loop
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

'''
print('End')                      #End


print(g)                          # <generator object f1 at ...>
print(next(g))                    # error
g = f1()
print(next(g))                    # One \n 25


# Most tricky program

def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
print(next(g))                           # 25
for x in g:
    print(x)                             # 10.8 \n Hyd
print()
for x in f1():
    print(x)                             # 25 \n 10.8 \n Hyd
print()
gen = f1()
print(next(gen))                         # 25
for x in f1():
    print(x)                             # 25 \n 10.8 \n Hyd
print(next(gen))                         # 10.8


# Generator exhausted case
g = (x * x for x in range(5))
for y in g:
    print(y)                            # 0 1 4 9 16
    time.sleep(2)
    print('Hello')                      # Hello after each number
for y in g:
    print(y)                            # (nothing, generator exhausted)


# Fresh generator each time
for y in (x * x for x in range(5)):
    print(y)                            # 0 1 4 9 16
    time.sleep(2)
for y in (x * x for x in range(5)):
    print(y)                            # 0 1 4 9 16
    time.sleep(2)


# Shared generator reference
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)                           # 0 1 4 9 16
    time.sleep(2)
for y in g2:
    print(y)                           # (nothing, already exhausted)
print(g1 is g2)                        # True


# List, Set, Dict, Generator comprehension
l = [x * x for x in range(5)]
print(l)                               # [0, 1, 4, 9, 16]
print(type(l))                         # <class 'list'>

s = {x * x for x in range(5)}
print(s)                               # {0, 1, 4, 16, 9} (unordered)
print(type(s))                         # <class 'set'>

d = {x: x * x for x in range(5)}
print(d)                               # {0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))                         # <class 'dict'>

g = (x * x for x in range(5))
print(g)                               # <generator object ...>
print(type(g))                         # <class 'generator'>


# Return vs Yield
def f1():
    return 10
    return 20
    return 30

def f2():
    yield 10
    yield 20
    yield 30
# End of the function
print(f1())                                    # 10
print(f1())                                    # 10
print(f1())                                    # 10
print()
g = f2()
print(next(g))                                 # 10
print(next(g))                                 # 20
print(next(g))                                 # 30
print(next(g))                                 # error


# Prove no waiting time for generator
from timeit import timeit
print(timeit('[x * x for x in range(500)]'))   # Slightly bigger time
print(timeit('(x * x for x in range(500))'))   # Much smaller time


# Prove no memory error for generator
import sys
list = [x * x for x in range(10000)]
gen = (x * x for x in range(10**50))
print(sys.getsizeof(list))                     # Larger 
print(sys.getsizeof(gen))                      # Just small byte



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''

# Generator for sum, difference, product, division
def calc_ops(a, b):
    yield f"Sum : {a + b}"
    yield f"Difference : {a - b}"
    yield f"Product : {a * b}"
    if b != 0:
        yield f"Division : {a / b}"
    else:
        yield "Division by zero is not permitted"

for result in calc_ops(10, 7):
    print(result)

'''
Output:
Sum : 17
Difference : 3
Product : 70
Division : 1.4285714285714286
'''

for result in calc_ops(10, 0):
    print(result)
'''
Output:
Sum : 10
Difference : 10
Product : 0
Division by zero is not permitted
'''

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

# Generator to yield numbers from x to y (without range)
def gen_range(x, y):
    while x <= y:
        yield x
        x += 1

for num in gen_range(10, 20):
    print(num)                                    # Output: 10 11 12 13 14 15 16 17 18 19 20



'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''


# Fibonacci generator
def fibo_gen(n):
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        if b > n:
            break
        yield b

for val in fibo_gen(10):
    print(val)
print("End")
'''
Output:
0
1
1
2
3
5
8
End
'''
