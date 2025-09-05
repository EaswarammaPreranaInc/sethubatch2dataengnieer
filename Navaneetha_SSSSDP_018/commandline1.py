'''
Write  a  program  to  determine  largest  command  line  input

1) py   prog2.py   10     20     30.8   7  40    35.6
    What  is  the  largest  command  line  input ?  ---> 40
    What  is  argv ?  --->  ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?   ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  ---> '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->
											Largest  string  is  obtained  but  not  largest  number

2) py  prog2.py
    What  is  the  output ?  ---> Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  largest  command  line  input ?  --->  'Vamsi'

4) py   prog2.py   25   'Ten'
    What  is  the  output ?  --->  Inputs  can  not  be  number  and  string

5) Hint1: Use  for  loop

6) Hint2: Use  try  and  except
'''
import sys

a = sys.argv[1:]  # command line inputs

if len(a) == 0:
    print("Pls send inputs")
elif all(x.replace('.', '', 1).isdigit() for x in a):  # all numbers
    largest = float(a[0])
    for val in a[1:]:
        if float(val) > largest:
            largest = float(val)
    print("Largest command line input:", largest)
elif all(x.isalpha() for x in a):  # all words
    largest = a[0]
    for val in a[1:]:
        if val > largest:
            largest = val
    print("Largest command line input:", largest)
else:
    print("Inputs can not be number and string")
