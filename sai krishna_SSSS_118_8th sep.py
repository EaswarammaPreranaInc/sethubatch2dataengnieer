1.def gcd(m, n):
    if n == 0:          # base case
        return m
    else:
        return gcd(n, m % n)   # recursive call

# Example 
m = int(input('Enter any number : '))
n = int(input('Enter any number : '))
print('Gcd :', gcd(m, n))


2.def sod(n):
    if n == 0:               # base case
        return 0
    else:                    # recursive case
        return (n % 10) + sod(n // 10)

# Example usage
n = int(input('Enter any number : '))
print('Sum of the digits :', sod(n))