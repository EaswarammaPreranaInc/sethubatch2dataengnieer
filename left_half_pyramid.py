'''
    Pattern  : Left Half Pyramid
    Input: ex-> 5
    o/p:
            * 
          * *
        * * *
      * * * *
    * * * * *           
'''

n = int(input('Enter no of rows : '))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()