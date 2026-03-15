# home works on 13/09/2025 questions


--------------------------------------------
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
print(next(g)) # stop iteration because no more generator are there to return and it is empty object
g = f1()
print(next(g))
---------
#outputs
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
Traceback (most recent call last):
  ...
StopIteration

-------------------------------------
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1() # creates an object g 
print(next(g)) # yields 25 
for  x  in   g: # yields 10.8 and hyd
	print(x) # prints 10.8 and hyd
print() 	# blank is printed
for  x  in   f1(): # creates a new generator which iterates the yields and print 
	print(x)  # prints 25,10.8 , hyd
print() # nothing except blank
gen = f1() # new generator created 
print(next(gen)) # yields 25 
for  x  in   f1(): # new generator values iterates i.e are 25 ,10.8,hyd
	print(x) # 25 ,10.8,hyd
print(next(gen)) # 10.8
-------
#outputs
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

-----------------------------------------
#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5)) # generator is an empty object 
for  y  in   g:
	print(y) # prints the squares of the 1,2,3,4
	time . sleep(2)
	print('Hello') # hello is printed 
for  y  in   g:
	print(y) # for every square of the generator range it prints 

----------

#outputs
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

-----------------------------------
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)

#outputs
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

-----------------------------
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


#outputs
0
1
4
9
16
True

-------------------------------

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


#outputs
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x7f...>
<class 'generator'>


-------------------------------

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
print(next(g))


-------
#outputs
10
10
10

10
20
30
StopIteration

-------------------------------------

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))

#
0.022341
0.000002

---------------------------------

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))

#outputs

87624   # memory taken by list of 10,000 items
112     # memory taken by generator (tiny, constant)
List --> memory grows with number of items.
Generator --> memory stays small (constant size).

------------------------------------
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
Enter   first  number  :   10
Enter   second  number  :   7
Sum : 17
Differnece :  3
Product :  70
Division : 1.4285714285714286

Enter   first  number  :   10
Enter   second  number  :   0
Sum : 10
Differnece :  10
Product :  0
Division  by zero  is  not  permitted
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#outputs

# Write a generator to yield sum, difference, product and division of 2 numbers

def calc_generator(a, b):
    yield f"Sum : {a + b}"
    yield f"Differnece : {a - b}"
    yield f"Product : {a * b}"
    if b == 0:
        yield "Division by zero is not permitted"
    else:
        yield f"Division : {a / b}"

# Driver code
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

for result in calc_generator(a, b):
    print(result)


-------------------------------------

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
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


---
'''
Design a generator to yield from x (may be 10) to y (may be 20)

Hint: Use generator function and for loop
Hint: Do not use range object
'''

def num_generator(start, end):
    while start <= end:   # loop manually without using range()
        yield start
        start += 1

# Driver code
x = int(input("Enter start value : "))
y = int(input("Enter end value : "))

for n in num_generator(x, y):
    print(n)

--------------------------------------------


'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
Enter the last value of fibonacci series:10
0
1
1
2
3
5
8
End

#outputs

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Driver code
last = int(input("Enter the last value of fibonacci series: "))
for num in fibonacci(last):
    print(num)
print("End")

--------------------------
