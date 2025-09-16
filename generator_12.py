'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1(b):
      Yield b
a= input(" enter a string:")
b= a.split()
g=f1(b)
For y in g
      Print(y)

Enter a string: hello world python
hello
world
python



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
#[10 , 20]
Class gen
{30 , 40 , 50}
Class gen
(60, 70, 80, 90)
Class gen
100
Class gen 




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
#begin
Process continues until the condition is true and unpacks the gen objects 
End



#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
# unpacks the gen objects until the given range and it stores all the elements and then unpacks the objects because of the * 




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
# before 
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
End of generator
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
After




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
#one
1
Two
2
Three
3
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
a , b , c = f1()#error too less objects created 
p , q , r , s , m = f1()#error too many objects created 




#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))# error no len() in generator
print(g * 3)#error no repetition for genarator function 
print(g[0])# no indexing in generator 
print(g[1 : 3])# no slicing in generator
print(*g)#1
2
3