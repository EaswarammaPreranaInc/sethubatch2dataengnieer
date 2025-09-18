# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
'''
Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m
'''
from random import *
string = input('Enter any string:  ')
for i in range(len(string)):
    r = randint(0, len(string) - 1)
    print(string[r])