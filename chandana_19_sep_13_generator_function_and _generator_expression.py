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
g = f1() # # creates an empty generator object
for   x   in   g: 
	print(x)
	time . sleep(1)
	print('Hello')
# End  of  for  loop
print('End')
print(g)
#print(next(g)) # # stopiteration error
g = f1() # new generator object is created
print(next(g))
'''
o/p:
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
type and address of generator function
one 
25
'''


# find outputs
import time
def f1():
	yield 25
	yield 10.8
	yield 'Hyd'
# end of generator
g=f1()
print(next(g))
for x in g:
	print(x)
print()
for x in f1():
	print(x)
print()
gen=f1()
print(next(gen))
for x in f1():
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
10.8'''


#Find  outputs
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g: # g was already fully in the first loop, the second loop has no elements left.
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
Hello'''



# Find  outputs 
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
'''
o/p:
0
1
4
9
16
0
1
4
9
16'''



# Find  outputs
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2: # generator is already exhausted so, this loop prints nothig
	print(y)
print(g1  is  g2) # g1 and g2 points to same object
'''
0
1
4
9
16
True'''



#  Find  outputs 
l = [x * x   for   x   in   range(5)]
print(l) # [0,1,4,9.16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0,1,4,9.16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0:0,1:1,2:4,3:9,4:16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # type and address of generator function
print(type(g)) # <class 'generator'>



#  Find  outputs
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
g = f2() # creates an empty generator object
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) # stopiteration error
'''
10
10
10

10
20
30'''



#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # give approximate execution time of the statement but the statement is not executed
print(timeit('( x * x   for  x  in  range(500) )')) # give approximate execution time to create an empty generator.



# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # returns size of object in terms of bytes
print(sys . getsizeof(gen)) # returns size of object in terms of bytes