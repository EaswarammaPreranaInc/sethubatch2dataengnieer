# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

import sys

if len(sys.argv) != 2:
    print("Please send one number as input")
    sys.exit()

try:
    n = int(sys.argv[1])
except:
    print("Input should be an integer")
    sys.exit()

if n % 2 == 0:
    print(n, "is Even number")
else:
    print(n, "is Odd number")
----------------------------
# Write  a  program  to  determine  average  of  command  line  inputs

import sys

if len(sys.argv) == 1:
    print("Please send inputs")
    sys.exit()

total = 0
count = 0

for v in sys.argv[1:]:
    try:
        num = float(v)
    except:
        print("All inputs should be numbers")
        sys.exit()
    total += num
    count += 1

avg = total / count
print("Average :", avg)
-----------------------------------
# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

import sys

if len(sys.argv) == 1:
    print("Please send inputs")
    sys.exit()

a = []
for v in sys.argv[1:]:
    try:
        n = float(v)
        if n.is_integer():
            n = int(n)
        a.append(n)
    except:
        a.append(v)

print("Ascending order :", sorted(a))
print("Descending order:", sorted(a, reverse=True))
---------------------------------------------------
# Find outputs  (Home  work)

print( 'green'   in   'Hyd  is  green  city') # True

print('day'   in   'Sankar  dayal  sarma') # True 

print('Green'   in   'Hyd  is  green  city') # False

print('d  is'   in   'Hyd  is  green  city') # True

print('dis'   in   'Hyd  is  green  city') # False

print('iniv'   in   'Srinivas') # False

print('iniv'   not   in   'Srinivas') # True
---------------------------------------
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'

print(a [ : 7 : 2]) --> string from indexes 0 to 7 in steps of 2 i.e. RmaR

print(a [ : 7]) --> string from indexes 0 to 7 in steps of 1 i.e. Rama Ra

print(a [2 : 4]) → Index 2 to 3. i.e. ma

print(a [2 : ])  → From index 2 to end i.e. ma  Rao

print(a [ : 4 ]) → From start to index 3 i.e. Rama

print(a [ : : 2]) --> from index 0 to end in steps of 2 i.e. Rm  a

print(a [-6 : -1]) --> from index -6 to -2 i.e. ma Ra

print(a [-6 : ]) --> from index -6 to end i.e. ma Rao

print(a [: -4 : -1]) --> from indexes 0 to -4 in steps of -1 i.e. oaR

print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra

print(a [-3 : ])  → From index -3 to end i.e. Rao

print(a [ : : ]) --> from indexes 0 to 7 in steps of 1 i.e. Rama Rao

print(a [ : ]) --> from indexes 0 to 7 in steps of 1 i.e. Rama Rao

print(a [ : : -1]) --> from indexes 0 to 7 in steps of -1 i.e. oaR amaR

print(a [ : : -2]) --> from indexes 0 to 7 in steps of -2 i.e. oRmR

print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR

print(a [2 : 8]) → From index 2 to end i.e. ma  Rao

print(a [2 : 8 : -1]) --> empty

print(a [ : -6 : -1]) → From index -1 to -5 in steps of -1 i.e. oaR a  

print(a [2 : -3]) → Index 2 to -2 i.e. ma

print(a [1 : 6 : 2]) --> from indexes 1 to 5 in steps of 2 i.e. aaR

print(a [ : -5 : -5])  → From end to index -4 i.e. o

print(a [2 : -5])  → Index 2 to -4 i.e. m

print(a [2 : -5 : 2]) → Index 2 to -4 in steps of 2 i.e. m

print(a [ : 0 : -1]) → Reverse from end to index 0 i.e. oaR ama

print(a [-5 : 0 : -2]) --> from indexes -5 to -7 in steps of -2 i.e. a  a
-------------------------------------------------
# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]

result = new_s1 + " " + new_s2

print(result)
----------------------------------
#  Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

s = input("Enter a string: ")

if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])
-------------------------------------
# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice

s = input("Enter a string: ")

print("Forward:")
for i in range(len(s)):
    print(s[i], end="")
print()

print("Reverse:")
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
print()
--------------------------------------
# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

s = input("Enter a string: ")

even = ""
odd = ""

for i in range(len(s)):
    if i % 2 == 0:
        even = even + s[i]
    else:
        odd = odd + s[i]

print("Even index characters:", even)
print("Odd index characters :", odd)
----------------------------------------------
# Write  a  program  to  merge  two  strings  to  form  a  new  string

a = input("Enter first string: ")
b = input("Enter second string: ")

i = 0
c = ""

while i < len(a) and i < len(b):
    c = c + a[i] + b[i]
    i = i + 1

c = c + a[i:] + b[i:]
print(c)
-----------------------------------------
# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

s = input("Enter a string: ")
out = ""

for ch in s:
    if ch not in out:
        out = out + ch

print(out)
---------------------------------------
# len()  function  demo  program  (Home  work)

print(len('Hyd'))  #  3

print(len('Rama Rao')) # 8

print(len('9247')) # 4

print(len('+-$')) # 3

print(len('')) # 0

print(len(' '))# 1

print(len('A2#')) # 3

print(len(3456)) # error

print('Sec'. len()) # syntax error
-------------------------------------------
# chr()  function  demo  program

print(chr(65))  #   Converts  unicode  value  65  to  'A'

print(chr(90)) #   Converts  unicode  value  90  to  'Z'

print(chr(97))  #   Converts  unicode  value  97  to  'a'

print(chr(122))  #   Converts  unicode  value  122  to  'z'

print(chr(48))  #   Converts  unicode  value  48  to  '0'

print(chr(57))  #   Converts  unicode  value  57  to  '9'

print(chr(36))  #   Converts  unicode  value  36  to  '$'

print(chr(32))  #   32 is a   'space'  character
----------------------------------------
# ord()  function  demo  program

print(ord('A'))  #  Converts  'A'  to  unicode  value  65

print(ord('Z')) #  Converts  'Z'  to  unicode  value  90

print(ord('a'))  #  Converts  'a'  to  unicode  value  97

print(ord('z'))  #  Converts  'z'  to  unicode  value  122

print(ord('0'))  #  Converts  '0'  to  unicode  value  48

print(ord('9'))  #  Converts  '9'  to  unicode  value  57

print(ord('$'))  #  Converts  '$'  to  unicode  value  36

print(ord(' '))  #  <space> is 32
-----------------------------------------------
# Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

s = input("Enter a string: ")
out = ""

for i in range(0, len(s), 2):
    ch = s[i]
    n = int(s[i+1])
    out = out + ch
    new_ch = chr(ord(ch) + n)
    out = out + new_ch

print(out)



























