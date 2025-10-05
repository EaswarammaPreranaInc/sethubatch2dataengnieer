'''
    Pattern: Full Pyramid
    Input: ex-> 5
    o/p:

                * 
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * *
'''

n = int(input('Enter no of rows : '))
k=1
for i in range(1,n+1):
    
    for spaces in range(n-i):
        print(' ',end=' ')
    
    for j in range(k):
        print('*',end=' ')
    k+=2
    print()