'''
The program prints a pyramid pattern of letters (like an alphabet diamond) for n rows.
For each row i:
left contains letters from A up to the required character for that row.
right is the reverse of left.
space is added between left and right starting from row 1 to maintain the pyramid shape.
For the first row, only a single sequence is printed without extra space.
The pattern is printed row by row to form a centered pyramid of letters.
'''

n=int(input("Enter Number of Rows = "))
for i in range(n):
    left = "".join(chr(65 + j) for j in range(n - i))
    right=left[::-1]
    space = " " * (2*i - 1) if i > 0 else ""
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
