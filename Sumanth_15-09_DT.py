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
#Program
def word_generator(s):
    for word in s.split():
        yield word

st = input("enter any string:")
print("Words of the string")
for word in word_generator(st):
    print (word)


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
	print(type(x)) # 
'''
Output:
[10,20]
<class 'list'>
{30,40,50}
<class 'set'>
60,70,80,90
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
print('Begin')
print(*g)
print('End')
'''
Output:
Begin 
prints all the numbers after are stored in memory
End'''


 #  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
#Output : prints all the elements after storing in memory



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
g = f1() 
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()  
print(x) #1
print(y) #2
print(z) #3
'''
Output:
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



# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() # too many values to unpack
p , q , r , s , m = f1() #too many values to unpack


#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g)) #gen has no length
#print(g * 3) #error  gen is empty 
#print(g[0]) #error it has no index
#print(g[1 : 3]) #indexing is not possible
print(*g) #unpacks elements that are yielded
#Output: 1 2 3
