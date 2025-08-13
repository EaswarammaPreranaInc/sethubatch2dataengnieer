"""
#1.wap a pattern program
How  many  lines ?  :5
    *
   **
  ***
 ****
*****
"""
n=int(input('enter no:'))
for i in range(1,n+1):
    print(' '(n-i)+(" "*i))
print()