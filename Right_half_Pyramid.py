'''
    Problem Statement: Write a program to print the right half pyramid pattern using stars.
    Input: An integer n representing the number of rows    ex: 5
    Output:
    *
    * *
    * * *
    * * * *
    * * * * *
'''
n = int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()