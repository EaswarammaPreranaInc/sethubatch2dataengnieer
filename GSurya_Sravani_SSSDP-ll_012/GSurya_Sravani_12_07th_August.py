'''  (Home  work)
Slice  demo  program
print(a[:7:2])        # Ram 
print(a[:7])          # Rama Ra
print(a[2:4])         # ma
print(a[2:])          # ma Rao
print(a[:4])          # Rama
print(a[::2])         # Ram 
print(a[-6:-1])       # ma Ra
print(a[-6:])         # ma Rao
print(a[:-4:-1])      # o
print(a[-3:-1])       # Ra
print(a[-3:])         # Rao
print(a[::])          # Rama Rao
print(a[:])           # Rama Rao
print(a[::-1])        # oaR amaR
print(a[::-2])        # oRmR
print(a[-2::-2])      # a mR
print(a[2:8])         # ma Rao
print(a[2:8:-1])      # empty string 
print(a[:-6:-1])      # oa
print(a[2:-3])        # ma
print(a[1:6:2])       # a a
print(a[:-5:-5])      # o
print(a[2:-5])        # empty string 
print(a[2:-5:2])      # empty string 
print(a[:0:-1])       # oaR ama
print(a[-5:0:-2])     # aa
# len()  function  demo  program  (Home  work)
print(len('Hyd'))         # 3
print(len('Rama Rao'))    # 8
print(len('9247'))        # 4
print(len('+-\$'))        # 3
print(len(''))            # 0
print(len(' '))           # 1  
print(len('A2#'))         # 3
print(len(3456))          # error TypeError: object of type 'int' has no len()
print('Sec'. len())       # error
# chr()  function  demo  program
print(chr(65))    # A
print(chr(90))    # Z
print(chr(97))    # a
print(chr(122))   # z
print(chr(48))    # 0
print(chr(57))    # 9
print(chr(36))    # $
print(chr(32))    #  ' '
# ord()  function  demo  program
print(ord('A'))   # 65
print(ord('Z'))   # 90
print(ord('a'))   # 97
print(ord('z'))   # 122
print(ord('0'))   # 48
print(ord('9'))   # 57
print(ord('$'))   # 36
print(ord(' '))   # 32


from  sys   import   argv
print(argv)
a=list(argv)
print(f"the max value of list is{max(a[1:])}")
C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py 25 30 40 35.5 86 32.5
['C:\\learnpython\\mypython.py', '25', '30', '40', '35.5', '86', '32.5']
the max value of list is86


from sys import argv
a=list(argv)
if int(a[1]) %2== 0:
   print("Even Number")
else:
   print("Odd Number")
C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py 30
Even Number

C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py 45
Odd Number


from sys import argv
try:
  print(argv)

  a = []
  for i in argv[1:]:      
      a.append(int(i))   
  print(f"The sum of list is {sum(a)}")
  print(f"The number of elements in list is {len(a)}")
except ValueError:
     print("only int numbers")
C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py 10 20 30 40 50.5
['C:\\learnpython\\mypython.py', '10', '20', '30', '40', '50.5']
only int numbers

C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py 10 20 30 40 50
['C:\\learnpython\\mypython.py', '10', '20', '30', '40', '50']
The sum of list is 150
The number of elements in list is 5


from sys import argv

print(argv) 
a = []
for i in argv[1:]:
    a.append(int(i))

print(f"The sorted list is {sorted(a)}")
print(f"The sorted list in descending order is {sorted(a, reverse=True)}")                                                                       C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py 10 25 11 4 2 50 90
['C:\\learnpython\\mypython.py', '10', '25', '11', '4', '2', '50', '90']
The sorted list is [2, 4, 10, 11, 25, 50, 90]
The sorted list in descending order is [90, 50, 25, 11, 10, 4, 2]


a=input("enter first stringof min 2 char string: ")
b= input("enter second char: ")
c=b[0:2]+ a[2:]
d=a[0:2]+b[2:]
n=c+" " +d
print(n)                                                                                                                                                                                 
C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
enter first stringof min 2 char string: java
enter second char: python
pyva jathon


a=input("enter a string: ")
c=a[0:2]
b=a[-2:]
n=c+b
print(n)                                                                                                                                                                              C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
enter a string: python
pyon


# Input string
s = "VAMSI"

# Forward direction using positive indexing
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

# Reverse direction using negative indexing
for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")
Character at index 0 : V
Character at index 1 : A
Character at index 2 : M
Character at index 3 : S
Character at index 4 : I
Character at index -1 : I
Character at index -2 : S
Character at index -3 : M
Character at index -4 : A
Character at index -5 : V



a="Rama rao"

odd=""
even=""
for i in range(len(a)):
       if i%2==0:
          even+=(a[i])
       else:
          odd+=(a[i])
print(even)
print(odd)                                      C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
Rm a
aaro


a = 'A4B3C2$5'
out = ''

for i in range(0, len(a), 2): 
    out += a[i] * int(a[i + 1])

print(out)


a="hyd"
b="vamsi"
i=0
c=""
while i<len(a) and i<len(b):
    c+=a[i:]+b[i:]
    i+=1
c += a[i:] + b[i:]
print(c)


a="Rama Rao"
duplicates=""
seen=""
for item in range(len(a)):
    if a[item]in seen:
        duplicates+=a[item]
    else:
     seen+=a[item]
print(seen)
print(duplicates)



s = input("Enter a string with alternate character and digit: ")

out = ""

for i in range(0, len(s), 2):
    ch = s[i]
    num = int(s[i + 1])
    next_char = chr(ord(ch) + num)

    # If character goes beyond 'Z', replace with '_'
    if ord(next_char) > ord('Z'):
        out += ch + "_"
    else:
        out += ch + next_char

print("Result:", out)
Enter a string with alternate character and digit: A4M3Z5D2
Result: AEMPZ_DF