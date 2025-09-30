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
if(len(argv) == 1):
    print('Pls send inputs')
    exit()

try:
    list = [ eval(x) for x in argv[1:] ] 
    print(f'The largest input is {max(list)}')
except TypeError:
    print('Input cannot be integer and string')



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
    What  is  the  output  ?  --->  Pls  send   an  integer input
'''

from sys import argv
try:
    if(len(argv) == 1):
        print('Please enter a integer input')
        exit()
    if( int(argv[1]) % 2 == 0):
        print('Even Number')
    else:
        print('Odd Number')
except ValueError:
    print('Please enter only integer input')


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
if(len(argv) == 1):
    print('Pls send number inputs')
    exit()
try:
    list = [eval(x) for x in argv[1:]]
    sum = 0
    for x in list:
        sum += x
    print(f'Average of given inputs is {sum/len(list)}')
except:
    print('Pls send number inputs')



'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  --->  sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs together
'''

from sys import argv
try:
    if(len(argv) == 1):
        print('Please send atleast 1 input')
        exit()
    asc = sorted ( [eval(x) for x in argv[ 1: ]])
    desc = sorted( [ eval(x) for x in argv[ 1: ]], reverse=True)
    print( f'Ascending order:  {asc}' )
    print( f'Descending order:  {desc}')
except TypeError:
    print('Please don\'t send number and string inputs together')


# chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  # Z
print(chr(97))  # a
print(chr(122)) # z
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(36))  # $
print(chr(32))  # <sp>


# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  #True
print('day'   in   'Sankar  dayal  sarma')     #True
print('Green'   in   'Hyd  is  green  city')   #False
print('d  is'   in   'Hyd  is  green  city')   #True
print('dis'   in   'Hyd  is  green  city')     #False
print('iniv'   in   'Srinivas')                #True
print('iniv'   not   in 'Srinivas')            #False


# len()  function  demo  program  (Home  work)
print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len('+-$'))        # 3
print(len(''))           # 0
print(len(' '))          # 1
print(len('A2#'))        # 3
#print(len(3456))        # Error
#print('Sec'. len())     # Error, str class do not have len method


# ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
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
Hint: Use  chr()  and  ord() functions

Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result : AEMPZ_DF

Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char and digit
'''

str = input('Enter  any  string  with  alternate  character  and  digit  : ')
try:
    ans = ''
    for i in range(0, len(str), 2):
        c = str[i]
        digit = int(str[i+1])
        ans += ( c + chr( ord(c) + digit) )
    print(ans)
except ValueError:
    print('Pls  enter  string  with  alternate  char and digit')


'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint: Use slice
Enter first string: Java
Enter second string: Python
Result  : Pyva Jathon

Enter first string: A
Enter second string: HYD
Input  should  be  a  min  of 2-char string
'''

from sys import argv
if(len(argv) == 1):
    print('Please enter two strings')
    exit()
if(len( argv[1]) < 2 or len(argv[2]) < 2):
    print('Input should be a min of 2-char string')
    exit()


input1 = argv[1]
input2 = argv[2]
str1 = input2[:2] + input1[2:]
str2 = input1[:2] + input2[2:]
print(str1, str2)



'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''

from sys import argv
if(len(argv) == 1):
    print('Please enter 1 input')
    exit()
if(len(argv[1]) < 4):
    print('')
    exit()
print( argv[1][:2] + argv[1][-2:])



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

from sys import argv
if(len(argv)==1):
    print('Enter a string input')
    exit()
str = argv[1]
for i in range(len(str)):
    print(f'Character  at  index  {i}  : {str[i]}')
for i in range(1, len(str)+1):
    print(f'Character  at  index  -{i} : {str[-i]}')


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


Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd indexes : AARO
'''

from sys import argv
if(len(argv)==1):
    print('Enter a string input')
    exit()
str = argv[1]
even = ''
odd = ''
for i in range(len(str)):
    if i % 2 == 0:
        even += str[i]
    else:
        odd += str[i]
print(f'String  at  even  indexes  : {even}')
print(f'String  at  odd  indexes  : {odd}')



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
								a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char of string

                                Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result : AAAABBBCC$$$$$

Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result : AAAABBBCC$$$$$

Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character and digit

'''

str = input('Enter  any  string  with  alternate  character  and  digit : ')
ans = ''
try:
    for i in range(0, len(str), 2):
        char = str[i]
        repeat = int(str[i+1])
        ans += char*repeat
    print(f'Result : {ans}')
except ValueError:
    print('String   should  have  alternate  character and digit')



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

Enter  first  string  :  HYD
Enter  second  string  :  VAMSI
Result : HVYADMSI

Enter  first  string  :  SAIRAM
Enter  second  string  :  HYD
Result : SHAYIDRAM
'''

str1 = input('Enter  first  string  :')
str2 = input('Enter  second  string  :')
ans = ''
i = 0
while( i < len(str1) and i < len(str2)):
    ans += (str1[i] + str2[i])
    i += 1
large_str = str1 if len(str1) > len(str2) else str2
while( i < len(large_str)):
    ans += large_str[i]
    i += 1
print(ans)



'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
																							Ignore  the  character

5) Hint:  Use  not  in operator


Enter  any  string  :  MISSISIPI
String  without  duplicates : MISP
'''

str = input('Enter  any  string  :  ')
ans = ''
for c in str:
    if c not in ans:
        ans += c
print(ans)




'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])    # Rm a
print(a [ : 7])        # Rama Ra
print(a [2 : 4])       # ma
print(a [2 : ])        # ma Rao
print(a [ : 4 ])       # Rama
print(a [ : : 2])      # Rm a
print(a [-6 : -1])     # ma Ra
print(a [-6 : ])       # ma Rao
print(a [: -4 : -1])   # oaR
print(a [-3 : -1])     #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])       # Rao
print(a [ : : ])       # Rama Rao
print(a [ : ])         # Rama Rao
print(a [ : : -1])     # oaR amaR
print(a [ : : -2])     # oRaa
print(a [ -2 : : -2])  # a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])       # ma Rao
print(a [2 : 8 : -1])  # ''
print(a [ : -6 : -1])  # oaR a
print(a [2 : -3])      # ma
print(a [1 : 6 : 2])   # aaR
print(a [ : -5 : -5])  # o
print(a [2 : -5])      # m
print(a [2 : -5 : 2])  # m
print(a [ : 0 : -1])   # oaR ama
print(a [-5 : 0 : -2]) # aa