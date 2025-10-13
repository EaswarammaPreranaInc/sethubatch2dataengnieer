
#================================= #  How  to  iterate  generator  with  for  loop

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
# print(next(g))
g = f1()
# print(next(g))
'''
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
'''
#================================= # Most  tricky  program

# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))
for  x  in   g:
	print(x)
print()
for  x  in   f1():
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))
'''
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
#================================= #Find  outputs (Home  work)

import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(.5)
	print('Hello')
for  y  in   g:
	print(y)
'''
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

#================================= # Find  outputs (Home  work)

import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
'''
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
#================================= # Find  outputs(Home  work)

import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(1)
for  y  in  g2:
	print(y)
print(g1  is  g2)
'''
0
1
4
9
16
True
'''
#================================= #  Find  outputs (Home  work)

l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))
print()
s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))
print()
d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))
print()
g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
'''
[0, 1, 4, 9, 16]
<class 'list'>

{0, 1, 4, 9, 16}
<class 'set'>

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>

<generator object <genexpr> at 0x000001B213A2A4D0>
<class 'generator'>
'''
#================================= #  Find  outputs (Home  work)

def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
10
10

10
20
30
Error becoz there is no next yield to return
'''
#================================= #  Prove  that  there  is  no  waiting  time  for  generator

from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''
17.317439100006595
0.2100190999917686
'''
#================================= # Prove  that  there  is  no  memory  error  for  generator

import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
'''
85176
200
'''
#=================================
'''

Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements

'''

import time
def f1(a,b):
   try:
      sum=a+b
      yield f'sum :{sum}'
      sub=a-b
      yield f'sub : {sub}'
      mul=a*b
      yield f'mul : {mul}'
      div=a/b
      yield f'div : {div}'
   except ZeroDivisionError:
      yield f'Division  by zero  is  not  permitted'

a=int(input("enter the num: "))
b=int(input("enter the num2: "))
for x in f1(a,b):
    print(x)
    time.sleep(.5)

#===============Enter   first  number  :   10
Enter   second  number  :   7

Sum : 17
Differnece :  3
Product :  70
Division : 1.4285714285714286
'''
sum :17
sub : 3
mul : 70
div : 1.4285714285714286
'''

#============= Enter   first  number  :   10
Enter   second  number  :   0

Sum : 10
Differnece :  10
Product :  0
Division  by zero  is  not  permitted
'''
sum :10
sub : 10
mul : 0
Division  by zero  is  not  permitted
'''

#=================================
'''

Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

def my_generator(x, y):
    while x <= y:
        yield x
        x += 1

x = int(input("Enter start: "))
y = int(input("Enter end: "))

for num in my_generator(x, y):
    print(num)

'''
Enter  start  value :  10
Enter  end  value :  20
10
11
12
13
14
15
16
17
18
19
20

'''

#=================================

'''

Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 ,

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''

def fibb(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter num : "))
for num in fibb(n):
    print(num)


'''
Enter num : 10
0
1
1
2
3
5
8
13
21
34
'''
