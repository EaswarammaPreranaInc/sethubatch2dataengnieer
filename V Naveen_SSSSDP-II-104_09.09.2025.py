'''#1.  Tricky  program
#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a) # 3 <nextline> 2 <nextline> 1
		a = a - 1
		f1() # 
		print('Hello') # Hello
		print('Hi') # hai
		print(a) # 0
	print('Bye') # bye
# End  of  the  function
a = 3
f1()
print('End') # End




#2.   Find  outputs
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
print('End') 
# Execute infinte times 3



#3.  Most  tricky   program
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
#43
#32
#21
#11




#4. Find  outputs   (Home  work)
def  f1(x):
	print(x) # 3<nextline>2<nextline>1
	if   x:
		f1(x - 1)
	print(x) # 0
# End  of  the  function
f1(3)
#3
#2
#1
#0
#0
#1
#2
#3





#5.  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1() # f1 function<nextline>f2 function<nextline> same output will be printed infinite times




#6.  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1() # f1 function
f2() # f2 function
print(f1  is  f2) # False
f2 = f1 
f2() # f1 function
print(f1  is  f2) # True
f2 = f1() 
print(f2) # f1 function<nextline>None
#f2() # Error





#7. Find  outputs (Home  work)
p = print # How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
#print('Hello') # Error
p('Hello') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'






#8. Find   outputs (Home  work)
x = id # How  to  assign  ref  'x'  to  id()  function
print(x(25)) # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len # How  to  assign  ref  'p'  to  len()  function
print(p('Hyd')) # How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd





#9. Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) # 60




#10. Find  outputs (Home  work)
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
# Begin
# Outer  function
# Hi
# 2nd  inner  function
# Hello
# 1st  inner  function
# Back  to  outer  function
# Bye






#11. Find  outputs  (Home  work)
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
# 30
# 10
# Bye




#12. Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
# 20
# 10




#13. Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer() # 10




#14. Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')
# 10
# 20
# 15
# Bye


#15.Write  a  recursive  function  for  fibonacci  term
def fib(i):   # 'i' is the term number (1-based index)
    if i == 1:
        return 0
    if i == 2:
        return 1
    return fib(i - 1) + fib(i - 2)
'''
#fib(5) =
'''
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for k in range(1,n+1):
    print(fib(k),end = ' ') # How  to  print  first  'n'  terms  of  fibonacci  series



#16. Write  a  recursive  power  function
def  power(a , b):
	if  b == 0:
		return  1
	if  b < 0 :
		return  (1 / a) * power(a , (b + 1))
	return  a * power(a, (b-1))
'''
#1) power(4.5 , 3) = # 91.125

#2) power(4.5 , -3) = 0.010973936899862825

#3) How  many  function  calls  are  in  power(a , b)  ? ---> 4
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(f'a : {a}, b : {b} and a ^ b : {power(a , b)}') # How  to  print  a , b  and  a ^ b
'''

#17. Write  a   recursive  function  to  reverse  a  number
from math import *
def  rev(n):
	if  n > 0 :
		return  (n % 10) * (10**(len(str(n))-1)) + rev(n // 10)
	else:
		return  0
'''
rev(946)  = 649
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number : ' ,rev(n))



