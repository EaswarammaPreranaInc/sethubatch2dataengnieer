'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  --->  sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''

import sys 

try:
    a = []
    for i in sys.argv[1:]:
        a.append(float(i))
    print('agrv list is : ',sys.argv)
    print('list a is : ',a)
    print('Ascending order : ',sorted(a))
    print('Decending order : ',sorted(a,reverse=True))
except ValueError:
    print(" Pls  don't  send  number  and  string  inputs  together")