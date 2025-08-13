#1st
from sys import argv
try:
    l=[]
    for i in argv[1:]:
        l.append(eval(i))
    print("largest is: ",max(l))
except ValueError:
    print("Enter atleast one input")
except NameError:
     print("Inputs cannot be a number and string")

#2nd
from sys import argv
try:
    a=int(argv[1])
    if(a%2==0):
        print("Even Number")
    else:
        print('Odd Number')
except :
    print("pls send an integer input")

#3rd
from sys import argv
try:
   a=[]
   for x in argv[1:]:
    a.append(float(x))
   s=sum(a)
   print("Average : ",(s/len(a)))
except:
  print("Pls send number Inputs")

#4th
from sys import argv
try:
    a=[]
    for x in argv[1:]:
        a.append(float(x))
    print('Ascending Order : ',sorted(a))
    print('Descending Order : ',sorted(a,reverse=True))
except:
    print("Pls don't send number and string inputs together")

#5th
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') #True
print('Green'   in   'Hyd  is  green  city')#False
print('d  is'   in   'Hyd  is  green  city')#True
print('dis'   in   'Hyd  is  green  city')#False
print('iniv'   in   'Srinivas') #True
print('iniv'   not   in'Srinivas')#False

#6th
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])#Rm a
print(a [ : 7])#Rama Ra
print(a [2 : 4])#ma
print(a [2 : ])#ma Rao
print(a [ : 4 ])#Rama
print(a [ : : 2])#Rm a
print(a [-6 : -1])#ma Ra
print(a [-6 : ])#ma rao
print(a [: -4 : -1])#oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])#Rao
print(a [ : : ])#Rama  Rao
print(a [ : ])#Rama  Rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2])#oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])#ma Rao
print(a [2 : 8 : -1])#BLANK
print(a [ : -6 : -1])#oaR a
print(a [2 : -3])#ma
print(a [1 : 6 : 2])#aaR
print(a [ : -5 : -5])#o


#7th
a=input("Enter first string: ")
b=input("Enter second string: ")
if len(a) or len(b) <2:
    print("Input should be a min of 2-char string")
else:
    print("Result: ",b[0:2]+a[2:]+" "+a[0:2]+b[2:])

#8th
a=input("Enter any string : ")
if len(a)>4:
    print(a[0:2]+a[-2:])

#9th
a=input("Enter any string: ")
for i in range(len(a)):
    print(f"Character at index  {i} :  {a[i]}")
for j in range(1,len(a)+1):
    print(f"Character at index {-j} :  {a[-j]}")

#10th
a=input("Enter any string: ")
Even=[]
Odd=[]
for i in range(len(a)):
    if i%2==0:
        Even.append(a[i])
    else:
        Odd.append(a[i])
print("String at Even indexes : ",*Even)
print("String at odd indexes : ",*Odd)

#11th
try:
    a=input("Enter any string with alternate character and digit: ")
    print("Result: ",end="")
    for i in range(0,len(a),2):
        print(a[i]*int(a[i+1]),end="")
except ValueError:
    print("String should have alternate character and digit")

#12th
a=input("enter first string: ")
b=input("enter second string: ")
result=""
i=j=0
while i < len(a) or j < len(b):
    if i < len(a):
        result += a[i]
        i += 1
    if j < len(b):
        result += b[j]
        j += 1
        print("merged string:",result)

#13th
a=input("enter any string:")
res=""
for i in a:
    if i not in res:
        res += i
print("string after removing duplicates:", res)

#14th
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao'))
print(len('9247'))
print(len('+-$'))
print(len(''))
print(len(' '))
print(len('A2#'))
print(len(3456))
print('Sec'. len())


#15th
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))
print(chr(97))
print(chr(122))
print(chr(48))
print(chr(57))
print(chr(36))
print(chr(32))


#16th
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord('0'))
print(ord('9'))
print(ord('$'))
print(ord(' '))



#17th
s = input("Enter string: ")
out = ""

for i in range(0, len(s), 2):
    out += s[i] + (chr(ord(s[i]) + int(s[i+1])) if ord(s[i]) + int(s[i+1]) <= ord('Z') else "_")

print(out)


