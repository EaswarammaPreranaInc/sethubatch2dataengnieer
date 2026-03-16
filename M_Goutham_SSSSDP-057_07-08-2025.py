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
    print('Please send inputs')
else:
    a = [ ]
    num = str = False

for i in argv[1:]:
    try:
        num = a.append(float(i))
        num = True
    except:
        a.append(i)
        str = True

    if num and str:
        print('Inputs can not be number and string')
    else:
        print('List:', a)
        print('Largest:', max(a))

'''
output:

List: [10.0, 20.0, 30.8, 7.0, 40.0, 35.6]
Largest: 40.0

List: ['Rama', 'Sita', 'Rajesh', 'Manohar', 'Vamshi', 'Amar']
Largest: Vamshi
'''




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

from sys import argv
print(argv)

try: 
        if int(argv[1])%2==0:
                  print('Even Number')
        else:
                  print('Odd Number')
except:
         print('Please Send an integer input')

'''output:
['dict.py', '26']
Even Number

['dict.py', '45']
Odd Number
'''




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


from sys import argv
print(argv)

if len(argv) == 1:
    print('Pls send number inputs')
else:
    try:
        nums = []
        for x in argv[1:]:
            nums.append(eval(x))
        print(f'Average: {sum(nums) // len(nums)}')
    except:
        print('Pls send number inputs')


#output:

['dict.py', '10.8', '25', 'True', '14.6', '19', 'False', '7.4']
Average: 11.0




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
print(argv)

try:
   a = []
   for i in argv[1:]:
        a.append(eval(i))
        print('Ascending order sort:', sorted(a))
        print('Descending order sort:', sorted(a, reverse=True))
except:
        print("Please don't send number and string inputs together")


'''
output:
['dict.py', '10.8', '25', 'True', '14.6', '19', 'False', '7.4']
Ascending order sort: [False, True, 7.4, 10.8, 14.6, 19, 25]
Descending order sort: [25, 19, 14.6, 10.8, 7.4, True, False]
'''



# Find outputs  (Home  work)

print( 'green'   in   'Hyd  is  green  city')	#True
print('day'   in   'Sankar  dayal  sarma')	#True
print('Green'   in   'Hyd  is  green  city')	#False
print('d  is'   in   'Hyd  is  green  city')	#True
print('dis'   in   'Hyd  is  green  city')	#False
print('iniv'   in   'Srinivas')		#True
print('iniv'   not   in   'Srinivas')		#False





