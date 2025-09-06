'''
The program converts a decimal number (base 10) into binary (base 2).
It initializes an empty string s to store the binary digits.
Using a while loop, it repeatedly divides the number by 2:
        If the remainder is 1 → append "1" to s
        If the remainder is 0 → append "0" to s
After the loop, the string is reversed using s[::-1] to get the correct binary order, and the result is printed.
'''

def Binary(n):
    if n == "0":
        return 0
    s=''
    while n > 0:
        if n%2 == 1:
            s+="1"
        else:
            s+="0"
        n=n//2
    return s[::-1]

n=int(input("Enter a number:"))
print(Binary(n))


'''
Output:

Enter a number: 5
101

Enter a number: 8
1000

Enter a number: 15
1111

'''


