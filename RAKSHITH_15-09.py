
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city

def wts(s):
    print('Words of the string')
    l=s.split()
    for i in l:
        yield i
s=input('Enter any string : ')
for i in wts(s):
    print(i)

output:-
Enter any string : Hyd is Green City
Words of the string
Hyd
is
Green
City


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


output:-
[10,20]
<class 'list'>
{30,40,50}
<class 'set'>
(60,70,80,90)
<class 'tuple'>
100
<class 'int'>

#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)
print('End')


output:-
Begin
Error memoryerror
End

#  Find  outputs
g = (x * x  for  x  in  range(50000000000))
print(*g)

output:-
Error memoryerror


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


output:-
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
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
After
Error stop iteration


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


output:-
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


# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()
p , q , r , s , m = f1()


output:-
Error Too many values to unpack 
Error not enough values to unpack (expected 5, got 4)


#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))
print(g * 3)
print(g[0])
print(g[1 : 3])
print(*g)


output:-
Error generator object has no attribute len()
Error unsopprted operand type for * generator and int
'generator' object is not subscriptable
'generator' object is not subscriptable
1 2 3


