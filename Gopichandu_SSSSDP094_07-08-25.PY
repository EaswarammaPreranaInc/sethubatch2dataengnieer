# '''
# Write  a  program  to  determine  largest  command  line  input

# 1) py   prog2.py   10     20     30.8   7  40    35.6
#     What  is  the  largest  command  line  input ?  ---> 40
#     What  is  argv ?  --->  ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
#     What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
#     How  to  determine  largest  element  of  list  'a' ?   ---> max(a)  i.e.  40
#     What  is  the  result  of  max(argv[1:]) ?  ---> '7'
#     What  is  the  issue  with  max(argv[1:])) ?  --->
# 													Largest  string  is  obtained  but  not  largest  number

# 2) py  prog2.py
#     What  is  the  output ?  ---> Pls  send  inputs

# 3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
#     What  is  the  largest  command  line  input ?  --->  'Vamsi'

# 4) py   prog2.py   25   'Ten'
#     What  is  the  output ?  --->  Inputs  can  not  be  number  and  string

# 5) Hint1: Use  for  loop

# 6) Hint2: Use  try  and  except
# '''
# import sys

# inputs = sys.argv[1:]

# # Case 2: No input
# if not inputs:
#     print("Pls send inputs")
#     sys.exit()

# # Try converting all inputs to float OR check if they are all strings
# all_numbers = True
# a = []

# for val in inputs:
#     try:
#         a.append(float(val))
#     except ValueError:
#         all_numbers = False
#         break  # Stop checking once a non-number is found

# # Case 4: Mix of number and string
# if not all_numbers:
#     # Check if it's a pure string list (like Case 3)
#     if all(not v.replace('.', '', 1).isdigit() for v in inputs):
#         print("Largest command line input:", max(inputs))
#     else:
#         print("Inputs can not be number and string")
# else:
#     # Case 1: All numbers (int or float)
#     print("Largest command line input:", int(max(a)))


# '''
# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

# 1) py  prog3.py  26
#     What  is  the  output ?  ---> Even  number

# 2) py  prog3.py  45
#     What  is  the  output ?  ---> Odd  number

# 3) py  prog3.py
#     What  is  the  output  ?  ---> Pls  send  an  integer  input

# 4) py  prog3.py  10.8
#     What  is  the  output ?  --->  Pls  send   an  integer  input

# 5) py  prog3.py  Ten
#     What  is  the  output  ?  --->  Pls  send   an  integer  input
# '''

# import sys

# try:
#     # Extract command line arguments (excluding script name)
#     inputs = sys.argv[1:]
#     num = int(inputs[0])
#     if (num%2==0):
#         print("even number")
#     else:
#         print("odd number")

# except:
#     print("Pls  send  integer  inputs")

# '''
# Write  a  program  to  determine  average  of  command  line  inputs

# 1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
#     What  is  argv ?  --->['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
#     What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
# 	How  to  determine  sum  of  list  elements ?  ---> sum(a)
#     How  to  determine  number  of  list  elements ?  ---> len(a)

# 2) py   prog4.py
#     What  is  the  output ?  ---> Pls  send  number  inputs

# 3) py   prog4.py  25   'Ten'
#     What  is  the  output  ?  --->  Pls  send  number  inputs
# '''

# import sys

# try:
#     # Extract command line arguments (excluding script name)
#     inputs = sys.argv[1:]
#     a = []
#     for val in inputs:
#         try:
#             num = float(val)
#             a.append(num)
#         except ValueError:
#             raise ValueError("Pls  send  number  inputs")


#     print("sum:", sum(a))
#     print("len:", len(a))

# except:
#     print("Pls  send  number  inputs")

# '''
# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

# 1) py  prog5.py  10   20    15.8   5   12.6
#     What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
#     What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
#     How  to  sort  list  'a' ?  --->  sorted(a)
#     How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

# 2) py  prog5.py   25   'Ten'
#     What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
# '''

# import sys

# try:
#     # Extract command line arguments (excluding script name)
#     inputs = sys.argv[1:]
#     a = []
#     for val in inputs:
#         try:
#             num = float(val)
#             a.append(num)
#         except ValueError:
#             raise ValueError("Pls don't send number and string inputs together")

#     # Sort ascending and descending
#     asc = sorted(a)
#     desc = sorted(a, reverse=True)

#     print("Ascending Order:", asc)
#     print("Descending Order:", desc)

# except:
#     print("Pls  don't  send  number  and  string  inputs  together")

