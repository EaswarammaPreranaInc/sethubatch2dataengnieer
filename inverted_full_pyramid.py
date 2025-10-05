'''
    Pattern: Inverted Full Pyramid
    Input: ex-> 5
    o/p:
                * * * * * * * * *
                  * * * * * * *
                    * * * * *
                      * * *
                        *                        
'''
n = int(input('Enter no of rows : '))
stars = 1
spaces = 0
for i in range(1,n+1):
    
    for j in range(spaces):
        print(' ',end=' ')
    spaces+=1
    
    for k in range(2*n-stars):
        print('*',end=' ')
    stars+=2
    print()
    