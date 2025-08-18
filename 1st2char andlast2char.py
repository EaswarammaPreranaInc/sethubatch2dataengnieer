'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''

from sys import argv

try:
    st1=argv[1]

    if(len(st1)<4):
        raise ValueError
    res=st1[:2] +st1[-2:]
    print(res)
except ValueError:
    print("Input has a minimum of four characters")