'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series
'''
def  fib(i):  
	if  i==0:
		return  0
	if  i==1:
		return  1
	return  fib(i-1) + fib(i-2)

n = int(input('How many terms ? :  '))
print('Fibonacci  series', fib(n-1))

'''
Write  a  recursive  power  function
'''
def  power(a , b):
	if  b == 0:
		return  1
	if  b>0:
		return  a * power(a, b-1)
	return  (1/a) * power(a, b+1)
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print("Result: ",  power(a,b))
'''
Write  a   recursive  function  to  reverse  a  number
'''
from math import *
def  rev(n):
	if  n == 0:
		return  0
	else:
		return  n%10 * 10**(len(str(n))-1) + rev(n//10)

n = int(input('Enter  any  number :  '))
print('Reverse Number: ', rev(n))
#  Tricky  program
#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a)#3     2      1
		a = a – 1#a = 2    a = 1      a=0
		f1()
		print('Hello')#Hello
		print('Hi')#Hi
		print(a)#0
	print('Bye')#Bye
# End  of  the  function
a = 3
f1()
print('End')#End
#   Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)
		a = a – 1	
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
#End  of  the  function
a = 3
f1()
print('End')
'''
3
3
3
3
3
... (many 3’s until recursion depth exceeded)
RecursionError: maximum recursion depth exceeded
'''
#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
#End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)
'''
32
21
11
'''
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)
'''
3
2
1
0
0
1
2
3
'''
#  Find  outputs
def  f1():
	print('f1  function')#f1 function
	f2()
	print('End  of  f1  function')#End of f1 function
def  f2():#never called
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()
#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()
f2()
print(f1  is  f2)
f2 = f1
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
f2()#TypeError
'''
f1 function
f2 function
False
f1 function
True
f1 function
None
'''
# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
p = print
p ('Hyderabad')#Hyderabad
print = None
print('Hello')#error
p('Hello')#Hello
# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
x = id
print(x(25)) # id of integer 25
p = len
print(p('Hyd'))#3
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))#60
# Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi')
	inner2()
	print('Hello')
	inner1()
	print('Back  to  outer  function')
# End of the function
print('Begin')
outer()
print('Bye')
'''
Begin
Outer function
Hi
2 nd inner function
Hello
1 st inner function
Back to outer function
Bye
'''
# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()
print('Bye')
'''
30
10
Bye
'''
# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)#20
		print(globals()['x'])#10
	inner()
outer()	
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)#10
	inner()
outer()
# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)#20
		x +=  7#x = 27
	# End  of  inner  function
	print(x)#10
	x += 5# x = 15
	inner()
	print(x)#15
# End  of  the  function
outer()
print('Bye')#Bye
