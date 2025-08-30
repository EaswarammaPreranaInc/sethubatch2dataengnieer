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

6) Hint2: Use  try and except
'''
from sys import argv
print(argv)
a = argv[1:]
print(a)
try:
    newlist = []
    for i in a:
        newlist.append(eval(i))
    print(newlist)
    print("Largest number is:",max(newlist))
except ValueError:
    print("Pls send inputs")
except TypeError:
    print("Inputs cannot be number and string")










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
    What  is  the  output  ?  --->  Pls  send   an  integer  input
'''
from sys import argv
print(argv)
a = argv[1:]
print(a)
try:
    for i in a:
        a = int(i)
        print(a)
        if a % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
except ValueError:
    print("Please send an integer input")














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
    What  is  the  output  ?  --->  Pls  send  number inputs
'''
from sys import argv
print(argv)
a = argv[1:]
newlist = []
try:
    for i in a:
        newlist.append(eval(i))
    print(newlist)
    print("Sum:", sum(newlist))
    print("Number of elements:", len(newlist))
    print("Average:",sum(newlist)/len(newlist))
except TypeError:
    print("Pls  send  number inputs")
except ZeroDivisionError:
    print("Pls send number inputs")












'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  --->  sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''
from sys import argv
print(argv)
a = argv[1:]
print(a)
try:
    newlist = []
    for i in a:
        newlist.append(float(i))
    print(sorted(newlist))
    print(sorted(newlist, reverse = True))
except ValueError:
    print("Pls don't send number and string inputs together")















# Find outputs  (Home  work)
print( 'green' in 'Hyd  is  green  city') # prints True
print('day' in 'Sankar  dayal  sarma') # prints True
print('Green' in 'Hyd  is  green  city') # prints False
print('d  is' in 'Hyd  is  green  city') # prints True
print('dis' in 'Hyd  is  green  city') # prints False
print('iniv' in 'Srinivas') # prints True
print('iniv' not in 'Srinivas') # prints False













'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6       -5      -4      -3       -2     -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # a[0 : 7 : 2] prints string from indexes  0 to 6 in steps of 2 i.e., Rm<space>a
print(a [ : 7]) # a[0 : 7 : 1] `prints string from indexes  0 to 6 in steps of 1 i.e., Rama<space>Ra
print(a [2 : 4]) # a[2 : 4 : 1] prints string from indexes  2 to 3 in steps of 1 i.e., ma
print(a [2 : ]) #a[2 : 8 : 1] prints string from indexes  2 to 7 in steps of 1 i.e., ma<space>Rao
print(a [ : 4 ]) #a[0 : 4 : 1] prints string from indexes  0 to 3 in steps of 1 i.e., Rama
print(a [ : : 2]) # a[0 : 8 : 2] prints string from indexes  0 to 7 in steps of 2 i.e., Rm<space>a
print(a [-6 : -1]) #a[-6 : -1 : 1] prints string from indexes  -6 to -2 in steps of 1 i.e., ma<space>Ra
print(a [-6 : ]) #a[-6 : 8 : 1] prints empty string because it never reaches index ma<space>Rao
print(a [: -4 : -1]) # a[-1 : -4 : -1] prints string from indexes  -1 to -3 in steps of -1 i.e., oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1] prints string from indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ]) #  a[-3 : 8 : 1] prints string from indexes -3 to -8 in steps of 1 i.e., Rao
print(a [ : : ]) # a[0 : 8 : 1] prints string from indexes 0 to 8 in steps of 1 i.e., Rama<space>Rao
print(a [ : ]) # a [0 : 8 : 1] prints string from indexes 0 to 8 in steps of 1 i.e., Rama<space>Rao
print(a [ : : -1]) # a[-1 : -9 : -1] prints string from indexes -1 to -8 in steps of -1 i.e., oaR<space>amaR
print(a [ : : -2]) # a[-1 : -9 : -1] prints string from indexes -1 to -8 in steps of -2 i.e., oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2] prints string  from indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8]) # a[2 : 8 : 1] prints string from indexes 2 to 7 in steps of 1 i.e.,ma<space>Rao
print(a [2 : 8 : -1]) # a[2 : 8 : -1] # prints empty string because it never reaches index 7
print(a [ : -6 : -1]) # a[-1 : -6 : -1] prints string from indexes -1 to -5 in steps of -1 i.e., oaR<space>a
print(a [2 : -3]) # a[2 : -3 : 1] prints string from indexes 2 to -4 in steps of 1 i.e., ma
print(a [1 : 6 : 2]) # a[1 : 6 : 2] prints string from indexes 1 to 6 in steps of 2 i.e., aaR
print(a [ : -5 : -5]) # a[-1 : -5 : -5] prints string from indexes -1 to -4 in steps of -5 i.e., o
print(a [2 : -5]) # a[2 : -5 : 1] prints string from indexes 2 to -6 in steps of 1 i.e., m
print(a [2 : -5 : 2]) # a[2 : -5 : 2] prints string from indexes 2 to -6 in steps of 2 i.e., m
print(a [ : 0 : -1]) # a[0 : 0 : -1] prints string from indexes 0 to -7 in steps of -1 i.e., oaR<space>ama
print(a [-5 : 0 :-2]) # a[-5 : 0 : -2] prints string from indexes -5 to -7 in steps of -2 i.e., aa













'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint: Use slice
'''
'''
Enter first string: Java
Enter second string: Python
Result  : Pyva Jathon

Enter first string: A
Enter second string: HYD
Input should be a min of 2-char string
'''
a = input("Enter first string:") # Java
b = input("Enter second string:") # Python
if len(a) < 2 or len(b) < 2:
    c = b[:2] + a[2:] # Py + va
    d = a[:2] + b[2:] # Ja + thon
    print("Result:", c, d)
