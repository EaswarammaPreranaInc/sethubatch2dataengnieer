'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
########### program #########
import time
def f1(n):
    for i in n.split():
        yield i
        time.sleep(1)
        
a = input("Enter string:")
g = f1(a)
print('Words of the string')
for i in g:
    print(i)

Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city


# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x) # [10,20] # {30 , 40 , 50}  # (60  , 70 , 80 , 90)   # 100
	print(type(x)) # <class 'list'> # <class 'set'>   # <class 'tuple'>  # <class 'int'>

#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1() # generator object
print('Begin') # Begin
print(*g) # unpacking elements and storing elements in generator # error
print('End') # End

#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # error


# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello') # Hello..end itimes
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20) # generator object
print('Before') # Before
print(list(g)) # convertion of generator to list
print('After') # after
print(next(g)) # stopiteration


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
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1() # generator object
for   m   in   g:
	print(m) # One 1  Two  2   three  3 end 
x ,  y ,  z  =  f1()  
print(x) # 1
print(y) # 2
print(z) # 3


# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() # too many values
p , q , r , s , m = f1() # not enough values


#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() # generator object
print(len(g)) # error
print(g * 3) # error
print(g[0]) #  1
print(g[1 : 3]) # 2 3
print(*g) # unpack