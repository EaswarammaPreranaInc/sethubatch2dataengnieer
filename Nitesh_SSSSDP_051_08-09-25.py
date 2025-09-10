'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3

2) gcd(4 , 7) =  gcd(7 , 4)  = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if  n == 0:
		return  m
	else:
		return   gcd(n, m%n)

m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd : ' , gcd(m,n))
	  


'''
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

sod(678) =  678 % 10 + sod(678 // 10)
              =  8 + sod(67)
              =  8 + 67 % 10 + sod(67 // 10)
              =  8 + 7 + sod(6)
              =  8 + 7 + 6 % 10 + sod(6 // 10)
              =  8 + 7 + 6 + sod(0)
              =  8 + 7 + 6 + 0
			  = 21

1) How  many  function  calls  are  in  sod(678) ?  --->  4

2) How  many  function  calls  are  in  sod(n-digit  number) ?  ---> n + 1
'''
def   sod(n):
	if n == 0:
		return  0
	else:
		return  n % 10 + sod(n//10)
'''
1) sod(9427) = 22
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits : ' , sod(9247))