'''  (Home  work)
Slice  demo  program
0      1      2       3        4       5       6       7
R      a      m       a                R       a       o
-8    -7     -6      -5       -4      -3      -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])	#  a[ 0 :  7 : 2]   --->  string  from  indexes   0  to   6  in  steps  of  2  	i.e.  Rm<space>a
print(a [ : 7])	#  a[ 0 :  7 : 1]   --->  string  from  indexes   0  to   6  in  steps  of  1  	i.e.  Rama<space>Ra
print(a [2 : 4])	#  a[ 2 :  4 : 1]   --->  string  from  indexes   2  to   3  in  steps  of  1  	i.e.  ma
print(a [2 : ])	#  a[ 2 :  8 : 1]   --->  string  from  indexes   2  to   7  in  steps  of  1  	i.e.  ma<space>Rao
print(a [ : 4 ])	#  a[ 0 :  4 : 1]   --->  string  from  indexes   0  to   3  in  steps  of  1  	i.e.  Rama
print(a [ : : 2])	#  a[ 0 :  8 : 2]   --->  string  from  indexes   0  to   7  in  steps  of  2  	i.e.  Rm<space>a
print(a [-6 : -1])	#  a[-6 : -1 : -1] --->  string  from  indexes  -6  to  -2  in  steps  of -1  i.e.  ma<space>Ra
print(a [-6 : ])	#  a[-6 :  8 : 1]   --->  string  from  indexes  -6  to   7  in  steps  of  1  	i.e.  ma<space>Rao
print(a [: -4 : -1])	#  a[-1 : -4 : -1] --->  string  from  indexes  -1  to  -3  in  steps  of -1  i.e.  oaR
print(a [-3 : -1])	#  a[-3 : -1 :  1] --->  string  from  indexes  -3  to  -2  in  steps  of -1  i.e.  Ra
print(a [-3 : ])	#  a[-3 :  8 : 1]   --->  string  from  indexes  -3  to   7  in  steps  of  1  	i.e.  Rao
print(a [ : : ])	#  a[ 0 :  8 : 1]   --->  string  from  indexes   0  to   7  in  steps  of  1  	i.e.  Rama<space>Rao
print(a [ : ])	#  a[ 0 :  8 : 1]   --->  string  from  indexes   0  to   7  in  steps  of  1  	i.e.  Rama<space>Rao
print(a [ : : -1])	#  a[-1 : -9 : -1] --->  string  from  indexes  -1  to  -8  in  steps  of -1  i.e.  oaR<space>amaR
print(a [ : : -2])	#  a[-1 : -9 : -2] --->  string  from  indexes  -1  to  -8  in  steps  of -2  i.e.  oRaa
print(a [ -2 : : -2])	#  a[-2 : -9 : -2] --->  string  from  indexes  -2  to  -8  in  steps  of -2  i.e.  a<space>mR
print(a [2 : 8])	#  a[ 2 :  8 : 1]   --->  string  from  indexes   2  to   7  in  steps  of  1  	i.e.  ma<space>Rao
print(a [2 : 8 : -1])	#  a[ 2 :  8 :-1]   --->  string  from  indexes   2  to   7  in  steps  of -1  	i.e.  (empty)  as step is negative
print(a [ : -6 : -1])	#  a[-1 : -6 :-1]  --->  string  from  indexes  -1  to  -5  in  steps  of -1 	i.e.  oaR<space>a
print(a [2 : -3])	#  a[ 2 : -3 : 1]   --->  string  from  indexes   2  to  -4  in  steps  of  1  	i.e.  ma
print(a [1 : 6 : 2])	#  a[ 1 :  6 : 1]   --->  string  from  indexes   1  to   5  in  steps  of  2  	i.e.  aaR
print(a [ : -5 : -5])	#  a[-1 : -5 : -5] --->  string  from  indexes  -1  to  -4  in  steps  of -5 	i.e.  o
print(a [2 : -5])	#  a[ 2 : -5 : 1]   --->  string  from  indexes   2  to  -6  in  steps  of  1  	i.e.  m
print(a [2 : -5 : 2])	#  a[ 2 : -5 : 2]   --->  string  from  indexes   2  to  -6  in  steps  of  2  	i.e.  m
print(a [ : 0 : -1])	#  a[-1 :  0 : -1] --->  string  from  indexes  -1  to   1  in  steps  of -1  	i.e.  oaR<space>ama
print(a [-5 : 0 : -2])#  a[-5 :  0 : -2] --->  string  from  indexes  -5  to   1  in  steps  of -2  i.e.  aa






'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''

s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

if len(s1) < 2 or len(s2) < 2:
	print('Input should be a min of 2-char string')
else:
    out = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
print("Result:", out)
'''
output:
Enter first string: Java
Enter second string: Python
Result  :   Pyva Jathon

Enter first string: A
Enter second string: HYD
Input  should  be  a  min  of  2-char  string
'''





'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''

a = input('Enter any string: ')

if len(a) < 4:
	print("")
else:
   	print(a[:2] + a[-2:])

'''
output:
Enter any string: PYTHON
PYON
'''


'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice

       	     		 0      1     2      3     4
Let  input  be		  V     A     M     S     I
			 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                 Character  at  index  1   :  A
								                 Character  at  index  2   :  M
							              	                 Character  at  index  3   :  S
								                 Character  at  index  4   :  I
								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
								                 Character  at  index  -5  :  V

Hint:  Use  two  for  loops
'''

a = input("Enter any string: ")
print("Forward direction:")
for i in range(len(a)):
	print(f"Character at index {i} : {a[i]}")
