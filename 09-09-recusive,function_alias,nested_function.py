'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def fib(i):  # 'i' is term number
	if i == 0:
		return 0
	if i == 1:
		return 1
	return fib(i-1) + fib(i-2)

n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for k in range(n):
	print(fib(k), end=' ')
print("\n")

# -------------------------------------------------------------

'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2
2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2
3) What  is  4.5 ^ 0 ?  ---> 1
'''


def power(a , b):
	if b == 0:
		return 1
	if b > 0:
		return a * power(a , b - 1)
	else:
		return 1/a * power(a , b + 1)

a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(f"{a} ^ {b} = {power(a,b)}")
print("\n")


# -------------------------------------------------------------

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
'''
from math import *

def rev(n):
	if n == 0:
		return 0
	else:
		length = len(str(n))
		return (n % 10) * int(pow(10, length - 1)) + rev(n // 10)

n = int(input('Enter  any  number :  '))   
print('Reverse   Number :  ' , rev(n))     
print("\n")


# -------------------------------------------------------------

#  Tricky  program
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
a = 3
f1()
print('End')
print("\n")


'''
3
2
1
Bye
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
End

'''

# -------------------------------------------------------------

def  f1():
	a = 3
	if  a:
		print(a)                                #3
		a = a - 1                                  
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
a = 3
f1()                      # error because it repated the continous without decrement
print('End')
print("\n")

# -------------------------------------------------------------

def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)                 #43 #32  #21 
x = 10
f1(x , x := x + 1)         
print(x)                  #11
print("\n")               #

# -------------------------------------------------------------

def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
f1(3)                              #3  #2 #1 #0 #0 #1 #2 #3
print("\n")                        #

# -------------------------------------------------------------

def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
# f1()                                     # WARNING: this will cause infinite recursion

print("\n")                                #

# -------------------------------------------------------------

def    f1():
	print('f1    function')
def    f2():
	print('f2  function')
f1()                                       #f1 function
f2()                                       #f2 function
print(f1  is  f2)                          #False                    
f2 = f1
f2()                                       #f1 function
print(f1  is  f2)                          #True
f2 = f1()                                  #f1 function
print(f2)                                  #None   
# f2()   # TypeError if executed
print("\n")                                #

# -------------------------------------------------------------

# Function reference examples
p = print
p("Hyderabad")            #Hyderabad
print = None
# print("Hello")          # will raise error
p("Hello")                #Hello
print("\n")               #

# -------------------------------------------------------------

x = id
print(x(25))             #id of 25
p = len
print(p("Hyd"))          #3
print("\n")

# -------------------------------------------------------------

def    f1(a):
	def   f2():
		return 10
	return  f2() + 20 +  a
print(f1(30))                     #60                        
print("\n")                       #

# -------------------------------------------------------------

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
print('Begin')                                #Begin
outer()                                       #Outer function   #Hi   #2nd inner function   #Hello    #1st inner function  #Back to outer function 
print('Bye')                                  #Bye
print("\n")                                   #

# -------------------------------------------------------------

x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()                         #30   #10  
print('Bye')                    #Bye
print("\n")                     #

# -------------------------------------------------------------

x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()                               #20 #10
print("\n")                           #

# -------------------------------------------------------------

x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()               #10 
print("\n")           #

# -------------------------------------------------------------

def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	print(x)
	x += 5
	inner()
	print(x)
outer()            #10  #20  #15
print('Bye')       #Bye
