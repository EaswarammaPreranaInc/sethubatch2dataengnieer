#Home Work-1
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
if len(argv) ==1:
    print("Pls  send  inputs")
res=argv[1]
print(argv)
# temp=
l=[]
for i in range(1,len(argv)):
    # res=max(res,argv[i])
    x=eval(argv[i])
    l.append(x)
try:
    print(max(l))
except TypeError:
    print("Inputs  can  not  be  number  and  string") #handle when string, int are passed 

#Home Work-2
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
if len(argv)==1 :
    print("Pls  send  an  integer  input")
try: 
    x=int(argv[1])
except:
    print("Pls  send  an  integer  input")
    exit()
if x%2==0:
    print("Even number")
else:
    print("Odd number")

#Home Work-3

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
l=[]
if len(argv)==1:
    print("Pls  send  number  inputs")
    exit()
for i in range(1,len(argv)):
    l.append(eval(argv[i]))
try:
    print(sum(l)/len(l))
except TypeError:
    print("Pls  send  number  inputs")

#Home Work-4
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
l=[]
for i in range(1,len(argv)):
    l.append(eval(argv[i]))
try:
    l=sorted(l) 
    print(f'Ascending Order: {l}')
    l=sorted(l, reverse=True)
    print(f'Descending Order: {l}')
except TypeError:
    print(" Pls  don't  send  number  and  string  inputs  together")

#Home Work-5
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') #False
print('d  is'   in   'Hyd  is  green  city') #False
print('dis'   in   'Hyd  is  green  city') #False
print('iniv'   in   'Srinivas')#True
print('iniv'   not   in   'Srinivas')#False

#Home Work-6
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # 0 to 6 in steps of 2, Rama Ra
print(a [ : 7]) # 0 to 6 in steps of 1, Rama Ra
print(a [2 : 4]) # 2 to 3 in steps of 1, ma
print(a [2 : ]) # 2 to 7 to in steps of 1, ma Rao
print(a [ : 4 ]) # 0 to 3 in steps 1, Rama
print(a [ : : 2]) # 0 to 7 in steps of 2, Rm R 0
print(a [-6 : -1]) # -6 to -2 in steps 1, ma Ra
print(a [-6 : ])#-6 to 7 in steps of 1, ma Rao
print(a [: -4 : -1]) #empty string
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ]) # -3 to 7 in steps of 1, Rao
print(a [ : : ]) # 0 to 7 in steps of 1, Rama Rao
print(a [ : ]) # 0 to 7 in steps of 1, Rama Rao
print(a [ : : -1])# -1 to -8 in steps of -1, oaR amaR
print(a [ : : -2])#-1 to -8 in steps of -2, oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8]) #2 to 7 in steps of 1, ma Rao
print(a [2 : 8 : -1]) # 2 to 9 in steps of -1, empty string
print(a [ : -6 : -1]) # empty string
print(a [2 : -3])# 2 to -4 in steps of -3, ma
print(a [1 : 6 : 2]) # 1 to 5 in steps of 2, am  
print(a [ : -5 : -5])# empty string
print(a [2 : -5]) # 2 to -6 in steps of 1, m
print(a [2 : -5 : 2]) # 2 to -6 in steps of 2, m
print(a [ : 0 : -1]) # -1 to 1 in steps of -1, oaR ama
print(a [-5 : 0 : -2])# -5 to 1 in steps of -2, aa

#Home Work-7
'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
s1=eval(input("Enter string1 in quotes: "))
s2=eval(input("Enter string2 in quotes: "))
if len(s1)<2 or len(s2)<2:
    print("Input  should  be  a  min  of  2-char  string")
    exit()
res=s2[:2]+s1[2:]+' '+s1[:2]+s2[2:]
print(res)

#Home Work-8
'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
s=eval(input("Enter the string: "))
if len(s)<4:
    print()
    exit()
print(s[:2]+s[-2:])

#Home Work-9
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
s=eval(input("Enter the string: "))
#forward direction
for i in range(len(s)):
    print(f'Character  at  index  {i}  :  {s[i]}')
#reverse direction
for i in range(1,len(s)+1):
    print(f'Character  at  index  {-i}  :  {s[-i]}')

#Home Work-10
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
s=eval(input("Enter input string: "))
odd=' '
even=' '
for i in range(len(s)):
    if i%2==0:
        even+=s[i]
    else:
        odd+=s[i]
print(odd)
print(even)

#Home Work-11
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
s=eval(input("Enter string: "))
res=' '
try:
    for i in range(0,len(s),2):
        res+=(s[i]*int(s[i+1]))
except ValueError:
    print("String   should  have  alternate  character  and  digit")
    exit()
print(res)

#Home Work-12
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
s1=eval(input("Enter 1st strig: "))
s2=eval(input("Enter 2nd string: "))
res=' '
t=min(len(s1),len(s2))
for i in range(t):
    res+=s1[i]
    res+=s2[i]
res+=(s1[t:len(s1)]+s2[t:len(s2)])
print(res)

#Home Work-13
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
s=eval(input("Enter the string: "))
res=''
for i in range(len(s)):
    if s[i] not in res:
        res+=s[i]
print(res)

#Home Work-14
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len('+-$'))#3
print(len(''))#0
print(len(' '))#1
print(len('A2#'))#3
# print(len(3456))#error, cannot be used for non sequences
# print('Sec'. len())#error, that string does not have the method len() to call 


'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
'''

#Home Work-15
# chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90)) #Z
print(chr(97)) #a
print(chr(122)) #z
print(chr(48)) #0
print(chr(57)) #9
print(chr(36)) #$
print(chr(32)) #' '



'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''

#Home Work-16
# ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z')) #90
print(ord('a')) #97
print(ord('z')) #122
print(ord('0')) #48
print(ord('9')) #57
print(ord('$')) #36
print(ord(' ')) #32



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

#Home Work-17
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

  4       'Z'           '5'          'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '_' = 'AEMPZ_'

  6       'D'           '2'          'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''
s=eval(input("Enter the string: "))
res=''
try:
    for i in range(0,len(s),2):
        res+=s[i]+chr(ord(s[i])+int(s[i+1]))
except ValueError:
    print("Pls  enter  string  with  alternate  char  and  digit")
    exit()
print(res)

