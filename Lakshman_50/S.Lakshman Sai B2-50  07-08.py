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
from sys import argv
if len(argv) == 1:
     print("Please send inputs")
else:
     inputs = argv[1:]
     num_count = 0
     str_count = 0
     values = []
     for item in inputs:
          try:
                val = float(item)
                values.append(val)
                num_count += 1
          except ValueError:
                values.append(item)
                str_count += 1
     if num_count > 0 and str_count > 0:
          print("Inputs cannot be a mix of numbers and strings")
     elif num_count > 0:
          print(f"Largest number: {max(values)}")
     else:
          print(f"Largest string: {max(values)}")


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
if len(argv) == 1:
    print("Pls send an integer input")
else:
    try:
        num = int(argv[1])
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")


            
'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
    How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  ---> Pls  send number inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send number inputs
'''
from sys import argv
if len(argv) == 1:
    print("Pls send number inputs")
else:
    values = []
    for item in argv[1:]:
        try:
            values.append(float(item))
        except ValueError:
            print("Pls send number inputs")
            break
    else:
        avg = sum(values) / len(values)
        print(f"Average: {avg}")



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
from sys import argv
if len(argv) == 1:
    print("Pls send inputs")
else:
    inputs = argv[1:]
    num_count = 0
    str_count = 0
    values = []
    for item in inputs:
        try:
            val = float(item)
            values.append(val)
            num_count += 1
        except ValueError:
            values.append(item)
            str_count += 1
    if num_count > 0 and str_count > 0:
        print("Pls don't send number and string inputs together")
    elif num_count > 0:
        print(f"Ascending order: {sorted(values)}")
        print(f"Descending order: {sorted(values, reverse=True)}")
    else:
        print(f"Ascending order: {sorted(values)}")
        print(f"Descending order: {sorted(values, reverse=True)}")


# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True 
print('day'   in   'Sankar  dayal  sarma')   # True
print('Green'   in   'Hyd  is  green  city')  # False
print('d  is'   in   'Hyd  is  green  city')  # True
print('dis'   in   'Hyd  is  green  city')    # False
print('iniv'   in   'Srinivas')               # True
print('iniv'   not   in   'Srinivas')         # False


'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])       # RmRao
print(a [ : 7])           # Rama Ra
print(a [2 : 4])          # ma
print(a [2 : ])           # ma Rao
print(a [ : 4 ])          # Rama
print(a [ : : 2])         # RmRao
print(a [-6 : -1])        # ma Ra
print(a [-6 : ])          # ma Rao
print(a [: -4 : -1])      # (empty string, as step is -1 but start < stop)
print(a [-3 : -1])        # Ra
print(a [-3 : ])          # Rao
print(a [ : : ])          # Rama Rao
print(a [ : ])            # Rama Rao
print(a [ : : -1])        # oaR amaR
print(a [ : : -2])        # oRa mR
print(a [ -2 : : -2])     # a mR
print(a [2 : 8])          # ma Rao
print(a [2 : 8 : -1])     # (empty string, as step is -1 but start < stop)
print(a [ : -6 : -1])     # (empty string, as step is -1 but start < stop)
print(a [2 : -3])         # ma 
print(a [1 : 6 : 2])      # a a
print(a [ : -5 : -5])     # (empty string, as step is -5 but start < stop)
print(a [2 : -5])         # m
print(a [2 : -5 : 2])     # m
print(a [ : 0 : -1])      # (empty string, as step is -1 but start < stop)
print(a [-5 : 0 : -2])    # mR

'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) < 2 or len(s2) < 2:
    print("Each string must have at least two characters")
else:
    swap_s1 = s2[:2] + s1[2:]
    swap_s2 = s1[:2] + s2[2:]
    print(f"{swap_s1} {swap_s2}")

'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
s = input("Enter a string: ")
if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])



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

Hint:  Use  two  for  loops
'''

s = input("Enter a string: ")
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")           
for i in range(len(s)):
    print(f"Character at index {-i-1} : {s[-i-1]}")           



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

3) Hint: Use  single  for  loop
'''

s = input("Enter a string: ")
even = ''
odd = ''
for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i] 
print(f"Even indexed characters: {even}")
print(f"Odd indexed characters: {odd}")


'''
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

                                Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result :   AAAABBBCC$$$$$
Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character  and  digit
                                '''

s = input("Enter a string with alternate character and digit: ")
out = ''
try:
    if len(s) % 2 != 0:
        raise ValueError
    for i in range(len(s), 2):
        out += s[i] * int(s[i + 1])
    print(out)
except (ValueError):
    print("String should have alternate character and digit")

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

Hint:  Use  single  while  loop  and  slice

Enter  first  string  :  HYD
Enter  second  string  :  VAMSI
Result  :   HVYADMSI

Enter  first  string  :  SAIRAM
Enter  second  string  :  HYD
Result  :   SHAYIDRAM
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
c = ''
i = 0
while i < len(s1) and i < len(s2):
     c += s1[i] + s2[i]
     i += 1
c += s1[i:] + s2[i:]
print(f"Result :  {c}")


'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
                                                                    Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
                                                                                            Ignore  the  character

5) Hint:  Use  not  in   operator

Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP
'''
s = input("Enter any string: ")
out = ''
for ch in s:
     if ch not in out:
          out += ch
print(f"String without duplicates : {out}")


# len()  function  demo  program  (Home  work)
print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len('+-$'))        # 3
print(len(''))           # 0
print(len(' '))          # 1
print(len('A2#'))        # 3
print(len(3456))       # TypeError: object of type 'int' has no len()
print('Sec'. len())    # SyntaxError: invalid syntax


# chr()  function  demo  program
print(chr(65))   # A
print(chr(90))   # Z
print(chr(97))   # a
print(chr(122))  # z
print(chr(48))   # 0
print(chr(57))   # 9
print(chr(36))   # $
print(chr(32))   #  

# ord()  function  demo  program
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32

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
Hint: Use  chr()  and  ord()  functions
Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result  :   AEMPZ_DF

Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char  and  digit
'''
s = input("Enter any string with alternate character and digit: ")
out = ''
try:
     if len(s) % 2 != 0:
          raise ValueError
     for i in range(0, len(s), 2):
          ch = s[i]
          num = int(s[i+1])
          next_ch_code = ord(ch) + num
          if 65 <= next_ch_code <= 90:
                out += ch + chr(next_ch_code)
          else:
                out += ch + '_'
     print(f"Result  :   {out}")
except (IndexError, ValueError):
     print("Pls enter string with alternate char and digit")