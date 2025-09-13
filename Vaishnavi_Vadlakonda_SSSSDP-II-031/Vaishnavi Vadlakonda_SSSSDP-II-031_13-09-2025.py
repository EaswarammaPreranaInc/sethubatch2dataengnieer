#  How  to  iterate  generator  with  for  loop
import time
def f1():
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1()
for x in g:
	print(x)
	time . sleep(1)
	print('Hello')
# End  of  for  loop
print('End')
print(g)
print(next(g))
g = f1()
print(next(g))
'''
Outputs
One
25
1sec
Hello
Two
10.8
1sec
Hello
Three
Hyd
1sec
Hello
Four
End
type and address of the generator function
stopiteration Error
'''









# Most  tricky  program
# Find  outputs(Home  work)
import  time
def f1():
	yield 25
	yield 10.8
	yield 'Hyd'
# End  of  generator
g = f1()
print(next(g))
for x in g:
	print(x) # 25<nextline>10.8<nextline>Hyd
print() # prints nothing
for x in f1():
	print(x) # prints 25<nextline>25<nextline>25 infinitely
print() # prints nothing
gen = f1()
print(next(gen)) # 25<nextline>10.8<nextline>Hyd
for x in f1():
	print(x) # prints 25<nextline>25<nextline>25 infinitely
print(next(gen)) # throws stopiteraton error









#Find  outputs (Home  work)
import time
g = (x * x for x in range(5))
for y in g:
	print(y) 
	time . sleep(2)
	print('Hello')
for y in g:
	print(y)
'''
Outputs
0
2sec
Hello
1
2sec
Hello
4
2sec
Hello
9
2sec
Hello
16
2sec
Hello
'''	








# Find  outputs (Home  work)
import time
for y in (x * x for x in range(5)):
	print(y)
	time.sleep(2)
for y in (x * x for x in range(5)):
	print(y)
	time.sleep(2)
'''
Outputs
0
2sec
1
2sec
4
2sec
9
2sec
16
2sec
0
2sec
1
2sec
4
2sec
9
2sec
16
'''	









# Find  outputs(Home  work)
import  time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
	print(y)
	time.sleep(2)
for y in g2:
	print(y)
print(g1 is g2)
'''
Outputs
0
2sec
1
2sec
4
2sec
9
2sec
16
2sec
True
'''
	  








#  Find  outputs (Home  work)
l = [x * x for x in range(5)]
print(l)
print(type(l))

s = {x * x for x in range(5)}
print(s)
print(type(s))

d = {x : x * x for x in range(5)}
print(d)
print(type(d))

g = (x * x for x in range(5))
print(g)
print(type(g))
'''
Outputs
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0:0, 1:1, 2:4, 3:9, 4:16}
<class 'dict'>
0
1
4
9
16
type and address of generator expression
'''









#  Find  outputs (Home  work)
def f1():
	return 10
	return 20
	return 30
def f2():
	yield 10
	yield 20
	yield 30
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
Outputs
10
10
10

10
20
30
stopiteration error
'''









#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x for x in range(500) ]')) # prints time taken for execution, here the execution starts after 500 elements stored in list
print(timeit('( x * x for x in range(500))')) # print time taken for execution, here the execution stsrts without waiting because generator object is always empty









# Prove that there is no memory error for generator
import  sys
list = [x * x for x in range(10000)]
gen = (x * x for x in range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # prints size of list, here the memory requires more because all 10000 elements should be stored
print(sys . getsizeof(gen)) # prints size of generator expression, here it requires no memory because no elements needs to be stored

	  







'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate elements
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
Division  by zero  is not permitted
'''
def f1(a, b):
	yield "Sum =" + str(a+b)
	yield "Difference =" + str(a-b)
	yield "Product =" + str(a*b)
	yield "Division =" + str(a/b)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
g = f1(a, b)
for i in g:
	print(i)
'''
Outputs
Enter first number:10
Enter second number:7
Sum =17
Difference =3
Product =70
Division =1.4285714285714286
'''









'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range object
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
def f1(x, y):
	value = x
	while value <= y:
		yield value
		value += 1
x = int(input("Enter low value:"))
y = int(input("Enter high value:"))
g = f1(x, y)
for i in g:
	print(i)
'''
Outputs
Enter low value:10
Enter high value:20
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









'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What are the first two terms ?  --->  0  and  1

4) Use generator function and for loop
Enter the last value of fibonacci series:10
0
1
1
2
3
5
8
End
'''
def f1(x):
	a = 0
	b = 1
	while a <= x:
		yield a
		a, b = b, a+b
x = int(input("Enter last value of fibonacci series:"))
g = f1(x)
for i in g:
	print(i)
print("End")
'''
Outputs
Enter last value of fibonacci series:10
0
1
1
2
3
5
8
End
'''