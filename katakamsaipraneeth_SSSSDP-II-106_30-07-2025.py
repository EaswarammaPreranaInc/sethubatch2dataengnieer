'''
Write  a  program  to  print  full  pyramid
    *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
#########program #############
n = int(input("How many lines:"))
for i in range(n):
    spaces = ' ' * (n - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)