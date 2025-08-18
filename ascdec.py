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

from sys import argv    

print(argv)
l=[]
if len(argv) == 1:
    print("Pls Enter the inputs")
else:
    for i in argv[1::]:
        l.append(eval(i))
    print(f'List is : {l}')
    print(f'Sorted List is : {sorted(l)}')
    print(f'Reverse Sorted List is : {sorted(l, reverse=True)}')


