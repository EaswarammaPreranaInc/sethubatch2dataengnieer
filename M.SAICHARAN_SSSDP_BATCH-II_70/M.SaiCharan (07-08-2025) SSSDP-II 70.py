                        NAME:M.SAICHARAN                     HOMEWORK
                        DATE:07-08-2025

1.'''
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
#Program:

from sys import argv
if len(argv) == 1:
    print("Pls send inputs")
    exit()
inputs = argv[1:]
converted = []

for a in inputs:
    try:
        converted.append(float(a))  
    except:
        break
if len(converted) == len(inputs):
    print("argv  --->", argv)
    print("list 'a'  --->", converted)
    print("largest command line input  --->", max(converted))

elif len(converted) == 0:
    print("argv  --->", argv)
    print("largest command line input  --->", max(inputs))

else:
    print("Inputs can not be number and string")



2.'''
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

#program:

from sys import argv
if len(argv) == 1:
    print("Pls send an integer input")
    exit()
x = argv[1]
try:
    num = int(x)
except:
    print("Pls send an integer input")
    exit()
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



3.'''
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

#program:

from sys import argv
if len(argv) == 1:
    print("Pls send number inputs")
    exit()
inputs = argv[1:]
a = []  

for a in inputs:
    try:
                a.append(eval(a))
    except:
        print("Pls send number inputs")
        exit()
total = sum(a)
count = len(a)
average = total / count
print("argv ? --->", argv)
print("list 'a' ? --->", a)
print("command line inputs --->", average)


4.Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  --->  sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''
#program:

import sys

inputs = sys.argv[1:]
try:
    numbers = [float(x) for x in inputs]
except ValueError:
    print("Please provide only numbers as input.")
    exit()
    
ascending = sorted(numbers)
print("Ascending:", ascending)

descending = sorted(numbers, reverse=True)
print("Descending:", descending)



5.# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')		#True
print('day'   in   'Sankar  dayal  sarma')		#True
print('Green'   in   'Hyd  is  green  city')		#False 
print('d  is'   in   'Hyd  is  green  city')		#True
print('dis'   in   'Hyd  is  green  city')		#False
print('iniv'   in   'Srinivas')				#False
print('iniv'   not   in   'Srinivas')			#True


6.Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])	# a[0: 7 : 2] ---> string from indexes 0 to 6 in steps of 2 i.e. Rm<space>a
print(a [ : 7])		#a[0: 7 : 1] ---> string from indexes 0 to 6 in steps of 1 i.e. Rama<space>Ra
print(a [2 : 4])	#a[2:4:1] ---> string from index 2 to 3 insteps of 1 i.e.ma
print(a [2 : ])		#a[2 : 8: 1]---> string from index 2 to 7 insteps of 1 i.e. ma<space>Rao
print(a [ : 4 ])	#a[0:4:1]---> string from index 0 to 3 in steps of 1 i.e. Rama
print(a [ : : 2])	#a[0:8:2]--->string from index 0 to 7 in steps of 2 i.e. Rmaao
print(a [-6 : -1])	#a[-6 : -2 :-1]---> string from index -6 to -2 in steps of -1 i.e. ma<space>Ra
print(a [-6 : ])	#a[-6 : -1 : 1] ---> string from index -6 to -1 in steps of 1 i.e. ma<space>Rao
print(a [: -4 : -1])	#Empty string because step is -ve 
print(a [-3 : -1])	#  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])	#a[-3 : -1 : 1 ] ---> string from index -3 to -1 insteps of 1 i.e. Rao
print(a [ : : ])	#a[0 : 8 : 1] ---> string from 0 to 7 in steps of 1 i.e. Rama Rao
print(a [ : ])		#a[0 : 8 : 1] ---> string from 0 to 7 in steps of 1 i.e. Rama Rao
print(a [ : : -1])	#a[0 : -9 : -1]---> string from 0 to -8 insteps of -1 i.e. oaR amaR
print(a [ : : -2])	#a[0 : -9 : -2]---> string from 0 to -9 insteps of -2 i.e. oRa mR
print(a [ -2 : : -2])	#  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])	#a[2: 8 : 1]---> string from index 2 to 7 in steps of 1 i.e. ma<space>Rao
print(a [2 : 8 : -1])	# Empty Result because step is -ve 
print(a [ : -6 : -1])	#a[0 :-6 : -1] Empty result 
print(a [2 : -3])	#[2 : -3 : 1]---> string from 2 to -4 in steps of 1 i.e. ma<space>
print(a [1 : 6 : 2])	#a[1 : 5 : 2] ---> string from 1 to 5 in steps of 2 i.e. aaR
print(a [ : -5 : -5])	#a[0 : -5 : -5] ---> Empty result
print(a [2 : -5])	# Empty ''
print(a [2 : -5 : 2])	#Empty ''
print(a [ : 0 : -1])	# Empty '' 
print(a [-5 : 0 : -2])	# aa

7.'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
Enter first string: Java
Enter second string: Python
Result  :   Pyva Jathon

Enter first string: A
Enter second string: HYD
Input  should  be  a  min  of  2-char  string

#program:

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result :", result)


8.'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
#program:
a = input("Enter a string: ")
if len(a) < 4:
    print("")
else:
 print(a[:2] + a[-2:])



9.'''
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

