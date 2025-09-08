#1st program
def  gcd(m , n):
	if  n>0:
		return  gcd(n,m%n)
	else:
		return m

m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('GCD: ',gcd(m,n))


#2nd program
def   sod(n):
	if n>0:
		return (n%10)+sod(n//10)
	else:
		return  n
        
n = int(input('Enter  any  number :   '))
print('Sum of the digits:',sod(n))