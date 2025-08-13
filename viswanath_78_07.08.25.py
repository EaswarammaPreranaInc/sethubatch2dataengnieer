Write  a  program  to  determine  largest  command  line  input
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

Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
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
  
Write  a  program  to  determine  average  of  command  line  inputs
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

Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
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

print('green' in 'Hyd  is  green  city')           # True
print('day' in 'Sankar  dayal  sarma')             # True
print('Green' in 'Hyd  is  green  city')           # False
print('d  is' in 'Hyd  is  green  city')           # True
print('dis' in 'Hyd  is  green  city')             # False
print('iniv' in 'Srinivas')                        # True
print('iniv' not in 'Srinivas')                    # False


Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
a = 'Rama Rao'
print(a[:7:2])          # Rm<space>a  -> indexes 0,2,4,6 (excluding 7)
print(a[:7])            # Rama Ra
print(a[2:4])           # ma
print(a[2:])            # ma Rao
print(a[:4])            # Rama
print(a[::2])           # Rm<space>a
print(a[-6:-1])         # ma<space>Ra
print(a[-6:])           # ma<space>Rao
print(a[:-4:-1])        # oaR  -> from -1 to -5 (excluding -5), in reverse
print(a[-3:-1])         # Ra
print(a[-3:])           # Rao
print(a[::])            # Rama Rao
print(a[:])             # Rama Rao
print(a[::-1])          # oaR amaR
print(a[::-2])          # oRaa
print(a[-2::-2])        # a<space>mR  -> from -2 to -8 (excluding -8), step -2
print(a[2:8])           # ma<space>Rao
print(a[2:8:-1])        # '' (empty string, step -1 cannot move forward from 2 to 8)
print(a[:-6:-1])        # oaR<space>a  -> from -1 to -6 (excluding -6), reverse
print(a[2:-3])          # ma
print(a[1:6:2])         # aaR  -> indexes 1,3,5
print(a[:-5:-5])        # o    -> from -1 to -5 (excluding -5), step -5 (only -1 used)
print(a[2:-5])          # m   -> index 2 to 2 (exclusive), empty
print(a[2:-5:2])        # m   -> same as above
print(a[:0:-1])         # oaR amaR -> from -1 to 1 (excluding 0), reverse
print(a[-5:0:-2])       # '' (empty string, step -2 cannot move forward from -5 to 0)

Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.Assume  that  each  string  has  a   minimum  of  two  characters
a=input('Enter the first string : ')
b=input('Enter the second string : ')
if (len(a)<2 or len(b)<2):
    print('input should be a minimum of 2 char')
else:    
     result = (b[:2]+a[2:],a[:2]+b[2:],sep= '  ')
     print(result)



Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters
a=input('Enter the string : ')
if (len(a)<4):
    print('')
else: 
    result = a[:2] + a[-2:]
    print(result)

Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
directions  without  slice
a = input('Enter the string : ')
b = ''
c = ''
for i in range(len(a)):
    b += a[i]
for j in range(len(a)):    
    c += a[-(j+1)]
print(f'Forward direction: {b}')
print(f'Reverse direction: {c}')

Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
a = input('Enter the string : ')
b = ''
c = ''
for i in range(len(a)):
    if i % 2 == 0:
        b += a[i]
    else:
        c += a[i]
print(f'even char: {b}')
print(f'odd char: {c}')

Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5
Result :   AAAABBBCC$$$$$
try:
    a = input("Enter the string: ") 
    b  = ”
    for i in range(0, len(a), 2): 
        c = a[i]
        d = int(a[i+1])
        b += c * d
    print(b)  
except(ValueError):
    print('Invalid input. String should have alternate characters and numbers')

Write  a  program  to  merge  two  strings  to  form  a  new  string 
a = input('Enter the first string : ')
b = input('Enter the second string : ')
c = ''
d = ''
for i in range(min(len(a),len(b))):
    c += a[i] + b[i]
if len(a)> len(b):
    d = c + a[len(b):]
else:
    d = c + b[len(a):]
print(d)   

Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a = input('Enter the first string : ')
c = ''
for i in range(len(a)):
    if a[i] not in c:
        c += a[i]
print(c)   

print(len('Hyd'))  # 3
print(len('Rama Rao'))  # 8
print(len('9247'))  # 4
print(len('+$-'))  # 3
print(len(''))  # 0
print(len(' '))  # 1
print(len('A2#'))  # 3
print(len(3456))  # Error: int has no length
print('Sec'. len())  # Error: invalid syntax

print(chr(65))  # 'A'
print(chr(90))  # 'Z'
print(chr(97))  # 'a'
print(chr(122)) # 'z'
print(chr(48))  # '0'
print(chr(57))  # '9'
print(chr(36))  # '$'
print(chr(32))  # ' ' (space)

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32

Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF
try:
    a =  input('Enter the string = ')
    b = ''
    for i in range(0,len(a),2):
        c = a[i]
        d = int(a[i+1])
        b += c
        b += chr(ord(c)+d)
    print(b)
except:
    print('Invalid input. Enter a string which has alternate character and number')
