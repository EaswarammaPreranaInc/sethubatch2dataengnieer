#  BATHINI RAJU SSSSDP 103



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
'''
[10,20]
class<'list'>
{30,40,50}
class<'set'>
(60 ,70 ,80 ,90)
class<'tuple'>
100
class <int'>'''


#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g) # 
print('End')
'''
Begin
may cause memory error for storing that much values

'''


#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # Memory error for storing that much values

# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20)
print('Before')
print(list(g))
print('After')
print(next(g))
'''
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
End  of  generator
[10,11,12,13,14,15,16,17,18,19,20]
After
Error(Stop iteration Error)

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
g = f1() 
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()  
print(x)
print(y)
print(z)
'''
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
3 '''


# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() #Error to many values in generator   but less references
p , q , r , s , m = f1()# Error less values in generator   but more  references



#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) #Error
print(g * 3) #Error
print(g[0]) #Error
print(g[1 : 3]) #Error
print(*g) #1 2 3


# PROGRAM

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city
'''


def div(s):
    for i in s.split():
        yield i
        
n=input("Enter any string :") # Hyd is green city
g=div(n)
for i in g:
    print(i) # Hyd
             # is   
             # green
             # city
