# write a recursive function to determine gcd 0r hcf of 2 numbers

def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
m=int(input("enter any number:"))
n=int(input("enter any number:"))
print("gcd",gcd(m,n))

'''
#outputs
enter any number:12
enter any number:15
gcd 3
'''
