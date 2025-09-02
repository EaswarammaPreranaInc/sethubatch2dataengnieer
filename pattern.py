'''
The program takes an integer input n from the user, which represents the number of rows to be printed.
For each row i, it generates a sequence of alphabets starting from ‘A’ up to (n - i) characters using chr(65 + j).
The sequence is then reversed to form the right-hand part of the pattern, ensuring symmetry.
A space of width (2*i - 1) is added in the middle (except for the first row), which increases with each row, creating a hollow effect.
Finally, the left sequence, spaces, and right sequence are combined and printed row by row, forming a hollow diamond-like alphabet pattern.
'''

n=int(input("Enter Number of Rows="))
for i in range(n):
    left = "".join(chr(65 + j) for j in range(n - i))
    right=left[::-1]
    space = " " * (2*i - 1) if i > 0 else ""
    if i == 0:
        print(left + right[1:]) 
    else:
        print(left + space + right)

'''
output:

Enter Number of Rows = 5

ABCDEDCBA
ABCD DCBA
ABC  CBA
AB   BA
A    A
'''

