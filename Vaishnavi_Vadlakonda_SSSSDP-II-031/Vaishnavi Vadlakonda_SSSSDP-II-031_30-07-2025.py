'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number of lines
'''
lines = int(input("How many lines?:"))
for i in range(lines):
    print(" " * (lines - i -1), end = "" )
    print("*" * (2 * i - 1))