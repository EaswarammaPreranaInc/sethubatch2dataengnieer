Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series
n=int(input('How many terms you want for fibonacci series:'))
a=0
b=1
print(f'{n} terms of fibonacci series are:',end='')
for i in range(1,n+1):
    print(a,end=' ')
    fib=a+b
    a=b
    b=fib
def fib(i):  
    if i==1:
        return 0
    if i==2:
        return 1
    return fib(i-1)+fib(i-2)
print()
print(fib(5))

Write  a  recursive  power  function
a=float(input('Enter base:'))
b=int(input('Enter power:'))
def power(a,b):
    if b>0:
        return a*power(a,b-1)
    if b<0:
        return 1/a*power(a,b+1)
    return 1
print(power(a,b))

Write  a   recursive  function  to  reverse  a  number
from math import *
def rev(n,rev_num=0):
    if n>0:
        return rev(n//10,rev_num*10+n%10)
    else:
        return rev_num
n=int(input('Enter any number:'))
print('Reverse number:',rev(n))

#  Tricky  program
#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a)                          3
                                      2
                                      1
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')                       Bye
                                     Hello
                                     Hi
                                     0
                                    Bye
                                    Hello
                                    Hi
                                    0
                                    Bye
                                    Hello
                                    Hi
                                    0
                                    Bye
# End  of  the  function
a = 3
f1()
print('End')                       End

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
f1()
print('End')                                      Recursion Error

#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)                                     43
                                               32
                                               21
#End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)                                       11

# Find  outputs   (Home  work)
def  f1(x):
	print(x)                                    3
                                              2
                                              1
                                              0
	if   x:
		f1(x - 1)
	print(x)                                    0
                                              1
                                              2
                                              3
# End  of  the  function
f1(3)

#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()                                            Recursion Error

#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')                 f1 function
def    f2():
        print('f2  function')                   f2 function
# End  of  the  function
f1()
f2()
print(f1  is  f2)                              false
f2 = f1
f2()
print(f1  is  f2)                              true
f2 = f1()
print(f2)                                      Error
f2()

# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function                                    p=print
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'          p('Hyderabad')
print = None
print('Hello')                                                                      Error
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'              p('Hello')
                                                                                    Hello

# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function                                            x=id
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25            print(x(25))
How  to  assign  ref  'p'  to  len()  function                                           p=len
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd            print(p('Hyd'))

# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))                                   60

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
Begin
Outer function
Hi
2nd inner function
Hello
1st inner function
Back to outer function
Bye

# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)                           30
		print(globals()['x'])              10
	inner()
outer()
print('Bye')                          Bye

# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)                         20
		print(globals()['x'])            10
	inner()
outer()

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)                       10
	inner()
outer()

# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)                               20
		x +=  7
	# End  of  inner  function
	print(x)                                 10
	x += 5
	inner()
	print(x)                                 15
# End  of  the  function
outer()
print('Bye')                               Bye
