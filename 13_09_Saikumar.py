#  How  to  iterate  generator  with  for  loop

import  time
def   f1():
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
# End  of  for  loop
print('End')
print(g)
#print(next(g))
g = f1()
print(next(g))

'''
Outputs:

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
<generator object f1 at 0x7daa5ce9dd80>
One
25
'''


# Most  tricky  program
# Find  outputs(Home  work)

def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End  of  generator
g = f1()
print(next(g))         # 25
for x in g:
    print(x)           # 10.8, Hyd
print()
for x in f1():
    print(x)           # 25, 10.8, Hyd
print()
gen = f1()
print(next(gen))       # 25
for x in f1():
    print(x)           # 25, 10.8, Hyd
print(next(gen))       # 10.8

'''
Outputs:

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


#Find  outputs (Home  work)

import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in g:
	print(y)
	
'''
Outputs:

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


# Find  outputs (Home  work)

import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
# Output: 0 1 4 9 16

for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time.sleep(2)
# Output: 0 1 4 9 16
	
'''
Outputs:

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


# Find  outputs(Home  work)

import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
# Output: 0 1 4 9 16
for  y  in  g2:
	print(y)
print(g1 is g2) # True

'''
Outputs:

0
1
4
9
16
True
'''


#  Find  outputs (Home  work)

l = [x * x for x in range(5)]
print(l)          # [0, 1, 4, 9, 16]
print(type(l))    # <class 'list'>

s = {x * x for x in range(5)}
print(s)          # {0, 1, 4, 9, 16}
print(type(s))    # <class 'set'>

d = {x: x * x for x in range(5)}
print(d)          # {0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))    # <class 'dict'>

g = (x * x for x in range(5))
print(g)          # <Type and address>
print(type(g))    # <class 'generator'>


#  Find  outputs (Home  work)

def f1():
    return 10
    return 20
    return 30
def f2():
    yield 10
    yield 20
    yield 30
# End  of  function
print(f1())       # 10
print(f1())       # 10
print(f1())       # 10
g = f2()
print(next(g))    # 10
print(next(g))    # 20
print(next(g))    # 30
print(next(g))    # Error there no more functions

'''
Outputs:

10
10
10
10
20
30
'''


#  Prove  that  there  is  no  waiting  time  for  generator

from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))       # 30.0
print(timeit('( x * x   for  x  in range(500) )'))       # 0.003


# Prove  that  there  is  no  memory  error  for  generator

import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))         # 87624
print(sys . getsizeof(gen))          # 112


'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate elements
'''

def calculator(a, b):
    yield "Sum : " + str(a + b)
    yield "Difference : " + str(a - b)
    yield "Product : " + str(a * b)
    if b != 0:
        yield "Division : " + str(a / b)
    else:
        yield "Division by zero is not permitted"

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
for result in calculator(a, b):
    print(result)


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range object
'''

def ele(x, y):
    while x <= y:
        yield x
        x += 1

start = int(input("Enter start value : "))
end = int(input("Enter end value : "))
for i in ele(start, end):
    print(i)


'''
Write  a   generator  to  generate  fibonacci  series
1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....
2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term
3) What  are  the  first  two  terms ?  --->  0  and  1
4) Use  generator  function  and for loop
'''

def fib(n):
    a, b = 0, 1
    yield a
    if n > 1:
        yield b
    for _ in range(2, n):
        a, b = b, a + b
        yield b

last = int(input("Enter the last value of fibonacci series: "))
for num in fib(last):
    print(num)
print("End")


