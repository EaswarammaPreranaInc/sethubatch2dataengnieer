#1st program
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

import time
def strtowords(s):
    words=s.split()
    for i in words:
        yield i
    
s=input("Enter any string: ")
g=strtowords(s)
print("Words to the string")
for k in g:
    print(k)
    time.sleep(1)


#2nd program
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
<class'list'>
{30,40,50} in any order as set is unordered
<class'set'>
(60,70,80,90)
<class'tuple'>
100
<class'int'>
'''


#3rd program
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')#Begin
#print(*g)#Memory error,as 100000000000000000000 number of elements cannot be stored at a small amount of time and there is shortage of space 
print('End')#End


#4th program
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000)) #empty generator obj is created
print(*g)#memory error


#5th program
# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20)
print('Before')#Before
print(list(g))
'''
Hello *11
End of generator
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''
print('After')#after
#print(next(g))#error,g obj is fully iterated already once


#6th program
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
'''
One
1
Two
2
Three 
3
End
'''
	
x ,  y ,  z  =  f1()  #One \N Two \n Three
print(x)#1
print(y)#2
print(z)#3


#7th program
# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()#excees values to unpack
#p , q , r , s , m = f1() #fewer elements to unpack


#8th program
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))#error ,there is no function len for generators
#print(g * 3)#error ,generators cannot be repeated
#print(g[0])#error , generators are not indexed
#print(g[1 : 3])#error, generators does not support slicing
print(*g)#1  2  3