''' 1) Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def words(s):
    list=s.split()
    for i in list:
        yield i
s=input('Enter any string : ')
print('Words of the string')
for i in words(s):
    print(i)

'''
output:
Enter any string : Hyd is Green City
Words of the string
Hyd
is
Green
City
'''



# 2) Find  outputs

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
output:
[10,20]
<class 'list'>
{30,40,50}
<class 'set'>
(60,70,80,90)
<class 'tuple'>
100
<class 'int'>
'''



# 3) Find  outputs

def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')          # Begin
print(*g)               # 1 2 3 4 5 6 7 8.....if generator containing huge number of elements to store it will throws memoryerror
print('End')            # End




# 4) Find  outputs

g = (x * x  for  x  in  range(500000000000000000))
print(*g)               # Error as generator contains huge number of elements to store it will throws memoryerror




# 5) Find  outputs  (Home  work)

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
print(next(g)) # stop iteration error 
'''
output:
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


# 6) Find    outputs (Home  work)

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
output:
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



# 7) Identify  error (Home  work)

def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()            # Error as there are too many elements to unpack 
p , q , r , s , m = f1()    # Error as there are less elements to unpack 




# 8) Find  outputs (Home  work)

def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))   # Error as generator has no len()
print(g * 3)    # Error as generator is empty object hence repeatation is not possible
print(g[0])     # Error as generator is not indexed
print(g[1 : 3]) # Error as generator is not indexed hence slicing is not possible
print(*g)       # Output: 1 2 3
