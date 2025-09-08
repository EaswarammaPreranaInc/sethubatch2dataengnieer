'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3

2) gcd(4 , 7) =  gcd(7 , 4)  = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if  ???
		return  ???
	else:
		return   ???
'''
1) gcd(4 , 6)  =
'''
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   ???)'''

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

# Example calculation
m = int(input('Enter any number : '))
n = int(input('Enter any number : '))
print('Gcd :', gcd(m, n))
