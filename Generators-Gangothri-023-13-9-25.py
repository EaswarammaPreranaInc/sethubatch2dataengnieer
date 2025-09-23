#  How  to  iterate  generator  with  for  loop
import  time
def   f1(): #  It  is  generator  function  due  to  yield
	print('One')
	yield  25  #   25  is   returned  to  for  loop  variable  'x'
	print('Two')
	yield  10.8  #    10.8  is   returned  to  for  loop  variable  'x'
	print('Three')
	yield  'Hyd'   #   'Hyd'   is   returned  to  for  loop  variable  'x'
	print('Four')
# End  of  generator
g = f1()  #  Creates  an  empty  generator  object
for  x  in  g:  #  'x'  is  that  element  yielded  by  generator
	print(x)
	time . sleep(1)
	print('Hello')
#  End  of  for  loop
print('End')
print(g)   #  _str_()  method   returns  type  and  address  of  object  'g'
#print(next(g)) #  StopIteration  Error :  Object  'g'  is   fully  iterated
g = f1() # Creates  another  generator  object  i.e.  2nd  object
print(next(g))  #  Prints  'One'  and  yields  25
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
Type  and  address  of  object  'g'
One
25

1) What  are  the  two  ways  to  iterate  a  generator ?  --->  next(g)  in  while  loop and
for  x  in  g:
2) How  to  iterate  a  sequence ?  --->  With  for  loop  only

3) Is  next(sequence)  valid ?  --->  No  becoz  argument  should  be  generator  but  not  sequence

4) Which  is  a  better  approach  to  iterate  a  generator (for  loop  (or)  next()  function ) ?  ---> for  loop   becoz  StopIteration  error  is  internally  handled  by  for  loop

5) How  long  is  for  loop  executed ?  --->  Until  StopIteration  error  is  raised
'''
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()  #  Creates  1st  generator  object
print(next(g))  #  1st  element  of   1st  gen  object  i.e.  25
for  x  in   g:   #  'x'  is  each  element  of  1st  gen  object  'g'  from  2nd  element
	print(x)    #  10.8  <next line>   Hyd  <next line>
print()
for  x  in   f1():  #  Creates  2nd  gen  object  which  is  iterated  with  for  loop  and  'x'  is  each  element  of  2nd   gen  object  from  1st   element
	print(x)   #  25  <next line>   10.8  <next line>  Hyd  <next line>
print()
gen = f1() #  Creates  3rd  gen  object
print(next(gen))  #  1st  element  of  3rd  gen  object  i.e.  25
for  x  in   f1():  #  Creates  4th  gen  object  which  is  iterated  with  for  loop  and  'x'  is  each  element  of  4th   gen  object  from  1st   element
	print(x)     #  25  <next line>   10.8  <next line>  Hyd  <next line>
print(next(gen))  #  2nd  element  of  3rd  gen  object  i.e.  10.8
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
'''
1) How  many  generator  objects  are  in  the  above  program ?  ---> Four
2) Which  objects  are  fully  iterated ?  ---> 1st , 2nd  and  4th  objects
3) How  many  elements  are  remainging  in  3rd  object ?  ---> Only  one  i.e.  Hyd
'''
#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5)) # Creates an empty generator object
for  y  in   g:
	print(y) 
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)
'''Output:
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello'''

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)): # Creates generator
	print(y) # 0 1 4 9 16 in new lines and wait for 2 seconds 
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0 1 4 9 16 in new lines and wait for 2 seconds
	time . sleep(2)


# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y) # 0 1 4 9 16 in new line 
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)# True

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)] # Stores 5 elements in the list
print(l)# [0,1,4,9,16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)} # Stores 5 elements in the set
print(s) # {0,1,4,9,16} in any order
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)} # Stores 5 elements in the set
print(d) # {0:0,1:1,2:4,3:9,4:16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5)) # creates an empty object
print(g) # __str__() method returns type and address of the generator
print(type(g)) # <class 'generator'>

#  Find  outputs (Home  work)
def  f1():
	return  10
	return  20 # Skipped due to return
	return  30 # skipped due to return
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1()) # 10
print(f1()) # 10
print(f1()) # 10
print()
g = f2() # creates an empty generator object
print(next(g)) # Yields first element 10
print(next(g)) # Yields first element 20
print(next(g)) # Yields first element 30
print(next(g)) # stop iteration error :Object 'g' is fully iterated

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # Execution time for storing 500 elements in the list: 17:43 sec
print(timeit('( x * x   for  x  in  range(500) )')) # Execution time for creating an empty generator object: 0.17 sec

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)] # Creates a list
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000)) # creates an empty gen object
print(sys . getsizeof(list)) # 85176 bytes
print(sys . getsizeof(gen)) # 200 bytes

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
import time 
def f1(x,y):
	yield F'Sum: {x+y}'
	yield F'Difference: {x-y}'
	yield F'Product: {x*y}'
	try:
		yield F'Division : {x/y}'
	except:
		yield 'Division by zero is not permitted'
a=eval(input("Enter first number: "))
b=eval(input("Enter second number: "))
g=f1(a,b)
for k in g:
	print(k)
	time.sleep(2)
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
import time
def f1(start, end):
	while start <= end:
		yield start
		start += 1
x=int(input("Enter start value: "))
y=int(input("Enter end value: "))
g=f1(x,y)
for m in g:
	print(m)
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
def fib(x):
	a=0
	yield a
	b=1
	yield b
	c=a+b
	while c<= x:
		yield c
		a=b
		c=a+b
x=int(input("Enter the last value of fibonacci series: "))
if x== 0:
	print(0)
	exit()
g=fib(x)
for term in g:
	print(term)
	time.sleep(0.5)
print('End')