'''
Write  a  program  to  determine  average  of  command  line  inputs

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

argv = sys.argv[1:]  # skip program name

if len(argv) == 0:
    print("Pls  send  an  integer  input")
else:
    try:
        a=[]
        for i in argv:
            a.append(float(i))
        print(f'Length : {len(a)}')
        print(f'Sum : {sum(a)}')
        print(f'Average : {sum(a)/len(a)}')
    except ValueError: 
        print("Pls  send   an  integer  input")
