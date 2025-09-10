'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3
'''
#Program to find gcd of two numbers
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
a=int(input())
b=int(input())
print(gcd(a,b))

#using recursion
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input())  
b=int(input())
print(gcd(a,b))


#Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
def sumofdigits(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumofdigits(n//10)

n=int(input("Enter a number : "))
print(sumofdigits(n))
