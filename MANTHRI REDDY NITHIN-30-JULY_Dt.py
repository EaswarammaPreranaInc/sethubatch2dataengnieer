'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
# program
n=int(input("Enter Number of line:"))
for i in range(n):
  print(" " * (n-i-1),end='')
  print("*" * (2 * i-1))

How  many  lines ?  :  7
      *
     ***
    *****
   *******
  *********
 ***********
*************