print("\nReverse direction:")
for i in range(-1, -len(a)-1, -1):
    	print(f"Character at index {i} : {a[i]}")

'''
output:
Enter any string: VAMSHI
Forward direction:
Character at index 0 : V
Character at index 1 : A
Character at index 2 : M
Character at index 3 : S
Character at index 4 : H
Character at index 5 : I

Reverse direction:
Character at index -1 : I
Character at index -2 : H
Character at index -3 : S
Character at index -4 : M
Character at index -5 : A
Character at index -6 : V

'''



'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

		0      1      2      3     4     5     6      7
Let  input  be           R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->
				Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->
				Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''

a = input("Enter any string: ")

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
output:

Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd  indexes  : AARO

'''


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

a = input("Enter any string with alternate character and digit: ")

if len(a) % 2 != 0:
	print("String should have alternate character and digit")

else:
    out = ""
    for i in range(0, len(a), 2):
        out += a[i] * int(a[i+1])
print("Result:", out)
'''
output:

Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result :   AAAABBBCC$$$$$

Enter  any  string  with  alternate  character  and  digit :  HYD
String   should  have  alternate  character  and  digit

'''



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
'''

a = input("Enter first string: ")
b = input("Enter second string: ")

i = 0
c = ""
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1

c += a[i:] + b[i:]
print("Result:", c)

'''
output:

Enter  first  string  :  HYD
Enter  second  string  :  VAMSI
Result  :   HVYADMSI

Enter  first  string  :  SAIRAM
Enter  second  string  :  HYD
Result  :   SHAYIDRAM
'''



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

s = input("Enter any string: ")
out = ""

for ch in s:
    if ch not in out:
        out += ch

print("String without duplicates:", out)

'''
output:

Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP
'''



# len()  function  demo  program  (Home  work)

print(len('Hyd'))	# 3
print(len('Rama Rao'))	# 8
print(len('9247'))	# 4
print(len('+-$'))	# 3
print(len(''))		# 0
print(len(' '))		# 1
print(len('A2#'))	# 3
print(len(3456))		# error as we can't use len for int
print('Sec'. len('12'))	# error as syntax for str len is not valid




# chr()  function  demo  program

print(chr(65))	#   Converts  unicode  value  65  to  'A'
print(chr(90))	#   Converts  unicode  value  90  to  'Z'
print(chr(97))	#   Converts  unicode  value  97  to  'a'
print(chr(122))	#   Converts  unicode  value  122 to  'z'
print(chr(48))	#   Converts  unicode  value  48  to  '0'
print(chr(57))	#   Converts  unicode  value  57  to  '9'
print(chr(36))	#   Converts  unicode  value  36  to  '$'
print(chr(32))	#   Converts  unicode  value  32  to  'space'




# ord()  function  demo  program

print(ord('A'))	#  Converts  'A'  to  unicode  value  65
print(ord('Z'))	#  Converts  'Z'  to  unicode  value  90
print(ord('a'))	#  Converts  'a'  to  unicode  value  97
print(ord('z'))	#  Converts  'z'  to  unicode  value  122
print(ord('0'))	#  Converts  '0'  to  unicode  value  48
print(ord('9'))	#  Converts  '9'  to  unicode  value  57
print(ord('$'))	#  Converts  '$'  to  unicode  value  36
print(ord(' '))	#  Converts  ' '  to  unicode  value  32



'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A     4     M     3    Z    5    D     2


   i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                          ''
  0       'A'           '4'          '' + 'A' + chr(65 + 4) = '' + 'A' + 'E' = 'AE'

  2       'M'           '3'          'AE' + 'M' + chr(77 + 3) = 'AE' + 'M' + 'P' = 'AEMP'

  4       'Z'           '5'          'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '_' = 'AEMPZ_'

  6       'D'           '2'          'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions

'''

s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0:
    print("Pls enter string with alternate char and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] + chr(ord(s[i]) + int(s[i+1]))
    print("Result:", out)

'''
output:

Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2
Result  :   AEMPZ_DF

Enter  any  string  with  alternate  character  and  digit  :  HYD
Pls  enter  string  with  alternate  char  and  digit
'''