# print( 'green'   in   'Hyd  is  green  city')#True
# print('day'   in   'Sankar  dayal  sarma') #True
# print('Green'   in   'Hyd  is  green  city')#False
# print('d  is'   in   'Hyd  is  green  city') #True
# print('dis'   in   'Hyd  is  green  city')#False
# print('iniv'   in   'Srinivas') #True
# print('iniv'   not   in   'Srinivas')#False
# '''  (Home  work)
# Slice  demo  program
# 0      1       2        3      4       5       6       7
# R      a      m        a               R       a       o
# -8    -7     -6      -5     -4      -3     -2      -1
# '''
# a = 'Rama Rao'
# print(a [ : 7 : 2]) # Rm a
# print(a [ : 7]) # Rama Ra
# print(a [2 : 4]) # ma
# print(a [2 : ]) #ma Rao
# print(a [ : 4 ]) #Rama
# print(a [ : : 2]) #Rm a
# print(a [-6 : -1]) #ma Ra
# print(a [-6 : ]) #ma Rao
# print(a [: -4 : -1]) #oaR
# print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
# print(a [-3 : ])#Rao
# print(a [ : : ])  #Rama Rao
# print(a [ : ]) #Rama Rao
# print(a [ : : -1]) # oaR amaR
# print(a [ : : -2]) # oRaa
# print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
# print(a [2 : 8]) #ma Rao
# print(a [2 : 8 : -1]) # empty
# print(a [ : -6 : -1]) #oaR a
# print(a [2 : -3]) #ma<space>
# print(a [1 : 6 : 2]) #aaR
# print(a [ : -5 : -5]) #o
# print(a [2 : -5]) #m
# print(a [2 : -5 : 2]) #m
# print(a [ : 0 : -1]) #oaR ama
# print(a [-5 : 0 : -2]) #aa
# '''
# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
# characters  of  the  two  strings.
# Assume  that  each  string  has  a   minimum  of  two  characters

# Let  inputs  be  Java  and  Python
# What  are  the  outputs ?  --->  Pyva<space>Jathon

# Hint:  Use  slice
# '''

# m="java programming"
# n="p"
# c=""
# try:
#     if len(m) and len(n)>=2:
#         c+=n[:2]+m[-2:]
#         c+=' '+m[:-2]+n[2:]
#         print(c)
#     else:
#         raise ValueError("")
# except:
#     print("Input  should  be  a  min  of  2-char  string")
# '''
# Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
# Print  an  empty  string  if  string  has  less  than  four  characters

# 1) Let  input  be  PYTHON
#     What  is  the  output ?  ---> PYON

# 2) Let  input  be  Hyd
#     What  is  the  output ?  --->  Nothing
# '''
# n="hyd"
# if len(n)>=4:
#     print(n[:2]+n[-2:])
# else:
#     print()
# '''
# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
# directions  without  slice

#        	     				  0      1     2      3     4
# Let  input  be		  V     A     M     S     I
# 			        		 -5    -4    -3    -2    -1

# What  are  the  outputs ?  --->  Character  at  index  0  :  V
# 								                 Character  at  index  1  :  A
# 								                 Character  at  index  2  :  M
# 							                     Character  at  index  3  :  S
# 								                 Character  at  index  4  :  I

# 								                 Character  at  index  -1  :  I
# 								                 Character  at  index  -2  :  S
# 								                 Character  at  index  -3  :  M
# 								                 Character  at  index  -4  :  A
# 								                 Character  at  index  -5  :  V

# Hint:  Use  two  for  loops
# '''
# n="Vamsi"
# for i,j in enumerate(n):
#     print(f"Character  at  index {i} :{j}")
# for i,j in enumerate(reversed(n)):
#     print(f"Character  at  index {i} :{j}")
# for i in range(len(n)-1,-1,-1):
#     print(f"Character  at  index {i-len(n)} :{j}")
# '''
# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

# 							 0      1      2      3     4     5     6      7
# Let  input  be        R      a     m      a             R     a      o

# odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
# even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a'

# 1) What  action  to  be  made  when  index  is  even ?  --->
# 																	Concatenate  the  character  to  even  object

# 2) What  action  to  be  made  when  index  is  odd ?  --->
# 																	Concatenate  the  characeter  to  odd  object

# 3) Hint: Use  single  for  loop
# '''

# n="RAMA RAO"
# even=""
# odd=""
# for i in range(len(n)):
#     if (i%2==0):
#         even+=n[i]
#     else:
#         odd+=n[i]
# print(even)
# print(odd)
# '''
# Let  input  be    A   4   B   3   C   2   $   5
#                          0   1    2   3   4   5   6   7

# What  is  the  output ?  --->  AAAABBBCC$$$$$

# 1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

# 2)  i        a[i]       a[i + 1]          out
#    -------------------------------------------------------
#                                                ''
#      0        'A'          '4'            '' + 'A' * 4 = 'AAAA'

# 	 2        'B'          '3'            'AAAA' + 'B' * 3 = 'AAAA' + 'BBB' = 'AAAABBB'

# 	 4        'C'          '2'            'AAAABBB' + 'C' * 2 = 'AAAABBB' + 'CC' = 'AAAABBBCC'

# 	 6        '$'          '5'            'AAAABBBCC' + '$' * 5 = 'AAAABBBCC' + '$$$$$' = 'AAAABBBCC$$$$$'
#    -------------------------------------------------------
# What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->
# 								a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
# '''
# n="A4B3C2$5"
# c=""
# try:
#     if len(n)%2!=0:
#         raise ValueError("string index out of range")
#     for i in range(0,len(n),2):
#         curr=n[i]
#         nxt=n[i+1]
#         if (nxt.isdigit()):
#             c+=(curr * int(nxt))
#         else:
#             raise ValueError("Invalid pattern")
#     print(c)
# except:
#     print("Pls  enter  string  with  alternate  char  and  digit")
# '''
# Write  a  program  to  merge  two  strings  to  form  a  new  string

