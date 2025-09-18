1 
#write a program to print the following pattern 
"""1
    1 2       
    1 2 3     
    1 2 3 4   
    1 2 3 4 5 
"""

"""
a=int(input("enter no.of rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()"""
2
#write a program to print the following pattern 
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1"""

"""
a=int(input("enter a no.of rows: "))
for i in range(a,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()"""

3
#write a program to print the following pattern 
"""
1 2 3 4 5 
  1 2 3 4
   1 2 3
    1 2
     1"""


"""
n=int(input("enter no.of rows: "))
for s in range(n,-1,-1):
    print(" "*(n-s),end=' ')
    for num in range(1,s+1):
        print(num,end=' ')
    print()"""


4
##write a program to print the following pattern 
"""
     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5
 """


"""row=int(input("enter no.of rows: "))
for i in range(1,row+1):
    print(" "*(row-i),end=' ')
    for num in range(1,i+1):
        print(num,end=" ")
    print()"""


5
#write a program to print the following pattern 
"""   1 
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
 """


"""
row=int(input("enter no.of rows: "))

for i in range(row+1):
    print(" "*(row-i),end=' ')
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)

    print()
"""
6
##write a program to print the following pattern 
"""
ABCDEFGFEDCBA
ABCDEF FEDCBA
ABCDE   EDCBA
ABCD     DCBA
ABC       CBA
AB         BA
A           A
"""


7
#write a program to print the following pattern 
"""
* 
**
***
****
*****
"""


"""a=int(input("enter a no.of numbers: "))
for i in range(a):
    print("*"*i,end=" ")
    print()"""


8.
#write a program to print the following pattern 
"""
***** 
****
***
**
*
"""

"""row=int(input("enter a no.of rows:"))
for sr in range(row,0,-1):
    print("*"*sr,end=" ")
    print()"""



9
#write a program to print the following pattern

"""  * 
    ***
   *****
  *******
 *********
"""

"""
row=int(input("no.of rows:"))
for p in range(1,row+1):
    print(" "*(row-p),"*"*(2*p-1),end=" ")
    
    print()
"""

10
#write a program to print the following pattern 
"""
 ********* 
  *******
   *****
    ***
     *
"""
"""
row=int(input("no.of rows:"))
for p in range(row,0,-1):
    print(" "*(row-p),"*"*(2*p-1),end=" ")
    
    print()"""

11
#write a program to print the following pattern


"""  * 
    ***
   *****
  *******
 *********
 *********
  *******
   *****
    ***
     *
     """
"""
row=int(input("no.of rows:"))
for p in range(1,row+1):
    
    print(" "*(row-p),"*"*(2*p-1),end=" ")
    print()
for p in range(row,0,-1):
    print(" "*(row-p),"*"*(2*p-1),end=" ")
    
    print()"""
    
12
#write a program to print the following pattern

""" *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
"""n = int(input("Enter size: "))  # size of diamond (half height)


for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()"""
13
#write a program to print the following pattern

"""
* * * * * 
*       *
*       *
*       *
* * * * *
"""
"""
rows=int(input("enter no of rows :"))
for row in range(rows):
    for clmn in range(rows):
        if row==0 or row==(rows-1) or clmn==0 or clmn==(rows-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""


14
#write a program to print the following pattern
"""
  * * * 
* * * * *
* * * * *
* * * * *
  * * *  
""" 

"""
rows = int(input("Enter number of rows: "))


print("  * * *")
for i in range(rows - 2):
    print("* * * * *")

print("  * * *")
"""