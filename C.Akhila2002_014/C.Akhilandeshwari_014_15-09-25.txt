Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def word_generator(a):
    words = a.split()
    for word in words:
        yield word
a = "Hyd is green city"  
for w in word_generator(a):
    print(w)     

Find  outputs
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

output:
[10 , 20]
<class list>
{30 , 40 , 50}
<class set>
(60 , 70 , 80 , 90)
<class tuple>
100
<class int>

 Find  outputs
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

output:
Begin
1 2 3 4 5 6 7 8 9....
(continues printing upto  100000000000000000000)
(end will never be printed)


 Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)

output:
0 1 4 9 16 25 36 49 64 81 100........
(continues printing squares of all numbers  from 0 upto 499,999,999,999,999,999)

Find  outputs  (Home  work)
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

output:
Before
Hello
.....
Hello(total 11 times)
End of generator 
[10 , 11, 12, 13, 14 , 15 , 16 , 17 ,18 ,19 ,20]
After
error


 Find    outputs (Home  work)
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

output:
one
1
two
2
three
3
End
one
two
three
End
1
2
3

Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()#error
p , q , r , s , m = f1()

 Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))#error
print(g * 3)#error
print(g[0])#error
print(g[1 : 3])#error
print(*g)#1 2 3