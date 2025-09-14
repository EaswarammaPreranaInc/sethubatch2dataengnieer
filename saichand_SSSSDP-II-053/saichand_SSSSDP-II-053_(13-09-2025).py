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
print(next(g))			# Stopitteration error
g = f1()
print(next(g))

#Output:
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
<Type and address of generator object>
One
25





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

#Output:
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






#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)

#Output:
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






# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)

#Output:
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

#Output:
0
1
4
9
16
True







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

#Output:
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<Type and address of generator object>
<class 'generator'>







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
print(next(g))				# Stopiteration error

#Output:
10
10
10

10
20
30







#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))			# prints time taken to execute
print(timeit('( x * x   for  x  in  range(500) )'))			# prints time taken to execute








# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))									# prints sizeof the list
print(sys . getsizeof(gen))									# prints sizeof the generator









'''
10.Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements

#Sample output:
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
'''

#Program:
def f1(a, b):
    yield f"Sum : {a + b}"
    yield f"Differnece : {a - b}"
    yield f"Product : {a * b}"
    try:
        yield f"Division : {a / b}"
    except:
        yield "Division by zero is not permitted"
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
for i in f1(a, b):
    print(i)






'''
11.Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object

#Sample output:
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

#Program:
def f1(x, y):
    value = x
    while value <= y:
        yield value
        value += 1
x = int(input("Enter start value : "))
y = int(input("Enter end value : "))
for num in f1(x, y):
    print(num)






'''
12.Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop

#Sample output:
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

#Program:
def fib(x):
    a, b = 0, 1
    while a <= x:
        yield a
        a, b = b, a + b
n = int(input("Enter the last value of fibonacci series:"))
for num in fib(n):
    print(num)
print("End")