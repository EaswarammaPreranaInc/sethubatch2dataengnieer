'''
The program first asks the user to enter the number of rows (n).
For each row, it generates a sequence of alphabets starting from ‘A’ using chr(65 + j) and decreases the number of characters with each new row.
The sequence is reversed to form the right-hand side (right), while spaces are added in the middle (space) to create symmetry in the pattern.
If it is the first row, the middle character is avoided to prevent duplication, otherwise the full mirrored pattern is printed.
'''

n=int(input("Enter Number of Rows="))
for i in range(n):
    left = "".join(chr(65 + j) for j in range(n - i))
    right=left[::-1]
    space = " " * (i) 
    if i == 0:
        print(left + right[1:]) 
    else:
        print(left + space + right)


'''
Output:

Enter Number of Rows = 5

ABCDEDCBA
ABCD DCBA
ABC   CBA
AB     BA
A       A
'''
