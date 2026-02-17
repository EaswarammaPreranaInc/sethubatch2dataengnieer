#TARUN BANALA      09-09-2025
#Long Programs
#Question 1:
'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
'''
def  fib(i):  #   'i'  is  term  number
	if  ???
		return  ???
	if  ???
		return  ???
	return  ???
 '''
'''
fib(5) =

n = int(input('How many terms ? :  '))
print('Fibonacci  series')'''
#How  to  print  first  'n'  terms  of  fibonacci  series

#Answer:
def fib(i):  # 'i' is term number (starting from 1)
    if i == 1:      # First term
        return 0
    if i == 2:      # Second term
        return 1
    return fib(i - 1) + fib(i - 2)  # Sum of previous two terms

n = int(input('How many terms ? : '))
print('Fibonacci series:')
for i in range(1, n + 1):
    print(fib(i), end=' ')

#Question 2:
'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''
'''def  power(a , b):
	if  ???
		return  ???
	if  ???
		return  ???
	return  ???
 '''
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
'''a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))'''
#How  to  print  a , b  and  a ^ b

#Answer:
def power(a, b):
    if b == 0:          # Any number to the power of 0 is 1
        return 1
    if b > 0:           # Positive exponent
        return a * power(a, b - 1)
    return (1 / a) * power(a, b + 1)  # Negative exponent

a = float(input('Enter base : '))
b = int(input('Enter power : '))
result = power(a, b)
print(f'{a} ^ {b} = {result}')

#Question 3:
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
'''from math import *
def  rev(n):
	if  ???
		return  ???
	else:
		return  ??'''
'''
rev(946)  =

n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))'''

#Answer:
from math import *

def rev(n):
    if n == 0:  # Base case: when number becomes 0
        return 0
    else:
        # Get the number of digits in the original number
        num_digits = len(str(n))
        # Extract last digit and multiply by appropriate power of 10
        return (n % 10) * (10 ** (num_digits - 1)) + rev(n // 10)

n = int(input('Enter any number : '))
print('Reverse Number : ', rev(n))
