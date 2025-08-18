import sys
args = sys.argv[1:]
if not args:
    print("Pls send inputs")
else:
    try:
        a = [float(x) for x in args]
        print("Largest command line input:", max(a))
    except ValueError:
        if all(x.isalpha() for x in args):
            print("Largest command line input:", max(args))
        else:
            print("Inputs can not be number and string")


import sys
if len(sys.argv) < 2:
    print("Pls send an integer input")
else:
    try:
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")


import sys
args = sys.argv[1:]
if not args:
    print("Pls send number inputs")
else:
    try:
        a = [float(x) for x in args]
        avg = sum(a) / len(a)
        print("Average:", avg)
    except ValueError:
        print("Pls send number inputs")


import sys
args = sys.argv[1:]
if not args:
    print("Pls send inputs")
else:
    try:
        a = [float(x) for x in args]
        print("Ascending order:", sorted(a))
        print("Descending order:", sorted(a, reverse=True))
    except ValueError:
        print("Pls don't send number and string inputs together")


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result:", result)


a = 'Rama Rao'

print(a[:7:2])       # 'RmR'
print(a[:7])         # 'Rama Ra'
print(a[2:4])        # 'ma'
print(a[2:])         # 'ma Rao'
print(a[:4])         # 'Rama'
print(a[::2])        # 'RmRo'
print(a[-6:-1])      # 'ma Ra'
print(a[-6:])        # 'ma Rao'
print(a[:-4:-1])     # 'oa '
print(a[-3:-1])      # 'Ra'
print(a[-3:])        # 'Rao'
print(a[::])         # 'Rama Rao'
print(a[:])          # 'Rama Rao'
print(a[::-1])       # 'oaR amaR'
print(a[::-2])       # 'oRaa'
print(a[-2::-2])     # 'a mR'
print(a[2:8])        # 'ma Rao'
print(a[2:8:-1])     # ''
print(a[:-6:-1])     # 'oaR a'
print(a[2:-3])       # 'ma '
print(a[1:6:2])      # 'aaR'
print(a[:-5:-5])     # 'o'
print(a[2:-5])       # 'm'
print(a[2:-5:2])     # 'm'
print(a[:0:-1])      # 'oaR ama'
print(a[-5:0:-2])    # 'a m'



s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result:", result)


s = input("Enter string: ")
if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])


s = input("Enter string: ")
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")
for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")


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


s = input("Enter any string with alternate character and digit: ")
if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("String should have alternate character and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] * int(s[i+1])
    print("Result:", out)



a = input("Enter first string: ")
b = input("Enter second string: ")
i = 0
c = ""
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print("Result:", c)



s = input("Enter any string: ")
out = ""
for ch in s:
    if ch not in out:
        out += ch
print("String without duplicates:", out)



s = input("Enter any string with alternate character and digit: ")
if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("Pls enter string with alternate char and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] + chr(ord(s[i]) + int(s[i+1]))
    print("Result:", out)



print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len('+-$'))        # 3
print(len(''))           # 0
print(len(' '))          # 1
print(len('A2#'))        # 3
print(len(3456))         # Error
print('Sec'. len())      # Error


print(chr(65))   # A
print(chr(90))   # Z
print(chr(97))   # a
print(chr(122))  # z
print(chr(48))   # 0
print(chr(57))   # 9
print(chr(36))   # $
print(chr(32))   # <space>


print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32



