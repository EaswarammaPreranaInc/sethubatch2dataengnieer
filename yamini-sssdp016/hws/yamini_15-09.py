'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1(n):
    yield 'Words of String'
    for i in n:
        yield i  
n=input().split()
g=f1(n)
for i in g:
    print(i)

# Find  outputs
def   f1():
        yield   [10 , 20]   # [10,20] is yielded at 1st iteration
        yield  {30 , 40 , 50}   # {30,40,50} is yielded at 2nd iteration
        yield  60  , 70 , 80 , 90   # (60,70,80,90) is yielded at 3rd iteration
        yield  100   # 100 is yielded at 4th iteration
# End  of  generator
g = f1()    # creating empty generator object
for   x   in   g:   # iterating the generator
	print(x)    # [10,20],{30 , 40 , 50},(60,70,80,90),100
	print(type(x))  # class list,class set,class tuple,class int


#  Find  outputs
def   f1():
	x = 1   # x is initalized to 1
	while  x <=  100000000000000000000: # whike condition is true
		yield  x    # all the elements yielded stored in gen object
		x +=  1 # x is uncremented by 1
# End of  generator
g = f1()    # empty generator object
print('Begin')  # prints begin
print(*g)   # stores all the elements in gen object may get memory error and waiting time as it has large number of elements to store
print('End')    # may not be printed due to error


#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))	# empty generator object
print(*g)	# executed the expression stores all elements in generator unpacks and generator becomes empty

# Find  outputs  (Home  work)
def   f1(begin , end):	# 10,20
	while  begin  <=  end:	# while cond is true
			print('Hello')	# prints hello 10 times
			yield  begin
			begin += 1
	print('End  of  generator') # prints end of generator 1 time 
#end of the genrator  function
g = f1(10 , 20)	# empty generaor object
print('Before')	# prints before
print(list(g))	# 1st the total function is  so prints hello 10 times and the result of yield stat are stored as generator which are converyted to list and gen becomes empty
print('After')	# prints after 
#print(next(g))  # error as generator is fully iterated


'''
1) What  are  the  four  events  for  list(g) ?  --->
	a) generator  function  is  fully  executed  without  stoping  in  the  middle  even  though  there  is  yield  statement
	b) All  those  elements  which  are  yielded  are  stored  in  generator  object (Non-empty  object)
	c) generator  object  is  converted  to  list
	d) generator  object  becomes  empty

2) What  are  the  two  drawbacks  of  list(g) ?  --->  a) Waiting  time  when  there  are  too  many  yield  statements
																				   b)  Possibility  of  MemoryError

3) Hence  list(g)  is  not  recommended  for  generator  as  we  are  losing   the  power  of  generator
'''

#  Find    outputs (Home  work)
def      f1():
	print('One')	#1st iteration
	yield    1	# 1 is yielded
	print('Two') 	#2nd iteration
	yield    2 	# 2 is yielded
	print('Three') 	#3rd iteration
	yield    3 	# 3 is yielded
	print('End') 	#4th iteration
# End  of  generator
g = f1() 	# empty generator object is created
for   m   in   g:	# iterating generator fun
	print(m)	# prints 1,2,3,4
x ,  y ,  z  =  f1()  # tuple packing so program is executed 1st adn yield statements result is stored to tuple
print(x)	# prints 1
print(y) 	# prints 2
print(z) # prints 3

# Identify  error (Home  work)
def  f1():	# tuple packing so program is executed 1st adn yield statements 
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()	# result is stored to tuple but it has 3 objects but func has 4 yield statements s
p , q , r , s , m = f1() # error as 5 objects but function has 4 yield statements 

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()	# empty generator object
print(len(g))	# error arg of len function should be sequence
print(g * 3)	# error as repetition is not possible for generator
print(g[0])	# error as generator is empty and has no indexing
print(g[1 : 3])	# error empty objects dosents have slicing
print(*g)	# stores all the elements in gen object and unpacked and printed the result of function adn generator becomes empty
