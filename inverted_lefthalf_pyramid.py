'''
    Pattern  : Inverted Left Half Pyramid
    Input: ex-> 6
    o/p:
    * * * * * *
      * * * * *
        * * * *
          * * *
            * *
              *
'''


n = int(input('Enter no of rows : '))
for i in range(1,n+1):
    
    for j in range(1,i):
        print(' ',end=' ')
    
    for j in range(n-i+1):
        print('*',end=' ')
 
    print()
    