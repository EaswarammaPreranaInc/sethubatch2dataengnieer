'''
    Pattern: Diamond Pattern
    Input: ex-> 5
    o/p:
                * 
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * *
          * * * * * * *
            * * * * *
              * * *
                *
'''


n = int(input('Enter no of rows : '))

# Upper Half
k = 1
for i in range(1,n+1):
    for spaces in range(n-i):
        print(' ',end=' ')
    for j in range(k):
        print('*',end=' ')
    k+=2
    print()

# Lower Half    
l = n+2
for i in range(1,n):   
    for spaces in range(i):
        print(' ',end=' ')    
    for j in range(l):
        print('*',end=' ')
    l-=2
    print()