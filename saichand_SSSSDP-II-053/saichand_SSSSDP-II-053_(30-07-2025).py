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
a = int(input("Enter the number of rows: "))
for i in range(1, a + 1):
    print(" " * (a - i), end="")
    print("*" * (2 * i - 1))
