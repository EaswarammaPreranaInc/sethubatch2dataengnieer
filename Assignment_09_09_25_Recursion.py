#Write  a  recursive  function  for  fibonacci  term
#Use  the  function  to  generate  fibonacci  series
def  fib(i):#   'i'  is  term  number
	if  i==0:
		return  0
	if i==1:
		return  1
            
	return  fib(i-1)+fib(i-2)

n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for j in range(fib(n)):
    print(fib(j))
#output:
How many terms ? :  5
Fibonacci  series
0
1
1
2
3

Write  a  recursive  power  function

def  power(a , b):
	if  b>0:
		return  a * power(a,b-1)
	if  b<0:
		return  (1/a)* power(a,b+1)
	return  1

a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
c=print(f'power of {a} ,{b} is {power(a,b)} ')

#output:
Enter  base :  4.5
Enter  power :  3
power of 4.5 ,3 is 91.125
Enter  base :  4.5
Enter  power :  -3
power of 4.5 ,-3 is 0.0005419228098697691 
Enter  base :  4.5
Enter  power :  0
power of 4.5 ,0 is 1 

#Write  a   recursive  function  to  reverse  a  number
def  rev(n):
    if n==0:
        return 0
    l=len(str(n))
    return n%10 * 10**(l-1) + rev(n//10)

n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))
#output:
Enter  any  number :  678
Reverse   Number :   876

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
f1()
print('End')
#output:
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

#Find  outputs
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
#output:
Infinite loop

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
#output:
43
32
21
11

# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)
#output:
3
2
1
0
0
1
2
3

#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()#Infinite loop

#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()#f1 function
f2()#f2 function
print(f1  is  f2)#False
f2 = f1
f2()#f1 function
print(f1  is  f2)#True
f2 = f1()
print(f2)#f1 function
f2()#None

# Find  outputs (Home  work)
p=print
p('Hyderabad')#Hyderabad
print = None
print('Hello')#Error
p('Hello')#Hello

# Find   outputs (Home  work)
x=id
print(x(25))#1368711693296
p=len
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
#output:
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye

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
#output:
30
10
Bye

# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
output:
20
10

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
#output:
10

# Find  outputs  (Home  work)
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
#output:
10
20
15
Bye



























