'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1


n = int(input('How many terms ? :  '))
print('Fibonacci  series')
How  to  print  first  'n'  terms  of  fibonacci  series


def fib(i):
    if i==1:
        return 0
    if i==2:
        return 1
    else:
        return fib(i-1)+fib(i-2)
    
n = int(input('Give the term :  '))
print('Fibonacci series : ',end='')
for i in range(1,n+1):
    print(fib(i),end=" ")


output:-
Give the term :  5
Fibonacci series : 0 1 1 2 3
        

-----------------------------------------------------------------------------------------------------------

Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1


1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->


How  to  print  a , b  and  a ^ b


def  power(a , b):
	if  b==0:
		return  1
	if  b >=0:
		return  a*power(a,b-1)
	return  (1/a)*power(a,b+1)

a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(f'power( {a} , {b} ) = {power(a,b):.4f}')

-----------------------------------------------------------------------------------------------------------


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

from math import *
def  rev(n):
	if  ???
		return  ???
	else:
		return  ??

rev(946)  =




def rev(n):
    if n==0:
        return 0
    return n%10 * 10**(len(str(n))-1) + rev(n//10)

n = int(input('Enter  any  number :  '))
print(f'Reverse   Number :   {rev(n)}')


-----------------------------------------------------------------------------------------------------------

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


output:-
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


-----------------------------------------------------------------------------------------------------------

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
print('End')



output:-
3 prints so many times 
the recursive f1() function calls more times so finally 
it is a RecursiveError 
-----------------------------------------------------------------------------------------------------------

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


output:-
43
32
21
11

-----------------------------------------------------------------------------------------------------------

# Find  outputs   (Home  work)
def  f1(x):
	print(x)    
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)


output:-
3
2
1
0
0
1
2
3
-----------------------------------------------------------------------------------------------------------

#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()


output:-
f1() function and f2() function calls alternatively .
So, the result is RecursiveError 

-----------------------------------------------------------------------------------------------------------

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
f2()

output:-
f1 function
f2 function
False
f1 function
True
f1 function
None
Error f2 Nonetype object is not callable
-----------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
#How  to  assign  ref  'p'  to  print()  function
p=print
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p('Hyderabad')
print = None
print('Hello')  # Nonetype object is not callable
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
print=p
print('Hello')


-----------------------------------------------------------------------------------------------------------

# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x=id
#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
#a=25
print(x(25))    # address like 1000211142
#How  to  assign  ref  'p'  to  len()  function
p=len
#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'
print(p('Hyd')) # 3

-----------------------------------------------------------------------------------------------------------

# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))

output:-
60
-----------------------------------------------------------------------------------------------------------

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


output:-
Begin
Outer function
Hi
2nd inner function
Hello
1st inner function
Back to outer function
Bye
-----------------------------------------------------------------------------------------------------------

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


output:-
30
10
Bye
-----------------------------------------------------------------------------------------------------------

# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()


output:-
20
10
-----------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()


output:-
10
-----------------------------------------------------------------------------------------------------------

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


output:-
10
20
15
Bye

'''