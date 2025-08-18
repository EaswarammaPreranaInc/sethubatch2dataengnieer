'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                 Character  at  index  1  :  A
								                 Character  at  index  2  :  M
							                     Character  at  index  3  :  S
								                 Character  at  index  4  :  I

								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
								                 Character  at  index  -5  :  V

Hint:  Use  two  for  loops
'''

from sys import argv

try:
    st1=argv[1]
    for i in range(len(st1)):
        print(f'Character  at  index {i} : {st1[i]}')
    print()
    for j in range(1,len(st1)+1):
        print(f'Character  at  index {-j} : {st1[-j]}')
except IndexError:
    print("Please provide a string as a command line argument.")    