else:
    print("Input should be a min of 2-char string")
    











'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''
a = input("Enter input:")
if len(a) >= 4:
    c = a[:2] + a[len(a)-2 :]
    print(c)
else:
    print("")
















'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                 Character  at  index  1  :  A
								                 Character  at  index  2  :  M
							                     Character  at  index  3  :  S
								                 Character  at  index  4  :  I

								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
								                 Character  at  index  -5  :  V

Hint:  Use  two for loops
'''
a = input("Enter any string:")
for i in range(len(a)):
    print("Character at index",i,":", a[i])
for j in range(1, len(a) + 1):
    print("Character at index", -j, ":", a[-j])















'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->
																	Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->
																	Concatenate  the  characeter  to  odd  object

3) Hint: Use  single for loop
'''
'''
Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd indexes : AARO
'''
a = input("Enter any string:")
even = ""
odd = ""
for i in range(len(a)):
    if i % 2 == 0:
        even += a[i]
    else:
        odd += a[i]  
print("String at even indexes:", even)      
print("String at odd indexes:", odd)  














'''
Let  input  be    A   4   B   3   C   2   $   5
                  0   1   2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                               ''
     0        'A'          '4'            '' + 'A' * 4 = 'AAAA'

	 2        'B'          '3'            'AAAA' + 'B' * 3 = 'AAAA' + 'BBB' = 'AAAABBB'

	 4        'C'          '2'            'AAAABBB' + 'C' * 2 = 'AAAABBB' + 'CC' = 'AAAABBBCC'

	 6        '$'          '5'            'AAAABBBCC' + '$' * 5 = 'AAAABBBCC' + '$$$$$' = 'AAAABBBCC$$$$$'
   -------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->
								a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''
'''
Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result : AAAABBBCC$$$$$

Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character and digit'
'''
a = input("Enter any string:")
b = ""
for i in range(0,len(a),2):
    b += a[i] * int(a[i + 1])
print(b)

















'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->  HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0      'H'        'V'          '' + 'H' + 'V' = 'HV'

1      'Y'        'A'          'HV' + 'Y' + 'A' = 'HVYA'

2      'D'       'M'          'HVYA' + 'D' + 'M' = 'HVYADM'
--------------------------------------------------------
Concatenate  remainging  characters   of  the  other  string  to  object  'c'
What  is  the  final  result ?  --->  'HVYADMSI'

Hint:  Use  single  while  loop and slice
'''
'''
Enter  first  string  :  HYD
Enter  second  string  :  VAMSI
Result : HVYADMSI

Enter  first  string  :  SAIRAM
Enter  second  string  :  HYD
Result : SHAYIDRAM
'''
a = input("Enter first string:")
b = input("Enter second string:")
result = ""
for i in range(len(a)):
    for j in range(len(b)):
       if i == j:
          result += a[i] + b[i]
result += a[i + 1:] + b[i + 1:]
print(result)
















'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
																							Ignore  the  character

5) Hint:  Use  not  in  operator
'''
'''
Enter  any  string  :  MISSISIPI
String  without  duplicates : MISP
'''
a = input("Enter any string:")
result = ""
for i in a:
    if i not in result:
        result += i
print(result)















# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  prints 3
print(len('Rama Rao')) # prints 8
print(len('9247')) # prints 4
print(len('+-$')) # prints 3
print(len('')) # prints 0
print(len(' ')) # prints 1
print(len('A2#')) # prinnts 3
print(len(3456)) # Error because non sequence has no len() function
print('Sec'. len()) # Error because len should have one string attribute

'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in the string
'''















# chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90)) # Converts unicode value 90 to 'Z'
print(chr(97)) # Converts unicode value 97 to 'a'
print(chr(122)) # Converts unicode value 122 to 'z'
print(chr(48)) # Converts unicode value 48 to 0
print(chr(57)) # Converts unicode value 57 to 9
print(chr(36)) # Converts unicode value 36 to $
print(chr(32)) # Converts unicode value 32 to space

'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''














# ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z')) # Converts 'Z' to unicode value 90
print(ord('a')) # Converts 'a' to unicode value 97
print(ord('z')) # Converts 'z' to unicode value 122
print(ord('0')) # Converts '0' to unicode value 48
print(ord('9')) # Converts '9' to unicode value 57
print(ord('$')) # Converts '$' to unicode value 36
print(ord(' ')) # Converts ' ' to unicode value 32

'''
ord()  function
------------------
1) What  does  ord()  function  do ?  ---> Converts  character  to  unicode  value

2) How  many  unicode  values  exist ?  ---> 512

3) What  is  the  range  of  unicode  values ?  ---> 0  to  511

4) What  are  the  unicode  values  of  'A'  -  'Z' ?  ---> 65  to  90
     What  are  the  unicode  values  of  'a'  -  'z' ?  ---> 97  to  122
     What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57

5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

Note:  chr()  and  ord()  are  quite  opposite functions
'''














'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


   i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                          ''
  0       'A'           '4'          '' + 'A' + chr(65 + 4) = '' + 'A' + 'E' = 'AE'

  2       'M'           '3'          'AE' + 'M' + chr(77 + 3) = 'AE' + 'M' + 'P' = 'AEMP'

  4       'Z'           '5'          'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '' = 'AEMPZ'

  6       'D'           '2'          'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord() functions
'''
'''
Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result : AEMPZ_DF

Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char and digit
'''
a = input("Enter string: ")
result = ""
try:
  for i in range(0, len(a), 2):
      result += a[i] + chr(ord(a[i]) + int(a[i + 1]))
  print("Result:", result)
except ValueError:
   print("Pls  enter  string  with  alternate  char and digit")
