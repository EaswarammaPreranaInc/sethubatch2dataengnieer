#  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One') # First  time
	yield  25 # First  time
	print('Two') # Second  time
	yield  10.8 # Second  time
	print('Three') # Third  time
	yield  'Hyd' # Third  time
	print('Four') # Fourth  time
# End  of  generator
g = f1() # generator  object
for   x   in   g:
	print(x) # 25  10.8  Hyd
	time . sleep(1) # 1  second  delay
	print('Hello') # Hello  Hello  Hello
# End  of  for  loop
print('End') # End
print(g) # <generator object f1 at 0x000001E2B8C1F700>
print(next(g)) # StopIteration
g = f1() # generator  object
print(next(g)) # One  25


# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1(): # function  object 
	yield  25 # generator  object
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()  # generator  object
print(next(g)) # 25
for  x  in   g:
	print(x) # 10.8  Hyd
print() # blank  line
for  x  in   f1():
	print(x) # 25  10.8  Hyd
print()
gen = f1() # generator  object
print(next(gen)) # 25
for  x  in   f1():
	print(x) # 25  10.8  Hyd
print(next(gen)) # 10.8



#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5)) # generator  object
for  y  in   g:
	print(y) # 0  1  4  9  16
	time . sleep(2) # sleep  for  2  seconds
	print('Hello') # Hello  Hello  Hello  Hello  Hello
for  y  in   g:
	print(y) # No  output


# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0  1  4  9  16
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0  1  4  9  16
	time . sleep(2)


# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y) # 0 1 4 9 16
	time . sleep(2)
for  y  in  g2:
	print(y) # No  output
print(g1  is  g2) # True


#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)] # list  comprehension
print(l) # [0, 1, 4, 9, 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)} # set  comprehension
print(s) # {0, 1, 4, 9, 16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)} # dict  comprehension
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5)) # generator  expression
print(g) # <generator object <genexpr> at 0x000001E2B8C1F700>
print(type(g)) # <class 'generator'>


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
print(f1()) # 10
print(f1()) # 10
print(f1()) # 10
print()
g = f2()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # StopIteration


#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # 17.662891000014497
print(timeit('( x * x   for  x  in  range(500) )')) # 0.45757669999147765


# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)] # list comprehension
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000)) # generator expression
print(sys . getsizeof(list)) # 85176
print(sys . getsizeof(gen)) # 208


'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
########### program #############
def calc(a , b):
    yield a + b
    yield a - b
    yield a * b
    try:
        yield a / b
    except StopIteration:
        pass
    except ZeroDivisionError:
        print('Division  by zero  is  not  permitted')
    

x = int(input('Enter   first  number  :   '))
y = int(input('Enter   second  number  :   '))
g = calc(x, y)

print(F'Sum : {next(g)}')
print(F'Differnece :  {next(g)}')
print(F'Product :  {next(g)}')
print(F'Division : {next(g)}')

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
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
########### program ###########
def  gen(x , y):
    while  x <= y:
        yield  x
        x += 1
a = int(input('Enter  starting  number  :  '))
b = int(input('Enter  ending  number  :  '))
g = gen(a, b)
for  i  in  g:
    print(i , end = ' ')

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
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
########### program ############
def  fib(n):  
    a , b = 0 , 1
    
    while  a < n:
        yield  a
        a , b = b , a + b
        

n = int(input('How many terms ? : '))
g = fib(n)
for  i  in  g:
    print(i)
print('End')

Enter the last value of fibonacci series:10
0
1
1
2
3
5
8
End