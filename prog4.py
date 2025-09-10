'''Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  ---> Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send  number  inputs
'''

import sys
try:
    if len(sys.argv) < 2:
        print("Pls send number inputs")
    else:
        a = []
        for x in sys.argv[1:]:
            try:
                a.append(eval(x))
            except:
                pass
        if len(a) != len(sys.argv[1:]):
            print("Pls send number inputs")
        else:
            print(sum(a) / len(a))
except:
    print("Error")