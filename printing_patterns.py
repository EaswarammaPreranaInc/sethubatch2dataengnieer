# 1)printing patterns
n=int(input("enter no of rows: "))
for i in range(1,n+1):
  for j in range(1,i+1):
     print(j,end=" ")
  print()

enter no of rows: 6
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

2)
n=int(input("enter no of rows: "))
for i in range(n,0,-1):
  for j in range(1,i+1):
     print(j,end=" ")
  print()

enter no of rows: 4
1 2 3 4
1 2 3
1 2
1

3)
n=int(input("enter no of rows: "))
for i in range(n,0,-1):
  print(" "*(n-i),end=" ")
  for j in range(1,i+1):
     print(j,end=" ")
  print()
enter no of rows: 4
 1 2 3 4
  1 2 3
   1 2
    1

4)
n=int(input("enter no of rows: "))
for i in range(1,n+1):
  print(" "*(n-i),end=" ")
  for j in range(1,i+1):
     print(j,end=" ")
  print()
enter no of rows: 4
    1
   1 2
  1 2 3
 1 2 3 4

5)
n=int(input("enter no of rows: "))
for i in range(n+1):
  print(" "*(n-i),end=" ")
  num=1
  for j in range(i+1):
     print(num,end=" ")
     num=num*(i-j)//(j+1)
  print()
enter no of rows: 4
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

6)
n=int(input("enter no of rows: "))
for i in range(1,n+1):
  print("*"*i,end=" ")
  print()
enter no of rows: 4
*
**
***
****

7)
n=int(input("enter no of rows: "))
for i in range(n,0,-1):
  print("*"*i,end=" ")
  print()
enter no of rows: 4
****
***
**
*

8)
n=int(input("enter no of rows: "))
for i in range(1,n+1):
  print(" "*(n-i),end=" ")
  print("*"*(2*i-1),end=" ")
  print()
enter no of rows: 4
    *
   ***
  *****
 *******

9)
n=int(input("enter no of rows: "))
for i in range(n,0,-1):
  print(" "*(n-i),end=" ")
  print("*"*(2*i-1),end=" ")
  print()

enter no of rows: 4
 *******
  *****
   ***
    *

10)
# Sorting,symmetric or not,inputing matrix,transpose of a matrix:
def symmetric():
   if rows==cols:
     return True
   else:
     return False
     
rows=int(input("enter number of rows: "))
cols=int(input("enter number of columns: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
       val=int(input(f"enter value at index{i+1} and index {j+1} : "))
       row.append(val)
    matrix.append(row)
for row in matrix:
   print(row)
print(symmetric())
print("transpose of a matrix:")
transpose=[]
for i in range(rows):
   zero=[]
   for j in range(cols):
      zero.append(0)
   transpose.append(zero)
for n in range(rows):
  for m in range(cols):
      transpose[m][n]=matrix[n][m]
for row in transpose:
    print(row)  
print(" after sorting each row and printing matrix:")
for row in matrix: 
   row.sort()
for row in matrix:
    print(row)

11)
# matrix multiplication:
     
# matrix multiplication:
     
rows=int(input("enter number of rows: "))
cols=int(input("enter number of columns: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
       val=int(input(f"enter value at index{i+1} and index {j+1} : "))
       row.append(val)
    matrix.append(row)
for row in matrix:
   print(row)
print("enter 2nd matrix :")
r=int(input("enter number of rows: "))
c=int(input("enter number of columns: "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
       v=int(input(f"enter value at index{i+1} and index {j+1} : "))
       row.append(v)
    m.append(row)
for row in m:
   print(row)
r=[]
for i in range(rows):
    row=[]
    for j in range(c):
       row.append(0)
    r.append(row)

for i in range(rows):
    for j in range(c):
       for k in range(cols):
            r[i][j]+=matrix[i][k]* m[k][j]
print("after multiplication:")
       
for row in r:
   print(row)






