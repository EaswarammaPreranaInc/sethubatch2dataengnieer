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
print(next(g))              # throws error
g = f1()
print(next(g))


#output
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
print(next(g))              # 25
for  x  in   g:
	print(x)                # 10.8 \n Hyd
print()
for  x  in   f1():
	print(x)                # 25 \n 10.8 \n Hyd
print()
gen = f1()
print(next(gen))            # 25 \n 
for  x  in   f1():
	print(x)                # 25 \n 10.8 \n Hyd
print(next(gen))            # 10.8




#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)
	


# output
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
	


#output
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


#output
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
print(l)                                        # [0,1,4,9,16]
print(type(l))                                  # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)                                        # {0,1,4,9,16}
print(type(s))                                  # <class 'set>

d = {x : x * x    for   x   in   range(5)}
print(d)                                        # {0:0,1:1,2:4,3:9,4:16}
print(type(d))                                  # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)                                        # type and address of generator
print(type(g))                                  # <class 'generator'>




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
print(f1())                                 # 10
print(f1())                                 # 10
print(f1())                                 # 10
print()
g = f2()
print(next(g))                              # 10
print(next(g))                              # 20
print(next(g))                              # 30
print(next(g))                              # error



#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))          # timeit for list 
print(timeit('( x * x   for  x  in  range(500) )'))         # timeit for generator



# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))        # 85176
print(sys . getsizeof(gen))         # 200



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''

def gen(a, b):
    yield f'Sum: {a + b}'
    yield f'Difference : {a - b}'
    yield f'Product : {a * b}'
    try:
        yield f'Division : {a / b}'
    except ZeroDivisionError:
        yield f'Division by zero is not permitted'
n1 = int(input('Enter first number:  '))
n2 = int(input('Enter second number:  '))
g = gen(n1, n2)
for x in g:
    print(x)
	



'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''



def gen(s, e):
    while s <= e:
        yield s
        s += 1
s = int(input('Enter start value:  '))
e = int(input('Enter end value:  '))
g = gen(s, e)
for x in g:
    print(x)
	


'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''



def gen(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
g = gen(10)
n = int(input('Enter the last value of fibonacci series: '))
for x in g:
    print(x)