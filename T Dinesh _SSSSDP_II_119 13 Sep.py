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
    print(x)# One \n 25 \n Hello \n Two \n 10.8 \n Hello \n Three \n Hyd \n Hello \n Four
    time.sleep(1)
    print('Hello')
# End of for loop
print('End')# End
print(g)# <generator object>
print(next(g))# error 
g = f1()
print(next(g))# One \n 25

# Most tricky program
# Find outputs(Home work)
import time
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
print(next(g))# 25
for x in g:
    print(x)# 10.8 \n Hyd
print()
for x in f1():
    print(x)# 25 \n 10.8 \n Hyd
print()
gen = f1()
print(next(gen))# 25
for x in f1():
    print(x)# 25 \n 10.8 \n Hyd
print(next(gen))# 10.8


#  Find  outputs (Home  work)
import time
g = (x * x for x in range(5))
for y in g:
    print(y)# 0, 1, 4, 9, 16
    time.sleep(2)
    print('Hello')
for y in g:
    print(y)# error



#  Find  outputs (Home  work)
import time
for y in (x * x for x in range(5)):
    print(y)# 0, 1, 4, 9, 16
    time.sleep(2)
for y in (x * x for x in range(5)):
    print(y)# 0, 1, 4, 9, 16
    time.sleep(2)


#  Find  outputs (Home  work)
import time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)# 0, 1, 4, 9, 16
    time.sleep(2)
for y in g2:
    print(y)# error
print(g1 is g2)# True

# Find outputs (Home work)
l = [x * x for x in range(5)]
print(l)# [0, 1, 4, 9, 16]
print(type(l))# <class 'list'>
s = {x * x for x in range(5)}
print(s)# {0, 1, 4, 9, 16}
print(type(s))# <class 'set'>
d = {x: x * x for x in range(5)}
print(d)# {0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))# <class 'dict'>
g = (x * x for x in range(5))
print(g)# <generator object ...>
print(type(g))# <class 'generator'>


#  Find  outputs (Home  work)
def f1():
    return 10
    return 20
    return 30
def f2():
    yield 10
    yield 20
    yield 30
# End of the function
print(f1())# 10
print(f1())# 10
print(f1())# 10
print()
g = f2()
print(next(g))# 10
print(next(g))# 20
print(next(g))# 30
print(next(g))# error


#  Prove  that  there  is  no  waiting  time  for  generator
from timeit import timeit
print(timeit('[x * x   for  x  in  range(500) ]'))# time for list comp (small value)
print(timeit('( x * x   for  x  in  range(500) )'))# time for generator (smaller)


# Prove  that  there  is  no  memory  error  for  generator
import sys
list = [x * x for x in range(10000)]
gen = (x * x for x in range(100000000000000000000000000000000000000000000000))
print(sys.getsizeof(list))# large
print(sys.getsizeof(gen))# small



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
def calculate(a, b):
    yield f'Sum : {a + b}'
    yield f'Differnece :  {a - b}'
    yield f'Product :  {a * b}'
    if b == 0:
        yield 'Division  by zero  is  not  permitted'
    else:
        yield f'Division : {a / b}'
a = int(input('Enter first number : '))
b = int(input('Enter first number : '))
calculate(a,b)
# Enter first number : 10
# Enter second number : 7
# Output:
# Sum : 17
# Differnece :  3
# Product :  70
# Division : 1.4285714285714286



'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def printing_range(a,b):
    current = a
    while current <= b:
        yield current
        current += 1
a = int(input('Enter start number : '))
b = int(input('Enter end number : '))
printing_range(a,b)
# Enter start value : 10
# Enter end value : 20
# Output: 10 11 12 13 14 15 16 17 18 19 20



'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
def fib(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
n = int(input('Enter the last value of fibonacci series:'))
fib(n)
# Enter the last value of fibonacci series:10
# Output: 0 1 1 2 3 5 8
# End