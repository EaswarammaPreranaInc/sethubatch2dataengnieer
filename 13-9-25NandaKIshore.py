#Nanda Kishore Vemula
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
print(next(g)) #Error
g = f1()
print(next(g)) 
'''
one
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
Type and Address of Generator
one 
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
'''
[0, 1, 4, 9, 16]
<class 'list'>
'''
s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))
'''
{0, 1, 4, 9, 16}
<class 'set'>
'''
d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))
'''
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
'''
g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
'''
<generator object <genexpr> at 0x7afbe73ddd80>
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
print(next(g))
'''
10
10
10

10
20
30
Error
'''

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #Prints current execution time(takes more time)
print(timeit('( x * x   for  x  in  range(500) )'))#Prints current execution time(takes less time)

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) #memory used by list to hold all values
print(sys . getsizeof(gen)) #memory used by generator object which doesn't store any values

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
#Program
def cal(a,b):
    print("Sum :" ,end=" ")
    yield a+b
    print("difference :" ,end=" ")
    yield a-b
    print("Product :" ,end=" ")
    yield a*b
    print("division :", end=" ")
    yield a/b
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
try:
    g=cal(a,b)   
    for i in g:
        print(i)
except:
    print("division by Zero not permitted")

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
#Program
def gen(x, y):
    while x <= y: 
        yield x     
        x += 1      
for num in gen(10, 20):
    print(num, end=" ")

'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
#Program
def gen(n):
    fl=0
    f2=1
    f3=0
    while(f3<n):
        yield f3
        f1=f2
        f2=f3
        f3=f1+f2
for i in gen(10):
    print(i)
        