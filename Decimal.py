'''
The program converts a binary number (entered as a string) into its decimal equivalent.
The input string is reversed to process the least significant bit first.
For each bit:
If the bit is "1", add 2**i to the result (i is the position index).
If the bit is "0", do nothing.
Finally, the decimal value is returned and printed.
'''

def dec(n):
    result=0
    n=n[::-1]
    for i in range(len(n)):
        if n[i] == "1":
            result+=2**i
    return result
n=input("Enter a Binary Number : ")
print(dec(n))


'''
Output:

Enter a Binary Number : 101
5

Enter a Binary Number : 1000
8

Enter a Binary Number : 1111
15

Enter a Binary Number : 11010
26

'''