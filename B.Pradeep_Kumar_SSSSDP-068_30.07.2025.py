'''
Write  a  program  to  print  full  pyramid
    *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''

x=int(input("enter a number to print Peramid : "))

for i in range(x):
    print(" "*(x-i)+"*"*(2*i+1))
