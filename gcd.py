'''
The program calculates the GCD (Greatest Common Divisor) of three numbers.
It defines a function gcd(a, b) which uses the Euclidean algorithm:
    Repeatedly replace (a, b) with (b, a % b) until b becomes 0.
    When b is 0, a is the GCD of the two numbers.
The program reads three integers a, b, and c from the user.
It calculates gcd(a, gcd(b, c)) to get the GCD of all three numbers and prints it.
'''

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a    
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
x=gcd(a,gcd(b,c))
print(x)


'''
Output:

Enter a: 12
Enter b: 18
Enter c: 24
6

Enter a: 7
Enter b: 14
Enter c: 21
7

'''