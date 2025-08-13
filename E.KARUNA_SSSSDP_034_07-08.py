from sys import argv
print(argv)
try:
    num=int(argv[1])
    if num%2==0:
        print("Even number")
    else:
        print("odd number")
except:
    print("pls send an integer input")
print()

from sys import argv
print(argv)
result = []
if len(argv)==1:
    print("pls send number inputs")
else:
    try:
        for i in range(1,len(argv)):
            num=argv[i]
            if '.' in argv[i]:
                num=float(argv[i])
                result.append(num)
            elif num.lower()=='true':  
                result.append(True)
            elif num.lower()=='false':
                result.append(False)
            else:   
                num=int(argv[i])
                result.append(num)    
        print("average of inputs: ",sum(result)/len(result))

    except:
        print("pls send number inputs")

print()

from sys import argv
print(argv)
result=[]
try:
    for i in range(1,len(argv)):
        if '.' in argv[i]:
            num=float(argv[i])
            result.append(num)
        else:
            num=int(argv[i])
            result.append(num)
    print("Ascending order :",sorted(result))
    print("descending order :",sorted(result,reverse=True))
except:
    print("pls do not send number and string inputs together")
print()

# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  # True  : 'green' is a substring of 'Hyd is green city'
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city')  # True
print('dis'   in   'Hyd  is  green  city')  #  False
print('iniv'   in   'Srinivas')  # True
print('iniv'   not   in   'Srinivas')  # False 
print()
'''(Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1'''

a = 'Rama Rao'
print(a [ : 7 : 2])  # a[0:7:2] : string from indexes o to 6 in steps of 2 i.e., Rm a
print(a [ : 7])  #  a[0:7:1] : Rama Ra
print(a [2 : 4])  #  a[2:4:1]  :  ma
print(a [2 : ])  #  a[2:8:1]   :  ma Rao
print(a [ : 4 ])  #  a[0:4:1]  :  Rama
print(a [ : : 2])   #  a[0:8:2]  : Rm a
print(a [-6 : -1])   #  a[-6:-1:1]  :  ma Ra
print(a [-6 : ])  #   a[-6:0:1]  :   ma Rao
print(a [: -4 : -1])  #  a[-1:-4:-1]  :  oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])  #  a[-3: :1]  :   Rao
print(a [ : : ])   #  a[0:8:1]  :  Rama Rao
print(a [ : ])  #  a[0:8:1]  :   Rama Rao
print(a [ : : -1])   #   a[-1:-9:1]  :  oaR amaR
print(a [ : : -2])   #   a[-1:-9:-2]  :   oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])  #  a[2:8:1]  :   ma Rao
print(a [2 : 8 : -1])    #   empty string
print(a [ : -6 : -1])     #   a[-1:-6:-1]  :   oaR a
print(a [2 : -3])  #  a[2:-3:1]  :  ma<>space
print(a [1 : 6 : 2])  #  a[1:6:2]  :   aaR
print(a [ : -5 : -5])   #  a[-1:-5:-5]  :    o
print(a [2 : -5])   #   a[2:-5:1]  :   m
print(a [2 : -5 : 2])   #  a[2:-5:2]  :  m
print(a [ : 0 : -1])  #  a[7:0:-1]  :  oaR ama
print(a [-5 : 0 : -2])   #  a[-5:9:-2]  :  aa
print()

num1=input("Enter First string : ")
num2=input("Enter second string : ")
if len(num1)>=2 and len(num2)>=2:
    print(num1[0:2]+num2[2:len(num2)+1] +" "+ num2[0:2]+num1[2:len(num1)+1])
else:
    print("Input should be a min of 2-char string")
print()

num=input("Enter a string : ")
if len(num)<4:
    print()
else:
    print(num[0:2] + num[-2:len(num):1])

print()

num=input("Enter a string : ")
for i in range(0,len(num)):
    print(F"character at index {i} :",num[i])
for i in range(-1,-len(num)-1,-1):
    print(F"character at index {i} :",num[i])
print()


number=input("Enter a string : ")
even_num=''
odd_num=''
for i in range(len(number)):
    if i%2==0:
        even_num+=number[i]
    else:
        odd_num+=number[i]
print("string at even indexes :",even_num)
print("string at odd indexes :",odd_num)

print()

num=input("enter any string with alternative character and digit :")
result=''
try:
    for i in range(0,len(num)):
        if i%2==0:
            num1=num[i]*int(num[i+1])
            result+=num1
    print(result)
except:
    print("string should have alternative character and digit")
print()

num1=input("Enter first string :")
num2=input("Enter second string :")
result=''
i=0
while i<len(num1) and i<len(num2):
    result+=num1[i]+num2[i]
    i+=1
result+=num1[i:]+num2[i:]
print(result)

print()
num1=input("Enter a string : ")
result=''
for i in range(0,len(num1)):
    if num1[i] not in result:
        result+=num1[i]
print("String without duplicate  : ",result)

# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247'))  #  4
print(len('+-$'))  #  3
print(len(''))  #  0
print(len(' '))  #  1
print(len('A2#'))  #  3
#print(len(3456)) #  error
print('Sec'. len())  #  error


# chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  #   'Z'
print(chr(97))  # 'a'
print(chr(122))  #  'z'
print(chr(48))  #   '0'
print(chr(57))  #  '9'
print(chr(36))  #   '$'
print(chr(32))  #  ' '

# ord()  function  demo  program
print(ord('A'))  #  65
print(ord('Z'))  #  90
print(ord('a'))  #  97
print(ord('z'))  #  122
print(ord('0'))  #  48
print(ord('9'))  #  57
print(ord('$'))  #  36
print(ord(' '))  # 32


num=input("Enter any string with alternate character and digit : ")
result=''
try:
    for i in range(0,len(num)):
        if i%2==0:
            result+=num[i]+chr(ord(num[i]) + int(num[i+1]))
    print(result)
except:
    print("pls enter string with alternate char and digit")
print()
#program to find largest command line input
from sys import argv
print(argv)
if len(argv) == 1:
    print("Please send inputs")
else:
    all_numbers = True
    all_strings = True
    a = []
    for arg in argv[1:]:
        try:
            x = float(arg)
            a.append(x)
            all_strings = False  
        except ValueError:
            a.append(arg)
            all_numbers = False  
    if all_numbers:
        print("Largest command input:", max(a))
    elif all_strings:
        print("Largest command input:", max(a))
    else:
        print("Inputs cannot be  numbers and strings")
