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
	if  i==1 :
		return  0
	if   i==2:
		return  1
	else :
		return  fib(i-1)+fib(i-2)

n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for i in range(n):
	print(fib(i+1))


'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''
def  power(a , b):
	if  b>0:
		return  a*power(a , b-1)
	if  b<0:
		return  1/a*power(a , b+1)
	if  b==0:   
	    return  1
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(power(a,b))


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
		k=len(str(n))
		return  (n%10)*(10**k-1)+rev(n//10)
	else:
		return  0
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

#  Tricky  program
#   Find  outputs
def  f1():
	global  a   # treat a as gloabal variable
	if  a:  #if value of a is non 0
		print(a)    # print a i.e 3 , prints 2 for inner func 1, prints 1 for 2nd inner func calll
		a = a - 1   # a is modifiesd to 2 ,  a is modified to 1 for inner func , a is modified to 0
		f1()    # again f1 is called as a is 2 , again inner func is called, again func is called but if stat is false as a is 0
		print('Hello')  # prints hello
		print('Hi') # prints hi
		print(a)    # prints 0
	print('Bye')    # prints bye when a is 0
# End  of  the  function
a = 3   # global variable a is created
f1()    # f1 function call
print('End')    # prints end

#   Find  outputs
def  f1():
	a = 3   # local a is 3
	if  a:
		print(a)    # prints a 3 , pritns a  ie 3
		a = a - 1   #a is modified to 2
		f1()    # function call f1 so f1 is called recursively as local a is always 3
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
#End  of  the  function
a = 3   # gloabl a is 3
f1()    # function call f1
print('End')

#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y): # f1(10,11) f1(21,11) f1(32,11) f1(43,11)
	if   x > 40:
		return  # empty return stat
	x += y  # x=21  x=31   x=41
	f1(x , y)   # f1(21,11)  f1(32,11)  f1(43,11)
	print(x)    # prints 43,32,21
#End  of  the  function
x = 10  # x=10
f1(x , x := x + 1)  # f1(10,11)
print(x)    # prints 11 as x is modified to 11

# Find  outputs   (Home  work)
def  f1(x): # f1(3)
	print(x)    # prints 3 prints 2 prints 1 prints 0
	if   x: # true true true
		f1(x - 1)   # f1(2) f1(1)   f1(0)
	print(x) # 0,1,2,3
# End  of  the  function
f1(3)   # function call

#  Find  outputs
def  f1():
	print('f1  function')
	f2()    # calls f2 function
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()    # calls f1 function so this is a infinite recursive function
	print('End  of  f2  function')
f1()    # function call f1

#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()    # function call f1 'f1 function' is printed
f2()  # function f2 'f2 function' is printed
print(f1  is  f2)   # false as both functions point to differnt objects
f2 = f1 # f1 function is assigm=ned to reference f2
f2()    # f1 function is called
print(f1  is  f2)   # true
f2 = f1()   # resutl of f1 function is stored in f2'f1    function'
print(f2)#'f1    function'
f2()        # as f2 is not a function ist is error

# Find  outputs (Home  work)
#How  to  assign  ref  'p'  to  print()  function
p=print
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p('Hyderabad')
print = None
print('Hello')  # error
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
p('Hello')

# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x=id
#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
print(x(25))
#How  to  assign  ref  'p'  to  len()  function
p=len
#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
print(p('Hyd'))

# Find  output(Home  work)
def    f1(a):   # a is 30
	def   f2(): # f2 is defined
		return  10  # 10 is returned to func call
	# End  of  f2  function
	return  f2() + 20 +  a  # f2 funct is called so 10+20+30=60
# End  of  f1  function
print(f1(30))   # f1(30 )is called

# Find  outputs (Home  work)
def  outer():   # outer func
	print('Outer  function')
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi') # PRINTS HI
	inner2()    # inner 2 is called so print '2nd  inner  function'
	print('Hello')  # print hello
	inner1()    # inner 1 is called so print '1st  inner  function'
	print('Back  to  outer  function')# print 'Back  to  outer  function'
# End of the function
print('Begin')  # prints begin
outer() # outer func is called
print('Bye')    # prints bye

# Find  outputs  (Home  work)
x = 10  # global x is 10
def  outer():
	x = 20  # local x is 20
	def   inner():
		x = 30  # local local x is 30
		print(x)    # prints 30 
		print(globals()['x'])   #prints 10	
		inner()  # inner func is called
outer() # outer func is called
print('Bye') #prints bye

# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():   
	x = 20  # local x is 20
	def   inner():  # inner func
		print(x)    # prints 20
		print(globals()['x'])    #prints 10
	inner() # inner func is called
outer() # outer func is called

# Find  outputs  (Home  work)
x = 10  #global x is 20
def  outer():
	def   inner():
		print(x)    # prints 10
	inner() # inner func is called
outer() # outer func is called

# Find  outputs  (Home  work)
def  outer():
	x = 10  # local x is 10
	def  inner():
		x = 20  # LOCAL LOCAL X IS 20
		print(x)# prints 20
		x +=  7# x=27
	# End  of  inner  function
	print(x)    #prints 10
	x += 5  # x=15
	inner() # calls inner
	print(x)    # print 15
# End  of  the  function
outer() #outer func is called
print('Bye')# prints bye
