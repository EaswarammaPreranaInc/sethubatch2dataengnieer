'''
    Pattern : Inverted Right Half Pyramid
    Input : 5
    Output :
    * * * * *
    * * * * 
    * * *
    * *
    *
'''


n = int(input('Enter no of rows : '))# read number of rows from user
for i in range(1,n+1):
    for j in range(n-i+1):
        print('*',end=' ')
    print()