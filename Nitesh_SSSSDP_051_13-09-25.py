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
#One 25 Two 10.8 Three Hyd Four 
# End  of  for  loop
print('End') #End
print(g) #<class 'generator'> address of g 
print(next(g)) #One 25
g = f1() 
print(next(g)) #One 25

# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) #25
for  x  in   g:
	print(x)
#10.8 Hyd
print()
for  x  in   f1():
	print(x)
# 25 10.8 Hyd
print()
gen = f1()
print(next(gen)) #25
for  x  in   f1():
	print(x)
#25 10.8 Hyd
print(next(gen)) #error

#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
#0 Hello 1 Hello 4 Hello 9 Hello 16 Hello
for  y  in   g:
	print(y) 
#0 1 4 9 16

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
#0 1 4 9 16 
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
#0 1 4 9 16

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
#0 1 4 9 16
for  y  in  g2:
	print(y)
#0 1 4 9 16
print(g1  is  g2)
#True

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) #[0,1,4,9,16]
print(type(l)) #<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) #{0,1,4,9,16}
print(type(s)) #<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0:0,1:1,2:4,3:9,4:16}
print(type(d)) #<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # empty generator object
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
print(f1()) #10
print(f1())#10
print(f1())#10
print()
g = f2()
print(next(g))#10
print(next(g))#20
print(next(g))#30
print(next(g))#error

#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #time taken to excecute this is in 10's of seconds
print(timeit('( x * x   for  x  in  range(500) )')) #for this the execution time is 0.1sec

# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000)) #no memory error
print(sys . getsizeof(list))  #10000
print(sys . getsizeof(gen))#0

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
def fun(a,b):
	print("Sum: ",end='')
	yield a+b
	print("Difference: ",end='')
	yield a-b
	print("Product: ",end='')
	yield a*b
	try:
	    t=a/b
	    print("Division: ",end='')
	    yield t
	except:
		yield "Division by zero is not permitted"
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
g=fun(a,b)
for i in range(4):
	print(next(g))

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def fun(x,y):
    t=x
    while t<=y:
        yield t
        t=t+1
x=int(input("Enter x: "))
y=int(input("Enter y: "))
g=fun(x,y)
try:
    while True:
        print(next(g),end=' ')
except:
    pass


'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
def fun(n):
   x=0 
   yield x 
   y=1 
   yield y 
   for i in range(n):
       t=x+y 
       x=y
       y=t 
       yield t

n=int(input("Enter n: "))  
g=fun(n)
for i in range(n):
    print(next(g))
 