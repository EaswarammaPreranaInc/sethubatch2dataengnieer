                            NAME:M.SAICHARAN                      HOMEWORK
                            DATE:15-09-2025

1.'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city

#Program:
def word_generator(s):
    for word in s.split():
        yield word   
string = input("Enter any string : ")
print("Words of the string")
for w in word_generator(string):
    print(w)



2.# Find  outputs
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

#Output:
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'


3.#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)      				#Memory Error
print('End')

#Output:
Begin



4.#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)				#Memory Error



5.# Find  outputs  (Home  work)
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
print(next(g))#Stop iteration

#Output:
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

6.#  Find    outputs (Home  work)
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

#Output:
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


7.# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()			#Error 
p , q , r , s , m = f1()		#Error



8.#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len				#Error
print(g * 3)				#Error
print(g[0])				#Error
print(g[1 : 3])				#Error
print(*g)				#1 2 3