'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def fun(s):
    s=s.split()
    for x in s:
        yield x
s=input("Enter the string: ")
g=fun(s)
for x in g:
    print(x)

# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))
#[10 , 20] <class 'list'>
#{30,40,50} <class 'set'>
#(60,70,80,90) <class 'tuple'>
#100 <class 'int'>

#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') #Begin
print(*g) #1 2 3 ... or waiting time /memory error 
print('End')#End

#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)#0 1 4 9 ... or waiting time /memory error 

# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20)
print('Before') #Before
print(list(g)) #[10,11,12,13,14,15,16,17,18,19,20]
print('After')#After
print(next(g))#error

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
g = f1() 
for   m   in   g:
	print(m) #One 1 Two 2 Three 3 End
x ,  y ,  z  =  f1()  
print(x) #1
print(y)#2
print(z)#3

# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() #error, fewer references provides
p , q , r , s , m = f1()#error, has fewer values

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) #error
print(g * 3) #error
print(g[0])#error
print(g[1 : 3])#error
print(*g)#1 2 3