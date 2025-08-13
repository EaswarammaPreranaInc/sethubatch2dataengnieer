



: '''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
: How  many  lines ?  :  7
      *
     ***
    *****
   *******
  *********
 ***********
*************


#########
# Full Pyramid Pattern

lines = int(input("How many lines? : "))

for i in range(lines):
    # Print spaces first
    print(' ' * (lines - i - 1), end='')
    # Print stars: 2*i + 1 stars per line
    print('*' * (2 * i + 1))



      *
     ***
    *****
   *******
  *********
 ***********
*************
