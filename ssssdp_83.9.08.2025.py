J Mani Pavan Kumar





: '''
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
########################
import sys

argv = sys.argv
if len(argv) == 1:
    print("Pls send inputs")
else:
    all_numbers = True
    all_strings = True
    a = []

    for val in argv[1:]:
        try:
            # Try converting to float → it's a number
            num = float(val)
            a.append(num)
            all_strings = False
        except ValueError:
            # Not a number → it's a string
            a.append(val)
            all_numbers = False

    if all_numbers:
        print("argv =", argv)
        print("list 'a' =", a)
        print("Largest command line input =", max(a))
    elif all_strings:
        print("argv =", argv)
        print("list 'a' =", a)
        print("Largest command line input =", max(a))  # Lexicographical
    else:
        print("Inputs can not be number and string")




: '''
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
#################################
import sys

if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        n = int(sys.argv[1])
        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")





: '''
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
##############################
import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send number inputs")
else:
    a = []
    for val in argv[1:]:
        try:
            # Handle boolean inputs explicitly
            if val == 'True':
                a.append(True)
            elif val == 'False':
                a.append(False)
            else:
                # Try converting to float
                a.append(float(val))
        except ValueError:
            # If any input is not a valid number or boolean
            print("Pls send number inputs")
            break
    else:
        print("argv =", argv)
        print("list 'a' =", a)
        print("Average =", sum(a) / len(a))



: '''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  --->  sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''
###################################
import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send some number inputs")
else:
    a = []
    all_numbers = True
    all_strings = True

    for val in argv[1:]:
        try:
            num = float(val)
            a.append(num)
            all_strings = False
        except ValueError:
            a.append(val)
            all_numbers = False

    if all_numbers:
        print("argv =", argv)
        print("list 'a' =", a)
        print("Ascending =", sorted(a))
        print("Descending =", sorted(a, reverse=True))
    elif all_strings:
        print("argv =", argv)
        print("list 'a' =", a)
        print("Ascending =", sorted(a))
        print("Descending =", sorted(a, reverse=True))
    else:
        print("Pls don't send number and string inputs together")



: # Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  ## True
print('day'   in   'Sankar  dayal  sarma')     ## True
print('Green'   in   'Hyd  is  green  city')   ## False
print('d  is'   in   'Hyd  is  green  city')   ## True
print('dis'   in   'Hyd  is  green  city')     ## False
print('iniv'   in   'Srinivas')                ## True
print('iniv'   not   in   'Srinivas')          ## False
##################################



: '''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])
print(a [ : 7])
print(a [2 : 4])
print(a [2 : ])
print(a [ : 4 ])
print(a [ : : 2])
print(a [-6 : -1])
print(a [-6 : ])
print(a [: -4 : -1])
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])
print(a [ : : ])
print(a [ : ])
print(a [ : : -1])
print(a [ : : -2])
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])
print(a [2 : 8 : -1])
print(a [ : -6 : -1])
print(a [2 : -3])
print(a [1 : 6 : 2])
print(a [ : -5 : -5])
print(a [2 : -5])
print(a [2 : -5 : 2])
print(a [ : 0 : -1])
print(a [-5 : 0 : -2])
###################################
1.  Rm 
2.  Rama Ra
3.  ma
4.  ma Rao
5.  Rama
6.  Rm a
7.  ma Ra
8.  ma Rao
9.  o
10. Ra
11. Rao
12. Rama Rao
13. Rama Rao
14. oaR amaR
15. oRmR
16. a mR
17. ma Rao
18. (empty)
19. oa
20. ma 
21. aaR
22. o
23. (empty)
24. (empty)
25. oaR am
26. aa




: '''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
#######################
# Input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Check minimum length
if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    # Swap first 2 characters and concatenate
    result = s2[:2] + s1[2:] + ' ' + s1[:2] + s2[2:]
    print("Result :", result)



: Enter first string: Java
Enter second string: Python
Result  :   Pyva Jathon

: Enter first string: A
Enter second string: HYD
Input  should  be  a  min  of  2-char  string



: '''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
####################
s = input("Enter a string: ")

if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])




: '''
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
####################################
s = input("Enter a string: ")

# Forward direction using positive indices
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

# Reverse direction using negative indices
for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")




: '''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

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
: Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd  indexes  : AARO

##################################
s = input("Enter any string: ")

even = ''
odd = ''

for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]

print("String at even indexes :", even)
print("String at odd indexes  :", odd)



: '''
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
   -------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->
								a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''
: Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result :   AAAABBBCC$$$$$
: Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character  and  digit
####################################
s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0:
    print("String should have alternate character and digit")
else:
    out = ''
    valid = True

    for i in range(0, len(s), 2):
        ch = s[i]
        count = s[i + 1]

        if not count.isdigit():
            valid = False
            break

        out += ch * int(count)

    if valid:
        print("Result :", out)
    else:
        print("String should have alternate character and digit")




: '''
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

Hint:  Use  single  while  loop  and  slice
'''
: Enter  first  string  :  HYD
Enter  second  string  :  VAMSI
Result  :   HVYADMSI
: Enter  first  string  :  SAIRAM
Enter  second  string  :  HYD
Result  :   SHAYIDRAM
###########################
a = input("Enter first string  : ")
b = input("Enter second string : ")

c = ''
i = 0

# Loop while both strings have characters left
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1

# Concatenate remaining part of the longer string
c += a[i:] + b[i:]

print("Result  :", c)




: '''
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
: Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP

#####################################
s = input("Enter any string: ")

out = ''

for ch in s:
    if ch not in out:
        out += ch  # Add only if it's not already included

print("String without duplicates :", out)




: # len()  function  demo  program  (Home  work)
print(len('Hyd'))       # 3
print(len('Rama Rao'))  # 8
print(len('9247'))      # 4
print(len('+-$'))       # 3
print(len(''))          # 0(empty string)
print(len(' '))         # 1
print(len('A2#'))       # 3
print(len(3456))        # due to an integer not a seqence
print('Sec'. len())     # syntax error


'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
'''
[07-08-2025 12:16] +91 99482 50500: # chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  # Z
print(chr(97))  # a
print(chr(122)) # z
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(36))  # $
print(chr(32))  # (space)



'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''
: # ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32



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
: '''
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
[07-08-2025 12:27] +91 99482 50500: Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result  :   AEMPZ_DF
[07-08-2025 12:27] +91 99482 50500: Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char  and  digit

#######################

s = input("Enter any string with alternate character and digit: ")

# Check if input length is even and in correct format
if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("Please enter string with alternate character and digit")
else:
    out = ''
    for i in range(0, len(s), 2):
        ch = s[i]
        num = int(s[i+1])
        new_code = ord(ch) + num
        
        # Check if new_code is within valid Unicode range (0–511)
        if new_code > 511:
            new_ch = '_'  # Use '_' if out of range
        else:
            try:
                new_ch = chr(new_code)
            except:
                new_ch = '_'
        
        out += ch + new_ch

    print("Result :", out)
