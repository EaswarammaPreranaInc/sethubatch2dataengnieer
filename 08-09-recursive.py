def gcd(m,n):
    if n==0:
        return m 
    else:
        return gcd(n,m%n)

m=int(input("enter a number "))
n=int(input("enter a second number "))
print('gcd:',gcd(m,n))

'''
enter a number  12
enter a second number  15
gcd: 3

'''

def sod(n):
    if n==0:
        return 0
    else:
        return(n%10) + sod(n//10)

n=int(input("enter a number:" ))
print('sum of digits :',sod(n))

'''
enter a number: 535
sum of digits : 13
'''
