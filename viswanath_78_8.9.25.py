q)Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers
ans) def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
m = int(input('Enter any number: '))
n = int(input('Enter any number: '))
print(f'GCD of {m}, {n} :', gcd(m, n)

q)Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
ans)def   sod(n):
	if  n == 0:
		return  0
	else:
		return  n%10+sod(n//10)
n = int(input('Enter  any  number  :  '))
print('sum of digits : ',sod(n))
