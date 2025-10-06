'''
    Pattern : Half Diamond Pattern
    Input : ex-> 6
    o/p:
        *
        * *
        * * *
        * * * *
        * * * * *
        * * * * * *
        * * * * *
        * * * *
        * * *
        * *
        *
'''

n = int(input('enter no of rows : '))

# Upper Half
for i in range(1,n+1):   
    for j in range(i):
        print('*',end=' ')    
    print()

# Lower Half 
for i in range(1,n+1):
    for j in range(n-i):
        print('*',end=' ')
    print()
