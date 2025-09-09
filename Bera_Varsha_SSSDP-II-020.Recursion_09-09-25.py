'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def  fib(n):  #   'i'  is  term  number
	if  n <=1:
		return  n
	if  n>1:
		return (fib(n-1)+fib(n-2))
	return  i
'''
fib(5) =
'''
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
# How  to  print  first  'n'  terms  of  fibonacci  series
for i in range(n):
	print(fib(i))
#output:
'''
How many terms ? :  5
Fibonacci  series
0
1
1
2
3
'''
'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''
def  power(a , b):
	if  b == 0:
		return  1
	if  b>0:
		return  a*power(a,b-1)
	return  (1/a)*power(a,b+1)
'''
1) power(4.5 , 3) =91.125

2) power(4.5 , -3) =0.010973936899862825

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
# How  to  print  a , b  and  a ^ b
print(power(a,b))
# output:
'''
Enter  base :  4.5
Enter  power :  3
91.125
Enter  base :  4.5
Enter  power :  -3
0.010973936899862825
'''
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
	if  n == 0:
		return  0
	else:
		return  n % 10 * (10)**(len(str(n))-1)+rev(n//10)
'''
rev(946)  = 649
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))
# output
# Enter  any  number :  946
# Reverse   Number :   649
