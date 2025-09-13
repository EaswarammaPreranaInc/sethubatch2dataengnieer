Dabbiru Sai Harsha Vardhan
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
#print(next(g)) # error
g = f1()
print(next(g))

'''OUTPUT:
One 
25
Hello
two
10.8
Hello
Three
Hyd
Hello
Four
End
type and address of generator function
StopIterationError
One 
25'''




# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) # 25
for  x  in   g:
	print(x) # 10.8 Hyd
print()
for  x  in   f1():
	print(x) # 25 10.8 Hyd
print()
gen = f1()
print(next(gen)) # 25
for  x  in   f1():
	print(x) # 25 10.8 Hyd
print(next(gen)) # 10.8



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
OUTPUT:
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
OUTPUT:
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
print(g1  is  g2) # True
'''
OUTPUT:
0
1
4
9
16
True
'''




#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0,1,4,9,16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0,1,4,9,16} in any order
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0:0,1:1,2:4.3:9,4:16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # type and address
print(type(g)) # <class 'generator'>



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
print(f1()) # 10
print(f1()) # 10
print(f1()) # 10
print()
g = f2()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # error




#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))



# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))




'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
import time
def f1(a,b):
    yield  f'sum = {a+b}'
    yield  f'difference = {a-b}'
    yield  f'product = {a*b}'
    try:
        yield  f'division = {a/b}'
    except:
        print('Division by zero is not permitted')
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
for x in f1(a,b):
    print(x)
    time.sleep(2)




'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
import time

def f1():
    yield 10
    yield 11
    yield 12
    yield 13
    yield 14
    yield 15
    yield 16
    yield 17
    yield 18
    yield 19
    yield 20
    
for x in f1():
    print(x)
    time.sleep(1)




'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
import time
def fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
        
n=int(input("Enter the last value of fibonacci series : "))
for i in fib(n):
    if (i<n):
        print(i)
        time.sleep(1)
print("End")
