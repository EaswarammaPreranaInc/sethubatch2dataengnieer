'''
Write  a  program  to  print  full  pyramid
     *
   ***
  *****
 *******
*********
Input  is  number of lines
'''
n = int(input("Enter number of Rows:"))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)