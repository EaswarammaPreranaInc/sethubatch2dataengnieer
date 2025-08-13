# Write  a  program  to  print  full  pyramid
    *
   ***
  *****
 *******
********* 
try:
    x = int(input('enter the no. of rows ='))
    for i in range(1,x+1):
        print( ' ' * (x - i ) + '*' * (2 * i - 1) + ' ' * (x + i + 1))
except:
    print('values must be integer.')
