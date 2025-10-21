'''
#FIBONACCI SERIES:
------------------
n=int(input("enter a number:"))
a,b = 0,1
for i in range (n):
    print(a,end=" " )
    a,b = b,a+b
------------------------------
'''
n=int(input("enter the number:"))
for rows in range (1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,2*rows):
        print(cols,end="")
    print()    
        

