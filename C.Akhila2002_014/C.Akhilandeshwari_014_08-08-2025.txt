#Program to  determine  largest  command  line  input
'''
from sys import argv
if len(argv) < 2:
    print("Please send inputs")
else:
    try:
        if int(eval(argv[1])) or float(eval(argv[1])):
            largest=eval(argv[1])
        for i in argv[1:]:
            num=eval(i)
            if num > largest:
                largest = num
        print("Largest input is:", largest)
    except NameError:
        largest=argv[1]
        for i in argv[1:]:
            if i > largest:
                largest = i
        print("Largest input is:", largest)
'''


#Program  to  determine  command  line  input  is  even  number  or  odd  number
'''
from sys import argv
if len(argv) != 2:
    print("Please give valid inputs")
else:
    try:
        if eval(argv[1])%2==0:
            print("Even number")
        else:
            print("Odd number") 
    except NameError:
        print("Please give valid integer input")
'''

#Program  to  determine  average  of  command  line  inputs
'''
from sys import argv
if len(argv) < 2:
    print("Please send inputs")
else:
    try:
        sum= 0
        for i in argv[1:]:
            sum += eval(i)
        average = sum / (len(argv) - 1)
        print("Average of inputs is:", average)
    except NameError:
        print("Please give valid numeric inputs")
'''


#Program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
'''
from sys import argv
if len(argv) < 2:
    print("Please send inputs")
else:
    try:
        elements=[eval(i) for i in argv[1:]]
        print(sorted(elements))
        print(sorted(elements, reverse=True))
    except NameError:
        elements = [i for i in argv[1:]]
        print(sorted(elements))
        print(sorted(elements, reverse=True))
'''

#Find outputs
'''
print('green' in 'Hyd  is  green  city')  #True
print('day' in 'Sankar  dayal  sarma')  #True
print('Green' in 'Hyd  is  green  city')  #False
print('d  is' in 'Hyd  is  green  city')  #True
print('dis' in 'Hyd  is  green  city')  #False
print('iniv' in 'Srinivas')  #True
print('iniv' not in 'Srinivas')  #False



a = 'Rama Rao'

print(a[:7:2])       # RmRo
print(a[:7])         # Rama Ra
print(a[2:4])        # ma
print(a[2:])         # ma Rao
print(a[:4])         # Rama
print(a[::2])        # RmRo
print(a[-6:-1])      # ma Ra
print(a[-6:])        # ma Rao
print(a[:-4:-1])     # oa
print(a[-3:-1])      # Ra
print(a[-3:])        # Rao
print(a[::])         # Rama Rao
print(a[:])          # Rama Rao
print(a[::-1])       # oaR amaR
print(a[::-2])       # oRmR
print(a[-2::-2])     # a mR
print(a[2:8])        # ma Rao
print(a[2:8:-1])     # 
print(a[:-6:-1])     # oa
print(a[2:-3])       # ma 
print(a[1:6:2])      # aaR
print(a[:-5:-5])     # o
print(a[2:-5])       # m
print(a[2:-5:2])     # m
print(a[:0:-1])      # oaR ama
print(a[-5:0:-2])    # a m


'''

#Program  to  concatenate  two  strings  separated  by  space  but  swap  first  two characters  of  the  two  strings.
'''
a=input("Enter first string: ")
b=input("Enter second string: ")
if len(a) < 2 or len(b) < 2:
    print("Both strings should have at least 2 characters")
else:
    print(b[:2]+a[2:]+' '+a[:2]+b[2:])
'''

#Program to print characters  of  the  string  in  forward  and  reverse directions  without  slice
'''
a=input("Enter a string: ")
print("Forward direction:") 
for i in range(len(a)):
    print(a[i], end=' ')
print("\nReverse direction:")
for i in range(len(a)-1, -1, -1):
    print(a[i], end=' ')   
'''

#Program  to  print  characters  at  even  and  odd  indexes  without  slice

'''
a=input("Enter a string: ")   
e=[]
o=[] 
for i in range(len(a)):
    if i%2==0:
        o.append(a[i])
    else:
        e.append(a[i])
print("Characters at even indexes:")
print(' '.join(e))
print("Characters at odd indexes:")
print(' '.join(o))
'''

#Program to repeat characters in a string based on the digit that follows it
'''''
a=input("Enter  any  string  with  alternate  character  and  digit:")
if len(a) < 2:
    print("String should have at least 2 characters")
else:
    try:
        result = ""
        for i in range(0, len(a), 2):
            char = a[i]
            count = int(a[i+1])
            result += char * count
        print("Result:", result)
    except ValueError:
        print("String   should  have  alternate  character  and  digit")
'''

# Program  to  merge  two  strings  to  form  a  new  string
'''
a=input("Enter first string: ")
b=input("Enter second string: ")
min_len = min(len(a), len(b))
result=""
for i in range(min_len):
    result += a[i] + b[i]       
if len(a) > min_len:
    result += a[min_len:]           
if len(b) > min_len:
    result += b[min_len:]           
print("Merged string:", result)
'''
#Program  to  remove  duplicate  characters  of  the  string  without  using  set
'''
a=input("Enter a string: ")
result=[]
for i in a:
    if i not in result:
        result.append(i)
print("String after removing duplicates:", ''.join(result))
'''

#Find Outputs:
'''
print(len('Hyd'))      # 3
print(len('Rama Rao')) # 8
print(len('9247'))     # 4
print(len('+-$'))      # 3
print(len(''))         # 0
print(len(' '))        # 1
print(len('A2#'))      # 3
print(len(3456))       # error
print('Sec'. len())    # error


print(chr(65))   # A
print(chr(90))   # Z
print(chr(97))   # a
print(chr(122))  # z
print(chr(48))   # 0
print(chr(57))   # 9
print(chr(36))   # $
print(chr(32))   #  (space)

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32

'''

# Let  input  be  A4M3Z5D2
# What  is  the  output ?  --->  AEMPZ_DF

a=input("Enter a string with alternate character and digit: ")
result=""
for i in range(0, len(a), 2):
    char = ord(a[i])
    num = a[i+1]
    if not num.isdigit():
        print("String should have alternate character and digit")
        break  
    num = int(num)
    result += a[i]+chr(char + num) 
print(result)