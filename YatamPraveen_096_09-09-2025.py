'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What is the fibonacci series ? --->  0, 1, 1, 2, 3, 5, 8, ...
2) What is the formula for 10th term ? ---> 9th term + 8th term
     What is the formula for 3rd term ? --->  2nd term +  1st  term
     What is the formula for ith term ? ---> (i-1)th term + (i-2)  term
3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def  fib(i):  #   'i'  is  term  number
	if  i == 1:
		return 0
	if  i == 2:
		return 1
	return fib(i-1) + fib(i-2)

n = int(input('How many terms ? : '))
print('Fibonacci  series')
# How  to  print  first  'n'  terms  of  fibonacci  series
for i in range(1, n+1):
    print(fib(i), end = ' ')





'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2
2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2
3) What  is  4.5 ^ 0 ?  ---> 1
'''
def  power(a , b):
	if b == 0:
		return 1
	if b < 0:
		return (1/a)*power(a, b+1)
	return a*power(a, b-1)
	
a = eval(input('Enter base : '))
b = int(input('Enter power : '))
#How  to  print  a , b  and  a ^ b
print(f'{a} ^ {b} = {power(a, b)}')





'''
Write  a  recursive  function  to  reverse  a  number
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
	if n == 0:
		return 0
	else:
		return   n%10 * 10**(len(str(n))-1) + rev(n//10)

n = int(input('Enter  any  number : '))
print('Reverse   Number : ' , rev(n))





#  Tricky  program
#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()                    #3<next_line>2<next_line>1<next_line>Bye<next_line>Hello<next_line>Hi<next_line>0<next_line>Bye<next_line>Hello<next_line>Hi<next_line>0<next_line>Bye<next_line>Hello<next_line>Hi<next_line>0<next_line>Bye
print('End')            #End





#   Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
#End  of  the  function
a = 3
f1()                            #This causes infinite recursion because a, which is a local variable, will always be reassigned to 3 resulting the if condition to be        print('End')			  always true. Then this results in continuous recursion





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
f1(x , x := x + 1)              #43<next_line>32<next_line>21
print(x)                        #11





# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)                           #3<next_line>2<next_line>1<next_line>0<next_line>0<next_line>1<next_line>2<next_line>3





#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End of f1 function')
def  f2():
	print('f2 function')
	f1()
	print('End of f2 function')
f1()                                    #This results in infinite recursion because, f1 calls f2. Again f2 calls f1. Then again f1 calls f2 and continues 





#  Find  outputs  (Home  work)
def    f1():
        print('f1 function')
def    f2():
        print('f2 function')
# End  of  the  function
f1()                            #f1 function
f2()                            #f2 function
print(f1 is f2)                 #False
f2 = f1
f2()                            #f1 function
print(f1 is f2)                 #True
f2 = f1()                       #prints f1 function as assigns None to f2
print(f2)                       #None
f2()                            #Throws error as None is not callable





# Find  outputs (Home  work)
#How  to  assign  ref  'p'  to  print()  function
p = print
#How to call print() function thru ref 'p' and print 'Hyderabad'
p('Hyderabad')
print = None
print('Hello')                      #Throws error as pvm interprets as None('Hello')
#How to call print() function thru ref 'p' and  print 'Hello'
p('Hello')





# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x = id
#How to call id() function thru ref 'x' and print id of object 25
print(x(25))
#How to assign ref 'p' to len() function
p = len
#How to call len() function thru ref 'p' and print length of 'Hyd'
print(p('Hyd'))





# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))                   		#60





# Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner1():
		print( '1st inner function')
	def  inner2():
		print('2nd inner function')
	print('Hi')
	inner2()
	print('Hello')
	inner1()
	print('Back to outer function')
# End of the function
print('Begin')                      #Begin          
outer()                             #Outer function<next_line>Hi<next_line>2nd inner function<next_line>Hello<next_line>1st inner function<next_line>Back to outer function
print('Bye')                        #Bye





# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()                             #30<next_line>10
print('Bye')                        #Bye





# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()                             #20<next_line>10





# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()                     #10





# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	# End of inner function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  the  function
outer()                             #10<next_line>20<next_line>15
print('Bye')                        #Bye