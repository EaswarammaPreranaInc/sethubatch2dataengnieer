#Name: Kamuju Sushma
#Home Work
'''
Write  a  program  to  print  full  pyramid
    *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
n=int(input("Enter n: "))
for i in range(n):
    print(' '*(n-i-1) ,end='')
    print('*'*(2*i+1),end='')
    print(' '*(n-i-1),end='')
    print()