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
print(next(g))##StopIterationError
g = f1()
print(next(g))
'''#output:
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
<generator object f1 at 0x0000025F2AB8DD90>
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
# print(next(gen))

'''# output:
# 25
# 10.8
# Hyd

# 25
# 10.8
# Hyd

# 25
# 25
# 10.8
# Hyd
# 10.8'''

#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)

'''# output:
# 0
# Hello
# 1
# Hello
# 4
# Hello
# 9
# Hello
# 16
# Hello'''

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
'''
#output:
#  0
# 1
# 4
# 9
# 16
# 0
# 1
# 4
# 9
# 16
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
# output:
# 0
# 1
# 4
# 9
# 16
# True
'''
#Find  outputs (Home  work)
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
output:
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x000002ABC66C64D0>
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
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))
'''
# output
10
10
10

10
20
30
'''

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''
 output:
# 201.41323029994965
# 3.4864033004269004
'''

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))#85176
print(sys . getsizeof(gen))#208

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
def operations(a, b):
    yield "Sum", a + b
    yield "Difference", a - b
    yield "Product", a * b
    if b != 0:
        yield "Division", a / b
    else:
        yield "Division", "Division by zero not allowed"
a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
for op, result in operations(a, b):
    print(f"{op} : {result}")
'''
output:
Enter first number : 5
Enter second number : 10
Sum : 15.0
Difference : -5.0
Product : 50.0
Division : 0.5
'''

def fibonacci(n):
    a =0
    b=1
    for _ in range(n):
        yield a          
        a, b = b, a + b  
n = int(input("Enter how many Fibonacci numbers you want: "))
for num in fibonacci(n):
    print(num)
# output:
# Enter how many Fibonacci numbers you want: 5
# 0
# 1
# 1
# 2
# 3



























