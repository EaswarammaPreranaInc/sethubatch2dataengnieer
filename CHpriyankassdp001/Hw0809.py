#1

'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3

2) gcd(4 , 7) =  gcd(7 , 4)  = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''


"""def  gcd(m , n):
	if  ???
		return  ???
	else:
		return   ???
'''
1) gcd(4 , 6)  =
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   ???)
"""

def gcd(m, n): # function header for gcd
    if n == 0:       # case for check n is 0 or not
        return m # if n is 0 it returns the m like gcd(3,0)=gcd(m,n) then it gives the 3
    else:            
        return gcd(n, m % n) # Here recursion will happens until n is 0

# Example run
m = int(input('Enter any number : '))
n = int(input('Enter any number : '))
print('Gcd : ', gcd(m, n))# function call and prints the Gcd:



#2

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
"""def   sod(n):
	if  ???
		return  ???
	else:
		return  ???
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , ???)
"""
def sod(n):
    if n == 0:   # case for check n is 0 or not         
        return 0 # if n is 0 return 0
    else:                 # Recursion case
        return (n % 10) + sod(n // 10) # recursion will happens until n is 0


n = int(input('Enter any number : '))
print('Sum of the digits : ', sod(n))# function call and prints the sod if digits