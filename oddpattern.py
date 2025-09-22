'''
Question:
Write a program to print a number pyramid with n rows where numbers start from 1 
and increase by 2 for each subsequent number. Each row is centered with spaces.
'''

n = int(input())
count = 1
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(count, end=" ")
        count += 2
    print()

'''
Output 1:
Input: 5
     1 
    3 5 
   7 9 11 
  13 15 17 19 
 21 23 25 27 29 

Output 2:
Input: 3
   1 
  3 5 
 7 9 11 
'''
