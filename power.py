'''
The program calculates a power of a power
The function power(a, b) computes  
manually using a loop:
If b == 0, it returns 1.
If b > 0, it multiplies a by itself b times.
If b < 0, it calculates a^{-b} and returns the reciprocal 1/(a^{-b}).
The main code reads three integers a, b, c from the user.
It calculates power(a, power(b, c)) and prints the result.
'''

def power(a,b):
    res=1
    if b == 0 :
        return 1
    elif b > 0:
        for i in range(b):
            res*=a
        return res
    else:
        b = b * -1
        for i in range(b):
            res*=a
        return 1/res
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
x=power(a,power(b,c))
print(x)


'''
Output:

Enter a: 2
Enter b: 3
Enter c: 2
512

'''