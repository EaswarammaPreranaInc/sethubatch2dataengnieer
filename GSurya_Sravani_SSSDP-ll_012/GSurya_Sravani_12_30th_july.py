'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''

n = int(input("Enter number of lines: "))  # User enters how many rows

for i in range(n):         
    spaces = ' ' * (n - i - 1)  
    stars = '*' * (2 * i + 1)     
    print(spaces + stars)