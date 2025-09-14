import  time
def   f1():
	print('One')    # 1st iterations prints one
	yield  25   # yields 25
	print('Two') # 2nd iterations prints two
	yield  10.8 # yields 10.8
	print('Three')# 3rd iterations prints three
	yield  'Hyd'    #yields hyd
	print('Four')   # prints four
# End  of  generator
g = f1()    # empty generator obj is created
for   x   in   g:   # iteration through generator obj on demand
	print(x)    # 25,10.8,hyd
time . sleep(1) # waits for 1 sec
print('Hello')  # prints hello
# End  of  for  loop
print('End')#prints end
print(g)# prints type and adress of g
print(next(g))  # error
g = f1()    # empty generated
print(next(g))  # prints hyd and yields 25

# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()    # empty generator object
print(next(g))  # 1st element of gen g 25
for  x  in   g: # remaining elements of g
	print(x)    # 10.8,hyd
print() # prints nothing
for  x  in   f1():  # new generator obj
	print(x)    # iprints all elements of g 25,10.8,hyd
print() # prints nothing
gen = f1()  # new gen object
print(next(gen))    # 1st elemet of gen 25
for  x  in   f1():  # another new object
	print(x)    # 25,10.8,hyd
print(next(gen))    # 2nd element of gen 10.8

#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))    # empty generator object
for  y  in   g: # now on demand it yields elements
	print(y)    # prints 1,2,9,16,25
	time . sleep(2)
	print('Hello')  # prints hello 5 times
for  y  in   g:
	print(y)    # as already g is iterated nothing is printed

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):  # empty generator is created and each element is called
	print(y)    # prints 1,4,9,16,25
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):  # anpther empty generator is created and each element is called
	print(y)    # prints 1,4,9,16,25
	time . sleep(2)

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5)) # new empty generator object is created
g2 = g1 # g2 points to empty generator g1
for  y  in  g1: # on demand
	print(y)    # yields elements 0,1,4,9,16
	time . sleep(2)
for  y  in  g2: # already yield statements in g1 are completed so nothing is printed
	print(y)    
print(g1  is  g2)   # true as both points to same object

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]   # list is created with 5 elements
print(l)    # prints [0,1,4,9,16]
print(type(l))  # class list

s = {x * x   for   x   in   range(5)}   # set is created with 5 elements
print(s)    # prints {0,1,4,9,16} in any order
print(type(s))  # class set

d = {x : x * x    for   x   in   range(5)}   # dictionary is created with 5 elements
print(d)    # prints {0:0,1:1,2:4,3:9,4:16} 
print(type(d)) #class dict

g = (x * x   for   x   in   range(5)) # empty generator is created
print(g)    # type and adress are printed
print(type(g))  # class generator

#  Find  outputs (Home  work)
def  f1():
	return  10  # returns 10 
	return  20 # remaining return statements are skipped
	return  30
def  f2():
	yield  10   # yields 10 for 1st iteration
	yield  20   # yields 20 for 2nd iteration
	yield  30   # yields 30 for 3rd iteration

# End  of  the  function
print(f1()) #calling f1 function prints 10
print(f1()) # prints 10
print(f1()) # prints 10
print()     # prints nothing
g = f2()    # empty generator object
print(next(g))  # prints 10
print(next(g))  # prints 20
print(next(g))  # prints 30
print(next(g)) # stop iteration error as all yield statemnts are completed

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))  # returns time taken for execution to iterate through the list.list stores all the elements and iterates
print(timeit('( x * x   for  x  in  range(500) )')) # returns time taken for execution to iterate through the generator. on demand generator yields elements

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))    # as all elements are stored in list it takes huge amount of memory
print(sys . getsizeof(gen)) # generator doesnt store elements 

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
def f1(n,m):
    yield n+m
    yield n-m
    yield n*m
    try:
        yield n/m
    except:
        yield 'Division  by zero  is not permitted'
n=int(input())
m=int(input())
for i in f1(n,m):
    print(i)

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def ran(x,y):
    yield x
    if x!=y:
        for v in ran(x+1,y):
            yield v

n=int(input())
m=int(input())
for i in ran(n,m):
    print(i)

'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''

def fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a=b
        b=a+b
n=int(input())

for i in fib(n):
    print(i)



