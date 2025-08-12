             Name: M.SAICHARAN                HOMEWORK
             Date: 30-07-2025            


1.'''
Write  a  program  to  print  full  pyramid
	 *
   *
  ***
 ***
***
Input  is  number  of  lines
'''

program:
a = int(input("Enter the number of lines for the pyramid: "))
for i in range(1, a + 1):
    spaces = ' ' * (a - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
output:
 Enter the number of lines for the pyramid: 7
      *
     ***
    *****
   *******
  *********
 ***********
*************
