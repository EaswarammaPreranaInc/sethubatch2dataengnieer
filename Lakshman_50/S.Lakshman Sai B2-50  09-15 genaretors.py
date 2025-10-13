
#===================================================
'''

Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def word_generator(text):
    words = text.split()
    for word in words:
        yield word

text = input("enter: ")
import time
for word in word_generator(text):
    print(word)

#=================================================== Enter  any   string  :  Hyd is green city
'''
enter: Hyd is green city
Hyd
is
green
city
'''
#=================================================== # Find  outputs

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
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''
#=================================================== #  Find  outputs

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
'''
Begin

'''
#=================================================== #  Find  outputs

g = (x * x  for  x  in  range(1000000000000000000000))
print(*g)
# for x in g:
# 	print(x)
'''
Error memory error
'''
#=================================================== # Find  outputs  (Home  work)

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
# print(next(g))
'''
Begin
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
'''

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

#=================================================== #  Find    outputs (Home  work)

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
3
'''
#=================================================== # Identify  error (Home  work)

def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() #Error becoz of less aruguments
p , q , r , s , m = f1() #Error becoz of extra arugument

#=================================================== #  Find  outputs (Home  work)

def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) #generator has no len()
print(g * 3) #unsupported opernd * for gen() and int
print(g[0]) #gen object is not sliceable or indexed
print(g[1 : 3]) ##gen object is not sliceable or indexed 
print(*g)   #1 2 3