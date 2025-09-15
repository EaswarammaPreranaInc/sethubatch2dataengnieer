'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

def f1(a):
    a=a.split(' ')
    for i in a:
        yield i

x=input("enter any string: ")
g=f1(x)
print('Words of the string')
for i in g:
    print(i)

'''
o/p:
enter any string: Hyd is green city
Words of the string
Hyd
is
green
city
'''


# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1() # creates an empty generator object
for   x   in   g:
	print(x)
	print(type(x))
'''
o/p:
[10,20]
<class 'list'>
{50,30,40}
<class 'set'>
(60,70,80,90)
<class 'tuple'>
100
<class 'int'>
'''

#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') # Begin
#print(*g) # unpack everything in generator g : it may cause memory error or waiting time
print('End') # End


#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
#print(*g)  #  unpack everything in generator g : it may cause memory error or waiting time



# Find  outputs 
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20) # generater object is created
print('Before')
print(list(g))  # collects all yielded values into a list
print('After')
#print(next(g)) # stopiteration error : generator g is exhausted becoz list(g) consumed it fully

'''
o/p:
Before
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
End  of  generator
[10,11,12,13,14,15,16,17,18,19,20]
After
'''


# Find outputs 
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1() 
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1() 
print(x)
print(y)
print(z)
'''
o/p:
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
'''


# Identify error 
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1() # error: too many values to unpack
#p , q , r , s , m = f1() # error: not enough values to unpack


# Find outputs 
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g)) # generator object has no length
#print(g * 3) # cannot repeat generator object
#print(g[0]) # generator object is not indexed
#print(g[1 : 3]) # generator object cannot be sliced
print(*g) # 1 2 3