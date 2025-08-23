
'''
Write  a  program  to  print  full  pyramid
    *
   ***
  *****
 *******
*********
Input is number of lines
'''
n = int(input('How many lines : '))
i = 0
while i < n:
	a = n - i - 1 
	print(' ' * a , end = '')
	print('*' * (2 * i + 1))
	i += 1
