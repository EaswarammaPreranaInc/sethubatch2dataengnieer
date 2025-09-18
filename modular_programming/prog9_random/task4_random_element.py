# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
'''
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
True
Hyd
Hyd
None
Hyd
(3+4j)
None
True
25
10.8
'''
from random import *
list = eval(input('Enter a list:  '))
for i in range(10):
    print(choice(list))