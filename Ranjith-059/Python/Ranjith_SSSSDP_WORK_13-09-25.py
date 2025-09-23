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
# 	time . sleep(1)
	print('Hello')
# End  of  for  loop
print('End')
print(g)
print(next(g))
g = f1()
print(next(g))
#One
#25
#Hello
#Two
#10.8
#Hello
#Three
#Hyd
#Hello
#Four
#End
# <generator objet f1 0x>
# error
#  one  # new genreator object creates
#25

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
# 25
#10.8
#Hyd
#
for  x  in   f1():
	print(x)
print()
# 25
#10.8
#Hyd
#
gen = f1()
print(next(gen))
# 25
for  x  in   f1():
	print(x)
print(next(gen))
# 25
#10.8
#Hyd
#10.8
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
# 0  # g created new object created
# Hello
# 1
# Hello
# 4
# Hello
# 9
# Hello
# 16
# Hello
for  y  in   g:
	print(y)
#A generator can only be traversed once.
# g is already empty generator one time use
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
# 0
# 1
# 4
# 9
#16
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
# 0
# 1
# 4
# 9
#16
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
# 0
# 1
# 4
# 9
# 16
# g2 is empty because g1 is iterate all
for  y  in  g2:
	print(y)
print(g1  is  g2) # True
# no for loop because g2 is empty
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) #[0, 1, 4, 9, 16]
print(type(l)) #<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) #{0, 1, 4, 9, 16}
print(type(s)) #<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) #<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) #<generator object <genexpr> at 0x7ddaaf7e9d80>
print(type(g)) #<class 'generator'>
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
print(f1())  # 10
print(f1()) #10
print(f1()) # 10 
print() # 
g = f2()
print(next(g)) # 10
print(next(g)) #20
print(next(g)) # 30
print(next(g)) # error stopiteration
#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # 20 sec
print(timeit('( x * x   for  x  in  range(500) )')) # 1 sec

import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # 85176
print(sys . getsizeof(gen)) # 200
def calculator(a, b):
    yield f"Sum : {a + b}"
    yield f"Difference : {a - b}"
    yield f"Product : {a * b}"
    if b != 0:
        yield f"Division : {a / b}"
    else:
        yield "Division : Not possible (division by zero)"

# --- Main program ---
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

for result in calculator(a, b):
    print(result)
def my_range(x, y):
    while x <= y:
        yield x
        x += 1

# --- Main program ---
x = int(input("Enter start (x): "))
y = int(input("Enter end (y): "))

for num in my_range(x, y):
    print(num)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# --- Main program ---
n = int(input("Enter how many terms you want: "))

for num in fibonacci(n):
    print(num)
