
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
#print(next(g)) #error: stop iteration error
g = f1()
print(next(g))
'''
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
<generator object f1 at 0x0000019AB2785FC0>
One
25
'''

# Most  tricky  program
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
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
    print(y)
    time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
    print(y)
    time . sleep(2)
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
# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
    print(y)
    time . sleep(2)
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
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))

d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))

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
<generator object <genexpr> at 0x00000217AFD0A5A0>
<class 'generator'>
'''
#  Find  outputs (Home  work)
def  f1():
    return  10
    return  20
    return  30
def  f2():
    yield  10
    yield  20
    yield  30
# End  of  the  function
print(f1()) #10
print(f1()) #10
print(f1()) #10
print()
g = f2()
print(next(g)) #10 \n 20 \n 30
print(next(g)) #error:stop Iteration error
print(next(g)) #error:stop Iteration error
print(next(g)) #error:stop Iteration error

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''
43.42108259999077
0.5383359999977984
'''
# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
'''
85176
200
'''
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate elements
'''

def operations(a, b):
    yield f"Sum = {a + b}"
    yield f"Difference = {a - b}"
    yield f"Product = {a * b}"
    if b != 0:
        yield f"Division = {a / b}"
    else:
        yield "Division = Not possible (division by zero)"

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

for result in operations(x, y):
    print(result)

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def g(x, y):
    while x <= y:
        yield x
        x += 1  
        
x = int(input("Enter start value: "))
y = int(input("Enter end value: "))

for num in g(x, y):
    print(num)

'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a   
        a, b = b, a + b  
        
n = int(input("Enter number of terms: "))

for term in fibonacci(n):
    print(term, end=" ")




    


