# Write  a  program  to  determine  largest  command  line  input

from sys import argv

if len(argv) == 1:
    print("Pls send inputs")
    exit()

a = []
try:
    for x in argv[1:]:
        a.append(float(x))
    largest = a[0]
    for num in a:
        if num > largest:
            largest = num
    print("argv =", argv)
    print("List a =", a)
    print("Largest command line input =", largest)
except ValueError:
    num_count = sum(x.replace('.', '', 1).isdigit() for x in argv[1:])
    if 0 < num_count < len(argv) - 1:
        print("Inputs can not be number and string")
    else:
        largest = argv[1]
        for val in argv[2:]:
            if val > largest:
                largest = val
        print("argv =", argv)
        print("Largest command line input =", largest)


#  Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

from sys import argv

if len(argv) != 2:
    print("Pls send an integer input")
    exit()

arg = argv[1]

try:
    num = int(arg)
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except ValueError:
    print("Pls send an integer input")


# Write  a  program  to  determine  average  of  command  line  inputs

from sys import argv

if len(argv) == 1:
    print("Pls send number inputs")
    exit()

a = []
try:
    for x in argv[1:]:
        if x.lower() == "true":
            a.append(True)
        elif x.lower() == "false":
            a.append(False)
        else:
            a.append(float(x))
    avg = sum(a) / len(a)
    print("argv =", argv)
    print("List a =", a)
    print("Average of inputs =", avg)
except ValueError:
    print("Pls send number inputs")


# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

from sys import argv

if len(argv) == 1:
    print("Pls send inputs")
    exit()

a = []
try:
    for x in argv[1:]:
        a.append(float(x))
    print("argv =", argv)
    print("List a =", a)
    print("Ascending order =", sorted(a))
    print("Descending order =", sorted(a, reverse=True))
except ValueError:
    num_count = sum(x.replace('.', '', 1).isdigit() for x in argv[1:])
    if 0 < num_count < len(argv) - 1:
        print("Pls don't send number and string inputs together")
    else:
        print("argv =", argv)
        print("List a =", argv[1:])
        print("Ascending order =", sorted(argv[1:]))
        print("Descending order =", sorted(argv[1:], reverse=True))


#  Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap first  two characters  of  the  two  strings. Assume  that  each  string  has  a   minimum  of  two  characters

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result :", result)


# Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string. Print  an  empty  string  if  string  has  less  than  four  characters

s = input("Enter a string: ")
if len(s) < 4:
    print("")
else:
    result = s[:2] + s[-2:]
    print(result)


'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice

       	     		  0      1     2      3     4
Let  input  be		  V      A     M      S     I
			 -5     -4    -3     -2    -1
'''

s = input("Enter any string: ")
for i in range(len(s)):
    print("Character at index", i, ":", s[i])
for i in range(-1, -len(s)-1, -1):
    print("Character at index", i, ":", s[i])


'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

		      0      1     2      3     4    5     6      7
Let  input  be        R      a     m      a          R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a'
'''

s = input("Enter any string: ")
even = ""
odd = ""
for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]
print("String at even indexes:", even)
print("String at odd indexes:", odd)


'''
Let  input  be           A   4   B   3   C   2   $   5
                         0   1   2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$
'''

a = input("Enter any string with alternate character and digit: ")

try:
    result = ""
    for i in range(0, len(a), 2):
        result += a[i] * int(a[i + 1])
    print("Result:", result)
except:
    print("Valid string — it has alternate characters and digits.")

'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->  HVYADMSI
'''

a = input("Enter first string: ")
b = input("Enter second string: ")
c = ""
i = 0
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print("Result :", c)


# Write  a  program  to  remove  duplicate  characters  of  the  string  without using  set

a = input("Enter any string: ")
out = ""
for ch in a:
    if ch not in out:
        out += ch  
print("String without duplicates :", out)


'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A     4     M     3    Z    5    D     2
'''

s = input("Enter any string with alternate character and digit: ")

try:
    out = ""
    for i in range(0, len(s), 2):
        ch = s[i]
        num = int(s[i+1])
        if 'A' <= ch <= 'Z' and ord(ch) + num <= ord('Z'):
            next_ch = chr(ord(ch) + num)
        else:
            next_ch = '_'
        out += ch + next_ch
    print("Result :", out)
except:
    print("Please enter string with alternate char and digit")


# Find outputs  (Home  work)

print('green' in 'Hyd  is  green  city')      # True
print('day' in 'Sankar  dayal  sarma')        # True
print('Green' in 'Hyd  is  green  city')      # False
print('d  is' in 'Hyd  is  green  city')      # True
print('dis' in 'Hyd  is  green  city')        # False
print('iniv' in 'Srinivas')                   # True
print('iniv' not in 'Srinivas')               # False


'''
(Home  work)
Slice  demo  program

0      1      2       3      4       5      6       7
R      a      m       a              R      a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''

a = 'Rama Rao'
print(a[:7:2])         # RmRo
print(a[:7])           # Rama Ra
print(a[2:4])          # ma
print(a[2:])           # ma Rao
print(a[:4])           # Rama
print(a[::2])          # RmRo
print(a[-6:-1])        # ma Ra
print(a[-6:])          # ma Rao
print(a[:-4:-1])       # oa 
print(a[-3:-1])        # Ra
print(a[-3:])          # Rao
print(a[::])           # Rama Rao
print(a[:])            # Rama Rao
print(a[::-1])         # oaR amaR
print(a[::-2])         # oRmR
print(a[-2::-2])       # a mR
print(a[2:8])          # ma Rao
print(a[2:8:-1])       #  (empty string, step -1 but start<stop)
print(a[:-6:-1])       # oao
print(a[2:-3])         # ma 
print(a[1:6:2])        # aaR
print(a[:-5:-5])       # o
print(a[2:-5])         # m
print(a[2:-5:2])       # m
print(a[:0:-1])        # oaR ama
print(a[-5:0:-2])      # a m


# len() function demo program

print(len('Hyd'))      # 3
print(len('Rama Rao')) # 8
print(len('9247'))     # 4
print(len('+-\$'))     # 3
print(len(''))         # 0
print(len(' '))        # 1
print(len('A2#'))      # 3


# chr() function demo program

print(chr(65))   # A
print(chr(90))   # Z
print(chr(97))   # a
print(chr(122))  # z
print(chr(48))   # 0
print(chr(57))   # 9
print(chr(36))   # $
print(chr(32))   # (space)


# ord() function demo program

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32
