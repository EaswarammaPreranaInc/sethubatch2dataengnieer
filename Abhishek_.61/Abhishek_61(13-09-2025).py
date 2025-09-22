#1

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
g = f1()    # Empty generator created
for   x   in   g:
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
Output:
--------
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
<class 'Generator'> And address of the object
Stopiteration Error
One
25
'''


#2

# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))  # 25
for  x  in   g:
	print(x)    # 25 <Next Line> 10.8 <Next Line> Hyd
print()
for  x  in   f1():
	print(x)    # 25 <Next Line> 10.8 <Next Line> Hyd
print()
gen = f1()
print(next(gen))   # 25
for  x  in   f1():
	print(x)   # 25 <Next Line> 10.8 <Next Line> Hyd
print(next(gen))   # 25



3

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
Hello'''


4

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)

#Output:
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



5

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
True'''



6

 #  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)            #  [0,1,4,9,16]
print(type(l))      # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)           # {0,1,4,9,16}
print(type(s))     # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)           # {0:1, 1:1, 2:4, 3:9, 4:16}
print(type(d))     # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)           # type and address of the generator
print(type(g))     # <class 'generatorexpression'>



7

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
print(f1())    # 10
print(f1())    # 10
print(f1())    # 10
print()
g = f2()
print(next(g))  # 10 
print(next(g))  # 20
print(next(g))  # 30
print(next(g))  # Error



8

 #  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))


#Output:
'''
13.02329529999406
0.1455798999813851
'''



9

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))


#Output:
'''--------
85176
200'''


10

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''

'''Output:
-------
Enter   first  number  :   10
Enter   second  number  :   7
Sum : 17
Difference :  3
Product :  70
Division : 1.4285714285714286'''

'''Output:
-------
Enter   first  number  :   10
Enter   second  number  :   0
Sum : 10
Difference :  10
Product :  0
Division  by zero  is  not  permitted'''

def calc(a, b):
    yield "Sum", a + b
    yield "Difference", a - b
    yield "Product", a * b
    if b != 0:
        yield "Division", a / b
    else:
        yield "Division", "by zero is not permitted"


x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

for i, j in calc(x, y):
    print(f"{i} : {j}")



11

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''


'''Output:
-------
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
#program:

x=int(input("Enter Starting Number: "))
y=int(input("Enter Ending Number: "))
def f1():
    while True:
        global x
        if x<=y:
            print(x)
            x += 1
        else:
            break
    yield ""
g=f1()
print(next(g))



12

'''
Write  a   generator  to  generate  Fibonacci  series

1) What  is  Fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''

x=int(input("Enter Number: "))
def f1():
    global x
    a = 0
    b = 1
    c = a + b
    print(a)
    while c<x:
       print(c)
       c = a + b  # 1
       a=b
       b = c
    yield "End"
g=f1()
print(next(g))



'''Output:
--------
Enter the last value of Fibonacci series:10
0
1
1
2
3
5
8
End'''