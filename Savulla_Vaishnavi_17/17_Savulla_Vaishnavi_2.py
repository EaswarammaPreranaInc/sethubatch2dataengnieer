'''
Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

1) py  prog3.py  26
    What  is  the  output ?  ---> Even  number

2) py  prog3.py  45
    What  is  the  output ?  ---> Odd  number

3) py  prog3.py
    What  is  the  output  ?  ---> Pls  send  an  integer  input

4) py  prog3.py  10.8
    What  is  the  output ?  --->  Pls  send   an  integer  input

5) py  prog3.py  Ten
    What  is  the  output  ?  --->  Pls  send   an  integer  input
'''
import sys

argv = sys.argv[1:]  # skip program name

if len(argv) == 0:
    print("Pls  send  an  integer  input")
else:
    try:
        a=[]
        for i in range(len(argv)):
            if int(argv[i])%2==0:
                 print("Even number")
            else:
                 print("Odd number")
    except ValueError: 
        print("Pls  send   an  integer  input")

    