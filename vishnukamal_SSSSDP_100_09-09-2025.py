
''' 1) Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def fib(i): 
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)

n = int(input('How many terms? : '))
print('Fibonacci series:')
for i in range(n):
    print(fib(i), end=' ')
'''
Output: 
How many terms? : 5
Fibonacci series:
0 1 1 2 3
'''



''' 2) Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''

def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1/a * power(a, b+1)
    return a * power(a, b - 1)
a = float(input('Enter base : '))
b = int(input('Enter power : '))
print(f'{a} ^ {b} = {power(a, b)}')

'''
Output:
Enter base : 4.5
Enter power : 3
4.5 ^ 3 = 91.125
'''



''' 3) Write  a   recursive  function  to  reverse  a  number

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
def rev(n):
    if n > 0:
        return (n % 10) * 10 ** (len(str(n))-1)+ rev(n // 10)
    else:
        return 0

n = int(input('Enter any number : '))
print('Reverse Number :', rev(n))

'''
Output:
Enter any number : 123456789
Reverse Number : 987654321
'''



# 4) Tricky  program
#   Find  outputs

def f1():
    global a
    if a:
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
'''
Outputs:
3
2
1
Bye
Hello
Hi
0
Hello
Hi
1
Hello
Hi
2
Bye
End
'''



# 5) Find  outputs
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

'''
Outputs:
3
3
3
3
Bye
Hello
Hi
3
Hello
Hi
3
Hello
Hi
3
Bye
End
'''



# 6) Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
#End  of  the  function
x = 10
f1(x , x :=x+1)
print(x)

'''
Output:
32
21
10
11
'''



# 7) Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)

'''
Output:
3
2
1
0
0
1
2
3
'''



# 8) Find  outputs

def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2 function')
f1()

'''
Output:
f1  function
f2  function
f1  function
f2  function
...
repeats continously due to no end for the above recursion so recursion error
'''



# 9) Find  outputs  (Home  work)

def f1():
    print('f1    function')
def f2():
    print('f2  function')
f1()                 # f1    function
f2()                 # f2  function
print(f1 is f2)      # Output: False, because they are two different functions
f2 = f1
f2()                 # f1 function now f2 refers to f1
print(f1 is f2)      # Output: True, because f2 now refers to the same function as f1
f2 = f1()            # calls f1(), prints f1 function then assigns None to f2
print(f2)            # None, because f1() returns None and f2 is assigned to that
f2()                 # Error we can't call None object 



# 10) Find outputs (Home work)
# How to assign ref 'p' to print() function
p = print
# How to call print() function thru ref 'p' and print 'Hyderabad'
print = None
p('Hyderabad')   # Output: Hyderabad
# How to call print() function thru ref 'p' and print 'Hello'
p('Hello')       # Output: Hello



# 11) Find outputs (Home work)

# How to assign ref 'x' to id() function
x = id
# How to call id() function thru ref 'x' and print id of object 25
print(x(25))         # Output: address of object '25'
# How to assign ref 'p' to len() function
p = len
# How to call len() function thru ref 'p' and print length of 'Hyd'
print(p('Hyd'))      # Output: 3



# 12) Find output(Home work)

def f1(a):
    def f2():
        return 10
    # End of f2 function
    return f2() + 20 + a
# End of f1 function
print(f1(30))               # 60



# 13) Find outputs (Home work)

def outer():
    print('Outer function')                   # Outer function
    def inner1():
        print('1st inner function')
    def inner2():
        print('2nd inner function')
    print('Hi')                               # Hi
    inner2()                                  # 2nd inner function
    print('Hello')                            # Hello
    inner1()                                  # 1st inner function
    print('Back to outer function')           # Back to outer function
# End of the function
print('Begin')                                # Begin
outer()
print('Bye')                                  # Bye
'''
Outputs:
Begin
Outer function
Hi
2nd inner function
Hello
1st inner function
Back to outer function
Bye
'''



# 14) Find outputs (Home work)

x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)                 # Output: 30
        print(globals()['x'])    # Output: 10
    inner()
outer()
print('Bye')                     # Output: Bye



# 15) Find outputs (Home work)

x = 10  # Gv
def outer():
    x = 20
    def inner():
        print(x)                # Output: 20
        print(globals()['x'])   # Output: 10
    inner()
outer()



# 16) Find outputs (Home work)

x = 10
def outer():
    def inner():
        print(x)     # Output: 10
    inner()
outer()



# 17) Find outputs (Home work)

def outer():
    x = 10
    def inner():
        x = 20
        print(x)# Output: 20
        x += 7
    # End of inner function
    print(x)    # Output: 10
    x += 5
    inner()
    print(x)    # Output: 15
# End of the function
outer()
print('Bye')    # Output: Bye

