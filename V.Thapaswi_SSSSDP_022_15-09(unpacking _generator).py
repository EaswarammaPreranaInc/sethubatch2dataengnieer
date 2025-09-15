'''
1) Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
string = input("Enter a string:")
def words(string):
   print("words of strings")
   for word in string.split():
      yield word

g = words(string)
for i in g:
    print(i)
'''
Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city
''' 
#2)  Find  outputs
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
[10 , 20]
<class 'list'>
{30 , 40 , 50}
<class 'set'>
(60  , 70 , 80 , 90)
<class 'set'>
100
<class 'int'>
'''
# 3) Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)     #  Memory error
print('End')

# 4)  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)             #Memory error

#5) Find  outputs  
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
[10,11,12,13,14,15,16,17,18,19,20]
After
'''



# 6)  Find    outputs 
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

# 7) Identify  error 
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()    # too many values to unpack
p , q , r , s , m = f1() #  here generator yielding 4 values expected 5


 # 8)  Find  outputs 
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))  # there is no length for generator
print(g * 3)  # not mutliplication
print(g[0])  # generator is always empty index not possible
print(g[1 : 3])  # there is no index slicing not possible
print(*g) # 1 2 3