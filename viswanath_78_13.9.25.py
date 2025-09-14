import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))  # 25
for  x  in   g:
	print(x)    # 10.8
	                # Hyd
print() # (prints a blank line)
for  x  in   f1():
	print(x # 25
	            # 10.8
	            # Hyd
print() # (prints a blank line)
gen = f1()
print(next(gen))  # 25
for  x  in   f1():
	print(x)  # 25
	              # 10.8
	              # Hyd
print(next(gen))  # 10.8

import time
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
print(next(g))
g = f1()
print(next(g))
outputs:
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
<generator object f1 at 0x...>
# Error: generator already exhausted
One
25

import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
    print(y)
    time . sleep(2)
    print('Hello')
for  y  in   g:
    print(y) # (nothing printed in second loop because generator is already exhausted)
outputs:
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

import  time
for  y  in   (x * x   for    x    in    range(5)):
    print(y) 
    time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
    print(y)
    time . sleep(2)
outputs:
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

import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
    print(y) # 0
    # 1
    # 4
    # 9
    # 16
    time . sleep(2)
for  y  in  g2:
    print(y) # (nothing printed in second loop because generator is already exhausted)
print(g1  is  g2) # True

l = [x * x   for   x   in   range(5)]
print(l)        # [0, 1, 4, 9, 16]
print(type(l))  # <class 'list'>
s = {x * x   for   x   in   range(5)}
print(s)        # {0, 1, 4, 16, 9}
print(type(s))  # <class 'set'>
d = {x : x * x    for   x   in   range(5)}
print(d)         # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d))   # <class 'dict'>
g = (x * x   for   x   in   range(5))
print(g)        # <generator object <genexpr> at 0x...>
print(type(g))  # <class 'generator'>

def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())  # 10
print(f1())  # 10
print(f1())  # 10
print()      # (prints a blank line)
g = f2()
print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30
print(next(g))  # Error: StopIteration (no more values to yield)

from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # 22.300202821999846
print(timeit('( x * x   for  x  in  range(500) )')) # 0.2831848460045876
# Generator created instantly, no waiting time for values

import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # 85176
print(sys . getsizeof(gen)) # 200 # Generator uses minimal memory → no memory error

q)'''Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate  elements'''
Ans)  import  time
def f1(a,b):
    try:
        yield f'sum of {a}+{b} = {a+b}'
        yield f'difference of {a}-{b} = {a-b}'
        yield f'product of {a}*{b} = {a*b}'
        yield f'division of {a}/{b} = {a/b}'
    except:
        print('division by 0 not permitted')
a = int(input('Enter the first input : '))
b = int(input('Enter the second input : ')) 
gen = f1(a,b)
for x in gen:
    print(x)
    time.sleep(1)

q)'''Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range  object'''
Ans)  import time
def f1(a,b):
if a > b:
        yield "Invalid input: start is greater than end"
    else:
        while a < b:
            yield a
            a += 1
            time.sleep(1)
         yield b
a = int(input('Enter the start value : '))
b = int(input('Enter the end value : ')) 
gen = f1(a,b)
for x in gen:
    print(x)

'''Write  a   generator  to  generate  fibonacci  series
1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....
2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term
3) What  are  the  first  two  terms ?  --->  0  and  1
4) Use  generator  function  and  for  loop'''
import  time
def f1(i):
    a=0
    b=1
    yield a 
    yield b
    while a+b<i:
        c = a+b
        yield c
        a=b
        b=c
i = int(input('Enter the last value of fibonacci series : '))
gen = f1(i)
for x in gen:
    print(x)
    time.sleep(2)



