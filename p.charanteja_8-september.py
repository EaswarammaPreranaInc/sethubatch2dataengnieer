#GCD (Greatest Common Divisor) – Recursive Function

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

m = int(input('Enter any number: '))
n = int(input('Enter any number: '))
print('Gcd: ', gcd(m, n))



'''
example output:
To compute gcd(4, 6):

gcd(4, 6)      # → gcd(6, 4)
gcd(6, 4)      # → gcd(4, 2)
gcd(4, 2)      # → gcd(2, 0)
gcd(2, 0)      # → returns 2
'''





#Sum of the Digits (SOD) – Recursive Function

def sod(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sod(n // 10)

n = int(input('Enter any number: '))
print('Sum of the digits: ', sod(n))

'''
example output:
To compute sod(9427):

sod(9427)  # → 7 + sod(942)
sod(942)   # → 2 + sod(94)
sod(94)    # → 4 + sod(9)
sod(9)     # → 9 + sod(0)
sod(0)     # → 0
# So: 7 + 2 + 4 + 9 = 22
'''


