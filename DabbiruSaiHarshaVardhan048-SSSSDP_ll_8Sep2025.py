'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3

2) gcd(4 , 7) =  gcd(7 , 4)  = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return   gcd(n, m%n)
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   gcd(m,n))
'''
1) gcd(4 , 6)  = 2
'''

'''
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
1) How  many  function  calls  are  in  sod(678) ?  --->  4
2) How  many  function  calls  are  in  sod(n-digit  number) ?  ---> n + 1
'''
def   sod(n):
	if  n == 0:
		return  0
	else:
		return  n%10 + sod(n//10)
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , sod(n))
'''
1) sod(9427) = 22
'''