# 1) Let  inputs  be    HYD   and   VAMSI
#    What  is  the  output  ?  --->  HVYADMSI

#              0     1    2
# a  --->   H     Y    D

#               0    1     2     3    4
# b  --->    V    A    M    S    I


# i       a[i]        b[i]          c
# --------------------------------------------------------
#                                     ''
# 0      'H'        'V'          '' + 'H' + 'V' = 'HV'

# 1      'Y'        'A'          'HV' + 'Y' + 'A' = 'HVYA'

# 2      'D'       'M'          'HVYA' + 'D' + 'M' = 'HVYADM'
# --------------------------------------------------------
# Concatenate  remainging  characters   of  the  other  string  to  object  'c'
# What  is  the  final  result ?  --->  'HVYADMSI'

# Hint:  Use  single  while  loop  and  slice
# '''
# m="Hyd"
# n="Vamsi"
# min_val=min(len(m),len(n))
# c=""
# while i<(min_val):
#     c+=m[i]
#     c+=n[i]
# if min_val==len(m):
#     c+=n[min_val:]
# else:
#     c+=m[min_val:]
# print(c)
# # for a,b in zip(m,n):
# #     c+=a+b
# # c+= m[len(n):] + n[len(m):]
# # print(c)
# '''
# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

# 1) Let  input  be   RAMA  RAO
#    What  is  the  output ? ---> RAM<space>O

# 2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

# 3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
# 																	Concatenate  the  character  to  out  object

# 4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
# 																							Ignore  the  character

# 5) Hint:  Use  not  in   operator
# '''
# n=input("Enter  any  string  : ")
# c=""
# for i in n:
#     if i not in c:
#         c+=i
# print(c)





# # len()  function  demo  program  (Home  work)
# print(len('Hyd'))  #  3
# print(len('Rama Rao')) # 8
# print(len('9247')) # 4
# print(len('+-$')) # 3
# print(len('')) # 0
# print(len(' ')) # 1
# print(len('A2#')) # 3
# print(len(3456)) # error
# print('Sec'. len()) # error


# '''
# What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
# '''
# # chr()  function  demo  program
# print(chr(65))  #   Converts  unicode  value  65  to  'A'
# print(chr(90)) #  Z
# print(chr(97)) # a
# print(chr(122)) # z
# print(chr(48))# 0
# print(chr(57)) # 9
# print(chr(36)) # $
# print(chr(32)) # space



# '''
# What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
# '''
# # ord()  function  demo  program
# print(ord('A'))  #  Converts  'A'  to  unicode  value  65
# print(ord('Z')) #90
# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('0'))  # 48
# print(ord('9')) # 57
# print(ord('$')) # 36
# print(ord(' ')) # 32



# '''
# ord()  function
# ------------------
# 1) What  does  ord()  function  do ?  ---> Converts  character  to  unicode  value

# 2) How  many  unicode  values  exist ?  ---> 512

# 3) What  is  the  range  of  unicode  values ?  ---> 0  to  511

# 4) What  are  the  unicode  values  of  'A'  -  'Z' ?  ---> 65  to  90
#      What  are  the  unicode  values  of  'a'  -  'z' ?  ---> 97  to  122
#      What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57

# 5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

# Note:  chr()  and  ord()  are  quite  opposite  functions
# '''

    
        

        
# '''
# Let  input  be  A4M3Z5D2

# What  is  the  output ?  --->  AEMPZ_DF

#  0     1     2     3    4    5    6     7
#  A    4     M    3    Z    5    D     2


#    i       a[i]      a[i + 1]         out
# --------------------------------------------------------------------------------
#                                           ''
#   0       'A'           '4'          '' + 'A' + chr(65 + 4) = '' + 'A' + 'E' = 'AE'

#   2       'M'           '3'          'AE' + 'M' + chr(77 + 3) = 'AE' + 'M' + 'P' = 'AEMP'

#   4       'Z'           '5'          'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '' = 'AEMPZ'

#   6       'D'           '2'          'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
# -----------------------------------------------------------------------------------
# Hint: Use  chr()  and  ord()  functions
# '''
# n="Hyd"
# c=''
# # for i in range(len(n)):
# #     if n[i].isdigit():
# #         if i==0:
# #             c+=(ord(n[i]))
# #         else:
# #             c+=chr(ord(n[i-1])+int(n[i]))
# #     else:
# #         c+=n[i]
# # print(c)
# try:
#     if len(n)%2!=0:
#         raise ValueError("string index out of range")
#     for i in range(0,len(n),2):
#         curr=n[i]
#         c+=curr
#         nxt=n[i+1]
#         if (nxt.isdigit()):
#              c+=chr(ord(curr)+int(nxt))
#         else:
#             raise ValueError("Invalid pattern")
#     print(c)
# except:
#     print("Pls  enter  string  with  alternate  char  and  digit")


for i in range(1,10):
    for j in range(2,8):
        a=i*j
        print(f'{i}{j}')