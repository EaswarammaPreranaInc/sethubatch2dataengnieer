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

args = sys.argv[1:]

if not args:
    print("Pls send number inputs")
else:
    try:
        nums = [float(x) for x in args]
        print("Ascending:", sorted(nums))
        print("Descending:", sorted(nums, reverse=True))
    except ValueError:
        if all(x.isalpha() for x in args):
            print("Ascending:", sorted(args))
            print("Descending:", sorted(args, reverse=True))
        else:
            print("Pls don't send number and string inputs together")
