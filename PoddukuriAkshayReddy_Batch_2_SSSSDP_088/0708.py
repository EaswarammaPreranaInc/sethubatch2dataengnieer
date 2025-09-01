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

# argv[0] is the script name
argv = sys.argv
print("argv =", argv)

# Case: no inputs provided
if len(argv) == 1:
    print("Pls send inputs")
    sys.exit()

# Try converting all arguments to numbers
a = []
all_numbers = True
all_strings = True

for arg in argv[1:]:
    try:
        # Try float conversion
        val = float(arg)
        a.append(val)
        all_strings = False
    except ValueError:
        # Not a number → keep as string
        all_numbers = False

# Case: mix of numbers and strings
if not all_numbers and not all_strings:
    print("Inputs can not be number and string")

# Case: all numbers
elif all_numbers:
    print("List a =", a)
    print("Largest command line input:", max(a))

# Case: all strings
else:
    print("Largest command line input:", max(argv[1:]))





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

argv = sys.argv

# Case 3: No argument provided
if len(argv) == 1:
    print("Pls send an integer input")
    sys.exit()

try:
    # Try converting to integer
    num = int(argv[1])
 
    # Check even or odd
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except ValueError:
    # This will run for floats, words, or anything not an integer
    print("Pls send an integer input")





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

argv = sys.argv
print("argv =", argv)

# Case: no inputs
if len(argv) == 1:
    print("Pls send number inputs")
    sys.exit()

a = []
try:
    # Convert each argument (after script name) to float or bool
    for arg in argv[1:]:
        if arg == "True":
            a.append(True)
        elif arg == "False":
            a.append(False)
        else:
            a.append(float(arg))
 
    print("List a =", a)
    avg = sum(a) / len(a)
    print("Average =", avg)

except ValueError:
    print("Pls send number inputs")





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
import sys

argv = sys.argv
print("argv =", argv)

# Case: no inputs
if len(argv) == 1:
    print("Pls send number inputs")
    sys.exit()

a = []
all_numbers = True
all_strings = True

try:
    # Try converting each to float
    for arg in argv[1:]:
        try:
            a.append(float(arg))
            all_strings = False
        except ValueError:
            all_numbers = False
            a.append(arg)

    # Check for mixed types
    if not all_numbers and not all_strings:
        print("Pls don't send number and string inputs together")
    elif all_numbers:
        print("List a =", a)
        print("Ascending :", sorted(a))
        print("Descending:", sorted(a, reverse=True))
    else:
        print("List a =", a)
        print("Ascending :", sorted(a))
        print("Descending:", sorted(a, reverse=True))

except Exception as e:
    print("Error:", e)







# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city')  # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False



'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # Rm a
print(a [ : 7]) # rama Ra
print(a [2 : 4]) # ma
print(a [2 : ])  # ma Rao
print(a [ : 4 ]) # Rama
print(a [ : : 2]) # Rm a
print(a [-6 : -1]) # ma Ra
print(a [-6 : ])  # ma Rao
print(a [: -4 : -1]) # oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])  # Rao
print(a [ : : ]) # Rama Rao
print(a [ : ])   # Rama Rao
print(a [ : : -1])  # oaR amaR
print(a [ : : -2])  # oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])  # ma Ra
print(a [2 : 8 : -1]) #  empty
print(a [ : -6 : -1]) # oaR a
print(a [2 : -3]) # ma
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5]) # o
print(a [2 : -5]) # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # oaR ama
print(a [-5 : 0 : -2]) # aa



'''
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

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]

    result = new_s1 + " " + new_s2
    print("Result :", result)





'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
x = input("Enetr a string:")
if len(x) < 4:
    print('Nothing')
else:
    result = ''
    for i in range(len(x)):
        if i==0 or i==1 or i==len(x)-1 or i==len(x)-2:
            result += x[i]
print(result)
 




'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
 			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->                                                  Character  at  index  0  :  V
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
x = input("Enter a string:")
for i in range(len(x)):
    print(f'character at {i} is {x[i]}')
print('Reverse order')
for i in range(-1,-(len(x)+1),-1):
    print(f'character at {i} is {x[i]}')
 




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
Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd  indexes  : AARO

x = input("Enter a string:")
even = ''
odd = ''
for i in range(len(x)):
    if i % 2 == 0:
        even += x[i]
    else:
        odd += x[i]
print(f'Even positions letters are: {even}, Odd positions letters are: {odd}')
 



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
'''

.Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result :   AAAABBBCC$$$$$


Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character  and  digit


s = input("Enter any string with alternate character and digit: ")

# Check validity: length even, chars at even positions are alpha, odd positions are digits
if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("Pls enter string with alternate char and digit")
else:
    resultt = ""
    for i in range(0, len(s), 2):
        ch = s[i]
        num = int(s[i+1])
        resultt += ch*num
    print("Result :", resultt)





'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->  HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
---
                                    ''
0      'H'        'V'          '' + 'H' + 'V' = 'HV'

1      'Y'        'A'          'HV' + 'Y' + 'A' = 'HVYA'

2      'D'       'M'          'HVYA' + 'D' + 'M' = 'HVYADM'
---
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

x = input("Enter first string: ")
x1 = input("Enter second string: ")

merged = ""
min_len = min(len(x), len(x1))

for i in range(min_len):
    merged += x[i] + x1[i]
 
merged += x[min_len:] + x1[min_len:]

print(f"The merged string is: {merged}")




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
'''

 Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP

x = input("Enter a string:")
uni = ''
for i in range(len(x)):
    if x[i] not in  uni:
        uni += x[i]
print(f'unique letters are:{uni}')




# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247'))  # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' '))  # 1
print(len('A2#')) # 3
print(len(3456)) # error bcz it is int
print('Sec'. len()) # error


'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
'''


 # chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  #   Converts  unicode  value  65  to  'Z'
print(chr(97))  #   Converts  unicode  value  65  to  'a'
print(chr(122)) #   Converts  unicode  value  65  to  'z'
print(chr(48))  #   Converts  unicode  value  65  to  '0'
print(chr(57))  #   Converts  unicode  value  65  to  '9'
print(chr(36))  #   Converts  unicode  value  65  to  '$'
print(chr(32))  #   Converts  unicode  value  65  to  ' '




'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''

 # ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z'))  #  Converts  'A'  to  unicode  value  90
print(ord('a'))  #  Converts  'A'  to  unicode  value  97
print(ord('z'))  #  Converts  'A'  to  unicode  value  122
print(ord('0'))  #  Converts  'A'  to  unicode  value  48
print(ord('9'))  #  Converts  'A'  to  unicode  value  57
print(ord('$'))  #  Converts  'A'  to  unicode  value  36
print(ord(' '))  #  Converts  'A'  to  unicode  value  32




'''
ord()  function
---
1) What  does  ord()  function  do ?  ---> Converts  character  to  unicode  value

2) How  many  unicode  values  exist ?  ---> 512

3) What  is  the  range  of  unicode  values ?  ---> 0  to  511

4) What  are  the  unicode  values  of  'A'  -  'Z' ?  ---> 65  to  90
     What  are  the  unicode  values  of  'a'  -  'z' ?  ---> 97  to  122
     What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57

5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

Note:  chr()  and  ord()  are  quite  opposite  functions
'''


'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


   i       a[i]      a[i + 1]         out
---
                                          ''
  0       'A'           '4'          '' + 'A' + chr(65 + 4) = '' + 'A' + 'E' = 'AE'

  2       'M'           '3'          'AE' + 'M' + chr(77 + 3) = 'AE' + 'M' + 'P' = 'AEMP'

  4       'Z'           '5'          'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '' = 'AEMPZ'

  6       'D'           '2'          'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
---
Hint: Use  chr()  and  ord()  functions
'''

Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result  :   AEMPZ_DF


 Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char  and  digit



s = input("Enter any string with alternate character and digit: ")

# Check validity: length even, chars at even positions are alpha, odd positions are digits
if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("Pls enter string with alternate char and digit")
else:
    result = ""
    for i in range(0, len(s), 2):
        ch = s[i]
        num = int(s[i+1])
        result += ch
        new_ord = ord(ch) + num
        if new_ord > ord('Z'):
            result += "_"
        else:
            result += chr(new_ord)
    print("Result :", result)

 