Hint:  Use  two  for  loops
'''

#program:
s = input("Enter a string: ")

for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")
print()

for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")



10.Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

		      0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->
 Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->
 Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''
 Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd  indexes  : AARO

#program:

s = input("Enter any string: ")
even = ""  
odd = ""   

for i in range(len(s)):
    if i % 2 == 0:       
        even += s[i]
    else:              
        odd += s[i]
print("String at even indexes :", even)
print("String at odd indexes  :", odd)


11.'''
Let  input  be    A   4   B   3   C   2   $   5 
                  0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                               ''
     0        'A'          '4'            '' + 'A' * 4 = 'AAAA'

	 2        'B'          '3'            'AAAA' + 'B' * 3 = 'AAAA' + 'BBB' = 'AAAABBB'

	 4        'C'          '2'            'AAAABBB' + 'C' * 2 = 'AAAABBB' + 'CC' = 'AAAABBBCC'

	 6        '$'          '5'            'AAAABBBCC' + '$' * 5 = 'AAAABBBCC' + '$$$$$' = 'AAAABBBCC$$$$$'
   ---------------------------------------------------…
 Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result :   AAAABBBCC$$$$$
 Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character  and  digit

#program:
s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0:
    print("String should have alternate character and digit")
else:
    result = ""
    for i in range(0, len(s), 2):   # 0, 2, 4, 6 ...
        result += s[i] * int(s[i+1])
    print("Result :", result)








'''
12.Write  a  program  to  merge  two  strings  to  form  a  new  string

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

Hint:  Use  single  while  loop  and  slice
'''
 Enter  first  string  :  HYD
Enter  second  string  :  VAMSI
Result  :   HVYADMSI
Enter  first  string  :  SAIRAM
Enter  second  string  :  HYD
Result  :   SHAYIDRAM

#program:
a = input("Enter first string : ")
b = input("Enter second string : ")
c = ''
i = 0

while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print("Result  : ", c)




13.'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
 Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
 Ignore  the  character

5) Hint:  Use  not  in   operator
'''
Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP

#program:

s = input("Enter any string : ")
out = ''
for ch in s:
    if ch not in out:   
        out += ch         
print("String without duplicates : ", out)

14.# len()  function  demo  program  (Home  work)
print(len('Hyd'))	#  3
print(len('Rama Rao'))	#8
print(len('9247'))	#4
print(len('+-$'))	#3
print(len(''))		#0
print(len(' '))		#1
print(len('A2#'))	#3
print(len(3456))	#Error
print('Sec'. len())	#Error

'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
'''


15.# chr()  function  demo  program
print(chr(65))	#Converts  unicode  value  65  to  'A'
print(chr(90))	#converts unicode value 90 to 'z'
print(chr(97))	#converts unicode value 97 to 'a'
print(chr(122))	#converts unicode value 122 to 'z'
print(chr(48))	#converts unicode value 48 to 'o'
print(chr(57))	#converts unicode value 57 to 9
print(chr(36))	#Converts unicode value 36 to $
print(chr(32))	#converts unicode value 32 to 'space'
'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''

16.# ord()  function  demo  program
print(ord('A'))	#Converts  'A'  to  unicode  value  65
print(ord('Z'))	#converts  'z'  to unicode value 90
print(ord('a'))	#converts  'a'  to unicode value 97
print(ord('z'))	#converts  'z'  to unicode value 122
print(ord('0'))	#converts  '0'  to unicode value 48
print(ord('9'))	#converts  '9'  to unicode value 57
print(ord('$'))	#converts  '$'  to unicode value 36
print(ord(' '))	#converts  ' '  to unicode value 32

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

Note:  chr()  and  ord()  are  quite  opposite  functions
'''

17. '''
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
Hint: Use  chr()  and  ord()  functions
'''
Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result  :   AEMPZ_DF
 Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char  and  digit

#program:
s = input("Enter: ")
try:
    out = ''.join(c + (chr(ord(c) + int(s[i+1])) if ord(c) + int(s[i+1]) <= 90 else '_') 
                  for i, c in enumerate(s[::2]))
    print("Result:", out)
except:
    print("Pls enter string with alternate char and digit")



