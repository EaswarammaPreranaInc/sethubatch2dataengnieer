Program to write recursive gcd

def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)

m = int(input("Enter any number: "))
n = int(input("Enter any number: "))
print('gcd: ',gcd(m,n))


#Program to write recursive sum of digits

def sod(n):
    if n==0:
        return 0
    else:
        return (n%10) + sod(n//10)
    
n = int(input('Enter any number : '))
print('Sum of the digits : ', sod(n))
