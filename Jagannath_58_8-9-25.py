Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers
def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
m=int(input('Enter any number:'))
n=int(input('Enter any number:'))
print('Gcd:',gcd(m,n))

Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
def sod(n):
    if n>0:
        return n%10+sod(n//10)
    else:
        return 0
n=int(input('Enter any number:'))
print('Sum of the digits:',sod(n))
