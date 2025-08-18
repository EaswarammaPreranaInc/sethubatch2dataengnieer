'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
from sys import argv

try:
    str1 = argv[1]
    str2 = argv[2]
    if len(str1) < 2 or len(str2) < 2:
        raise ValueError
    result = str2[:2] + str1[2:] + " and " + str1[:2] + str2[2:]
    print(result)
except ValueError:
    print("Input has a minimum of two characters")