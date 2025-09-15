#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1(string):
    a=string.split()
    for i in a:
        yield i
        
a=input("enter any string: ")
for i in f1(a):
    print(i)
    

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
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') #Begin
print(*g) #error
print('End') #  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) #error# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator') #End  of  generator
#end of the genrator  function
g = f1(10 , 20)
print('Before') #Before
print(list(g)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('After') #After
print(next(g)) #error
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
3
'''# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() #error 
p , q , r , s , m = f1() #error#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) #error 
print(g * 3) #Error
print(g[0]) #error
print(g[1 : 3]) #error
print(*g) # 1 2 3
# In[ ]:




