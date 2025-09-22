'''
Question:
Write a program to print a number pyramid where each row contains numbers increasing
from 1 to the row number and then decreasing back to 1, forming a symmetrical pattern.
'''

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    second = ""
    spaces = " " * (n - i)
    for j in range(1, i + 1):
        second += str(j)
    print(spaces + second[:-j:-1] + second)

'''
Output 1:
Enter number of rows: 5
    1
   121
  12321
 1234321
123454321

Output 2:
Enter number of rows: 3
  1
 121
12321
'''
