'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def  fib(i):  #   'i'  is  term  number
	if  i > 1:
		return  fib(i - 1) + fib(i - 2)
	if  i == 0:
		return  0
	return  1
'''
fib(5) = fib(4) + fib(3) = (fib(3) + fib(2)) = fib(2) + fib(1) = (fib(1) + fib(0)) + 1 = (1 + 0) + 1 = 2
'''
n = int(input('How many terms ? : '))
print('Fibonacci  series', fib(n))
How  to  print  first  'n'  terms  of  fibonacci  series


'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''
def  power(a , b):
	if  b > 0:
		return  a * power(a,b-1)
	if  b<0 :
		return  (1/a) * power(a, b+1)
	return  1
'''
1) power(4.5 , 3) = 4.5 * power(4.5, 2) = 4.5 * 4.5 *power(4.5, 1)=4.5 *4.5*4.5*power(4.5,0)=4.5*4.5*4.5

2) power(4.5 , -3) =1/4.5 * power(4.5,-2) 

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(power(a,b))
How  to  print  a , b  and  a ^ b


'''
Write  a   recursive  function  to  reverse  a  number

rev(678) =  678 % 10 *  10 ^ (3 - 1)  +  rev(678 // 10)
              =  800  +  rev(67)
              =  800  +  67 % 10 * 10 ^ (2 - 1) + rev(67 // 10)
              =  800  +  70 + rev(6)
              =  800  +  70 + 6 % 10 * 10 ^ (1 - 1) + rev(6 // 10)
              =  800  +  70 + 6 + rev(0)
              =  800  +  70 + 6 + 0
			  = 876

1) How  many  function  calls  are  in  rev(678) ?  --->   4

2) How  many  function  calls  are  in  rev(n-digit number)  ? ---> n + 1

3) How  to  obtain  length  of a  number ?  --->  len(str(n))
'''
from math import *
def  rev(n):
	if  n>0:
		return  int(n % 10 * pow(10,len(str(n))-1)) + rev(n//10)
	else:
		return  0
'''
rev(946)  = 946 % 10 * 10^(3-1) + rev(946//10) = 6 * 100 + rev(946//10) = 649
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))



#  Tricky  program
#   Find  outputs
def  f1(): # fun header
	global  a # consider a as global
	if  a:
		print(a) # 3 2 1
		a = a - 1 # 2 1 0
		f1() # 2 1 0
		print('Hello') # Hello
		print('Hi') # Hi
		print(a) # 0
	print('Bye') # bye
# End  of  the  function
a = 3 # int obj
f1() # 
print('End') # End


#   Find  outputs
def  f1():
	a = 3 # 0 
	if  a:
		print(a) # 3 2 1
		a = a - 1 # 2 1 0
		f1() # 2 1 0
		print('Hello') # Hello
		print('Hi') # Hi
		print(a) # 0
	print('Bye')
#End  of  the  function
a = 3 # int obj
f1() # 
print('End') # End


#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y):  
	if   x > 40:
		return 
	x += y # 11
	f1(x , y) 
	print(x) # 40  37  34  31  28  25  22  19  16  13
#End  of  the  function
x = 10 # int obj
f1(x , x := x + 1) # 40  37  34  31  28  25  22  19  16  13
print(x) # 11


# Find  outputs   (Home  work)
def  f1(x):
	print(x) # 3  2  1
	if   x:
		f1(x - 1) # recurssion
	print(x) # 0
# End  of  the  function
f1(3)


#  Find  outputs
def  f1():
	print('f1  function') # f1 function
	f2() # f2 fun
	print('End  of  f1  function') # End of f1 function
def  f2():
	print('f2  function') # f2 function
	f1() # f1 fun
	print('End  of  f2  function')
f1()


#  Find  outputs  (Home  work)
def    f1():
        print('f1    function') # f1 function
def    f2():
        print('f2  function') # f2 function
# End  of  the  function
f1()
f2()
print(f1  is  f2) # False
f2 = f1 
f2() # f1    function
print(f1  is  f2) # True
f2 = f1() # f1    function
print(f2) # none
f2() # error


# Find  outputs (Home  work)
p = print # How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello') error
p('Hello') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'


# Find   outputs (Home  work)
x = id # How  to  assign  ref  'x'  to  id()  function
x(25) # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len # How  to  assign  ref  'p'  to  len()  function
p('Hyd') # How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd


# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a # f2() + 20 + 30 # 10+20+30
# End  of  f1  function
print(f1(30)) # 60


# Find  outputs (Home  work)
def  outer():
	print('Outer  function') # Outer function
	def  inner1():
		print( '1st  inner  function') # 1st  inner  function
	def  inner2():
		print('2nd  inner  function') # 2nd  inner  function
	print('Hi') # hi
	inner2()
	print('Hello')
	inner1()
	print('Back  to  outer  function') # Back  to  outer  function
# End of the function
print('Begin') # Begin
outer() # fun call
print('Bye') # Bye


# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x) # 30
		print(globals()['x']) # 20
	inner() 
outer()
print('Bye') # Bye


# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x) # error
		print(globals()['x']) # 20
	inner()
outer()


# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x) # error
	inner()
outer()


# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x) # 20
		x +=  7 # 27
	# End  of  inner  function
	print(x) # 10
	x += 5 # 15
	inner() 
	print(x) # 15
# End  of  the  function
outer()
print('Bye') # Bye