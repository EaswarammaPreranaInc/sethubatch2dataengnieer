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
print('End')  #  End
print(g)  #  function name and address
print(next(g))  #  Stop iteration Error
g = f1()
print(next(g))  #  One 25

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
print(next(g))  #  25
for  x  in   g:
	print(x)  #  10.8  'Hyd'
print()
for  x  in   f1():
	print(x)  #  25  10.8  'Hyd'
print()
gen = f1()
print(next(gen))  #  25
for  x  in   f1():
	print(x)  #  25  10.8  Hyd
print(next(gen))  #  10.8



#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)  
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)  #  alraedy yielded so not yielded again
 
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
	print(y)  #  0,1,4,9,16
	time . sleep(2)
for  y  in  g2:
	print(y)  #  Already yielded
print(g1  is  g2)  #  True



#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)  #  [0,1,4,9,16]
print(type(l))  #  class list

s = {x * x   for   x   in   range(5)}
print(s)  #  {0,1,4,9,16}
print(type(s))  #  class set

d = {x : x * x    for   x   in   range(5)}
print(d)  #  {0:0 , 1:1 , 2:4 , 3:9 , 4:16}
print(type(d))  #  class dict

g = (x * x   for   x   in   range(5))
print(g)  #  function name and address
print(type(g))  #  class generator



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
print(f1())  #  10
print(f1())  #  10
print(f1())  #  10
print()
g = f2()
print(next(g))  #  10
print(next(g))  #  20
print(next(g))  #  30
print(next(g))  #  Stop iteration Error


#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))  #  Execution time is 22 seconds
print(timeit('( x * x   for  x  in  range(500) )'))  #  exection time is 0.3 seconds
#  Hence the generator execution is no waiting time


# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))  #  size of list=85176
print(sys . getsizeof(gen))  #  size of generator=200
# Hence Proved  that  there  is  no  memory  error  for  generator


'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements

Enter   first  number  :   10
Enter   second  number  :   7
Sum : 17
Differnece :  3
Product :  70
Division : 1.4285714285714286
'''
import time
def calcy(x,y):
    print("Sum : ",end="")
    yield x+y
    print("Difference : ",end="")
    yield x-y
    print("Product : ",end="")
    yield x*y
    try:
        print("Division : ",end="")
        yield x/y
    except ZeroDivisionError:
        print("Division  by zero  is not permitted")
x=int(input("Enter 1st number : "))
y=int(input("enter a 2nd number : "))

for p in calcy(x,y):
    print(p)
    time.sleep(2)



'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object

Enter  start  value :  10
Enter  end  value :  20
10,11,12,13,14,15,16,17,18,19,20
'''

def calcy(x,y):
    val=x
    while val<=y:
        yield val
        val+=1
x=int(input("Enter start value : "))
y=int(input("enter end value : "))
for k in calcy(x,y):
    print(k)


'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop

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

n=int(input("Enter the last value of fibonacci series : "))
def fib(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
g = fib(n)
for i in g:
    print(i)


